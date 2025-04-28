'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile

# Use a method to attempt to extract the zip file with a given password
def attempt_extract(zf_handle, password):
    try:
        #convert string to binary to match the encryption used when the file was encrypted
        zf_handle.extractall(pwd=password.encode('utf-8'))
        return True
    except:
        return False

def main():
    print("[+] Beginning bruteforce ")
    try:
        with ZipFile('enc.zip') as zf:
            #open the file, read the file, ignore any errors so that the program does not crash
            with open('rockyou.txt', 'r', errors='ignore') as f:
                # Iterate through password entries in rockyou.txt
                for line in f:
                    #remove any whitespace or extra characters
                    password = line.strip()
                    # Attempt to extract the zip file using each password
                    if attempt_extract(zf, password):
                        print(f"[+] Password Found: {password}")
                        return

        print(f"[!] Password not found in list")
    # Handle correct password extract versus incorrect password attempt)
    except FileNotFoundError as e:
        print(f"[!] File not found: {e}")

if __name__ == "__main__":
    main()