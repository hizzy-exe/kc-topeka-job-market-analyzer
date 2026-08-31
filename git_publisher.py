import subprocess
import os

# ⚠️ TYPE YOUR CHOSEN PORTFOLIO CONFIGURATIONS BELOW:
GITHUB_REPO_URL = "https://github.com/hizzy-exe/kc-topeka-job-market-analyzer.git"
GITHUB_EMAIL = "haydonebarnes@gmail.com"
GITHUB_NAME = "hizzy-exe"

# Set the working directory to your project folder
project_dir = r"C:\Users\haydo\OneDrive\Desktop\Github Projects\kc-topeka-job-market-analyzer"
os.chdir(project_dir)

def run_git_cmd(cmd_list):
    try:
        result = subprocess.run(cmd_list, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Git Command Error Details:")
        print(e.stderr)
        raise

print("Starting Git Version Control Pipeline...\n")

# 1. Initialize Git local repository tracking
print("Initializing Git tracking...")
run_git_cmd(["git", "init"])

# 2. BRAND NEW STEP: Register your identity with Git to prevent Error 128
print("Configuring your analyst profile name and email...")
run_git_cmd(["git", "config", "--global", "user.email", GITHUB_EMAIL])
run_git_cmd(["git", "config", "--global", "user.name", GITHUB_NAME])

# 3. Stage all files (excluding what we blocked in .gitignore)
print("Staging project files...")
run_git_cmd(["git", "add", "."])

# 4. Create your official initial version commit message
print("Creating initial commit snapshot...")
run_git_cmd(["git", "commit", "-m", "Initial commit: Production ready enterprise job market analyzer pipeline"])

# 5. Target the main default publishing branch
print("Setting default branch to main...")
run_git_cmd(["git", "branch", "-M", "main"])

# 6. Link your local project to your online GitHub repository url
print("Connecting local repository to remote GitHub URL...")
try:
    run_git_cmd(["git", "remote", "add", "origin", GITHUB_REPO_URL])
except Exception:
    run_git_cmd(["git", "remote", "set-url", "origin", GITHUB_REPO_URL])

# 7. Upload your files to GitHub
print("Uploading assets to GitHub live servers (watch for a browser login window)...")
run_git_cmd(["git", "push", "-u", "origin", "main"])

print("\n=== SUCCESS! YOUR PROJECT IS LIVE ON GITHUB ===")
