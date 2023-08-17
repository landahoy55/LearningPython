'Unable to do this as list comprhension - how do you quit out of the list?'

def firstword(l):

    #  word = []
    # for letter in l:
    #     word.append(letter)
    #     if letter == " " :
    #          break

    # word = [letter for letter in l if letter != " "]

    # word_assembled = "".join(word)

    #return word_assembled 

    words = l.split()
    the_first_word = words[0]
    return the_first_word


print(firstword("Ere we go"))