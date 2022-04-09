from re import match


def translate(text):

    morse_dictionary = {'A': '.-', 'B': '-...', 'C': '-.-.',
                        'D': '-..', 'E': '.', 'F': '..-.',
                        'G': '--.', 'H': '....', 'I': '..',
                        'J': '.---', 'K': '-.-', 'L': '.-..',
                        'M': '--', 'N': '-.', 'O': '---',
                        'P': '.--.', 'Q': '--.-', 'R': '.-.',
                        'S': '...', 'T': '-', 'U': '..-',
                        'V': '...-', 'W': '.--', 'X': '-..-',
                        'Y': '-.--', 'Z': '--..', ' ': '.....',
                        }
    reversed_dict = {val: key for key, val in morse_dictionary.items()}


    if ifmorse(text) == 0:
        return ' '.join(morse_dictionary[i] for i in text.upper()) #aaaa zwraca morsea
    elif ifmorse(text) == 1:
        return ''.join(reversed_dict[i] for i in text.split()) #.-.-.-
    else:
        return -1


def ifmorse(word):

    pattern_reverse = r'^[\. -]*$' #sprawdza czy sa kropki / kreski
    pattern = r'^[a-z A-Z]+$'   #sprawdza czy tekst czytany

    if match(pattern, word):
        return 0            #word is acceptable, but not coded by Morse
    elif match(pattern_reverse, word):
        return 1            #word is coded by Morse
    else:
        return -1           #word is not acceptable

