const nodemailer = require('nodemailer');

function createTransport() {
  return nodemailer.createTransport({
    host: process.env.SMTP_HOST,
    port: parseInt(process.env.SMTP_PORT || '465'),
    secure: true,
    auth: {
      user: process.env.SMTP_USER,
      pass: process.env.SMTP_PASS,
    },
  });
}

function userEmail(nome, struttura, tipo, ruolo, email) {
  return `<!DOCTYPE html>
<html lang="it">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head>
<body style="margin:0;padding:0;background:#e8edf2;font-family:Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#e8edf2;padding:40px 20px;">
<tr><td align="center">
<table width="600" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:14px;overflow:hidden;box-shadow:0 8px 40px rgba(0,0,0,.12);">

  <!-- HEADER -->
  <tr><td style="background:#172A3A;padding:36px 48px 32px;">
    <table width="100%" cellpadding="0" cellspacing="0">
      <tr><td>
        <table cellpadding="0" cellspacing="0"><tr>
          <td style="width:36px;height:36px;background:#74B3CE;border-radius:8px;text-align:center;vertical-align:middle;">
            <span style="font-family:Georgia,serif;font-size:18px;font-weight:700;color:#172A3A;">A</span>
          </td>
          <td style="padding-left:10px;">
            <span style="font-family:Georgia,serif;font-size:20px;color:#ffffff;">Assis<strong>Team24</strong></span>
          </td>
        </tr></table>
      </td></tr>
      <tr><td style="height:24px;"></td></tr>
      <tr><td>
        <div style="display:inline-block;background:rgba(116,179,206,.18);border:1px solid rgba(116,179,206,.35);border-radius:100px;padding:5px 16px;font-size:12px;font-weight:700;color:#74B3CE;letter-spacing:.06em;margin-bottom:14px;">RICHIESTA RICEVUTA</div>
        <h1 style="font-family:Georgia,serif;font-size:28px;color:#ffffff;font-weight:400;line-height:1.3;margin:0 0 12px;">Grazie per il tuo interesse,<br><em>${nome}.</em></h1>
        <p style="font-size:15px;color:rgba(255,255,255,.65);line-height:1.6;margin:0;">Abbiamo ricevuto la tua richiesta. Ti contatteremo entro <strong style="color:#74B3CE;">24 ore</strong> per fornirti l'accesso alla demo.</p>
      </td></tr>
    </table>
  </td></tr>

  <!-- INTRO -->
  <tr><td style="padding:32px 48px 20px;">
    <p style="font-size:15px;color:#4a6070;line-height:1.7;margin:0;">Nel frattempo, ecco un riassunto di cosa troverai in AssisTeam24 — il gestionale pensato per semplificare il lavoro quotidiano delle strutture sanitarie.</p>
  </td></tr>

  <!-- FEATURES GRID -->
  <tr><td style="padding:0 48px 28px;">
    <table width="100%" cellpadding="0" cellspacing="0">
      <tr>
        <td width="48%" style="vertical-align:top;padding-right:8px;padding-bottom:12px;">
          <table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f8fb;border:1px solid #dde8f0;border-radius:10px;">
            <tr><td style="padding:18px 20px;">
              <div style="font-size:22px;margin-bottom:8px;">&#128203;</div>
              <div style="font-size:13px;font-weight:700;color:#172A3A;margin-bottom:5px;">Cartella Clinica Digitale</div>
              <div style="font-size:12px;color:#6b8899;line-height:1.5;">Terapie, diaria, parametri vitali, scale di valutazione e moduli specialistici in un unico posto.</div>
            </td></tr>
          </table>
        </td>
        <td width="48%" style="vertical-align:top;padding-left:8px;padding-bottom:12px;">
          <table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f8fb;border:1px solid #dde8f0;border-radius:10px;">
            <tr><td style="padding:18px 20px;">
              <div style="font-size:22px;margin-bottom:8px;">&#128101;</div>
              <div style="font-size:13px;font-weight:700;color:#172A3A;margin-bottom:5px;">7 Profili di Accesso</div>
              <div style="font-size:12px;color:#6b8899;line-height:1.5;">Medico, coordinatore, operatore, medico di base, amministrazione, paziente e super admin — ognuno con la propria interfaccia dedicata.</div>
            </td></tr>
          </table>
        </td>
      </tr>
      <tr>
        <td width="48%" style="vertical-align:top;padding-right:8px;padding-bottom:12px;">
          <table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f8fb;border:1px solid #dde8f0;border-radius:10px;">
            <tr><td style="padding:18px 20px;">
              <div style="font-size:22px;margin-bottom:8px;">&#128276;</div>
              <div style="font-size:13px;font-weight:700;color:#172A3A;margin-bottom:5px;">Comunicazioni & Alert</div>
              <div style="font-size:12px;color:#6b8899;line-height:1.5;">Alert automatici per parametri critici e messaggistica interna con selezione del destinatario.</div>
            </td></tr>
          </table>
        </td>
        <td width="48%" style="vertical-align:top;padding-left:8px;padding-bottom:12px;">
          <table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f8fb;border:1px solid #dde8f0;border-radius:10px;">
            <tr><td style="padding:18px 20px;">
              <div style="font-size:22px;margin-bottom:8px;">&#128274;</div>
              <div style="font-size:13px;font-weight:700;color:#172A3A;margin-bottom:5px;">Sicurezza & GDPR</div>
              <div style="font-size:12px;color:#6b8899;line-height:1.5;">Finestra di modifica tracciata, accessi profilati e piena conformità GDPR su tutti i dati clinici.</div>
            </td></tr>
          </table>
        </td>
      </tr>
      <tr>
        <td width="48%" style="vertical-align:top;padding-right:8px;">
          <table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f8fb;border:1px solid #dde8f0;border-radius:10px;">
            <tr><td style="padding:18px 20px;">
              <div style="font-size:22px;margin-bottom:8px;">&#9889;</div>
              <div style="font-size:13px;font-weight:700;color:#172A3A;margin-bottom:5px;">Efficienza Operativa</div>
              <div style="font-size:12px;color:#6b8899;line-height:1.5;">Terapie e diari su più pazienti in un colpo solo — meno tempo in burocrazia, più ai pazienti.</div>
            </td></tr>
          </table>
        </td>
        <td width="48%" style="vertical-align:top;padding-left:8px;">
          <table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f8fb;border:1px solid #dde8f0;border-radius:10px;">
            <tr><td style="padding:18px 20px;">
              <div style="font-size:22px;margin-bottom:8px;">&#127917;</div>
              <div style="font-size:13px;font-weight:700;color:#172A3A;margin-bottom:5px;">100% Personalizzabile</div>
              <div style="font-size:12px;color:#6b8899;line-height:1.5;">Moduli configurabili per ogni profilo: ogni utente vede solo ciò che è rilevante per il suo ruolo.</div>
            </td></tr>
          </table>
        </td>
      </tr>
    </table>
  </td></tr>

  <!-- CALLOUT -->
  <tr><td style="padding:0 48px 36px;">
    <table width="100%" cellpadding="0" cellspacing="0" style="background:#172A3A;border-radius:12px;">
      <tr><td style="padding:22px 26px;">
        <table width="100%" cellpadding="0" cellspacing="0">
          <tr>
            <td width="44" style="vertical-align:top;">
              <div style="width:40px;height:40px;background:rgba(116,179,206,.2);border-radius:10px;text-align:center;line-height:40px;font-size:20px;">&#8987;</div>
            </td>
            <td style="padding-left:14px;vertical-align:middle;">
              <div style="font-size:14px;font-weight:700;color:#ffffff;margin-bottom:4px;">Sarai ricontattato entro 24 ore</div>
              <div style="font-size:13px;color:rgba(255,255,255,.6);line-height:1.5;">Riceverai accesso a una versione dimostrativa con funzionalità selezionate per esplorare il sistema liberamente, senza impegno.</div>
            </td>
          </tr>
        </table>
      </td></tr>
    </table>
  </td></tr>

  <!-- FOOTER -->
  <tr><td style="background:#f4f8fb;border-top:1px solid #dde8f0;padding:22px 48px;">
    <table width="100%" cellpadding="0" cellspacing="0">
      <tr>
        <td><p style="font-size:12px;color:#8aa4b4;line-height:1.6;margin:0;">Hai ricevuto questa email perché hai compilato il form su <a href="https://assisteam-landing.vercel.app" style="color:#74B3CE;text-decoration:none;">assisteam-landing.vercel.app</a>.<br>Per qualsiasi domanda scrivi a <a href="mailto:info@assisteam24.it" style="color:#74B3CE;text-decoration:none;">info@assisteam24.it</a></p></td>
        <td align="right" style="white-space:nowrap;"><span style="font-family:Georgia,serif;font-size:13px;color:#8aa4b4;">Assis<strong style="color:#172A3A;">Team24</strong></span></td>
      </tr>
    </table>
  </td></tr>

</table>
</td></tr></table>
</body></html>`;
}

function internalEmail(nome, cognome, struttura, tipo, ruolo, email, telefono, messaggio, data) {
  const rows = [
    ['Nome', `${nome} ${cognome}`],
    ['Struttura', struttura],
    ['Tipo struttura', tipo || '—'],
    ['Ruolo', ruolo || '—'],
    ['Email', email],
    ['Telefono', telefono || '—'],
    ['Note', messaggio || '—'],
  ];
  const tableRows = rows.map((r, i) => `
    <tr style="background:${i % 2 === 0 ? '#f4f8fb' : '#ffffff'};">
      <td style="padding:12px 20px;font-size:12px;font-weight:700;color:#8aa4b4;letter-spacing:.06em;text-transform:uppercase;width:30%;border-bottom:1px solid #dde8f0;">${r[0]}</td>
      <td style="padding:12px 20px;font-size:14px;color:#172A3A;border-bottom:1px solid #dde8f0;">${r[1]}</td>
    </tr>`).join('');

  return `<!DOCTYPE html>
<html lang="it">
<head><meta charset="UTF-8"></head>
<body style="margin:0;padding:0;background:#e8edf2;font-family:Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#e8edf2;padding:40px 20px;">
<tr><td align="center">
<table width="600" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:14px;overflow:hidden;box-shadow:0 8px 40px rgba(0,0,0,.12);">
  <tr><td style="background:#172A3A;padding:22px 40px;">
    <table width="100%" cellpadding="0" cellspacing="0">
      <tr>
        <td><span style="font-family:Georgia,serif;font-size:17px;color:#ffffff;">Assis<strong>Team24</strong></span></td>
        <td align="right"><div style="display:inline-block;background:#74B3CE;border-radius:100px;padding:4px 14px;font-size:12px;font-weight:700;color:#172A3A;">Nuova richiesta demo</div></td>
      </tr>
    </table>
  </td></tr>
  <tr><td style="padding:28px 40px 16px;">
    <h2 style="font-family:Georgia,serif;font-size:20px;color:#172A3A;font-weight:400;margin:0 0 6px;">Nuova richiesta demo ricevuta</h2>
    <p style="font-size:13px;color:#8aa4b4;margin:0;">${data}</p>
  </td></tr>
  <tr><td style="padding:0 40px 28px;">
    <table width="100%" cellpadding="0" cellspacing="0" style="border:1px solid #dde8f0;border-radius:10px;overflow:hidden;">
      ${tableRows}
    </table>
  </td></tr>
  <tr><td style="padding:0 40px 32px;">
    <a href="mailto:${email}" style="display:inline-block;background:#172A3A;color:#ffffff;text-decoration:none;padding:12px 28px;border-radius:8px;font-size:14px;font-weight:700;">Rispondi a ${nome} &#8594;</a>
  </td></tr>
  <tr><td style="background:#f4f8fb;border-top:1px solid #dde8f0;padding:16px 40px;">
    <p style="font-size:12px;color:#8aa4b4;margin:0;">Email automatica generata da assisteam-landing.vercel.app</p>
  </td></tr>
</table>
</td></tr></table>
</body></html>`;
}

module.exports = async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const { nome, cognome, struttura, tipo, ruolo, email, telefono, messaggio } = req.body;

  if (!nome || !email || !struttura) {
    return res.status(400).json({ error: 'Campi obbligatori mancanti' });
  }

  const now = new Date().toLocaleString('it-IT', { timeZone: 'Europe/Rome', dateStyle: 'long', timeStyle: 'short' });
  const transporter = createTransport();

  try {
    await Promise.all([
      transporter.sendMail({
        from: '"AssisTeam24" <noreply@assisteam24.it>',
        to: email,
        subject: 'Grazie per aver richiesto la demo — AssisTeam24',
        html: userEmail(nome, struttura, tipo, ruolo, email),
      }),
      transporter.sendMail({
        from: '"AssisTeam24" <noreply@assisteam24.it>',
        to: 'info@assisteam24.it',
        replyTo: email,
        subject: `Nuova richiesta demo — ${nome} ${cognome} (${struttura})`,
        html: internalEmail(nome, cognome, struttura, tipo, ruolo, email, telefono, messaggio, now),
      }),
    ]);

    return res.status(200).json({ success: true });
  } catch (err) {
    console.error(err);
    return res.status(500).json({ error: err.message });
  }
};
