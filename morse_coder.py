import json
import re


def get_morse(alphabet):
    
    with open("morse-code.json", "r") as file:
        data = json.load(file)
        morse_letter = data[f"{alphabet}"]
    return morse_letter

def get_word():
    
    user_word = str(input("What is your word/Sentence for translate? -> ")).lower()
    
    user_letters = list(user_word)
    
    re_list = re.findall("[a-zA-Z,.?!-/@() ]" , user_word)
    
    while re_list != user_letters:   
        user_word = str(input("Invalid Characters In Your Text!\nWhat is your word/Sentence for translate? -> ")).lower()
        user_letters = list(user_word)
        re_list = re.findall("[a-zA-Z,.?!-/@() ]" , user_word)

    return user_letters

def get_code():
    user_code = str(input("Code Please -> "))
    user_code_split = user_code.split()
    
    return user_code_split



def encoder(code):
    
    with open("morse-code.json", "r") as file:
        file_data = json.load(file)
        inv_map = {v: k for k, v in file_data.items()}
        enc = inv_map[f"{code}"]
    return enc



def main():
    
    x = int(input("For Encode ->1\nFor Decode -> 2\n->"))
    
    if x == 1:

        for i in get_word():
            print(f"{get_morse(i)} ", end="")
        print("")
    
    elif x == 2:
        
        for i in get_code():
            print(f"{encoder(i)}", end= "")
        print("")

    


if __name__ == "__main__":
    main()
