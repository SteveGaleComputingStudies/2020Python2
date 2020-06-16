
import subprocess
r = subprocess.run([r'C:\Windows\System32\ping.exe', '10.0.0.138'],capture_output=True) 
print(r.stdout)
