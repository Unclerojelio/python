# File
import string

lower_words = []
uniq_words = []
f = open('twotribes', 'r')
file = f.read()
out = file.translate(string.maketrans("",""), string.punctuation)
words = out.split()
for word in words:
    lower_words.append(word.lower())
for word in lower_words:
    if not(word in uniq_words):
        uniq_words.append(word)
for word in sorted(uniq_words):
    print word
