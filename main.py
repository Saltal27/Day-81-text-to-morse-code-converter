MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '＄': '...-..-', '@': '.--.-.', ' ': '/'
}

print("""
 _      ____  ____  ____  _____   ____  ____  ____  _____
/ \__/|/  _ \/  __\/ ___\/  __/  /   _\/  _ \/  _ \/  __/
| |\/||| / \||  \/||    \|  \    |  /  | / \|| | \||  \  
| |  ||| \_/||    /\___ ||  /_   |  \__| \_/|| |_/||  /_ 
\_/  \|\____/\_/\_\\____/\____\  \____/\____/\____/\____\

      """)
print("Welcome to the Text-Morse Code Converter! \nThis tool allows you to convert text into Morse code.")

running = True
while running:
    user_input = input("Enter a string to convert to Morse code:\n").upper()
    corresponding_morse_code = ""
    for char in user_input:
        if char in MORSE_DICT:
            corresponding_morse_code += MORSE_DICT[char]
        else:
            print(f"Invalid character: {char}. Skipping...")
            corresponding_morse_code += char

    print(f"Here is your Morse code: {corresponding_morse_code}")

    again = input("Do you want to convert another string?\nType 'y' for 'yes' or 'n' for 'no'\n").lower()
    if again == "n":
        running = False
        print("Understandable, have a great day!")
    else:
        pass
