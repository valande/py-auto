#!/usr/bin/bash

# Connect to qwiklabs via ssh, 
# replacing username, ipaddress and keyfile first 

username="student-00-d5d35fbcb3ed"
ipaddress="34.171.93.139"
keyfile="/home/v4l4nd3/Descargas/qwiklabs-L78420733.pem"

chmod 600 ${keyfile}
ssh -i ${keyfile} ${username}@${ipaddress}
