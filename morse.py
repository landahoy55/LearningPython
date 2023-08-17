letter_to_morse = {
        'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 
        'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 
        'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
        'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
        '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
        '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', ' ':'/'
    }



def encode(message): 

    # `morse` is a list which will eventually contain the 
    # strings for each morse code letter in the message.
    # a change
    
    if "!" in message: 
            raise ValueError(f"'!' is not a valid string :(")
    
    morse = [ letter_to_morse[letter.lower()] for letter in message ]

    # for letter in message:
    #     morse_letter = letter_to_morse[letter.lower()]
    #     morse.append(morse_letter)

    # We need to join together Morse code letters with spaces
    morse_message = " ".join(morse)

    return morse_message


# We need to invert the dictionary. This will create a dictionary
# that can go from the morse back to the letter
morse_to_letter = {}
for letter in letter_to_morse:
    morse = letter_to_morse[letter]
    morse_to_letter[morse] = letter


def decode(message):

    # Now we cannot read by letter. We know that morse letters are
    # separated by a space, so we split the morse string by spaces
    morse_letters = message.split(" ")

    english = [ morse_to_letter[letter] for letter in morse_letters]

    # for letter in morse_letters:
    #     english_letter = morse_to_letter[letter]
    #     english.append(english_letter)

    # Rejoin, but now we don't need to add any spaces
    english_message = "".join(english)

    return english_message


