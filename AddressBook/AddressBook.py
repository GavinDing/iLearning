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
        self.name = self.name
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
        print('please create %s.' % g_book)
        exit(1)
    except:
        print('write to file error.')
        file.close()
        exit(2)
    else:
        file.close()

#load data from map to book
try:
    file = open(g_book, mode='rb')
except FileNotFoundError:
    print('please create %s.' % g_book)
    exit(1)
else:
    try:
        g_map = p.load(file)
    except EOFError:
        file.close()
        writeToFile()
    else:
        file.close()
        
#display help info of this program
def dispHelpInfo():
    print('help         -- show help info')
    print('quit/exit    -- exit this program')
    print('showAll      -- show all address info')
    print('add          -- add a new address')

#get user's command adn process it
cmd_quit = ('quit', 'q', 'Q', 'exit', '退出')
cmd = input("CMD:")
while cmd not in cmd_quit:
    if('help' == cmd):
        dispHelpInfo()
    
    #get the nexe command
    cmd = input("CMD:")
    
