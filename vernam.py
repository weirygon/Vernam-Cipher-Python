#!/usr/bin/python3

import sys

def asciiToBin(c):
    quoc = 1
    bin = []
    binario = []
    
    c_bkp = c

    while quoc >= 1:
        resto = c% 2
        bin.insert(0,resto)
        quoc = c // 2
        c = quoc

    for i in bin:
        binario.append(i)

    while(len(binario) < 7): binario.insert(0, 0)

    return binario

def encrypt(f_key, f_text):

    size = len(f_key.read())
    f_key.seek(0)

    for i in range(size):
        print(f_key.readline(i), i)

    
def main():

    print(f'{" Vernam Cipher ":=^50}')

    try:

        if sys.argv[1] == "-c":

            f_key = open(sys.argv[2], "r")
            f_in = open(sys.argv[3], "r")

            if(len(f_key.read()) != len(f_in.read())):
                print("[-] The file key %s different size of %s" % (sys.argv[2], sys.argv[3]))

            f_key.seek(0)
            f_in.seek(0)

            encrypt(f_key, f_in)
        
        if sys.argv[1] == "-d":
            pass

    except IndexError:
        print("[-] No file in argv")
        sys.exit()    
    except FileNotFoundError:
        print("[-] File not exits", sys.argv[2], "or", sys.argv[3])
        sys.exit()

main()