import json
from xml.dom.minidom import CharacterData


def get_morse(alphabet):
    with open("morse-code.json", "r") as file:
        data = json.load(file)
        morse_letter = data[f"{alphabet}"]
        return morse_letter

def get_characters():
    with open("morse-code.json", "r") as file:
        data = json.load(file)
        characters = list(data)
        return characters


def main():
    
    user_word = input("What is your word/Sentence for translate? -> ")
    user_letters = list(user_word.lower())
    character_list = get_characters()
    
    while len(set(character_list).intersection(set(user_letters))) == 0 :
        user_word = input("Invalid Character! Please try again. What is your input?")
        user_letters = list(user_word.lower())
    
    print(f"Your Word ({user_word.upper()}) is in Morse Alphabet: ")
    for letters in user_letters:
        print(get_morse(letters),end=" ")




if __name__ == "__main__":
    main()
