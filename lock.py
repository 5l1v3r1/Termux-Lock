# lock system automatic
# By Ubaii ID

import time, os
import getpass
import sys
import getopt

#Color
H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'
 
def usage():
      print '''
               Tools ini sudah di pasang system automatic
               jadi anda tidak bisa menjalankan nya secara manual.
           '''
 
def main():
    if len(sys.argv) < 2 :
            usage()
            sys.exit(1)
    try:
            options,args=getopt.getopt(sys.argv[1:], 'ahli :')
    except getopt.GetoptError:
        usage()
        sys.exit(1)
 
    options2= []
     
    for i in options :
              if i not in options2:
                      options2.append(i)
    del(options)
        
    for o,a in options2:
                if o == '-u':
                        uninstall()
                if o == '-l':
                        lock()
                if o == '-c':
                        os.system('clear')
 

def lock():
	print(H+' PLEASE LOGIN ')
	print(W+"""           /\ /|
          |||||||
           \ | \
/
      _ _ /  @ @
     /    \   =>X<=
   /|      |   /
   \|     /__| |
     \_____\ \__\
""")
	try:
		usr = raw_input('username: ')
		print('SELAMAT DATANG '+usr+'')
		psw = getpass.getpass()
	except:
		print(O+' Ngapain hayoo?')
		lock()
	if usr == 'Ubaii' and psw == 'ID': # Ganti Dengan sesuka ente yak :)
		print('SUKSES LOGIN.!!!')
		exit()
	else:
		print('USERNAME DAN PASSWORD SALAH!!!')
		lock()

if __name__ == '__main__':
          main() 
