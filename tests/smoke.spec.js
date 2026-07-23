const { test, expect } = require('@playwright/test');

const pages = [
  'index.html',
  'about.html',
  'activities.html',
  'gallery.html',
  'donate.html',
  'contact.html',
  'privacy.html',
  'terms.html',
];

test.describe('public site smoke', () => {
  for (const pagePath of pages) {
    test(`${pagePath} loads without console errors`, async ({ page }) => {
      const errors = [];
      page.on('console', (message) => {
        if (message.type() === 'error') errors.push(message.text());
      });
      await page.goto(`/${pagePath}`);
      await expect(page.locator('main')).toBeVisible();
      await expect(page.locator('title')).toHaveCount(1);
      expect(errors).toEqual([]);
    });
  }

  test('keyboard users can reveal skip link', async ({ page }) => {
    await page.goto('/index.html');
    await page.keyboard.press('Tab');
    await expect(page.getByText('Skip to main content')).toBeFocused();
  });

  test('donor confirmation validates consent before submit', async ({ page }) => {
    await page.goto('/donate.html');
    await page.fill('#donor-name', 'Test Donor');
    await page.fill('#donor-email', 'donor@example.com');
    await page.fill('#donor-amount', '5000');
    await page.click('#donor-submit');
    await expect(page.getByText('Please confirm donor privacy consent')).toBeVisible();
  });
});
