import os
try: import requests
except: os.system("pip install requests")
try: raw=requests.get(input("Enter raw link: ")).content
except: print("That website doesn't exist or has error.")
exec(raw)
input()