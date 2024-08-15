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
  ' ': " "}


print('''  ____        __  __                     
 |  _ \\ _   _|  \\/  | ___  _ __ ___  ___ 
 | |_) | | | | |\\/| |/ _ \\| '__/ __|/ _ \\
 |  __/| |_| | |  | | (_) | |  \\__ \\  __/
 |_|    \\__, |_|  |_|\\___/|_|  |___/\\___|
        |___/                            ''')
print("Welcome to PyMorse!")
running = True
while running:
 user_to_morse = input("Enter a message to convert: ")
 if user_to_morse == "Stop Running!":
  running = False
 else:
  morse = []
  for letter in user_to_morse:
   if letter in list_of_morse:
    morse.append(list_of_morse[letter])
   else:
    morse.append(letter)
  print(f"PyMorsed message: {' '.join(morse)}")


