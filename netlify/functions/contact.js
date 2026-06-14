const JSON_HEADERS = {
  'Content-Type': 'application/json',
  'Cache-Control': 'no-store',
};

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

  const name = String(payload.name || '').trim();
  const email = String(payload.email || '').trim();
  const message = String(payload.message || '').trim();
  const type = String(payload.type || 'general').trim();

  if (!name || name.length > 80) return response(400, { error: 'Name is required' });
  if (!isEmail(email) || email.length > 100) return response(400, { error: 'Valid email is required' });
  if (message.length < 10 || message.length > 2000) return response(400, { error: 'Message must be 10-2000 characters' });
  if (payload.website) return response(202, { ok: true });

  const webhookUrl = process.env.CONTACT_WEBHOOK_URL;
  if (!webhookUrl) {
    return response(503, { error: 'Contact backend is not configured' });
  }

  const forwardBody = {
    type: 'contact',
    submittedAt: new Date().toISOString(),
    name,
    email,
    interest: type,
    message,
  };

  const webhookResponse = await fetch(webhookUrl, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(forwardBody),
  });

  if (!webhookResponse.ok) return response(502, { error: 'Notification delivery failed' });
  return response(202, { ok: true });
};
