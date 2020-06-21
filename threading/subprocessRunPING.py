# https://docs.python.org/3/library/subprocess.html
import subprocess

output = subprocess.run([r'C:\Windows\System32\ping.exe', '10.0.0.138'], capture_output=True)
print(output.stdout)