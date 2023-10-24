#!/usr/bin/bash

# Source oneshot credentials
. ./shlib/oneshotcred.sh

# Connect to qwiklabs via ssh, 
keyfile="/home/v4l4nd3/Descargas/${keyfilename}"
chmod 600 ${keyfile}
ssh -i ${keyfile} ${username}@${ipaddress}
