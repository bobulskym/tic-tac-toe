import random
import subprocess

# Randomly choose which script to run
script_to_run = random.choice(["player_starts.py", "ai_starts.py"])

print(f"Starting game: {script_to_run}")

# Run the selected script
subprocess.run(["python", script_to_run])
