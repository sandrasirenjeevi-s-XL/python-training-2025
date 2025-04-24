import re

ip=input("enter the ip address:")
patt= r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}" \
          r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
if re.match(patt,ip):
    print("OK")
else:
    print("NOT OK")