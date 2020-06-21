
#!/usr/bin/env python3

import sys
import subprocess

with open(sys.argv[1]) as file:
    for line in file.readlines():
        string = line
        string = string.replace("fix", "fox")
        subprocess.run(["mv", string, line])

