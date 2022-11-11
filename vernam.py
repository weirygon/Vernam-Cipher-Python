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

def binToAscii(bin):
    binario = ''.join([str(item) for item in bin])
    char = int(binario,2)
    
    return char

def encrypt(f_key, f_text):
    size = len(f_key.read())
    f_key.seek(0)

    f_out = open( (f_text.name + "Crypt.txt"), "w")

    for i in range(size):
        char_k = ord(f_key.readline(1))
        char_t = ord(f_text.readline(1))
        char_c = ""

        bin_k = asciiToBin(char_k)
        bin_t = asciiToBin(char_t)
        bin_c = [0,0,0,0,0,0,0]

        for i in range(len(bin_k)):
            if bin_k[i] != bin_t[i]:
                bin_c[i] = 1

        char_c = chr(binToAscii(bin_c))
        f_out.write(char_c)
        
    return f_out
    
def main():

    print(f'{" Vernam Cipher ":=^50}')

    print("[*] Inform the option:")
    print("1 - Encrypt")
    print("2 - Decrypt")

    option = 1  #input("=> ")

    try:

        file = "chave.dat" #input("File key: ")
        f_key = open(file, "r")
        file = "text.txt"  #input("File text: ")
        f_in = open(file, "r")

    except FileNotFoundError:
        print("[-]File %s not found" % file)
        exit()

    if(len(f_key.read()) != len(f_in.read())):
        print("[-] The file key %s different size of %s" % (f_key.name, f_in.name))
        exit()
        
    f_key.seek(0)
    f_in.seek(0)
    
    if option == 1:
        f_out = encrypt(f_key, f_in)
        
    elif option == 2:
            pass

    print("[+] The %s file was created successfully" % f_out.name)

main()