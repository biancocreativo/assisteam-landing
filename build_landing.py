#!/usr/bin/env python3
"""Build landing page v4 — SVG icons, security section, role screenshots, no emoji."""
import os, base64

SCREENS_DIR = "screens_hd"

def b64(name):
    path = os.path.join(SCREENS_DIR, f"{name}.jpg")
    if not os.path.exists(path): return ""
    if os.path.getsize(path) < 15000: return ""
    with open(path, "rb") as f:
        return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()

# All image keys
IMG_KEYS = [
    "medico_dashboard","medico_comunicazioni","medico_turni","medico_pazienti",
    "coord_dashboard","coord_turni","coord_personale","coord_pazienti","coord_comunicazioni",
    "operatore_dashboard","operatore_controlli",
    "superadmin_dashboard","superadmin_staff","superadmin_staff_crea",
    "superadmin_pazienti","superadmin_pazienti_crea",
    "sub_terapia","sub_terapia_s",
    "sub_scale_index","sub_scale_index_s",
    "sub_braden","sub_braden_s",
    "sub_diaria","sub_diaria_s",
    "sub_parametri","sub_parametri_s",
    "sub_presidi","sub_presidi_s",
    "cartella_moduli_section","cartella_moduli_top",
    "op_terapie_a","op_terapie_b","op_diarie_a","op_diarie_b",
    "role_medico_terapia","role_medico_terapia_s",
    "role_coord_turni","role_coord_turni_s",
    "role_operatore_controlli","role_operatore_controlli_s",
    "role_admin_crea_paziente","role_admin_pazienti",
    "role_mdb_cartella","role_mdb_cartella_s","role_mdb_comunicazioni",
    "comms_medico","comms_operatore","comms_nuova_msg","comms_alert_panel",
    "comms_coordinatore",
]
imgs = {k: b64(k) for k in IMG_KEYS}

def img_tag(key, alt=""):
    src = imgs.get(key,"")
    if src: return f'<img src="{src}" alt="{alt}" loading="lazy">'
    return f'<div class="placeholder">{alt}</div>'

def lbcard(key, scroll_key, alt, label):
    src = imgs.get(key,"")
    src2 = imgs.get(scroll_key, src)
    if not src: return f'<div class="screen-card"><div class="placeholder">{alt}</div><div class="screen-label">{label}</div></div>'
    return (f'<div class="screen-card" onclick="openLBSrc(\'{src2}\',\'{alt}\')" tabindex="0" role="button">'
            f'<img src="{src}" alt="{alt}" loading="lazy">'
            f'<div class="screen-label">{svg("zoom",14)} {label}</div></div>')

def panel_img(key, alt, cap):
    src = imgs.get(key,"")
    if src:
        cap_escaped = cap.replace("'","&apos;")
        return f'<img src="{src}" alt="{alt}" onclick="openLBSrc(\'{src}\',\'{cap_escaped}\')" loading="lazy">'
    return f'<div class="placeholder">{alt}</div>'

def role_card(img_key, badge_icon, badge_label, title, features, chips=None):
    sc = imgs.get(img_key,"")
    if sc:
        img_html = f'<div class="role-screenshot-wrap" onclick="openLBSrc(\'{sc}\',\'{badge_label}\')" style="cursor:zoom-in"><img src="{sc}" alt="{badge_label}" loading="lazy"></div>'
    else:
        img_html = f'<div class="placeholder">{badge_label}</div>'
    feat_li = "\n".join(f"<li>{f}</li>" for f in features)
    chips_html = ""
    if chips:
        chips_html = '<div class="role-types">' + "".join(f'<span class="role-type-chip">{c}</span>' for c in chips) + "</div>"
    return f"""
      <div class="role-card">
        {img_html}
        <div class="role-info">
          <div class="role-badge">{svg(badge_icon,15)} {badge_label}</div>
          <h3>{title}</h3>
          <ul class="role-features">{feat_li}</ul>
          {chips_html}
        </div>
      </div>"""

# ── SVG ICON LIBRARY ─────────────────────────────────────────────────────────
def svg(name, size=20, color="currentColor"):
    s = str(size)
    base = f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    shapes = {
        "stethoscope":  '<path d="M6 3a2 2 0 0 1 2-2h.5a2 2 0 0 1 2 2v7a4 4 0 0 1-8 0V3a2 2 0 0 1 2-2H6z"/><path d="M10 15v1a5 5 0 0 0 5 5h0a5 5 0 0 0 5-5v-3"/><circle cx="20" cy="12" r="2"/>',
        "clipboard":    '<path d="M9 5H7a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2h-2"/><rect x="9" y="3" width="6" height="4" rx="1"/><line x1="9" y1="12" x2="15" y2="12"/><line x1="9" y1="16" x2="13" y2="16"/>',
        "user-cross":   '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/><line x1="17" y1="11" x2="22" y2="16"/><line x1="22" y1="11" x2="17" y2="16"/>',
        "settings":     '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/>',
        "folder-user":  '<path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/><circle cx="12" cy="14" r="2"/><path d="M8.5 19c0-2 1.6-3.5 3.5-3.5s3.5 1.5 3.5 3.5"/>',
        "user-laptop":  '<rect x="2" y="3" width="20" height="13" rx="2"/><path d="M8 21h8m-4-5v5"/><circle cx="12" cy="9" r="3"/>',
        "pill":         '<path d="m10.5 20.5 10-10a4.95 4.95 0 1 0-7-7l-10 10a4.95 4.95 0 1 0 7 7z"/><line x1="8.5" y1="8.5" x2="15.5" y2="15.5"/>',
        "file-text":    '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/>',
        "check-circle": '<polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>',
        "zoom":         '<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/>',
        "bar-chart":    '<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/>',
        "hospital":     '<rect x="3" y="2" width="18" height="20" rx="2"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01M16 6h.01M12 6h.01M12 10h.01M12 14h.01M8 10h.01M8 14h.01M16 10h.01M16 14h.01"/><line x1="12" y1="4" x2="12" y2="8"/><line x1="10" y1="6" x2="14" y2="6"/>',
        "calendar":     '<rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>',
        "refresh":      '<polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/>',
        "message":      '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
        "lock":         '<rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
        "list":         '<line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/>',
        "alert":        '<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
        "users":        '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
        "mail":         '<path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/>',
        "globe":        '<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
        "phone":        '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 12a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.64 1h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 8.6a16 16 0 0 0 6 6l.94-.94a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
        "shield":       '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
        "shield-check": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/>',
        "clock":        '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
        "swipe":        '<path d="M7 11V7a5 5 0 0 1 9.9-1"/><path d="M14 9.1V6a3 3 0 0 1 6 0v5"/><path d="M20 11v2a8 8 0 0 1-16 0v-4"/><line x1="3" y1="8" x2="7" y2="8"/>',
        "sliders":      '<line x1="4" y1="21" x2="4" y2="14"/><line x1="4" y1="10" x2="4" y2="3"/><line x1="12" y1="21" x2="12" y2="12"/><line x1="12" y1="8" x2="12" y2="3"/><line x1="20" y1="21" x2="20" y2="16"/><line x1="20" y1="12" x2="20" y2="3"/><line x1="1" y1="14" x2="7" y2="14"/><line x1="9" y1="8" x2="15" y2="8"/><line x1="17" y1="16" x2="23" y2="16"/>',
        "check":        '<polyline points="20 6 9 17 4 12"/>',
        "arrow-right":  '<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>',
        "x":            '<line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>',
        "plus":         '<line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/>',
        "eye":          '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>',
        "sparkle":      '<path d="M12 3l1.5 4.5L18 9l-4.5 1.5L12 15l-1.5-4.5L6 9l4.5-1.5z"/><path d="M19 3l.7 2.3L22 6l-2.3.7L19 9l-.7-2.3L16 6l2.3-.7z"/><path d="M5 17l.7 2.3L8 20l-2.3.7L5 23l-.7-2.3L2 20l2.3-.7z"/>',
    }
    body = shapes.get(name, f'<circle cx="12" cy="12" r="8"/><text x="12" y="12">?</text>')
    return f"{base}{body}</svg>"

# ── ICON wrapper helpers ────────────────────────────────────────────
def icon_badge(name, label):
    return f'<div class="role-badge">{svg(name,14)} {label}</div>'

def feat_icon(name):
    return f'<div class="feature-icon">{svg(name,22)}</div>'

def check_li(text):
    return f'<li><div class="check-icon">{svg("check",12,"var(--teal)")}</div>{text}</li>'

def eff_li(icon_name, title, text):
    return f'<li><div class="eff-icon">{svg(icon_name,16)}</div><span class="txt"><strong>{title}</strong> {text}</span></li>'

def contact_item(icon_name, content):
    return f'<div class="contact-item">{svg(icon_name,16)} {content}</div>'

# ─────────────────────────────────────────────────────────────────────────────
html = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AssisTeam24 — La cartella clinica digitale che semplifica la cura</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --navy:#172A3A;--teal:#74B3CE;--teal-dark:#4e9ab8;--white:#FFFFFF;
  --offwhite:#F3F7FB;--muted:#5b7a91;--border:#dce8f0;
  --radius:12px;
  --shadow:0 4px 24px rgba(23,42,58,.08);
  --shadow-lg:0 12px 48px rgba(23,42,58,.14);
}}
html{{scroll-behavior:smooth}}
body{{font-family:'Outfit',sans-serif;color:var(--navy);background:var(--white);line-height:1.6;-webkit-font-smoothing:antialiased;}}
h1,h2,h3,h4{{font-family:'DM Serif Display',serif;line-height:1.2;}}
a{{color:inherit;text-decoration:none}}
img{{max-width:100%;display:block;}}
.placeholder{{background:#e8f0f6;border:2px dashed var(--border);border-radius:var(--radius);display:flex;align-items:center;justify-content:center;color:var(--muted);font-size:.875rem;min-height:200px;}}
section{{padding:96px 0}}
.container{{max-width:1180px;margin:0 auto;padding:0 32px}}
.label{{display:inline-block;font-family:'Outfit',sans-serif;font-size:.75rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--teal);background:rgba(116,179,206,.12);padding:6px 14px;border-radius:100px;margin-bottom:20px;}}
.section-center{{text-align:center;max-width:720px;margin:0 auto 64px}}
.section-center h2,.section-head h2{{font-size:clamp(1.9rem,3vw,2.6rem);margin-bottom:16px}}
.section-center p,.section-head p{{color:var(--muted);font-size:1.05rem;line-height:1.7}}
.section-head{{text-align:center;max-width:680px;margin:0 auto 64px}}
.btn{{display:inline-flex;align-items:center;gap:8px;border-radius:8px;padding:10px 22px;font-family:'Outfit',sans-serif;font-size:.9rem;font-weight:600;cursor:pointer;transition:all .2s;border:none;}}
.btn-primary{{background:var(--teal);color:var(--white)}}
.btn-primary:hover{{background:var(--teal-dark);transform:translateY(-1px);box-shadow:0 6px 20px rgba(116,179,206,.35)}}
.btn-outline{{background:transparent;color:var(--navy);border:1.5px solid var(--border)}}
.btn-outline:hover{{border-color:var(--teal);color:var(--teal)}}
.btn-lg{{padding:14px 32px;font-size:1rem;border-radius:10px}}
.btn-xl{{padding:18px 40px;font-size:1.05rem;border-radius:12px}}
svg{{flex-shrink:0;}}

/* ── NAV ── */
nav{{position:sticky;top:0;z-index:100;background:rgba(255,255,255,.92);backdrop-filter:blur(12px);border-bottom:1px solid var(--border);}}
.nav-inner{{max-width:1180px;margin:0 auto;padding:0 32px;height:68px;display:flex;align-items:center;justify-content:space-between;}}
.logo{{display:flex;align-items:center;gap:10px}}
.logo-badge{{width:36px;height:36px;border-radius:9px;background:var(--navy);display:flex;align-items:center;justify-content:center;color:var(--teal);font-family:'DM Serif Display',serif;font-size:1rem;}}
.logo-text{{font-family:'Outfit',sans-serif;font-weight:700;font-size:1.05rem;color:var(--navy)}}
.logo-text span{{color:var(--teal)}}
.nav-links{{display:flex;align-items:center;gap:28px;list-style:none}}
.nav-links a{{font-size:.875rem;font-weight:500;color:var(--muted);transition:color .2s}}
.nav-links a:hover{{color:var(--navy)}}

/* ── HERO ── */
#hero{{padding:80px 0 0;background:linear-gradient(180deg,#f3f7fb 0%,#ffffff 100%);overflow:hidden;}}
.hero-inner{{max-width:1180px;margin:0 auto;padding:0 32px;display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center;}}
.hero-copy{{padding-bottom:80px}}
.hero-copy h1{{font-size:clamp(2.4rem,4vw,3.4rem);color:var(--navy);margin-bottom:24px;}}
.hero-copy h1 em{{color:var(--teal);font-style:normal}}
.hero-copy p{{font-size:1.1rem;color:var(--muted);max-width:480px;margin-bottom:36px;line-height:1.7;}}
.hero-actions{{display:flex;gap:14px;flex-wrap:wrap;margin-bottom:48px}}
.hero-stats{{display:flex;gap:32px;padding-top:32px;border-top:1px solid var(--border);flex-wrap:wrap;}}
.stat-item h3{{font-family:'DM Serif Display',serif;font-size:1.8rem;color:var(--navy);}}
.stat-item p{{font-size:.83rem;color:var(--muted);margin-top:2px}}
.hero-visual{{position:relative;padding-bottom:80px;align-self:end;}}
.browser-frame{{background:var(--navy);border-radius:12px 12px 0 0;overflow:hidden;box-shadow:0 20px 80px rgba(23,42,58,.22);}}
.browser-bar{{background:#1e3447;padding:12px 16px;display:flex;align-items:center;gap:8px;}}
.browser-dot{{width:10px;height:10px;border-radius:50%;}}
.browser-url{{flex:1;background:rgba(255,255,255,.08);border-radius:5px;padding:5px 12px;font-size:.78rem;color:rgba(255,255,255,.4);font-family:'Outfit',sans-serif;}}
.browser-frame img,.browser-frame .placeholder{{border-radius:0;width:100%;aspect-ratio:16/9;object-fit:cover;object-position:top;}}
.hero-badge{{position:absolute;bottom:100px;right:-20px;background:var(--white);border:1px solid var(--border);border-radius:12px;padding:14px 18px;box-shadow:var(--shadow-lg);display:flex;align-items:center;gap:12px;font-size:.85rem;font-weight:600;color:var(--navy);white-space:nowrap;}}
.hero-badge-icon{{width:36px;height:36px;border-radius:8px;background:rgba(116,179,206,.15);display:flex;align-items:center;justify-content:center;color:var(--teal);}}

/* ── PROBLEMA ── */
#problema{{background:var(--navy);color:var(--white)}}
#problema .label{{color:var(--teal);background:rgba(116,179,206,.15)}}
.problema-grid{{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center;}}
.problema-copy h2{{font-size:clamp(1.9rem,3vw,2.6rem);color:var(--white);margin-bottom:20px}}
.problema-copy p{{color:rgba(255,255,255,.65);font-size:1.05rem;line-height:1.75;}}
.checklist{{list-style:none;display:flex;flex-direction:column;gap:14px}}
.checklist li{{display:flex;align-items:flex-start;gap:14px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.08);border-radius:10px;padding:14px 18px;font-size:.95rem;color:rgba(255,255,255,.85);line-height:1.5;}}
.check-icon{{width:22px;height:22px;border-radius:50%;flex-shrink:0;background:rgba(116,179,206,.2);display:flex;align-items:center;justify-content:center;margin-top:1px;}}

/* ── CARTELLA ── */
#cartella{{background:var(--offwhite)}}
.features-row{{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-bottom:56px;}}
.feature-tag{{background:var(--white);border:1px solid var(--border);border-radius:100px;padding:7px 16px;font-size:.85rem;font-weight:500;color:var(--navy);display:flex;align-items:center;gap:7px;}}
.feature-tag .dot{{width:6px;height:6px;border-radius:50%;background:var(--teal);flex-shrink:0;}}
.screens-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;}}
.screen-card{{border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow);border:1px solid var(--border);transition:transform .25s,box-shadow .25s;cursor:zoom-in;}}
.screen-card:hover{{transform:translateY(-4px);box-shadow:var(--shadow-lg)}}
.screen-card img,.screen-card .placeholder{{width:100%;aspect-ratio:16/9;object-fit:cover;object-position:top}}
.screen-label{{background:var(--white);padding:11px 16px;font-size:.8rem;font-weight:600;color:var(--muted);border-top:1px solid var(--border);display:flex;align-items:center;gap:6px;}}

/* ── EFFICIENZA ── */
#efficienza{{background:var(--white)}}
.efficienza-inner{{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:start;}}
.efficienza-copy h2,.perso-copy h2{{font-size:clamp(1.9rem,3vw,2.6rem);margin-bottom:20px}}
.efficienza-copy > p{{color:var(--muted);font-size:1.02rem;line-height:1.75;margin-bottom:28px;}}
.eff-points{{list-style:none;display:flex;flex-direction:column;gap:18px;}}
.eff-points li{{display:flex;align-items:flex-start;gap:14px;}}
.eff-icon{{width:32px;height:32px;border-radius:8px;background:rgba(116,179,206,.15);display:flex;align-items:center;justify-content:center;color:var(--teal);flex-shrink:0;margin-top:2px;}}
.eff-points .txt{{font-size:.95rem;color:var(--navy);line-height:1.6;}}
.panel-stack{{display:flex;flex-direction:column;gap:20px;}}
.panel-frame{{background:var(--navy);border-radius:10px;overflow:hidden;box-shadow:var(--shadow-lg);}}
.panel-bar{{background:#1e3447;padding:9px 14px;display:flex;align-items:center;gap:7px;}}
.panel-bar-dot{{width:8px;height:8px;border-radius:50%;}}
.panel-bar-label{{margin-left:6px;font-size:.73rem;color:rgba(255,255,255,.38);font-family:'Outfit',sans-serif;}}
.panel-frame img{{width:100%;display:block;aspect-ratio:16/7;object-fit:cover;object-position:top;cursor:zoom-in;transition:opacity .2s;}}
.panel-frame img:hover{{opacity:.9}}
.panel-caption{{background:var(--offwhite);padding:10px 16px;font-size:.79rem;color:var(--muted);font-weight:600;border-top:1px solid var(--border);}}

/* ── SICUREZZA ── */
#sicurezza{{background:var(--navy);color:var(--white)}}
#sicurezza .label{{color:var(--teal);background:rgba(116,179,206,.15)}}
.sic-grid{{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center;}}
.sic-copy h2{{font-size:clamp(1.9rem,3vw,2.6rem);color:var(--white);margin-bottom:20px}}
.sic-copy > p{{color:rgba(255,255,255,.6);font-size:1.02rem;line-height:1.75;margin-bottom:32px;}}
.sic-cards{{display:flex;flex-direction:column;gap:16px;}}
.sic-card{{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.09);border-radius:12px;padding:20px 22px;display:flex;gap:16px;align-items:flex-start;}}
.sic-icon{{width:40px;height:40px;border-radius:10px;background:rgba(116,179,206,.15);display:flex;align-items:center;justify-content:center;color:var(--teal);flex-shrink:0;}}
.sic-card h4{{font-family:'Outfit',sans-serif;font-weight:700;font-size:.95rem;color:var(--white);margin-bottom:5px;}}
.sic-card p{{font-size:.88rem;color:rgba(255,255,255,.55);line-height:1.55;}}
.sic-stat-row{{display:grid;grid-template-columns:1fr 1fr;gap:20px;}}
.sic-stat{{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:12px;padding:24px;text-align:center;}}
.sic-stat .num{{font-family:'DM Serif Display',serif;font-size:2.2rem;color:var(--teal);line-height:1;margin-bottom:8px;}}
.sic-stat p{{font-size:.85rem;color:rgba(255,255,255,.5);line-height:1.4;}}

/* ── PERSONALIZZAZIONE ── */
#personalizzazione{{background:var(--offwhite)}}
.perso-head{{text-align:center;max-width:640px;margin:0 auto 56px;}}
.perso-head h2{{font-size:clamp(1.9rem,3vw,2.7rem);margin-bottom:14px;}}
.perso-head > p{{color:var(--muted);font-size:1.02rem;line-height:1.75;}}
.spotlight-rows{{display:flex;flex-direction:column;gap:0;border:1px solid var(--border);border-radius:16px;overflow:hidden;background:var(--white);box-shadow:var(--shadow);margin-bottom:32px;}}
.spotlight-row{{display:flex;gap:20px;align-items:flex-start;padding:22px 26px;border-bottom:1px solid var(--border);transition:background .18s;}}
.spotlight-row:last-child{{border-bottom:none;}}
.spotlight-row:hover{{background:rgba(116,179,206,.04);}}
.spotlight-icon{{width:44px;height:44px;border-radius:10px;background:rgba(116,179,206,.12);color:var(--teal);display:flex;align-items:center;justify-content:center;flex-shrink:0;}}
.spotlight-body{{flex:1;}}
.spotlight-body h4{{font-family:'Outfit',sans-serif;font-weight:700;font-size:.95rem;color:var(--navy);margin-bottom:4px;display:flex;align-items:center;gap:10px;flex-wrap:wrap;}}
.spotlight-body p{{font-size:.87rem;color:var(--muted);line-height:1.55;}}
.exclusive-badge{{font-size:.7rem;font-weight:700;letter-spacing:.03em;padding:2px 9px;border-radius:100px;background:rgba(116,179,206,.13);border:1px solid rgba(116,179,206,.28);color:var(--teal-dark);white-space:nowrap;}}
.perso-callout-bar{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:40px;}}
.perso-callout{{border-radius:12px;padding:20px 22px;display:flex;gap:14px;align-items:flex-start;}}
.perso-callout.teal{{background:linear-gradient(135deg,rgba(116,179,206,.13) 0%,rgba(116,179,206,.05) 100%);border:1px solid rgba(116,179,206,.28);}}
.perso-callout.navy{{background:linear-gradient(135deg,rgba(23,42,58,.06) 0%,rgba(23,42,58,.02) 100%);border:1px solid rgba(23,42,58,.12);}}
.perso-callout .pc-icon{{width:38px;height:38px;border-radius:9px;display:flex;align-items:center;justify-content:center;flex-shrink:0;}}
.perso-callout.teal .pc-icon{{background:rgba(116,179,206,.18);color:var(--teal);}}
.perso-callout.navy .pc-icon{{background:rgba(23,42,58,.09);color:var(--navy);}}
.perso-callout h4{{font-family:'Outfit',sans-serif;font-weight:700;font-size:.88rem;color:var(--navy);margin-bottom:4px;}}
.perso-callout p{{font-size:.82rem;color:var(--muted);line-height:1.5;}}
.dashboards-strip{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;}}
.dash-thumb{{border-radius:10px;overflow:hidden;box-shadow:var(--shadow);border:1px solid var(--border);cursor:zoom-in;transition:transform .2s,box-shadow .2s;}}
.dash-thumb:hover{{transform:translateY(-3px);box-shadow:var(--shadow-lg);}}
.dash-thumb img,.dash-thumb .placeholder{{width:100%;aspect-ratio:16/9;object-fit:cover;object-position:top;display:block;}}
.dash-thumb-label{{background:var(--white);padding:7px 11px;font-size:.73rem;font-weight:600;color:var(--muted);border-top:1px solid var(--border);display:flex;align-items:center;gap:5px;}}
/* ── COMUNICAZIONI ── */
#comunicazioni{{background:var(--white)}}
.comms-top{{display:grid;grid-template-columns:1fr 1.15fr;gap:64px;align-items:center;margin-bottom:40px;}}
.comms-copy-left{{}}
.comms-copy-left h2{{font-size:clamp(1.9rem,3vw,2.6rem);margin-bottom:16px;}}
.comms-copy-left > p{{color:var(--muted);font-size:1.02rem;line-height:1.75;margin-bottom:28px;}}
.comms-points{{list-style:none;display:flex;flex-direction:column;gap:18px;}}
.comms-points li{{display:flex;gap:14px;align-items:flex-start;}}
.comms-pt-icon{{width:38px;height:38px;border-radius:9px;background:rgba(116,179,206,.12);display:flex;align-items:center;justify-content:center;color:var(--teal);flex-shrink:0;margin-top:2px;}}
.comms-points .ct{{font-size:.92rem;color:var(--navy);line-height:1.6;}}
.comms-points .ct strong{{display:block;font-weight:700;margin-bottom:2px;}}
.comms-featured{{border-radius:14px;overflow:hidden;box-shadow:var(--shadow-lg);border:1px solid var(--border);cursor:zoom-in;transition:transform .2s;}}
.comms-featured:hover{{transform:translateY(-3px);}}
.comms-featured img{{width:100%;aspect-ratio:16/9;object-fit:cover;object-position:top;display:block;}}
.comms-featured-label{{background:var(--white);padding:10px 16px;font-size:.8rem;font-weight:600;color:var(--muted);border-top:1px solid var(--border);display:flex;align-items:center;gap:7px;}}
.comms-bottom{{display:grid;grid-template-columns:1fr 1fr;gap:20px;}}
.comms-small{{border-radius:12px;overflow:hidden;box-shadow:var(--shadow);border:1px solid var(--border);cursor:zoom-in;transition:transform .2s,box-shadow .2s;}}
.comms-small:hover{{transform:translateY(-3px);box-shadow:var(--shadow-lg);}}
.comms-small img{{width:100%;aspect-ratio:16/9;object-fit:cover;object-position:top;display:block;}}
.comms-small-label{{background:var(--white);padding:9px 14px;font-size:.77rem;font-weight:600;color:var(--muted);border-top:1px solid var(--border);display:flex;align-items:center;gap:6px;}}

/* ── FUNZIONALITÀ ── */
#funzionalita{{background:var(--white)}}
.features-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;}}
.feature-card{{background:var(--offwhite);border:1px solid var(--border);border-radius:var(--radius);padding:28px;transition:border-color .2s,box-shadow .2s;}}
.feature-card:hover{{border-color:var(--teal);box-shadow:0 4px 20px rgba(116,179,206,.12);}}
.feature-icon{{width:46px;height:46px;border-radius:10px;background:rgba(116,179,206,.15);display:flex;align-items:center;justify-content:center;color:var(--teal);margin-bottom:16px;}}
.feature-card h3{{font-family:'Outfit',sans-serif;font-weight:700;font-size:1rem;margin-bottom:8px}}
.feature-card p{{font-size:.88rem;color:var(--muted);line-height:1.6}}

/* ── RUOLI ── */
#ruoli{{background:var(--offwhite)}}
.roles-grid{{display:grid;grid-template-columns:1fr 1fr;gap:28px;}}
.role-card{{background:var(--white);border:1px solid var(--border);border-radius:16px;overflow:hidden;box-shadow:var(--shadow);transition:box-shadow .25s;}}
.role-card:hover{{box-shadow:var(--shadow-lg)}}
.role-screenshot img,.role-screenshot .placeholder,.role-screenshot-wrap img{{width:100%;aspect-ratio:16/9;object-fit:cover;object-position:top;}}
.role-screenshot-wrap{{overflow:hidden;transition:opacity .2s;}}
.role-screenshot-wrap:hover img{{opacity:.9;}}
.role-info{{padding:24px 28px}}
.role-badge{{display:inline-flex;align-items:center;gap:7px;background:var(--offwhite);border:1px solid var(--border);border-radius:100px;padding:5px 14px;font-size:.8rem;font-weight:600;color:var(--navy);margin-bottom:10px;}}
.role-info h3{{font-family:'DM Serif Display',serif;font-size:1.35rem;margin-bottom:12px;}}
.role-features{{list-style:none;display:flex;flex-direction:column;gap:7px}}
.role-features li{{display:flex;align-items:flex-start;gap:9px;font-size:.88rem;color:var(--muted);line-height:1.45;}}
.role-features li::before{{content:'';width:5px;height:5px;border-radius:50%;background:var(--teal);flex-shrink:0;margin-top:8px;}}
.role-types{{display:flex;flex-wrap:wrap;gap:5px;margin-top:12px;}}
.role-type-chip{{font-size:.73rem;font-weight:600;padding:3px 10px;border-radius:100px;background:rgba(116,179,206,.1);border:1px solid rgba(116,179,206,.22);color:var(--teal-dark);}}

/* ── CTA ── */
#cta{{background:var(--navy);color:var(--white);text-align:center;}}
#cta h2{{font-size:clamp(2rem,3.5vw,3rem);color:var(--white);margin-bottom:16px;}}
#cta p{{color:rgba(255,255,255,.6);font-size:1.05rem;margin-bottom:40px;max-width:500px;margin-left:auto;margin-right:auto;}}
.cta-actions{{display:flex;gap:16px;justify-content:center;flex-wrap:wrap;margin-bottom:56px}}
.btn-white{{background:var(--white);color:var(--navy);font-weight:700;}}
.btn-white:hover{{background:#f0f7fc;box-shadow:0 8px 30px rgba(255,255,255,.18)}}
.contact-row{{display:flex;gap:28px;justify-content:center;flex-wrap:wrap;padding-top:40px;border-top:1px solid rgba(255,255,255,.1);}}
.contact-item{{display:flex;align-items:center;gap:9px;font-size:.95rem;color:rgba(255,255,255,.65);}}
.contact-item a{{color:var(--teal)}}
.contact-item svg{{color:rgba(255,255,255,.35);}}

footer{{background:#0f1e2a;padding:28px 32px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px;}}
.footer-tagline{{font-size:.85rem;color:rgba(255,255,255,.3);font-style:italic}}
.footer-copy{{font-size:.82rem;color:rgba(255,255,255,.25)}}

/* ── LIGHTBOX ── */
.lb-overlay{{display:none;position:fixed;inset:0;z-index:999;background:rgba(10,20,30,.88);backdrop-filter:blur(5px);align-items:center;justify-content:center;padding:20px;}}
.lb-overlay.open{{display:flex;}}
.lb-box{{position:relative;max-width:1240px;width:100%;border-radius:14px;overflow:hidden;box-shadow:0 32px 100px rgba(0,0,0,.5);}}
.lb-box img{{width:100%;display:block;}}
.lb-close{{position:absolute;top:12px;right:12px;width:36px;height:36px;border-radius:50%;background:rgba(255,255,255,.12);backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,.18);color:#fff;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background .2s;}}
.lb-close:hover{{background:rgba(255,255,255,.22)}}
.lb-caption{{position:absolute;bottom:0;left:0;right:0;background:linear-gradient(transparent,rgba(10,20,30,.8));color:#fff;padding:28px 20px 16px;font-size:.85rem;font-family:'Outfit',sans-serif;}}

/* ── DEMO MODAL ── */
.demo-overlay{{display:none;position:fixed;inset:0;z-index:1000;background:rgba(10,20,30,.72);backdrop-filter:blur(6px);align-items:center;justify-content:center;padding:24px;overflow-y:auto;}}
.demo-overlay.open{{display:flex;}}
.demo-box{{background:var(--white);border-radius:20px;max-width:560px;width:100%;box-shadow:0 32px 100px rgba(0,0,0,.3);overflow:hidden;margin:auto;}}
.demo-header{{background:var(--navy);padding:28px 32px 24px;position:relative;}}
.demo-header h3{{font-family:'DM Serif Display',serif;font-size:1.65rem;color:var(--white);margin-bottom:5px;}}
.demo-header p{{font-size:.88rem;color:rgba(255,255,255,.5);}}
.demo-close{{position:absolute;top:14px;right:14px;width:30px;height:30px;border-radius:50%;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.15);color:rgba(255,255,255,.6);cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background .2s;}}
.demo-close:hover{{background:rgba(255,255,255,.2)}}
.demo-body{{padding:24px 32px 28px;}}
.form-row{{display:grid;grid-template-columns:1fr 1fr;gap:14px;}}
.form-group{{display:flex;flex-direction:column;gap:5px;margin-bottom:14px;}}
.form-group label{{font-size:.8rem;font-weight:600;color:var(--navy);}}
.form-group input,.form-group select,.form-group textarea{{border:1.5px solid var(--border);border-radius:8px;padding:9px 13px;font-family:'Outfit',sans-serif;font-size:.9rem;color:var(--navy);outline:none;transition:border-color .2s;background:var(--white);}}
.form-group input:focus,.form-group select:focus,.form-group textarea:focus{{border-color:var(--teal);box-shadow:0 0 0 3px rgba(116,179,206,.13);}}
.form-group textarea{{resize:vertical;min-height:80px;}}
.form-group select{{appearance:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%235b7a91' stroke-width='1.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 13px center;}}
.form-submit{{width:100%;padding:13px;border-radius:10px;background:var(--teal);color:var(--white);font-family:'Outfit',sans-serif;font-size:.95rem;font-weight:700;border:none;cursor:pointer;transition:all .2s;margin-top:6px;}}
.form-submit:hover{{background:var(--teal-dark);box-shadow:0 6px 20px rgba(116,179,206,.35);}}
.form-success{{text-align:center;padding:36px 20px;display:none;}}
.form-success .s-icon{{color:var(--teal);margin-bottom:16px;display:flex;justify-content:center;}}
.form-success h4{{font-family:'DM Serif Display',serif;font-size:1.55rem;margin-bottom:10px;}}
.form-success p{{color:var(--muted);font-size:.92rem;}}

@media(max-width:900px){{
  .hero-inner,.problema-grid,.roles-grid,.efficienza-inner,.sic-grid,.comms-top{{grid-template-columns:1fr}}
  .hero-visual,.hero-badge{{display:none}}
  .screens-grid,.features-grid{{grid-template-columns:1fr 1fr}}
  .perso-callout-bar,.dashboards-strip,.comms-bottom,.sic-stat-row{{grid-template-columns:1fr 1fr}}
}}
@media(max-width:600px){{
  .screens-grid,.features-grid,.roles-grid,.perso-screens{{grid-template-columns:1fr}}
  section{{padding:64px 0}}
  .nav-links{{display:none}}
  .form-row{{grid-template-columns:1fr}}
  .demo-body,.demo-header{{padding-left:20px;padding-right:20px;}}
  .sic-stat-row{{grid-template-columns:1fr}}
}}
</style>
</head>
<body>

<!-- DEMO MODAL -->
<div class="demo-overlay" id="demoModal" onclick="if(event.target===this)closeDemo()">
  <div class="demo-box">
    <div class="demo-header">
      <button class="demo-close" onclick="closeDemo()">{svg("x",14)}</button>
      <h3>Richiedi una demo gratuita</h3>
      <p>Ti ricontatteremo entro 24 ore per organizzare una sessione personalizzata.</p>
    </div>
    <div class="demo-body">
      <div id="demoForm">
        <div class="form-row">
          <div class="form-group"><label>Nome *</label><input type="text" placeholder="Mario" required></div>
          <div class="form-group"><label>Cognome *</label><input type="text" placeholder="Rossi" required></div>
        </div>
        <div class="form-group"><label>Nome della struttura *</label><input type="text" placeholder="es. Casa di Cura Villa Verde" required></div>
        <div class="form-row">
          <div class="form-group"><label>Tipo di struttura</label>
            <select><option value="">Seleziona...</option><option>RSA / Casa di riposo</option><option>Clinica privata</option><option>Ospedale</option><option>Ambulatorio</option><option>Centro di riabilitazione</option><option>Altro</option></select>
          </div>
          <div class="form-group"><label>Ruolo</label>
            <select><option value="">Seleziona...</option><option>Direttore sanitario</option><option>Coordinatore infermieristico</option><option>Responsabile IT</option><option>Medico</option><option>Amministratore</option><option>Altro</option></select>
          </div>
        </div>
        <div class="form-row">
          <div class="form-group"><label>Email *</label><input type="email" placeholder="mario.rossi@struttura.it" required></div>
          <div class="form-group"><label>Telefono</label><input type="tel" placeholder="+39 XXX XXX XXXX"></div>
        </div>
        <div class="form-group"><label>Note o richieste specifiche</label><textarea placeholder="Raccontaci la vostra situazione attuale e cosa vorreste migliorare..."></textarea></div>
        <button class="form-submit" onclick="submitDemo()">Invia richiesta demo</button>
      </div>
      <div class="form-success" id="demoSuccess">
        <div class="s-icon">{svg("check-circle",48,"var(--teal)")}</div>
        <h4>Richiesta inviata!</h4>
        <p>Grazie, ti ricontatteremo entro 24 ore per organizzare la tua demo personalizzata.</p>
      </div>
    </div>
  </div>
</div>

<!-- LIGHTBOX -->
<div class="lb-overlay" id="lbModal" onclick="closeLB()">
  <div class="lb-box" onclick="event.stopPropagation()">
    <img id="lbImg" src="" alt="">
    <button class="lb-close" onclick="closeLB()">{svg("x",14)}</button>
    <div class="lb-caption" id="lbCaption"></div>
  </div>
</div>

<!-- NAV -->
<nav>
  <div class="nav-inner">
    <a href="#hero" class="logo">
      <div class="logo-badge">A</div>
      <span class="logo-text">Assis<span>Team24</span></span>
    </a>
    <ul class="nav-links">
      <li><a href="#cartella">Cartella Clinica</a></li>
      <li><a href="#efficienza">Semplicità</a></li>
      <li><a href="#sicurezza">Sicurezza</a></li>
      <li><a href="#personalizzazione">Personalizzazione</a></li>
      <li><a href="#comunicazioni">Comunicazioni</a></li>
      <li><a href="#ruoli">Ruoli</a></li>
      <li><a href="#cta">Contatti</a></li>
    </ul>
    <button class="btn btn-primary" onclick="openDemo()">Richiedi Demo</button>
  </div>
</nav>

<!-- HERO -->
<section id="hero">
  <div class="hero-inner">
    <div class="hero-copy">
      <div class="label">Gestionale per strutture sanitarie</div>
      <h1>La cartella clinica digitale che <em>semplifica la cura.</em></h1>
      <p>Centralizza cartelle cliniche, attività, comunicazioni e processi in un unico ambiente digitale. Meno frammentazione, più tempo per i pazienti.</p>
      <div class="hero-actions">
        <button class="btn btn-primary btn-lg" onclick="openDemo()">Richiedi una demo gratuita</button>
      </div>
      <div class="hero-stats">
        <div class="stat-item"><h3>100%</h3><p>Personalizzabile</p></div>
        <div class="stat-item"><h3>10 min</h3><p>Finestra sicurezza</p></div>
        <div class="stat-item"><h3>Multi</h3><p>Struttura</p></div>
        <div class="stat-item"><h3>6</h3><p>Profili di accesso</p></div>
      </div>
    </div>
    <div class="hero-visual">
      <div class="browser-frame">
        <div class="browser-bar">
          <div class="browser-dot" style="background:#ff5f57"></div>
          <div class="browser-dot" style="background:#febc2e"></div>
          <div class="browser-dot" style="background:#28c840"></div>
          <div class="browser-url">assisteam24.vercel.app/staff/medico</div>
        </div>
        {img_tag("medico_dashboard","Dashboard Medico")}
      </div>
      <div class="hero-badge">
        <div class="hero-badge-icon">{svg("stethoscope",18)}</div>
        Dashboard Medico · in tempo reale
      </div>
    </div>
  </div>
</section>

<!-- PROBLEMA → SOLUZIONE -->
<section id="problema">
  <div class="container">
    <div class="problema-grid">
      <div class="problema-copy">
        <div class="label">Il problema</div>
        <h2>La frammentazione rallenta la cura.</h2>
        <p>Ogni giorno strutture e professionisti gestiscono cartelle cliniche, attività operative, comunicazioni, turni e informazioni distribuite su più sistemi e processi. Questa frammentazione rallenta il lavoro quotidiano, aumenta la complessità organizzativa e sottrae tempo alla cura del paziente.</p>
      </div>
      <div>
        <div class="label" style="color:var(--teal);background:rgba(116,179,206,.15)">La soluzione</div>
        <ul class="checklist">
          {check_li("Cartella clinica digitale centralizzata e multidisciplinare")}
          {check_li("Comunicazioni e alert in tempo reale tra i reparti")}
          {check_li("Gestione turni e disponibilità del personale integrata")}
          {check_li("Accessi profilati per ruolo: da medico ad amministrazione")}
          {check_li("Tracciabilità completa di terapie, parametri e somministrazioni")}
          {check_li("Sicurezza integrata con conferma swipe e finestra di modifica")}
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- CARTELLA CLINICA -->
<section id="cartella">
  <div class="container">
    <div class="section-center">
      <div class="label">Il cuore del prodotto</div>
      <h2>Cartella Clinica Digitale</h2>
      <p>Una gestione centralizzata e multidisciplinare del paziente, progettata per garantire continuità assistenziale, tracciabilità e coordinamento tra professionisti. Clicca su ogni schermata per ingrandirla.</p>
    </div>
    <div class="features-row">
      <div class="feature-tag"><span class="dot"></span>Diario clinico</div>
      <div class="feature-tag"><span class="dot"></span>Terapie e somministrazioni</div>
      <div class="feature-tag"><span class="dot"></span>PAI e scale di valutazione</div>
      <div class="feature-tag"><span class="dot"></span>Parametri vitali</div>
      <div class="feature-tag"><span class="dot"></span>Presidi</div>
      <div class="feature-tag"><span class="dot"></span>Allergie</div>
    </div>
    <div class="screens-grid">
      {lbcard("sub_terapia","sub_terapia_s","Pagina terapie","Terapie attive e prescrizioni")}
      {lbcard("sub_scale_index","sub_scale_index_s","Scale di valutazione","Indice scale: Braden, Morse, ADL e altre")}
      {lbcard("sub_diaria","sub_diaria_s","Diario clinico","Diario clinico quotidiano e note")}
      {lbcard("sub_parametri","sub_parametri_s","Parametri vitali","Rilevazione e storico parametri")}
      {lbcard("sub_presidi","sub_presidi_s","Presidi","Registro presidi e ausili assegnati")}
      {lbcard("cartella_moduli_section","cartella_moduli_top","Moduli personalizzabili","Servizio psicologico, nutrizione, logopedia e altri moduli specialistici")}
    </div>
  </div>
</section>

<!-- EFFICIENZA -->
<section id="efficienza">
  <div class="container">
    <div class="efficienza-inner">
      <div class="efficienza-copy">
        <div class="label">Ottimizzazione operativa</div>
        <h2>Meno tempo sulle schermate, più tempo sui pazienti.</h2>
        <p>Le attività ripetitive che ogni operatore affronta decine di volte al giorno sono state riprogettate per essere il più rapide possibile.</p>
        <ul class="eff-points">
          {eff_li("pill","Terapie multi-paziente:","l'operatore seleziona più pazienti e conferma la somministrazione di una terapia in un solo passaggio, senza ripetere l'operazione paziente per paziente.")}
          {eff_li("file-text","Diaria collettiva:","è possibile redigere una nota di diaria e applicarla a più pazienti contemporaneamente, personalizzando solo le variazioni individuali — ideale per turni con molti assistiti.")}
          {eff_li("list","Tracciabilità automatica:","ogni azione viene registrata con timestamp, operatore e contesto clinico, eliminando la compilazione manuale dei registri di reparto.")}
        </ul>
      </div>
      <div class="panel-stack">
        <div class="panel-frame">
          <div class="panel-bar">
            <div class="panel-bar-dot" style="background:#ff5f57"></div>
            <div class="panel-bar-dot" style="background:#febc2e"></div>
            <div class="panel-bar-dot" style="background:#28c840"></div>
            <span class="panel-bar-label">Panel Terapie — selezione multi-paziente</span>
          </div>
          {panel_img("op_terapie_a","Panel terapie","Panel Terapie — selezione multi-paziente")}
          <div class="panel-caption">Seleziona più pazienti e somministra in un click</div>
        </div>
        <div class="panel-frame">
          <div class="panel-bar">
            <div class="panel-bar-dot" style="background:#ff5f57"></div>
            <div class="panel-bar-dot" style="background:#febc2e"></div>
            <div class="panel-bar-dot" style="background:#28c840"></div>
            <span class="panel-bar-label">Panel Diarie — scrittura collettiva</span>
          </div>
          {panel_img("op_diarie_a","Panel diarie","Panel Diarie — scrittura collettiva")}
          <div class="panel-caption">Redigi la diaria una volta, applicala a tutti</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- SICUREZZA -->
<section id="sicurezza">
  <div class="container">
    <div class="sic-grid">
      <div class="sic-copy">
        <div class="label">Sicurezza integrata</div>
        <h2>Ogni azione è tracciata, verificata e reversibile.</h2>
        <p>In un contesto clinico, un errore di registrazione può avere conseguenze reali. AssisTeam24 è progettato con meccanismi attivi di sicurezza che proteggono l'integrità dei dati e prevengono errori operativi.</p>
        <div class="sic-cards">
          <div class="sic-card">
            <div class="sic-icon">{svg("clock",20)}</div>
            <div>
              <h4>Finestra di modifica di 10 minuti</h4>
              <p>Ogni azione registrata può essere modificata o annullata entro 10 minuti dalla sua creazione. Oltre questa finestra, il dato diventa immodificabile, garantendo l'integrità del registro clinico.</p>
            </div>
          </div>
          <div class="sic-card">
            <div class="sic-icon">{svg("swipe",20)}</div>
            <div>
              <h4>Conferma swipe per azioni critiche</h4>
              <p>Le operazioni a elevato impatto clinico richiedono una gesture di swipe deliberata, eliminando conferme accidentali.</p>
            </div>
          </div>
          <div class="sic-card">
            <div class="sic-icon">{svg("shield-check",20)}</div>
            <div>
              <h4>Log immutabile e audit trail</h4>
              <p>Ogni azione è registrata con utente, timestamp e contesto. L'audit trail è accessibile agli amministratori e rispetta i requisiti di tracciabilità per strutture sanitarie accreditate.</p>
            </div>
          </div>
        </div>
      </div>
      <div>
        <div class="sic-stat-row" style="margin-bottom:24px">
          <div class="sic-stat">
            <div class="num">10'</div>
            <p>Finestra massima<br>di modifica di ogni azione</p>
          </div>
          <div class="sic-stat">
            <div class="num">0</div>
            <p>Conferme accidentali<br>grazie al sistema swipe</p>
          </div>
          <div class="sic-stat">
            <div class="num">100%</div>
            <p>Azioni tracciate<br>con timestamp e autore</p>
          </div>
          <div class="sic-stat">
            <div class="num">GDPR</div>
            <p>Gestione dati<br>conforme al regolamento</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- PERSONALIZZAZIONE -->
<section id="personalizzazione">
  <div class="container">
    <div class="perso-head">
      <div class="label">Esperienza su misura</div>
      <h2>Ogni utente vede solo ciò che gli serve.</h2>
      <p>AssisTeam24 non è uguale per tutti. Ogni profilo ha la propria interfaccia, il proprio menu e le proprie azioni esclusive — alcune funzioni esistono solo per chi le può eseguire.</p>
    </div>

    <div class="spotlight-rows">
      <div class="spotlight-row">
        <div class="spotlight-icon">{svg("stethoscope",20)}</div>
        <div class="spotlight-body">
          <h4>Medico <span class="exclusive-badge">Azione esclusiva</span></h4>
          <p>Solo il medico può <strong>prescrivere e modificare le terapie</strong> nella cartella clinica del paziente. Il pulsante di prescrizione non compare ad altri profili.</p>
        </div>
      </div>
      <div class="spotlight-row">
        <div class="spotlight-icon">{svg("user-cross",20)}</div>
        <div class="spotlight-body">
          <h4>Operatore sanitario <span class="exclusive-badge">Azione esclusiva</span></h4>
          <p><strong>Registrazione della somministrazione</strong> e <strong>controlli giornalieri d'emergenza</strong>: funzioni visibili e utilizzabili solo dagli operatori sanitari, invisibili agli altri ruoli.</p>
        </div>
      </div>
      <div class="spotlight-row">
        <div class="spotlight-icon">{svg("clipboard",20)}</div>
        <div class="spotlight-body">
          <h4>Coordinatore <span class="exclusive-badge">Azione esclusiva</span></h4>
          <p>Solo il coordinatore può <strong>assegnare, modificare e sostituire i turni</strong> del personale di reparto — con vista completa sulle disponibilità.</p>
        </div>
      </div>
    </div>

    <div class="perso-callout-bar">
      <div class="perso-callout teal">
        <div class="pc-icon">{svg("clock",18)}</div>
        <div>
          <h4>Countdown turno sempre visibile</h4>
          <p>Ogni utente vede il tempo rimanente al termine del turno direttamente nell'interfaccia — la gestione è sempre sincronizzata con i tempi reali di reparto.</p>
        </div>
      </div>
      <div class="perso-callout navy">
        <div class="pc-icon">{svg("sliders",18)}</div>
        <div>
          <h4>Visibilità moduli configurata dal Super Admin</h4>
          <p>L'amministratore decide quali moduli clinici ogni profilo può vedere personalizzando al meglio l'esperienza di ogni utente.</p>
        </div>
      </div>
    </div>

    <div class="dashboards-strip">
      <div class="dash-thumb" onclick="openLB(this)">
        {img_tag("medico_dashboard","Dashboard Medico")}
        <div class="dash-thumb-label">{svg("stethoscope",12)} Medico</div>
      </div>
      <div class="dash-thumb" onclick="openLB(this)">
        {img_tag("coord_dashboard","Dashboard Coordinatore")}
        <div class="dash-thumb-label">{svg("clipboard",12)} Coordinatore</div>
      </div>
      <div class="dash-thumb" onclick="openLB(this)">
        {img_tag("operatore_dashboard","Dashboard Operatore")}
        <div class="dash-thumb-label">{svg("user-cross",12)} Operatore</div>
      </div>
      <div class="dash-thumb" onclick="openLB(this)">
        {img_tag("superadmin_dashboard","Dashboard Super Admin")}
        <div class="dash-thumb-label">{svg("settings",12)} Super Admin</div>
      </div>
    </div>
  </div>
</section>

<!-- COMUNICAZIONI -->
<section id="comunicazioni">
  <div class="container">
    <div class="comms-top">
      <div class="comms-copy-left">
        <div class="label">Comunicazioni di reparto</div>
        <h2>Informazioni critiche sempre al posto giusto.</h2>
        <p>Il flusso di comunicazione è integrato nel gestionale: non servono app esterne, email o telefonate per aggiornare il team su situazioni cliniche urgenti o ordinarie.</p>
        <ul class="comms-points">
          <li>
            <div class="comms-pt-icon">{svg("alert",18)}</div>
            <div class="ct">
              <strong>Alert automatici per parametri critici</strong>
              Quando i parametri vitali superano le soglie cliniche configurate, il sistema genera un alert immediato visibile a medici e coordinatori.
            </div>
          </li>
          <li>
            <div class="comms-pt-icon">{svg("message",18)}</div>
            <div class="ct">
              <strong>Messaggi a singoli o a tutto il team</strong>
              Scegli il destinatario: un singolo operatore, un ruolo specifico o l'intero reparto. Le comunicazioni sono archiviate e rintracciabili.
            </div>
          </li>
          <li>
            <div class="comms-pt-icon">{svg("eye",18)}</div>
            <div class="ct">
              <strong>Visibilità contestuale per ruolo</strong>
              Gli alert clinici raggiungono chi ha la competenza per agire: al medico, all'infermiere di turno o al coordinatore — mai in modo indiscriminato.
            </div>
          </li>
        </ul>
      </div>
      <div class="comms-featured" onclick="openLB(this)">
        {img_tag("comms_medico","Inbox comunicazioni del medico")}
        <div class="comms-featured-label">{svg("message",13)} Inbox comunicazioni — vista Medico</div>
      </div>
    </div>
    <div class="comms-bottom">
      <div class="comms-small" onclick="openLB(this)">
        {img_tag("comms_alert_panel","Pannello alert automatici")}
        <div class="comms-small-label">{svg("alert",12)} Alert automatici parametri critici</div>
      </div>
      <div class="comms-small" onclick="openLB(this)">
        {img_tag("comms_nuova_msg","Nuova comunicazione con scelta destinatario")}
        <div class="comms-small-label">{svg("send",12)} Nuova comunicazione con scelta destinatario</div>
      </div>
    </div>
  </div>
</section>

<!-- FUNZIONALITÀ -->
<section id="funzionalita">
  <div class="container">
    <div class="section-head">
      <div class="label">L'ecosistema</div>
      <h2>Tutto ciò che serve, in un solo posto.</h2>
      <p>AssisTeam24 copre ogni aspetto operativo della struttura sanitaria, dal letto del paziente alla gestione amministrativa.</p>
    </div>
    <div class="features-grid">
      <div class="feature-card">{feat_icon("bar-chart")}<h3>Dashboard operativa</h3><p>Panoramica in tempo reale su pazienti, attività e alert clinici per ogni profilo di accesso.</p></div>
      <div class="feature-card">{feat_icon("hospital")}<h3>Gestione reparto</h3><p>Lista pazienti strutturata con stato, reparto assegnato e accesso diretto alla cartella clinica.</p></div>
      <div class="feature-card">{feat_icon("calendar")}<h3>Calendario clinico</h3><p>Pianificazione visite, appuntamenti e attività con vista mensile, settimanale e giornaliera.</p></div>
      <div class="feature-card">{feat_icon("refresh")}<h3>Turni e disponibilità</h3><p>Creazione e gestione dei turni del personale con visualizzazione delle disponibilità per reparto.</p></div>
      <div class="feature-card">{feat_icon("message")}<h3>Comunicazioni & alert</h3><p>Messaggistica interna strutturata, notifiche cliniche e alert urgenti tra operatori e reparti.</p></div>
      <div class="feature-card">{feat_icon("lock")}<h3>Accessi profilati</h3><p>Ogni utente accede solo a ciò che è rilevante per il suo ruolo, con permessi configurabili dall'amministratore.</p></div>
      <div class="feature-card">{feat_icon("list")}<h3>Tracciabilità completa</h3><p>Log di ogni azione clinica e operativa, con storico somministrazioni e modifiche alla cartella.</p></div>
      <div class="feature-card">{feat_icon("alert")}<h3>Controlli di emergenza</h3><p>Schede rapide per la rilevazione parametri in situazioni critiche, accessibili da operatori e infermieri.</p></div>
      <div class="feature-card">{feat_icon("users")}<h3>Area familiare</h3><p>Modulo dedicato alla comunicazione con familiari e caregiver, con aggiornamenti controllati sullo stato del paziente.</p></div>
    </div>
  </div>
</section>

<!-- RUOLI -->
<section id="ruoli">
  <div class="container">
    <div class="section-head">
      <div class="label">6 profili di accesso</div>
      <h2>Uno strumento per ogni ruolo.</h2>
      <p>AssisTeam24 si adatta al profilo di ogni operatore sanitario, mostrando solo le funzionalità rilevanti e riducendo il carico cognitivo quotidiano.</p>
    </div>
    <div class="roles-grid">

      {role_card("role_medico_terapia","stethoscope","Medico","Pagina terapie in evidenza",[
        "Cartelle cliniche e diario del paziente",
        "Prescrizione e revisione terapie attive",
        "Calendario visite e appuntamenti",
        "Piano Assistenziale Individuale (PAI) e scale di valutazione",
        "Comunicazioni con il team multidisciplinare",
      ])}

      {role_card("role_coord_turni","clipboard","Coordinatore di reparto","Gestione turni del personale",[
        "Pianificazione e visualizzazione turni settimanali",
        "Monitoraggio disponibilità e sostituzioni",
        "Gestione anagrafica del personale",
        "Ricezione e distribuzione farmaci",
        "Alert clinici e comunicazioni urgenti",
      ])}

      {role_card("role_operatore_controlli","user-cross","Operatore sanitario","Attività quotidiane semplificate",[
        "Conferma somministrazione terapie con swipe in un click",
        "Compilazione diaria e schede di controllo rapido",
        "Rilevazione parametri vitali con inserimento guidato",
        "Visualizzazione turni assegnati con countdown fine turno",
        "Comunicazioni con medico e coordinatore",
      ],["Infermiere","OSS","Fisioterapista","Nutrizionista","Logopedista","Terapista occupazionale","Psicologo","Assistente sociale","Educatrice","Altro"])}

      {role_card("superadmin_staff_crea","settings","Super Amministratore","Creazione e configurazione utenti",[
        "Creazione nuovi utenti e assegnazione del profilo",
        "Configurazione permessi granulari per struttura e reparto",
        "Ogni utente vede solo le funzioni e i reparti di sua competenza",
        "Gestione multi-struttura centralizzata",
        "Monitoraggio alert di sistema e log operativi",
      ])}

      {role_card("role_admin_crea_paziente","folder-user","Amministrazione","Registrazione nuovo paziente",[
        "Registrazione nuovi pazienti e gestione anagrafica",
        "Visualizzazione reparto e stato di ricovero",
        "Accesso alle informazioni amministrative della cartella",
        "Coordinamento con il personale sanitario per l'accoglienza",
        "Gestione documenti, consensi e privacy GDPR",
      ])}

      {role_card("role_mdb_cartella","user-laptop","Medico di base","Cartella clinica del proprio paziente",[
        "Visibilità sulle cartelle dei propri assistiti ricoverati",
        "Possibilità di aggiungere note e aggiornamenti clinici",
        "Comunicazione diretta con il team medico e infermieristico",
        "Ricezione di alert su variazioni cliniche rilevanti",
        "Accesso limitato ai soli pazienti di pertinenza",
      ])}

    </div>
  </div>
</section>

<!-- CTA -->
<section id="cta">
  <div class="container">
    <div class="label" style="color:var(--teal);background:rgba(116,179,206,.15);margin-bottom:28px">Inizia oggi</div>
    <h2>Pronto a trasformare<br>la tua struttura?</h2>
    <p>Richiedi una demo gratuita personalizzata. Ti mostriamo AssisTeam24 in azione nel contesto della tua struttura sanitaria.</p>
    <div class="cta-actions">
      <button class="btn btn-white btn-xl" onclick="openDemo()">Richiedi demo gratuita</button>
    </div>
    <div class="contact-row">
      {contact_item("mail", '<a href="mailto:info@assisteam24.it">info@assisteam24.it</a>')}
      {contact_item("globe", '<a href="https://www.assisteam24.it">www.assisteam24.it</a>')}
      {contact_item("phone", '+39 XXX XXX XXXX')}
    </div>
  </div>
</section>

<footer>
  <div style="display:flex;align-items:center;gap:10px;">
    <div class="logo-badge" style="width:32px;height:32px;font-size:.9rem">A</div>
    <span style="font-family:'Outfit',sans-serif;font-weight:700;font-size:.95rem;color:rgba(255,255,255,.75)">Assis<span style="color:var(--teal)">Team24</span></span>
  </div>
  <span class="footer-tagline">Un nuovo modo di organizzare la cura.</span>
  <span class="footer-copy">&copy; 2026 AssisTeam24. Tutti i diritti riservati.</span>
</footer>

<script>
function openDemo(){{document.getElementById('demoModal').classList.add('open');document.body.style.overflow='hidden';}}
function closeDemo(){{document.getElementById('demoModal').classList.remove('open');document.body.style.overflow='';}}
function submitDemo(){{document.getElementById('demoForm').style.display='none';document.getElementById('demoSuccess').style.display='block';setTimeout(closeDemo,3500);}}
function openLB(card){{
  const img=card.querySelector('img');
  if(!img)return;
  const cap=card.querySelector('.screen-label,.perso-screen-label');
  document.getElementById('lbImg').src=img.src;
  document.getElementById('lbCaption').textContent=cap?cap.innerText.replace(/^\W+/,'').trim():img.alt;
  document.getElementById('lbModal').classList.add('open');
  document.body.style.overflow='hidden';
}}
function openLBSrc(src,cap){{
  if(!src)return;
  document.getElementById('lbImg').src=src;
  document.getElementById('lbCaption').textContent=cap||'';
  document.getElementById('lbModal').classList.add('open');
  document.body.style.overflow='hidden';
}}
function closeLB(){{document.getElementById('lbModal').classList.remove('open');document.body.style.overflow='';}}
document.addEventListener('keydown',e=>{{if(e.key==='Escape'){{closeLB();closeDemo();}}}});
</script>
</body>
</html>
"""

with open("index.html","w",encoding="utf-8") as f:
    f.write(html)

size = os.path.getsize("index.html")
print(f"✓ index.html — {size/1024/1024:.1f} MB")
