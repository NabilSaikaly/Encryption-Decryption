# Cryptography: Encryption and Decryption 

## **WARNING**
1. Please use these information for educational purposes only, reproduce on your own environment and on dummy documents/files that aren't valuable to any individual or to any organization/company.  
Please note that if, for any reason, these information are used to cause any harm whether intentionally or not, law enforcements could track, prosecute and take legal actions as this can be considered a cybercrime of type: **RANSOMWARE**.
2. If you are building your own scripts, make sure to run them on a safe environment: Meaning on a directory that does not contain sensible information/files.  
Perform these operations on dummy files that can tolerate being damaged without recovery (Extra Precautions).  
3. If this is the first time you are working with encryption/decryption software and on a Bash Shell, it is recommended to check the "Interactive Encryption & Decryption Script with Safe Environment" Section first.

## Libraries Required
- Cryptography Fernet Class (Download using `pip install cryptography`)  
- OS (pre-installed)


## Working Procedure
### Encryption Script  
In `encrypt.py`, the working procedure is as follows:  
1. Define the files to protect from the encryption process in a list named: protected_files. By Convention, protect:  
      - The Encryption Script  
      - The Decryption Script   
      - The Encryption/Decryption Key  
2. Scan the files to encrypt in the target directory and append them to the target_files list.
3. Generate the encryption/decryption key to be used when encrypting and decrypting using the Fernet Class.
4. Instantiate the Fernet Class by giving the encryption key as a parameter.
5. Loop over the files to encrypt in target_files and for each file:  
    1. Read the content and save them to content_to_encrypt.
    2. Encrypt the content using the **Fernet Encryption Method**.
    3. Write the encrypted content to the original file.

### Decryption Script  
In `decrypt.py`, the working procedure is as follows:
1. Define the files to exclude from the decryption process (Usually the same files protected from the encryption process)
2. Same as step 2 in Encryption, but these target_files will now be decrypted.
3. Fetch the encryption/decryption key
4. Instantiate the Fernet Class by giving the encryption/decryption key as parameter.
5. Loop over the files to decrypt in target_files and for each file:  
    1. Fetch the encrypted content
    2. Decrypt the content using the **Fernet Decryption Method**.
    3. Write the decrypted content to the original file

## Interactive Encryption & Decryption Script with Safe Environment
Better used if using an encryption software for the first time since, any mistake can encrypt your files without recovery.
The main purpose of `safe_encryptor.py` is to allow the user visualize the encryption and decryption process via an interactive program.  
After running the safe_encryptor.py script, you can afterwards, read the encryption and decryption scripts (encrypt.py and decrypt.py) to understand the working mechanism 
and the structure behind the code and try to build your own script.  
But before doing anything, read the following points to know how the safe_encryptor.py script operates.

safe_encryptor.py Working Procedure:

1. A Directory on your desktop will be created as a Safe Environment to test the encryption and decryption scripts. Make sure to run safe_encryptor.py from your desktop's shell as working directory (on a Bash Shell)

2. In this Safe Environment, 3 random text documents will be created so that 
   the user can verify the encryption during execution and confirm the effectiveness 
   of the decryption script.

3. The safe_encryptor.py script will first run an encryption script to encrypt the files
   then will ask the user for a key, and if the correct secret key is entered, then
   the decryption script will run and decrypt the files.

4. The secret key is: ilovecoding


Note: After completing these steps, you can start on reading the individual
encrypt.py and decrypt.py scripts but make sure you save AND run them in a directory
that can tolerate losing the files in it for good in case anything happens unexpectedly and crashes the program (For Example: Sometimes the generated encryption/decryption key experiences some token issues)  
Finally, after taking the correct precautions, build your own scripts and enjoy cryptography and fernet! 

Thanks,  
Nabil
