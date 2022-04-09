import Morse
import audio
import sys

print("Wprowadz zwrot, by go przetłumaczyć: ")
words = input()
if Morse.ifmorse(words) == -1:
    if words[-4:] == '.wav':
        decoded = audio.wav2morse(words)
        print("Plik kodował:",decoded,"\nCo oznacza: ", Morse.translate(decoded))
    else:
        print("Incorrect input")
        sys.exit(0)
else:
    print("Tłumaczenie wiadomości: ",words,"\nTo: ",Morse.translate(words))







######################-WEJSCIA-PROBNE-######################
#print(Morse.translate("Python"))
#print(Morse.translate("Python_is_a_snake"))
#print(Morse.translate("..... .--. -.-- - .... --- -."))
#print(Morse.translate("-.. . .. --"))


# Tworzenie nagran dzwiekowych:
# https://www.meridianoutpost.com/resources/etools/calculators/calculator-morse-code.php?