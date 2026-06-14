const { randomUUID } = require('node:crypto');
const JSON_HEADERS = {
  'Content-Type': 'application/json',
  'Cache-Control': 'no-store',
};
const ACK_OPTIONS = new Set(['anonymous', 'first_name', 'organisation', 'custom']);

function response(statusCode, body) {
  return { statusCode, headers: JSON_HEADERS, body: JSON.stringify(body) };
}

function isEmail(value) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(String(value || ''));
}

exports.handler = async (event) => {
  if (event.httpMethod !== 'POST') return response(405, { error: 'Method not allowed' });

  let payload;
  try {
    payload = JSON.parse(event.body || '{}');
  } catch {
    return response(400, { error: 'Invalid JSON' });
  }

  const donorId = randomUUID();
  const name = String(payload.name || '').trim();
  const email = String(payload.email || '').trim();
  const amount = Number(payload.amount || 0);
  const acknowledgement = ACK_OPTIONS.has(payload.acknowledgement) ? payload.acknowledgement : 'anonymous';
  const displayName = String(payload.displayName || '').trim().slice(0, 80);

  if (!name || name.length > 80) return response(400, { error: 'Name is required' });
  if (!isEmail(email) || email.length > 100) return response(400, { error: 'Valid email is required' });
  if (!Number.isFinite(amount) || amount < 1) return response(400, { error: 'Valid amount is required' });
  if (payload.consent !== true) return response(400, { error: 'Consent is required' });

  const webhookUrl = process.env.DONOR_WEBHOOK_URL;
  if (!webhookUrl) {
    return response(503, { error: 'Donor backend is not configured' });
  }

  const privateRecord = {
    type: 'donor_confirmation',
    donorId,
    submittedAt: new Date().toISOString(),
    donor: { name, email },
    donation: { amount, currency: 'NGN' },
    acknowledgement: { preference: acknowledgement, displayName },
  };

  const webhookResponse = await fetch(webhookUrl, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(privateRecord),
  });

  if (!webhookResponse.ok) return response(502, { error: 'Donor notification delivery failed' });
  return response(202, { ok: true, donorId });
};
