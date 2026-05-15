#!/usr/bin/env python3
"""Capture communications and alert screenshots at 1920x1080."""
import os, time
from playwright.sync_api import sync_playwright

BASE = "https://assisteam24.vercel.app"
DIR  = "screens_hd"
VP   = {"width": 1920, "height": 1080}

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

def shot(page, name, scroll_y=0):
    if scroll_y > 0:
        page.evaluate(f"window.scrollTo(0,{scroll_y})")
        time.sleep(0.8)
    else:
        page.evaluate("window.scrollTo(0,0)")
        time.sleep(0.3)
    path = f"{DIR}/{name}.jpg"
    page.screenshot(path=path, type="jpeg", quality=88, full_page=False)
    kb = os.path.getsize(path)//1024
    print(f"  ✓ {name}.jpg ({kb} KB)")

def dump(page):
    links = page.evaluate("""() =>
        Array.from(document.querySelectorAll('a[href],button'))
            .map(e=>({t:e.innerText.trim().substring(0,60), h:e.href||'btn'}))
            .filter(e=>e.t)
    """)
    for l in links[:25]:
        print(f"    '{l['t']}' → {l['h']}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    # ── MEDICO comunicazioni ─────────────────────────────────────────
    print("\n=== MEDICO comunicazioni & alert ===")
    ctx = browser.new_context(viewport=VP)
    pg = ctx.new_page()
    login(pg, "VM001")

    go(pg, "/staff/medico/comunicazioni")
    shot(pg, "comms_medico")
    shot(pg, "comms_medico_s", scroll_y=400)

    # Alert panel (click alert badge if present)
    go(pg, "/staff/medico")
    time.sleep(1)
    # Try to open alert dropdown/panel
    clicked = pg.evaluate("""() => {
        const els = [...document.querySelectorAll('button,a')];
        const a = els.find(e => e.innerText.toLowerCase().includes('alert') || e.getAttribute('aria-label')?.toLowerCase().includes('alert'));
        if (a) { a.click(); return true; }
        return false;
    }""")
    if clicked:
        time.sleep(1.5)
        shot(pg, "comms_alert_panel")

    pg.close(); ctx.close()

    # ── OPERATORE comunicazioni ──────────────────────────────────────
    print("\n=== OPERATORE comunicazioni ===")
    ctx = browser.new_context(viewport=VP)
    pg = ctx.new_page()
    login(pg, "VM003")

    go(pg, "/staff/operatore/comunicazioni")
    shot(pg, "comms_operatore")
    shot(pg, "comms_operatore_s", scroll_y=400)

    # Prova a creare nuova comunicazione
    clicked = pg.evaluate("""() => {
        const els = [...document.querySelectorAll('button,a')];
        const b = els.find(e => {
            const t = e.innerText.toLowerCase();
            return t.includes('nuova') || t.includes('scrivi') || t.includes('invia') || t.includes('componi') || t.includes('+') || t.includes('new');
        });
        if (b) { b.click(); return b.innerText.trim(); }
        return null;
    }""")
    if clicked:
        time.sleep(1.5)
        shot(pg, "comms_nuova_msg")
        print(f"    → opened: '{clicked}'")

    pg.close(); ctx.close()

    # ── COORDINATORE comunicazioni ───────────────────────────────────
    print("\n=== COORDINATORE comunicazioni ===")
    ctx = browser.new_context(viewport=VP)
    pg = ctx.new_page()
    login(pg, "VM002")

    go(pg, "/staff/coordinatore/comunicazioni")
    shot(pg, "comms_coordinatore")
    shot(pg, "comms_coordinatore_s", scroll_y=400)

    # Alert page
    go(pg, "/staff/coordinatore/alert", wait=2)
    if "login" not in pg.url:
        shot(pg, "comms_alert_coord")

    pg.close(); ctx.close()

    # ── SUPER ADMIN comunicazioni ────────────────────────────────────
    print("\n=== SUPER ADMIN comunicazioni ===")
    ctx = browser.new_context(viewport=VP)
    pg = ctx.new_page()
    login(pg, "VM006")

    go(pg, "/super-admin/comunicazioni")
    shot(pg, "comms_superadmin")
    shot(pg, "comms_superadmin_s", scroll_y=400)

    pg.close(); ctx.close()
    browser.close()

print("\nDone!")
for f in sorted(os.listdir(DIR)):
    if "comms" in f or "alert" in f:
        kb = os.path.getsize(f"{DIR}/{f}")//1024
        print(f"  {f}  {kb} KB")
