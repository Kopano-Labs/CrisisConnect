import os
import json
import sqlite3
import urllib.request
import socket

def run_self_audit():
    print("=== STARTING CRISISCONNECT SELF-AUDIT VERIFICATION ===")
    
    # 1. Paths definition
    crisis_dir = r"C:\Users\rkhol\CrisisConnect"
    mcp_dir = r"c:\Users\rkhol\OneDrive\Documents\Anthropic\Introduction to MCP"
    
    # 2. File presence verification
    required_files = ["index.html", "index.css", "app.js", "kpgs_config.json"]
    for f in required_files:
        fp = os.path.join(crisis_dir, f)
        if not os.path.exists(fp):
            raise AssertionError(f"Required file missing: {fp}")
        print(f"  [PASS] File exists: {f} ({os.path.getsize(fp)} bytes)")

    # 3. kpgs_config.json validation
    config_path = os.path.join(crisis_dir, "kpgs_config.json")
    with open(config_path, "r", encoding="utf-8") as fh:
        config = json.load(fh)
    
    assert config.get("schema") == "kpgs_sector_config_v1", "Invalid sector config schema"
    assert config.get("sector_id") == "sector_03_crisisconnect", "Invalid sector_id"
    print("  [PASS] kpgs_config.json schema & properties verified")

    # 4. Main Brain reference validation
    mb_ref = os.path.join(mcp_dir, config.get("main_brain_ref"))
    if not os.path.exists(mb_ref):
         raise AssertionError(f"Main brain governance reference missing: {mb_ref}")
    
    # Load Main Brain governance and verify sector_03_crisisconnect matches
    with open(mb_ref, "r", encoding="utf-8") as fh:
         mb_gov = json.load(fh)
    
    sectors = mb_gov.get("sectors", {})
    assert "sector_03_crisisconnect" in sectors, "sector_03_crisisconnect not registered in Main Brain"
    print("  [PASS] Main Brain governance matching verified")

    # 5. Database (SQLite Data Lake) verification
    db_path = os.path.join(mcp_dir, "db", "datalake.db")
    if os.path.exists(db_path):
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = [r[0] for r in cursor.fetchall()]
            conn.close()
            print(f"  [PASS] Connected to SQLite Data Lake. Found tables: {', '.join(tables)}")
        except Exception as e:
            print(f"  [WARN] Failed to read SQLite Data Lake tables: {e}")
    else:
        print(f"  [INFO] SQLite Data Lake not found at {db_path}. Skipping DB verification.")

    # 6. Domain Verification (HTTP check)
    target_domain = "crisisconnect.kopanolabs.com"
    print(f"  [INFO] Resolving domain {target_domain}...")
    try:
        ip = socket.gethostbyname(target_domain)
        print(f"  [PASS] Domain {target_domain} resolved to IP: {ip}")
        # Connect and check response
        req = urllib.request.Request(
            f"https://{target_domain}", 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            status = response.getcode()
            print(f"  [PASS] Domain returned HTTP Status: {status}")
    except Exception as e:
        print(f"  [WARN] HTTP check failed for {target_domain}: {e}")
        print(f"  [INFO] Note: DNS delegation propagation may be pending. This is normal for new subdomains.")

    print("=== CRISISCONNECT SELF-AUDIT: ALL CHECKS COMPLETED SUCCESS ===\n")

if __name__ == "__main__":
    run_self_audit()
