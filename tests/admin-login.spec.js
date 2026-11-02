const { test, expect } = require('@playwright/test');

// The browser must never decide whether a PIN is right: it asks the server.
// These tests stand in for the server so every outcome can be scripted.
const RIGHT = 'right-pin';
const outcomes = {
  [RIGHT]: { status: 200, body: { ok: true } },
  'locked-pin': { status: 429, body: { error: 'Too many incorrect attempts. Try again in 15 minutes.', retryAfterSeconds: 900 } },
  'down-pin': { status: 503, body: { error: 'Sign-in is temporarily unavailable. Please try again shortly.' } },
};
const wrong = { status: 401, body: { error: 'Invalid PIN', attemptsLeft: 3 } };

let verifyRequests;

test.beforeEach(async ({ page }) => {
  verifyRequests = [];
  await page.route(/^https?:\/\/(?!127\.0\.0\.1)/, (route) => route.abort());
  await page.route('**/.netlify/functions/admin-data**', async (route) => {
    const req = route.request();
    if (req.method() === 'POST') {
      const body = JSON.parse(req.postData() || '{}');
      if (body.action === 'verify') {
        verifyRequests.push(body);
        const o = outcomes[body.pin] || wrong;
        return route.fulfill({ status: o.status, contentType: 'application/json', body: JSON.stringify(o.body) });
      }
    }
    return route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify({ value: null }) });
  });
});

async function openSharedLogin(page, path) {
  await page.goto(path);
  await page.waitForLoadState('networkidle');
  await page.keyboard.press('Control+Shift+A');
  await expect(page.locator('#login-modal')).toBeVisible();
}

test.describe('shared login form (every page except league)', () => {
  test('the right PIN logs in, after asking the server', async ({ page }) => {
    await openSharedLogin(page, '/about.html');
    await page.fill('#admin-pin-inp', RIGHT);
    await page.click('text=Sign In');
    await expect(page.locator('#cms-toolbar')).toBeVisible();
    expect(verifyRequests).toEqual([{ action: 'verify', pin: RIGHT }]);
    expect(await page.evaluate(() => sessionStorage.getItem('thrive_admin_v3'))).toBe('1');
  });

  test('a wrong PIN is refused and says how many tries are left', async ({ page }) => {
    await openSharedLogin(page, '/about.html');
    await page.fill('#admin-pin-inp', 'nope');
    await page.click('text=Sign In');
    await expect(page.locator('#login-err')).toContainText('Incorrect PIN. 3 attempts left.');
    await expect(page.locator('#cms-toolbar')).toBeHidden();
    expect(await page.evaluate(() => sessionStorage.getItem('thrive_admin_v3'))).toBeNull();
  });

  test('a locked-out client sees the server\'s lockout message', async ({ page }) => {
    await openSharedLogin(page, '/about.html');
    await page.fill('#admin-pin-inp', 'locked-pin');
    await page.click('text=Sign In');
    await expect(page.locator('#login-err')).toContainText('Too many incorrect attempts. Try again in 15 minutes.');
  });

  test('when the server is down, says so instead of calling the PIN wrong', async ({ page }) => {
    await openSharedLogin(page, '/about.html');
    await page.fill('#admin-pin-inp', 'down-pin');
    await page.click('text=Sign In');
    await expect(page.locator('#login-err')).toContainText('unavailable');
    await expect(page.locator('#login-err')).not.toContainText('Incorrect');
  });
});

test.describe('league page login form (its own modal)', () => {
  async function openLeagueLogin(page) {
    await page.goto('/league.html');
    await page.waitForLoadState('networkidle');
    await page.keyboard.press('Control+Shift+A');
    await expect(page.locator('#login-modal')).toBeVisible();
  }

  test('the right PIN logs in and reveals the admin controls', async ({ page }) => {
    await openLeagueLogin(page);
    await page.fill('#pin-input', RIGHT);
    await page.click('#login-modal >> text=Sign In');
    await expect(page.locator('#admin-toggle-btn')).toHaveText('Log Out');
    await expect(page.locator('#cms-btn')).toBeVisible();
    expect(verifyRequests).toEqual([{ action: 'verify', pin: RIGHT }]);
  });

  test('a wrong PIN is refused with the server\'s count of tries left', async ({ page }) => {
    await openLeagueLogin(page);
    await page.fill('#pin-input', 'nope');
    await page.click('#login-modal >> text=Sign In');
    await expect(page.locator('#login-err')).toContainText('Incorrect PIN. 3 attempts left.');
    await expect(page.locator('#cms-btn')).toBeHidden();
  });

  test('a locked-out client sees the server\'s lockout message', async ({ page }) => {
    await openLeagueLogin(page);
    await page.fill('#pin-input', 'locked-pin');
    await page.click('#login-modal >> text=Sign In');
    await expect(page.locator('#login-err')).toContainText('Try again in 15 minutes');
  });
});
