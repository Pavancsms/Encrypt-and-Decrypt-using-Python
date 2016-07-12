#Pavan Kumar Assignment 1

# Include the Dropbox and gnupg modules

import dropbox
import gnupg
import sys,os
from os import path

access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
client = dropbox.client.DropboxClient(access_token)
print 'linked account: ', client.account_info()

#set gnupg home
#gpg = gnupg.GPG(gnupghome='C:/Program Files (x86)/GNU/GnuPG')
gnupghome='C:/Program Files (x86)/GNU/GnuPG'
#gnupg.encoding='utf-8'
gpg = gnupg.GPG()

#encrypt file
temp = sys.argv[1]
file_path = path.abspath(temp)
outputfile = os.path.basename(file_path)
f = open(file_path, 'rb')
encryptionStatus = gpg.encrypt_file(f, recipients='pav1',output=outputfile)

print 'status: ', encryptionStatus.status
print 'stderr: ', encryptionStatus.stderr


f = open(outputfile, 'rb')
response = client.put_file(outputfile, f)
print "uploaded:", response

f = client.get_file(outputfile)
code = raw_input("Enter the passphrase here: ").strip()

decryptionStatus = gpg.decrypt_file(f,passphrase = code)
print 'status: ', decryptionStatus.status
print 'stderr: ',decryptionStatus.stderr