
def how_many_vowels(sentence):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    total = 0
    
    
    
    for char in sentence: # for every letter in the sentence
     if 'a' == char: # if "a" is the same letter in the sentece, then add 1 to a variable
        a += 1
     if 'e' == char: # if "e" is the same letter in the sentece, then add 1 to a variable
        e += 1
     if 'i' == char: # if "i" is the same letter in the sentece, then add 1 to a variable
        i += 1
     if 'o' == char: # if "o" is the same letter in the sentece, then add 1 to a variable
        o += 1
     if 'u' == char: # if "u" is the same letter in the sentece, then add 1 to a variable
        u += 1
     
    total = a + e + i + o + u # all the number combined 
    
    print('Overall = ' + str(total)) # total printed
    print('a = ' + str(a)) # numbr of "a" in the sentence
    print('e = ' + str(e)) # numbr of "e" in the sentence
    print('i = ' + str(i)) # numbr of "i" in the sentence
    print('o = ' + str(o)) # numbr of "o" in the sentence
    print('u = ' + str(u)) # numbr of "u" in the sentence 

if __name__ == '__main__':
    how_many_vowels('This sentence should have 10 vowels') # erase and type your own sentence between the qoutes

    