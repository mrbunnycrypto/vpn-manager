import os
import subprocess

# Configuration
project_name = "vpn-manager"
github_repo_url = "https://github.com/mrbunnycrypto/vpn-manager.git"
readme_content = f"# {project_name}\n\nThis is a host-to-site VPN manager project."

# Step 1: Create a project directory
if not os.path.exists(project_name):
    os.mkdir(project_name)
    print(f"Created project directory: {project_name}")
else:
    print(f"Directory '{project_name}' already exists.")

# Step 2: Navigate to the project directory
os.chdir(project_name)

# Step 3: Create a README.md file
with open("README.md", "w") as f:
    f.write(readme_content)
print("Created README.md file.")

# Step 4: Initialize a Git repository
subprocess.run(["git", "init"], check=True)
print("Initialized Git repository.")

# Step 5: Add files to the repository
subprocess.run(["git", "add", "."], check=True)
print("Staged all files.")

# Step 6: Commit the changes
subprocess.run(["git", "commit", "-m", "Initial commit with README.md"], check=True)
print("Committed initial changes.")

# Step 7: Add remote origin (your GitHub repo URL)
subprocess.run(["git", "remote", "add", "origin", github_repo_url], check=True)
print(f"Added remote origin: {github_repo_url}")

# Step 8: Push to the remote repository
subprocess.run(["git", "branch", "-M", "main"], check=True)
subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
print("Pushed to GitHub repository.")
