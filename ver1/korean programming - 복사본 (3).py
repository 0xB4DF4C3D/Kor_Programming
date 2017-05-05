# -*- coding: utf-8 -*-
#임의의 함수에서 변수 깊은 참조 문제
import hangul
ss = input("input : ")
ss = ss.replace('!','\n')
ss = ss.splitlines()
c1 = c2 = c3 = c4 = 65                                                          #c1 for 패
test = 100;
i = j = 0
cur = ss[i][j]                                                                  # cur means current position of process (cursor)
director = 2                                                                    #director is direction of process  1 is up, 2 is right, 3 is down, 4 is left, 0 is end
def FuncDirector():
    global i,j
    if director == 0 : test = 0
    if director == 1 : i -= 1
    if director == 2 : j += 1
    if director == 3 : i += 1
    if director == 4 : j -= 1

def ijCorrecter():
    global i,j
    if i >= len(ss) or i < 0 : i = 0;                                                     #check for out of index
    if j >= len(ss[i]) or j < 0 : j = 0;

def i2n(arg1) :
    if arg1 == 'ㄱ': return 1
    elif arg1 == 'ㄴ': return 2
    elif arg1 == 'ㄷ': return 3
    elif arg1 == 'ㄹ': return 4
    elif arg1 == 'ㅁ': return 5
    elif arg1 == 'ㅂ': return 6
    elif arg1 == 'ㅅ': return 7
    elif arg1 == 'ㅇ': return 8
    elif arg1 == 'ㅈ': return 9
    elif arg1 == 'ㅊ': return 0
    else : return 0

def i2v(arg1):
    if arg1 == 'ㅋ': return c1


while director and test:
    if not hangul.is_hangul(cur):break
    elif hangul.is_consonant(cur) : ini = hangul.get_initial(cur); fin = hangul.get_final(cur)   #in first, extract initial,vowel,finish from the cur
    elif hangul.is_vowel(cur) :  mid = hangul.get_vowel(cur)
    else : ini = hangul.get_initial(cur); fin = hangul.get_final(cur); mid = hangul.get_vowel(cur)

    test -= 1

    FuncDirector()

    if mid == 'ㅗ' : director = 1                                               #process director
    if mid == 'ㅏ' : director = 2
    if mid == 'ㅜ' : director = 3
    if mid == 'ㅓ' : director = 4



    if mid == 'ㅏ' or 'ㅓ' or 'ㅗ' or 'ㅜ':
        if ini == 'ㅉ' :
            while 1:
                FuncDirector()
                ijCorrecter()
                cur = ss[i][j]
                if hangul.get_vowel(cur) == 'ㅣ' : break
        elif fin != '' :
            skipblock = i2n(fin)
            while skipblock:
                FuncDirector()
                ijCorrecter()
                cur = ss[i][j]
                skipblock -= 1

    if mid == 'ㅛ' : c1+=i2n(fin)
    if mid == 'ㅠ' : c1-=i2n(fin)

    if mid == 'ㅐ' :
        if ini == 'ㅍ' : print(chr(c1),end='')

    ijCorrecter()
    cur = ss[i][j]

