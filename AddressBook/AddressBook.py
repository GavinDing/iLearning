#!/usr/bin/python
#Filename: AddressBook.py
#Desc    : An address book build in python.

import pickle as p


#address modle
class Address:
    name  = ''
    email = ''
    phone = ''
    memo  = ''

    def __init__(self):
        #do nothing
        self.name  = self.name
    def __init__(self, name, email, phone, memo):
        self.name  = name
        self.email = email
        self.phone = phone
        self.memo  = memo
        
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setEmail(self, email):
        self.email = email
    def getEmail(self):
        return self.email
    def setPhone(self ,phone):
        self.phone = phone
    def getPhone(self):
        return self.phone
    def setMemo(self, memo):
        self.memo = memo
    def getMemo(self):
        return self.memo

#file to save data
g_book = 'book.data'
#map to save data
g_map  = {'author':Address('author', 'ffding@cqu.edn.cn', '15951869525', 'author of this program'),}

#write map data to file
def writeToFile():     
    try:
        file = open(g_book, mode='wb')
        p.dump(g_map, file)
    except FileNotFoundError:
        return
    except:
        print('write to file error')
        file.close()
    else:
        file.close()
    return

#welcome the user
print('''*****************************************************''')
print('''Welcome to gavin's software <address book>.''')
print('''*****************************************************''')
print('''-----------------------------------------------------''')
print('''If you don't know what to do, just type 'help'.''')
print('''-----------------------------------------------------''')
#load data from file to map
try:
    file = open(g_book, mode='rb')
except FileNotFoundError:
    print('''Now, you can add items to your address book.''')
else:
    try:
        g_map = p.load(file)
    except EOFError:
        file.close()
        #when there's no data in the file, write author's data into it.
        writeToFile()
    else:
        file.close()
        
#display help info of this program
def dispHelpInfo():
    print('help         -- show help info')
    print('quit/exit    -- exit this program')
    print('show/all     -- show all address info')
    print('query/get    -- get an item by name')
    print('add          -- add a new address item')
    print('remove/rm    -- remove an item from address book')
    print('update/up    -- update an item in address book')
    return

#display all items in the address book
def showAll():
    for name, addr in g_map.items():
        email = addr.getEmail()
        phone = addr.getPhone()
        memo  = addr.getMemo()
        print('contact %s at: ' % name)
        if(email):
            print('    Email: %s' % email)
        if(phone):
            print('    Phone: %s' % phone)
        if(memo):
            print('    Memo : %s' % memo)
    return

#find an item in address book
def find(name):
    if (name in g_map):
        addr  = g_map[name]
        email = addr.getEmail()
        phone = addr.getPhone()
        memo  = addr.getMemo()
        print('contact %s at: ' % name)
        if(email):
            print('    Email: %s' % email)
        if(phone):
            print('    Phone: %s' % phone)
        if(memo):
            print('    Memo : %s' % memo)
    return

#get an item by name
def query():
    name = input("name:")
    if (name in g_map):
        find(name)
    else:
        print('%s not in this address book' % name)
    return

#add an item to address book
def add():
    name = input("name:")
    if (not name):
        print('must set name for an item in this address book')
        return
    if (name in g_map):
        print('%s already in this address book' % name)
        find(name)
        return
    email = input("email:")
    phone = input("phone:")
    memo  = input("memo:")
    addr = Address(name, email, phone, memo)
    g_map[name] = addr
    writeToFile()
    return

#remove an item from address book
def remove():
    name = input("name:")
    if (name not in g_map):
        print('%s not in this address book' % name)
        return
    del g_map[name]
    writeToFile()
    return

#update an item in address book
def update():
    name = input("name:")
    if (name not in g_map):
        print('%s not in this address book' % name)
        return
    addr  = g_map[name]
    email = input("email:")
    if (email):
        addr.setEmail(email)
    phone = input("phone:")
    if (phone):
        addr.setPhone(phone)
    memo  = input("memo:")
    if (memo):
        addr.setMemo(memo)
    g_map[name] = addr
    writeToFile()
    return

#get user's command and process it
cmd_quit = ('quit', 'q', 'Q', 'exit', '退出')
cmd = input("CMD:")
while cmd not in cmd_quit:
    if('help' == cmd):
        dispHelpInfo()
    if('show' == cmd  or 'all' == cmd):
        showAll()
    if('query' == cmd or 'get' == cmd):
        query()
    if('add' == cmd):
        add()
    if('rm' == cmd or 'remove' == cmd):
        remove()
    if('up' == cmd or 'update' == cmd):
        update()
        
    #get the nexe command
    cmd = input("CMD:")
else:
    print('Thanks for using this software developed by gavin.')
    
