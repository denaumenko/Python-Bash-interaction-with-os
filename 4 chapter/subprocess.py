import subprocess

subprocess.run(["sleep", '2'])

result = subprocess.run(["host","8.8.8.8"],capture_output=True)
print(result.stdout)