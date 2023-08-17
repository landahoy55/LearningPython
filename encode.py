def decode(message): 

    letter_to_morse = {
        'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 
        'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 
        'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
        'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
        '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
        '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', ' ':'/'
    }

    message = "SOS We have hit an iceberg and need help quickly"


    # `morse` is a list which will eventually contain the 
    # strings for each morse code letter in the message.
    morse = []

    for letter in message:
        morse_letter = letter_to_morse[letter.lower()]
        morse.append(morse_letter)

    # We need to join together Morse code letters with spaces
    morse_message = " ".join(morse)

    return morse_message