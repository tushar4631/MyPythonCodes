pyg = 'ay'

original = raw_input('Enter a word:')
word = original.lower()
first = word[0]
new_word = word[1:len(new_word)] + first + pyg

if len(original) > 0 and original.isalpha():
    print "ok " + original
else:
    print 'empty'
    
print "Piglatin word for " + original + " is- " + new_word + "!"