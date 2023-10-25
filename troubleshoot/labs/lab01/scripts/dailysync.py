#!/usr/bin/env python3
import subprocess
src = "/home/student-00-e8d3bdaae06e/data/prod/"
dest = "/home/student-00-e8d3bdaae06e/data/prod_backup/"
subprocess.call(["rsync", "-azv", src, dest])
