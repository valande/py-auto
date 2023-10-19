#!/usr/bin/env python3

import sys
import subprocess

with open(sys.argv[1], "r") as file:
    for line in file.readlines():
        line = line.strip()
        newline = line.replace("jane", "jdoe")
        #print(line + " will be " + newline)
        #subprocess.run(["echo", "mv", line, newline])
        subprocess.run(["mv", line, newline])
    file.close()

