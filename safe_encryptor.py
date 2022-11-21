import time
import os 

greeting_message = '''
Hello! Welcome to this interactive program.
Have you read the README file?
Enter 'N' for NO.
Type anything for YES
-> '''

msg1 = input(greeting_message)
if msg1.lower() == 'n':
	print("Please read the README File because it is critical, then come back!")	
	exit()
	

print("Creating Safe Environment...")

time.sleep(2)

safe_environment = '''
cd 
cd Desktop
mkdir TestEnvironment
cd TestEnvironment
echo "Usernames" > usernames.txt
echo "Passwords" > passwords.txt
echo "Phone Number" > phonenumbers.txt
'''
os.system(safe_environment)

env_message = '''
The safe environment has been created successfully.
Notice 'TestEnvironment' Directory on your desktop.
Navigate to the directory and check the content of the text files,
they are readable content.
When done checking the text files, Enter anything to proceed to the encryption process -> \n'''

env_input = input(env_message)

encryption_decryption_pyscript = """
#!/usr/bin/env python3

import os 
import time
from cryptography.fernet import Fernet 

files_to_encrypt = []
print("Generating Key...")
time.sleep(2)
key = Fernet.generate_key()
with open('encryptionkey.key','wb') as key_object:
	key_object.write(key)

print("Finding the files to enrcypt...")
time.sleep(1)
for index,file in enumerate(os.listdir()):
	if file =='encrypt.py' or file == 'decrypt.py' or file =='encryptionkey.key':
		continue
	print(f"File #{index}: {file}")	
	files_to_encrypt.append(file)

for file in files_to_encrypt:
	with open(file,'rb') as file_object:
		content_to_encrypt = file_object.read()
	print(f"Encrypting file: {file}")	
	encrypted_content = Fernet(key).encrypt(content_to_encrypt)

	with open(file, 'wb') as file_object:
		file_object.write(encrypted_content)
	print(f"{file} got encrypted successfully.")
	time.sleep(2)

milestone_msg = '''
\nThe files in 'TestEnvironment' on the desktop are fully encrypted.
Navigate to the directory to make sure of that, then Enter anything to continue
to the Decryption process -> '''
milestone = input(milestone_msg)


active = True

while active:
	secret_key = input("Enter secret key to decrypt the files: ")		
	if secret_key.lower() == 'ilovecoding':
		active = False
		print("Decryption Script Access: Permitted") 
		decryption_script = '''
#!/usr/bin/env python3
import os 
import time
from cryptography.fernet import Fernet

files_to_decrypt= []

print("Retrieving the key...")
time.sleep(2)

with open('encryptionkey.key','rb') as key_object:
	key = key_object.read()

for index,file in enumerate(os.listdir()):
	if file == 'encrypt.py' or file =='decrypt.py' or file =='encryptionkey.key':
		continue
	with open(file,'rb') as file_object:
		content_to_decrypt = file_object.read()
	print(f"Decrypting File #{index}: {file}")	
	decrypted_content = Fernet(key).decrypt(content_to_decrypt)	
	with open(file,'wb') as file_object:
		file_object.write(decrypted_content)
	print(f"{file} got decrypted successfully.")	'''

		with open('decrypt.py','w') as decryption_script_object:
			decryption_script_object.write(decryption_script)

		os.system('python3 decrypt.py')
		os.system('echo "Files Decrypted"')
	

	else:
		print("Wrong Key. Files remain encrypted.")	
"""

bash_script = '''
#!/bin/bash
vari1=$(pwd)
cd
vari="$(pwd)/Desktop/TestEnvironment"

cd $vari1
echo "$vari" > path.txt

'''
os.system(bash_script)

with open('path.txt','r') as path_object:
	path = path_object.read().strip()

with open(f"{path}/encrypt.py",'w') as script_object:
	script_object.write(encryption_decryption_pyscript)

bash_script_2 = '''

#!/bin/bash
vari1=$(pwd)
cd
vari="$(pwd)/Desktop/TestEnvironment"
cd $vari
python3 encrypt.py '''

os.system(bash_script_2)

bash_script_3 = '''
#!/bin/bash
echo "Deleting the Encryption Scripts from the TestEnvironment..."
sleep 2
rm -rf 'path.txt'
cd
targetdir="$(pwd)/Desktop/TestEnvironment"
cd $targetdir
rm -rf 'encrypt.py'
rm -rf 'decrypt.py'
rm -rf 'encryptionkey.key'
'''
os.system(bash_script_3)


deletion_request = '''
Do you want to delete the TestEnvironment directory? Y/N: '''

deletion_request_input = input(deletion_request)

if deletion_request_input.lower() == 'y':
	bash_script_4 = '''
#!/bin/bash
echo "Deleting the Test Environment Directory..."
sleep 2
rm -rf TestEnvironment '''
	os.system(bash_script_4)
	print(f"Quitting Python in 3 seconds...")
	time.sleep(3)
	print("\n Bye!")
	exit()
else:
	print(f"Quitting Python in 3 seconds...")
	print("\n Bye!")
	time.sleep(3)
	exit()

