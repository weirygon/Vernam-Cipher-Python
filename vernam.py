#!/usr/bin/python3

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

def genKey(file):
    pass

def encrypt(f_key, f_text):
    size = len(f_key.read())
    f_key.seek(0)

    f_out_name = ''

    for i in f_text.name:
        if i == ".":    break
        f_out_name = f_out_name + i

    f_out = open( (f_out_name + "Crypt.txt"), "w", encoding="ascii")

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

def decrypt(f_key, f_text):
    size = len(f_key.read())
    f_key.seek(0)

    f_out_name = ''

    for i in f_text.name:
        if i == ".":    break
        f_out_name = f_out_name + i

    f_out = open( (f_out_name + "Decrypt.txt"), "w")

    f_text = open(f_text.name, "rb")

    for i in range(size):
        char_k = ord(f_key.readline(1))
        char_t = ord(f_text.readline(1))
        char_d = ""

        bin_k = asciiToBin(char_k)
        bin_t = asciiToBin(char_t)
        bin_d = [1,1,1,1,1,1,1]

        for i in range(len(bin_k)):
            if bin_k[i] == bin_t[i]:
                bin_d[i] = 0

        char_d = chr(binToAscii(bin_d))
        f_out.write(char_d)
    
    return f_out
    
def main():
    print()
    print(f'{" Vernam Cipher ":=^50}')

    print("[*] Inform the option:")
    print("1 - Encrypt")
    print("2 - Decrypt")

    try:
        option = int(input("=> "))
        if option < 1 or option > 2:
            print("[-] Error: Invalid Option!")
            exit()

        file = input("File key: ")
        f_key = open(file, "r", encoding="ascii")
        file = input("File text: ")
        f_in = open(file, "r",encoding="ascii")

        if(len(f_key.read()) != len(f_in.read())):
            print("[-] The file key %s different size of %s" % (f_key.name, f_in.name))
            exit()

    except UnicodeDecodeError:
        print("[-] Error: Encoding of %s file is not ASCII!" % f_in.name)
        exit()

    except FileNotFoundError:
        print("[-]File %s not found" % file)
        exit()
    
    except KeyboardInterrupt:
        print("\n[-] Exiting...")
        exit()
    
    except ValueError:
        print("[-]Error : Only integer numbers!")
        exit()

    f_key.seek(0)
    f_in.seek(0)

    if option == 1:
        f_out = encrypt(f_key, f_in)
        
    elif option == 2:
        f_out = decrypt(f_key, f_in)

    else:
        print(option, type(option))
        print("[-] Error: Invalid option!")
        exit()

    print("[+] The %s file was created successfully" % f_out.name)

main()