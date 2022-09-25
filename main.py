master_pwd = input("What is the master password? ")


def view():
    with open('passwords.txt', 'r') as f:  # with closes files automatically afterwards. a append w overwrite r read
        for line in f.readlines():
            data= line.rstrip()
            user, passw = data.split("|")
            print("Account: ", user, "| Password: ", passw)
            #print("Password: ", passw)
            #print(line.rstrip()) #.rstrip strips carriage return end of line

def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    with open('passwords.txt','a') as f: #with closes files automatically afterwards. a append w overwrite r read
        f.write(name + "|" + pwd + "\n")

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