# Backend & Donor Privacy Implementation Guide

The current website is a static frontend. It can present donation instructions, but it must not be the source of truth for donor identities, private donation references, admin credentials, uploads, or participant personal data.

## Recommended production architecture

1. **Frontend:** Keep the static HTML/CSS/JS site for public content and calls to action.
2. **Backend API:** Add a small HTTPS API for contact messages, donor confirmations, admin login, content updates, uploads, and audit logs.
3. **Database:** Store donor and programme records in a managed database with encryption at rest and point-in-time backups.
4. **Object storage:** Store photos/videos in private buckets by default; publish only approved public assets through a CDN.
5. **Transactional email:** Send donor acknowledgements and internal notifications through a provider such as Postmark, SendGrid, or AWS SES.

## Donor identity protection model

- **Separate private and public data:** Store legal name, email, amount/reference, and notes in a private `donors` table. Publish only anonymised impact totals or explicit opt-in display names.
- **Use donor IDs:** Generate a random donor ID for reconciliation. Do not expose bank references or email addresses in URLs, local storage, analytics events, or public leaderboards.
- **Consent-first acknowledgements:** Add an `acknowledgement_preference` field: `anonymous`, `first_name`, `organisation`, or `custom_display_name`.
- **Role-based access:** Limit donor identity access to authorised finance/admin users. Volunteers and public content editors should not see donor identities.
- **Audit logging:** Record who viewed, edited, exported, or deleted donor records.
- **Encryption:** Use TLS in transit, database encryption at rest, and field-level encryption for especially sensitive notes or references when available.
- **Retention:** Define a retention window for accounting/legal needs, then delete or anonymise records.

## Minimal API endpoints

| Endpoint | Purpose | Security requirements |
|---|---|---|
| `POST /api/contact` | Sponsor/volunteer/general enquiries | CAPTCHA or rate limit, validation, spam honeypot, email notification |
| `POST /api/donor-confirmations` | Donor submits transfer confirmation privately | Validation, consent field, encrypted storage, no public response data |
| `GET /api/admin/donors` | Finance/admin donor reconciliation | Authenticated session, MFA recommended, role check, audit log |
| `PATCH /api/admin/content` | CMS edits | Authenticated admin role, CSRF protection, audit log, backups/versioning |
| `POST /api/admin/uploads` | Media upload | Authenticated admin role, file type/size validation, malware scanning, consent status |

## Safer deployment options

- **Fast path:** Netlify/Vercel static frontend + serverless functions + managed Postgres/Supabase with row-level security.
- **More controlled:** Node/Express or Django API + managed Postgres + S3-compatible object storage + CDN.
- **Form-only interim:** Use a reputable form backend for contact/donor confirmations, but disable public donor names until a proper database and consent workflow exist.


## Included serverless starter

This repository includes Netlify-compatible starter functions:

- `netlify/functions/contact.js` validates contact enquiries and forwards them to `CONTACT_WEBHOOK_URL`.
- `netlify/functions/donor-confirmation.js` validates donor confirmations, generates a private donor ID, and forwards records to `DONOR_WEBHOOK_URL`.

To enable them in production, set `SITE_CONFIG.API.contact` to `/.netlify/functions/contact`, set `SITE_CONFIG.API.donor_confirmation` to `/.netlify/functions/donor-confirmation`, and configure the webhook environment variables in the hosting provider. Webhooks should point to a private CRM/database/email automation endpoint with restricted access, not a public spreadsheet.

## Do not do this

- Do not store donor identity in `localStorage`.
- Do not put donor names or bank references in Git, JavaScript config, analytics events, screenshots, or public pages without opt-in consent.
- Do not rely on a frontend PIN as production admin security.
- Do not send sensitive donation confirmations to shared inboxes without access control and retention rules.
