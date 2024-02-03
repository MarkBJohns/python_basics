def print_upper_words(words):
    '''This function takes in a list of words and returns each
    of them capitalized.'''
    for word in words:
        print(word.upper())
        
print('''
      =====================
      print_upper_words()
      =====================''')

print('["happy","sad","angry"]')
print_upper_words(['happy','sad','angry'])

#--------------------------------------------------------------------------

def print_upper_by_e(words):
    '''This function takes in a list of words, and if any of the words
    begin with the letter "e" (not case sensitive), it will return that
    word capitalized.'''
    for word in words:
        if word.lower().startswith('e'):
            print(word.upper())

print('''
      ====================
      print_upper_by_e()
      ====================''')

print('["every","Elephant","is","eating","walnuts","and","eclairs"]')
print_upper_by_e(['every','Elephant','is','eating','walnuts','and','eclairs'])

#--------------------------------------------------------------------------

print('''
      ====================
      print_upper_by_letters
      ====================''')

def print_upper_by_letters(words, letters=[]):
    '''This function takes in a list of words, as well as a list of letters.
    If any of the words entered begin with any of the letters entered (not
    case sensitive), it will return those words capitalized.
    
    If no letters are entered, it will return all words in the list.'''
    for word in words:
        if not letters or word.lower()[0] in letters:
            print(word.upper())

print('["apple","banana","cashew","doughnut"],["b","d"]')
print_upper_by_letters(['apple','banana','cashew','doughnut'],['b','d'])

print('["test","without","letters"]')
print_upper_by_letters(['test','without','letters'])
