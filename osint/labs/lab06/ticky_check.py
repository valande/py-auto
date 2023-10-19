#!/usr/bin/env python3

import sys
import re
import operator

error = {}
per_user = {}

with open(sys.argv[1], "r") as syslog:
    for line in syslog:
        result = re.search(r".+ticky:\s(\w+)\s([\w+\s+']+)\[?.+\]?\s?\((\w+)\)", line.strip()) # INFO & ERROR ok
        if not result is None:
            msgtype, msgtext, msguser = result[1], result[2], result[3]
            #print("tipo: " + msgtype + ", mensaje: " + msgtext + ", usuario: " + msguser)
            if msgtype == "ERROR":
                error[msgtext] = error.get(msgtext, 0) + 1
                if per_user.get(msguser):
                    per_user[msguser]["ERROR"] = per_user.get(msguser)["ERROR"] + 1
                else:
                    per_user[msguser] = {"ERROR": 1, "INFO": 0}
            else:
                if per_user.get(msguser):
                    per_user[msguser]["INFO"] = per_user.get(msguser)["INFO"] + 1
                else:
                    per_user[msguser] = {"ERROR": 0, "INFO": 1}
    syslog.close()

with open("error_message.csv", "w") as errors:
    errors.write("Error,Count\n")
    for key, value in sorted(error.items(), key=operator.itemgetter(1), reverse=True):
        #print(key + "," + str(value))
        errors.write(key + "," + str(value) + "\n")
    errors.close()

with open("user_statistics.csv", "w") as users:
    users.write("Username,INFO,ERROR\n")
    for key, value in sorted(per_user.items(), key=operator.itemgetter(0)):
        #print(key + "," + str(value["ERROR"]) + "," + str(value["INFO"]))
        users.write(key + "," + str(value["ERROR"]) + "," + str(value["INFO"]) + "\n")
    users.close()
