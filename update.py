import os
import subprocess

# Save the original directory
orig_dir = os.getcwd()

# # run the ghp-import -n -p -f _build/html
# subprocess.run(["ghp-import", "-n", "-p", "-f", "_build/html"], check=True)

# Run the command jb build --all . after the loop
subprocess.run(["jb", "build", "--all", "."], check=True)

# # Push and sync the repository to GitHub make sure to change the 'Update repo' message
# subprocess.run(["git", "add", "."], check=True)
# subprocess.run(["git", "commit", "-m", "update.py testing"], check=True)
# subprocess.run(["git", "push"], check=True)
