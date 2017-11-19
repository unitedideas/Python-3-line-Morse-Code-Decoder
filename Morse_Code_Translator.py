#By Shane Cheek

# Need a dictionary to key the characters
mcode = {'A': '.-', 'B': '-...', 'C': '-.-.',
         'D': '-..', 'E': '.', 'F': '..-.',
         'G': '--.', 'H': '....', 'I': '..',
         'J': '.---', 'K': '-.-', 'L': '.-..',
         'M': '--', 'N': '-.', 'O': '---',
         'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-',
         'V': '...-', 'W': '.--', 'X': '-..-',
         'Y': '-.--', 'Z': '--..',

         '.': ".-.-.-", ',': "--..--", "?": "..--..",
         '/': "-..-.", "@": ".--.-.", " ": " ",

         '0': '-----', '1': '.----', '2': '..---',
         '3': '...--', '4': '....-', '5': '.....',
         '6': '-....', '7': '--...', '8': '---..',
         '9': '----.'
         }

# Need to get an input from the user
decoded = input("Please enter a sentence: ").upper()

# Done in 3 lines with Jeff's help
print (" ".join([mcode[key] for key in decoded]))
# Thanks Jeff

