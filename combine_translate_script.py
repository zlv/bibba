#copyright (c) 2016 Evgenii Lezhnin
import sys
import unicodedata as ud

latin_letters= {}

def is_latin(uchr):
    try: return latin_letters[uchr]
    except KeyError:
         return latin_letters.setdefault(uchr, 'LATIN' in ud.name(uchr))

def only_roman_chars(unistr):
    return all(is_latin(uchr)
           for uchr in unistr
           if uchr.isalpha()) # isalpha suggested by John Machin
t = {}
f = []
list = []
if len(sys.argv)==3 : #combine files argv1 -- destination, argv2 -- source
    f.append(open(sys.argv[1],"r"))
    f.append(open(sys.argv[2],"r"))
    for s in f[0] :
        a = s.split('=',1)
        if not a[0] in list :
            list.append(a[0])
        t[a[0]] = a[1]
    count = 0
    for s in f[1] :
        a = s.split('=',1)
        if a[0] in t and t[a[0]]!=a[1] and only_roman_chars(t[a[0]]) and not only_roman_chars(a[1]):
            count += 1
            t[a[0]] = a[1]
    for i in list :
        print(i+'='+t[i][:-1])
if len(sys.argv)==2 : #remove dublicats
    f.append(open(sys.argv[1],"r"))
    for s in f[0] :
        a = s.split('=',1)
        if not a[0] in list :
            list.append(a[0])
        t[a[0]] = a[1]
    for i in list :
        print(i+'='+t[i][:-1])
