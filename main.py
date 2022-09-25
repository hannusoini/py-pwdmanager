from cryptography.fernet import Fernet

#def write_key():
#    key = Fernet.generate_key()
#    with open("key.key", "wb") as key_file:
#        key_file.write(key)

#write_key()

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master password? ")
key = load_key() #* master_pwd #.encode()   #encode()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:  # with closes files automatically afterwards. a append w overwrite r read
        for line in f.readlines():
            data= line.rstrip()
            user, passw = data.split("|")
            print("Account: ", user, "| Password: ", fer.decrypt(passw.encode()).decode())
            #print("Password: ", passw)
            #print(line.rstrip()) #.rstrip strips carriage return end of line

def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    with open('passwords.txt','a') as f: #with closes files automatically afterwards. a append w overwrite r read
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Add new or View passwords or Quit (A/V/Q)? ").lower()
    if mode =="q":
        break
    elif mode =="v":
        view()
    elif mode =="a":
        add()
    else:
        print("Invalid selection.")
        continue