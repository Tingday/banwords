#--*-- coding:utf-8 --*--
def has_banwords(text):#判断是否存在禁词
    banwords = getbanwords()
    words = []
    for word in banwords:
        if word in text:
            words.append(word)
    return words

def getbanwords():
    f = open('banwords.txt', mode='r')
    lines = f.readlines()
    txtdata = []
    for line in lines:
        line = line.strip('\n')
        txtdata.append(line)
    return txtdata

def replace_banword(banwords, text):
    for word in banwords:
        if word in text:
            text = text.replace(word, '*' * len(word.decode('utf-8')))
    return text

def nobantext(text):
    return replace_banword(has_banwords(text), text)

