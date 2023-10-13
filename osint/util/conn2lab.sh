#!/usr/bin/bash

# Connect to qwiklabs via ssh, 
# replacing username, ipaddress and keyfile first 

username="student-00-951e14db22d5"
ipaddress="35.190.150.63"
keyfile="~/Descargas/qwiklabs-L78288381.pem"

chmod 600 ${keyfile}
ssh -i ${keyfile} ${username}@${ipaddress}
