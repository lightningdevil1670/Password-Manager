from cryptography.fernet import Fernet

# we ran this function to generate key file, we needed it to run just once to generate the permanent key and to get that key.
'''
def write_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)

write_key()
         '''

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key




key = load_key() 
fer = Fernet(key)

def view():
     with open('password.txt', 'r') as f:
         for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|')   # this line will convert hello|world|very|hard to -> ['Hello', 'World','very','hard']
            print('User: ', user, '|  Password: ', fer.decrypt(passw.encode()).decode())

 

def add():
    name = input('Account name: ')
    pwd = input('Password: ')


    with open('password.txt', 'a') as f:
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + '\n')

        

while True:

    mode = input('Would you like to add a new password, or iew the existing ones (view/add)? press q to quit: ').lower()
    if mode == 'q':
        break

    if mode == 'view':
        view()

    elif mode== 'add':
        add()


    else:
        print('Invalid Mode')
        continue