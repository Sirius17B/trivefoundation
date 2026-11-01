const { test, expect } = require('@playwright/test');
const fs = require('node:fs');
const path = require('node:path');

// Every page in the site, discovered rather than listed, so a new page is
// covered the day it is added.
const pages = fs.readdirSync(path.join(__dirname, '..')).filter((f) => f.endsWith('.html'));
const viewports = { desktop: { width: 1280, height: 800 }, mobile: { width: 390, height: 800 } };

// Labels that only an administrator should ever see.
const ADMIN_LABELS = /edit site content|admin login|log out|site settings|save all changes/i;

// What a logged-in admin looks like to the client (see AdminAuth in js/main.js).
const loginAsAdmin = () => sessionStorage.setItem('thrive_admin_v3', '1');

// Stock photos and fonts from other hosts are irrelevant here and make
// "network idle" slow and flaky.
test.beforeEach(async ({ page }) => {
  await page.route(/^https?:\/\/(?!127\.0\.0\.1)/, (route) => route.abort());
});

test.describe('anonymous visitors never see admin controls', () => {
  for (const [vpName, viewport] of Object.entries(viewports)) {
    for (const pagePath of pages) {
      test(`${pagePath} @ ${vpName}`, async ({ page }) => {
        await page.setViewportSize(viewport);
        await page.goto(`/${pagePath}`);
        await page.waitForLoadState('networkidle');

        // Anything the site itself marks admin-only must be hidden. This is
        // what catches a component class (e.g. .btn) out-ranking the hide rule.
        for (const el of await page.locator('.admin-only').all()) {
          const label = await el.evaluate((n) => `${n.tagName.toLowerCase()}#${n.id} .${n.className}`);
          expect(await el.isVisible(), `${label} is visible to a visitor`).toBe(false);
        }

        // Anything that merely looks like an admin control must be hidden too,
        // even if someone forgot to mark it admin-only.
        const controls = page.locator('button, a, [role=button]').filter({ hasText: ADMIN_LABELS });
        for (const el of await controls.all()) {
          const text = (await el.innerText()).trim();
          expect(await el.isVisible(), `"${text}" is visible to a visitor`).toBe(false);
        }
      });
    }
  }
});

test.describe('admins still get their controls', () => {
  test('league.html shows Edit Site Content and Log Out once logged in', async ({ page }) => {
    await page.addInitScript(loginAsAdmin);
    await page.goto('/league.html');
    await page.waitForLoadState('networkidle');
    await expect(page.locator('#cms-btn')).toBeVisible();
    await expect(page.locator('#admin-toggle-btn')).toHaveText('Log Out');
  });

  test('logging out on league.html hides them again', async ({ page }) => {
    await page.addInitScript(loginAsAdmin);
    await page.goto('/league.html');
    await page.waitForLoadState('networkidle');
    await page.locator('#admin-toggle-btn').click();
    await expect(page.locator('#cms-btn')).toBeHidden();
    await expect(page.locator('#admin-toggle-btn')).toBeHidden();
  });
});
