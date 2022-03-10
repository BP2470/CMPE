f = open("document.txt","r")
d = f.read()
count = dict()
def word_counting(str):
    words = str.split()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

word_counting(d)
for key, value in count.items():
    print(key, ': ', value)




