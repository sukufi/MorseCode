import json
import string

with open("morse-code.json", "r") as file:
    data = json.load(file)

def get_morse(alphabet):
    with open("morse-code.json", "r") as file:
        data = json.load(file)
        morse_data = data[f"{alphabet}"]
        return morse_data



def main():
    userWord = input("What is your word/Sentence for translate? -> ")
    userLetters = list(userWord.lower())
    print(f"Your Word ({userWord.upper()}) is in Morse Alphabet: ")
    for letters in userLetters:
        print(get_morse(letters),end=" ")
        
main()
