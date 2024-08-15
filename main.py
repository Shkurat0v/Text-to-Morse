list_of_morse = {"A": ".-",
  "B": "-...",
  "C": "-.-.",
  "D": "-..",
  "E": ".",
  "F": "..-.",
  "G": "---",
  "H": "....",
  "I": "..",
  "J": ".---",
  "K": "-.-",
  "L": ".-..",
  "M": "--",
  "N": ".-.",
  "O": "---",
  "P": ".--.",
  "Q": "--.-",
  "R": ".-.",
  "S": "...",
  "T": "-",
  "U": "..-",
  "V": "...-",
  "W": ".--",
  "X": "-..-",
  "Y": "-.--",
  "Z": "--..",
  'a': '.-',
  'b': '-...',
  'c': '-.-.',
  'd': '-..',
  'e': '.',
  'f': '..-.',
  'g': '--.',
  'h': '....',
  'i': '..',
  'j': '.---',
  'k': '-.-',
  'l': '.-..',
  'm': '--',
  'n': '-.',
  'o': '---',
  'p': '.--.',
  'q': '--.-',
  'r': '.-.',
  's': '...',
  't': '-',
  'u': '..-',
  'v': '...-',
  'w': '.--',
  'x': '-..-',
  'y': '-.--',
  'z': '--..',
  '0': '-----',
  '1': '.----',
  '2': '..---',
  '3': '...--',
  '4': '....-',
  '5': '.....',
  '6': '-....',
  '7': '--...',
  '8': '---..',
  '9': '----.',
  '.': '.-.-.-',
  ',': '--..--',
  '?': '..--..',
  '!': '-.-.--',
  '/': '-..-.',
  ':': '---...',
  ';': '-.-.-.',
  '+': '.-...',
  '-': '-....-',
  '_': '..--.-',
  '"': '.-..-.',
  '@': '.--.-.',
  '=': '-...-',
  }

morse_code_reversed = {}
for letter, code in list_of_morse.items():
   morse_code_reversed[code] = letter



print('''  ____        __  __                     
 |  _ \\ _   _|  \\/  | ___  _ __ ___  ___ 
 | |_) | | | | |\\/| |/ _ \\| '__/ __|/ _ \\
 |  __/| |_| | |  | | (_) | |  \\__ \\  __/
 |_|    \\__, |_|  |_|\\___/|_|  |___/\\___|
        |___/                            ''')
print("Welcome to PyMorse! Choose a convertion type.")
running = True
while running:
 choose = input("Text-to-Morse or Morse-to-Text (type 1 or 2): ")
 if choose == "Stop Running!":
  running = False
 elif choose == "1":
  user_input = input("Enter a message to convert: ")
  morse = []
  for letter in user_input:
   if letter in list_of_morse:
    morse.append(list_of_morse[letter])
   else:
    morse.append(letter)
  print(f"PyMorsed message: {' '.join(morse)}")
 elif choose == "2":
   user_input = input("Enter a message to convert: ")
   text = ""
   for word in user_input.split(" "):
       for letter in word.split("/"):
           if letter in morse_code_reversed:
               text += morse_code_reversed[letter]
           else:
               text += "ㅤ"
       
   print("Unmorsed message:", text.strip())
 else:
   print("Enter a valid number or command.")


