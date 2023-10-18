#!/usr/bin/bash

# Download qwiklabs resources via scp, 
# replacing username, ipaddress and keyfilename first 

username="student-00-d5d35fbcb3ed"
ipaddress="35.196.113.103"
keyfilename="qwiklabs-L79440969.pem"

keyfile="/home/v4l4nd3/Descargas/${keyfilename}"
chmod 600 ${keyfile}
scp -i ${keyfile} -r ${username}@${ipaddress}:/home/${username} ./
