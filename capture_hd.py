#!/usr/bin/env python3
"""Full HD re-capture of all screens at 1920x1080, no compaction."""
import os, time
from playwright.sync_api import sync_playwright

BASE = "https://assisteam24.vercel.app"
DIR  = "screens_hd"
os.makedirs(DIR, exist_ok=True)

def login(page, user):
    page.goto(f"{BASE}/login", wait_until="networkidle")
    time.sleep(1.5)
    page.evaluate("""(u) => {
        const s = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype,'value').set;
        const un = document.getElementById('username');
        const pw = document.getElementById('password');
        s.call(un,u); un.dispatchEvent(new Event('input',{bubbles:true}));
        s.call(pw,'123456'); pw.dispatchEvent(new Event('input',{bubbles:true}));
    }""", user)
    time.sleep(0.4)
    page.evaluate("document.querySelector('form').dispatchEvent(new Event('submit',{bubbles:true,cancelable:true}))")
    time.sleep(3.5)

def go(page, path, wait=2.5):
    page.goto(f"{BASE}{path}", wait_until="networkidle")
    time.sleep(wait)

def shot(page, name, scroll_y=0, full=False):
    if scroll_y > 0:
        page.evaluate(f"window.scrollTo(0,{scroll_y})")
        time.sleep(0.8)
    elif scroll_y == 0:
        page.evaluate("window.scrollTo(0,0)")
        time.sleep(0.3)
    path = f"{DIR}/{name}.jpg"
    page.screenshot(path=path, type="jpeg", quality=88, full_page=full)
    kb = os.path.getsize(path)//1024
    print(f"  ✓ {name}.jpg ({kb} KB)")
    return path

VP = {"width": 1920, "height": 1080}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    # ── MEDICO (VM001) ───────────────────────────────────────────────
    print("\n=== MEDICO VM001 ===")
    ctx = browser.new_context(viewport=VP)
    pg = ctx.new_page()
    login(pg, "VM001")

    go(pg, "/staff/medico");                     shot(pg, "medico_dashboard")
    go(pg, "/staff/medico/pazienti");            shot(pg, "medico_pazienti")
    go(pg, "/staff/medico/calendario");          shot(pg, "medico_calendario")
    go(pg, "/staff/medico/comunicazioni");       shot(pg, "medico_comunicazioni")
    go(pg, "/staff/medico/turni");               shot(pg, "medico_turni")

    # Cartella PT-301 — overview (top)
    go(pg, "/staff/medico/pazienti/PT-301")
    shot(pg, "cartella_overview_top")
    shot(pg, "cartella_overview_mid", scroll_y=500)

    # Cartella — sezione moduli (in basso dove ci sono tutti i moduli)
    # scroll verso il fondo dove compaiono i moduli personalizzabili
    for sy in [800, 1200, 1600, 2000, 2400]:
        pg.evaluate(f"window.scrollTo(0,{sy})")
        time.sleep(0.5)
        h = pg.evaluate("document.body.scrollHeight")
        if sy >= h - 1200:
            break
    shot(pg, "cartella_moduli_section")
    # full-page scroll per catturare anche il pannello superiore dei moduli
    go(pg, "/staff/medico/pazienti/PT-301")
    pg.evaluate("window.scrollTo(0, document.body.scrollHeight * 0.55)")
    time.sleep(0.8)
    shot(pg, "cartella_moduli_top")
    pg.evaluate("window.scrollTo(0, document.body.scrollHeight * 0.75)")
    time.sleep(0.8)
    shot(pg, "cartella_moduli_mid")

    # Sub-pages — terapia
    go(pg, "/staff/medico/pazienti/PT-301/terapia")
    shot(pg, "sub_terapia")
    shot(pg, "sub_terapia_s", scroll_y=400)

    # Sub-pages — diaria
    go(pg, "/staff/medico/pazienti/PT-301/diaria")
    shot(pg, "sub_diaria")
    shot(pg, "sub_diaria_s", scroll_y=400)

    # Sub-pages — parametri vitali
    go(pg, "/staff/medico/pazienti/PT-301/parametri-vitali")
    shot(pg, "sub_parametri")
    shot(pg, "sub_parametri_s", scroll_y=400)

    # Sub-pages — presidi
    go(pg, "/staff/medico/pazienti/PT-301/presidi")
    shot(pg, "sub_presidi")
    shot(pg, "sub_presidi_s", scroll_y=350)

    # Scale di valutazione — PAI index (lista scale)
    go(pg, "/staff/medico/pazienti/PT-301/pai")
    shot(pg, "sub_scale_index")
    shot(pg, "sub_scale_index_s", scroll_y=400)

    # Scale — Braden (aperta)
    go(pg, "/staff/medico/pazienti/PT-301/pai/braden")
    shot(pg, "sub_braden")
    shot(pg, "sub_braden_s", scroll_y=400)

    # Servizio psicologico
    go(pg, "/staff/medico/pazienti/PT-301/servizio-psicologico")
    shot(pg, "sub_psico")
    shot(pg, "sub_psico_s", scroll_y=400)

    # Piano assistenziale
    go(pg, "/staff/medico/pazienti/PT-301/piano-assistenziale")
    shot(pg, "sub_piano_ass")
    shot(pg, "sub_piano_ass_s", scroll_y=400)

    # Terapia (ruolo)
    go(pg, "/staff/medico/pazienti/PT-301/terapia")
    shot(pg, "role_medico_terapia")
    shot(pg, "role_medico_terapia_s", scroll_y=350)

    pg.close(); ctx.close()

    # ── COORDINATORE (VM002) ─────────────────────────────────────────
    print("\n=== COORDINATORE VM002 ===")
    ctx = browser.new_context(viewport=VP)
    pg = ctx.new_page()
    login(pg, "VM002")

    go(pg, "/staff/coordinatore");              shot(pg, "coord_dashboard")
    go(pg, "/staff/coordinatore/turni");        shot(pg, "coord_turni"); shot(pg, "coord_turni_s", scroll_y=400)
    go(pg, "/staff/coordinatore/personale");    shot(pg, "coord_personale")
    go(pg, "/staff/coordinatore/pazienti");     shot(pg, "coord_pazienti")
    go(pg, "/staff/coordinatore/comunicazioni");shot(pg, "coord_comunicazioni")

    # ruolo turni
    go(pg, "/staff/coordinatore/turni")
    shot(pg, "role_coord_turni")
    shot(pg, "role_coord_turni_s", scroll_y=400)

    pg.close(); ctx.close()

    # ── OPERATORE (VM003) ────────────────────────────────────────────
    print("\n=== OPERATORE VM003 ===")
    ctx = browser.new_context(viewport=VP)
    pg = ctx.new_page()
    login(pg, "VM003")

    go(pg, "/staff/operatore");                 shot(pg, "operatore_dashboard")
    go(pg, "/staff/operatore/controlli");       shot(pg, "operatore_controlli"); shot(pg, "role_operatore_controlli"); shot(pg, "role_operatore_controlli_s", scroll_y=400)

    # Terapie panel
    go(pg, "/staff/operatore/pazienti")
    pg.evaluate("""()=>{ const b=Array.from(document.querySelectorAll('button')).find(b=>b.innerText.trim().toLowerCase()==='terapie'); if(b)b.click(); }""")
    time.sleep(2)
    shot(pg, "op_terapie_a")
    shot(pg, "op_terapie_b", scroll_y=350)

    # Diarie panel
    go(pg, "/staff/operatore/pazienti")
    pg.evaluate("""()=>{ const b=Array.from(document.querySelectorAll('button')).find(b=>b.innerText.trim().toLowerCase()==='diarie'); if(b)b.click(); }""")
    time.sleep(2)
    shot(pg, "op_diarie_a")
    shot(pg, "op_diarie_b", scroll_y=350)

    pg.close(); ctx.close()

    # ── SUPER ADMIN (VM006) ──────────────────────────────────────────
    print("\n=== SUPER ADMIN VM006 ===")
    ctx = browser.new_context(viewport=VP)
    pg = ctx.new_page()
    login(pg, "VM006")

    go(pg, "/super-admin");                     shot(pg, "superadmin_dashboard")
    go(pg, "/super-admin/staff");               shot(pg, "superadmin_staff")
    go(pg, "/super-admin/pazienti");            shot(pg, "superadmin_pazienti")

    # Crea utente — clicca button
    go(pg, "/super-admin/staff")
    pg.evaluate("""()=>{ const els=[...document.querySelectorAll('button,a')]; const b=els.find(e=>e.innerText.toLowerCase().includes('crea utente')||e.innerText.toLowerCase().includes('nuovo utente')); if(b)b.click(); }""")
    time.sleep(2)
    shot(pg, "superadmin_staff_crea")
    shot(pg, "superadmin_staff_crea_s", scroll_y=400)

    # Aggiungi paziente
    go(pg, "/super-admin/pazienti")
    pg.evaluate("""()=>{ const els=[...document.querySelectorAll('button,a')]; const b=els.find(e=>e.innerText.toLowerCase().includes('aggiungi')||e.innerText.toLowerCase().includes('nuovo paziente')); if(b)b.click(); }""")
    time.sleep(2)
    shot(pg, "role_admin_crea_paziente")
    shot(pg, "role_admin_crea_paziente_s", scroll_y=400)

    pg.close(); ctx.close()

    # ── MEDICO DI BASE (VM001 come proxy) ────────────────────────────
    print("\n=== MEDICO DI BASE (via VM001) ===")
    ctx = browser.new_context(viewport=VP)
    pg = ctx.new_page()
    login(pg, "VM001")

    go(pg, "/staff/medico/pazienti/PT-301")
    shot(pg, "role_mdb_cartella")
    shot(pg, "role_mdb_cartella_s", scroll_y=350)
    go(pg, "/staff/medico/comunicazioni")
    shot(pg, "role_mdb_comunicazioni")

    pg.close(); ctx.close()
    browser.close()

print("\n=== Done! ===")
files = sorted(f for f in os.listdir(DIR) if f.endswith('.jpg'))
for f in files:
    kb = os.path.getsize(f"{DIR}/{f}")//1024
    print(f"  {f}  {kb} KB")
print(f"\nTotal: {len(files)} files")
