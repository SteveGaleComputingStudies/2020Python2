# https://docs.python.org/3/library/subprocess.html#popen-constructor
import subprocess

processjl = subprocess.Popen([r'C:\Windows\System32\ping.exe', '10.0.0.138'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)
stdout, stderr = processjl.communicate()
print(stdout)