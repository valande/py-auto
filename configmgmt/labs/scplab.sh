#!/usr/bin/bash

# Source oneshot credentials
. ./shlib/oneshotcred.sh

# Download qwiklabs resources via scp, 
keyfile="/home/v4l4nd3/Descargas/${keyfilename}"
chmod 600 ${keyfile}
scp -i ${keyfile} -r ${username}@${ipaddress}:/home/${username} ./
