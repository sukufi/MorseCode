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


def main():
    for i in get_word():
        print(get_morse(i), end="")
    print("")

if __name__ == "__main__":
    main()
