# Name: Vipul Purohit
# Roll No: IC-2K24-96

text = input('Enter a sentence: ')
words = text.split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print('Word counts:', counts)
