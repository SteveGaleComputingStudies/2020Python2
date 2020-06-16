# doesnt work yet
import subprocess
#out = subprocess.getoutput('dir')
#out = subprocess.check_output('dir', shell=True)
#print(out)

import subprocess
r = subprocess.run(["dir", "/w"],capture_output=True) 
print(r.stdout)

subprocess.run()