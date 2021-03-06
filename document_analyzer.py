f = open("document.txt","r",encoding='utf-8')
d = f.read()
count = dict()
temp = ""
def word_counting(str):
    words = str.split()
    for word in words:
        temp = ""
        for i in word:
            if i.isalpha():
                temp = "".join([temp, i])
                word = temp
            if i == '.':
                if word.find('com'):
                    temp = "".join([temp, i])
                    word = temp
                else:
                    temp = "".join([temp, i])
                    word = temp
            if i == "'":
                if word.find("'s") or word.find("'t") or word.find("'d") or word.find("'ve") or word.find("'ll"):
                    temp = "".join([temp, i])
                    word = temp
                else:
                    temp = "".join([temp, i])
                    word = temp
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

word_counting(d)
f.close()
print('')
count = dict(sorted(count.items(), key=lambda item: (-item[1],item[0]))[:5])

for key, value in count.items():
    print(f"{key}: {value}")





