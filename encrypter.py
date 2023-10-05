import random


password = input("Enter your access key: ")
key = ["SUB2Harry", "XpolioN@OP"]  #if you don't know the password

# functions 

def encrypt(a):
    if isinstance(a, str):
        input_words = a.split(" ")
        encrypted_words = []

        for word in input_words:
            if len(word) < 3:
                encrypted_word = word[::-1]
            else:
                rand_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '~']
                first_letter = word[0]
                y_temp = word[1:] + first_letter
                encrypted_word = ""
                for _ in range(3):
                    y = random.choice(rand_chars) + y_temp + random.choice(rand_chars)
                    y_temp = y
                    encrypted_word = y
            encrypted_words.append(encrypted_word)

        final_result = " ".join(encrypted_words)
        return final_result
    else:
        return "Type error"


def decrypt(a):
    if isinstance(a, str):
        input_words = a.split(" ")
        decrypted_words = []
        for word in input_words:
            if len(word) < 3:
                decrypted_word = word[::-1]
            else:
                y_temp = word[3:-3]
                last_letter = y_temp[-1]
                y_temp2 = y_temp[0:-1]
                y = last_letter + y_temp2
                decrypted_word = y
            decrypted_words.append(decrypted_word)
        final_result = " ".join(decrypted_words)
        return final_result
    else:
        return "Type error"

def getcmd():
    cmd = input("Enter command: ")
    valid_cmd = ['1','2','0']
    if cmd in valid_cmd:
        return cmd
    else:
        print("pls enter valid command")
        getcmd()


# this funtions below is made for this code will requir edits to use in other proggrams
# feel free to use any funtions
# mainly made to loop in certain senarios

def matchCase(cmd):
    if (cmd == "1"):
        print("Enter what you wanna encrypt:")
        st = input("> ")
        encrypted_st = encrypt(st)
        print("Encypted string is:")
        print(encrypted_st)
        main()
    elif (cmd == "2"):
        print("Enter what you wanna decrypt:")
        st = input("> ")
        Decrypted_st = decrypt(st)
        print("Decypted string is:")
        print(Decrypted_st)
        main()
    elif(cmd == "0"):
        print("Successfully quitted")


def main():
    cmd = getcmd()
    matchCase(cmd)
    
# main

if password in key:
    print ("Verified")
    print ("What you want to do? \n(1 for Encrypt) , (2 for decrypt) , (0 to quit)")
    main()


else:
    print("NO Access")
