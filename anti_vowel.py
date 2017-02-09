#a, e, i, o, u
def anti_vowel(text):
    word = ''
    for i in text:
        if (i != 'a' and i != 'A' and i != 'e' and i != 'E'
        and i != 'i' and i != 'I' and i != 'o' and i != 'O'
        and i != 'u' and i != 'U'):
            #print i
            word += i
    #print word
    return word

anti_vowel('Anreas TEre!')