import subprocess
import os

def run_git():
    cwd = r"C:\Users\rkhol\CrisisConnect"
    print("=== RUNNING GIT INITIALIZATION VIA SUBPROCESS ===")
    
    steps = [
        ["git", "init"],
        ["git", "add", "."],
        ["git", "commit", "-m", "Initial commit - CrisisConnect node under KPGS Layer 6"],
        ["git", "remote", "add", "origin", "https://github.com/Kopano-Labs/CrisisConnect.git"],
        ["git", "remote", "-v"]
    ]
    
    for step in steps:
        print(f"Executing: {' '.join(step)}")
        res = subprocess.run(step, cwd=cwd, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"  [WARN] Exit code: {res.returncode}")
            if res.stdout:
                print(f"  Stdout: {res.stdout.strip()}")
            if res.stderr:
                print(f"  Stderr: {res.stderr.strip()}")
        else:
            print(f"  [SUCCESS]")
            if res.stdout:
                print(f"  Stdout: {res.stdout.strip()}")

if __name__ == "__main__":
    run_git()
