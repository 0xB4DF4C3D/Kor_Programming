# -*- coding: utf-8 -*-
#임의의 함수에서 변수 깊은 참조 문제
import hangul
ini = mid = fin = ''
ss = input("input : ")
ss = ss.replace('!','\n')
ss = ss.splitlines()
c1 = c2 = c3 = c4 = 65                                                          #c1 for 패
s1 = s2 = 'Sample'
test = 100;
i = 0
j = -1
cur = ss[i][j]                                                                  # cur means current position of process (cursor)
director = 2                                                                    #director is direction of process  1 is up, 2 is right, 3 is down, 4 is left, 0 is end

def move():
    global i,j,director,cur,ini,mid,fin

    if director == 1 : i -= 1
    if director == 2 : j += 1
    if director == 3 : i += 1
    if director == 4 : j -= 1

    if i >= len(ss) or i < 0 : i = 0;                                                     #check for out of index
    if j >= len(ss[i]) or j < 0 : j = 0;

    cur = ss[i][j]

    if not hangul.is_hangul(cur):pass
    elif hangul.is_consonant(cur) :ini = hangul.get_initial(cur); fin = hangul.get_final(cur)   #in first, extract initial,vowel,finish from the cur
    elif hangul.is_vowel(cur) :  mid = hangul.get_vowel(cur)
    else : ini = hangul.get_initial(cur); fin = hangul.get_final(cur); mid = hangul.get_vowel(cur)

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
    elif arg1 == 'ㅋ': return c1
    elif arg1 == 'ㅌ': return c2
    elif arg1 == 'ㅍ': return c3
    elif arg1 == 'ㅎ': return c4
    else : return 0

def vs(arg1,arg2):
    global c1,c2,c3,c4,s1,s2
    if arg1 == 'ㅋ': c1 = arg2
    if arg1 == 'ㅌ': c2 = arg2
    if arg1 == 'ㅍ': c3 = arg2
    if arg1 == 'ㅎ': c4 = arg2
    if arg1 == 'ㄲ': s1 = arg2
    if arg1 == 'ㅆ': s2 = arg2

def va(arg1,arg2):
    global c1,c2,c3,c4,s1,s2
    if arg1 == 'ㅋ': c1 += arg2
    if arg1 == 'ㅌ': c2 += arg2
    if arg1 == 'ㅍ': c3 += arg2
    if arg1 == 'ㅎ': c4 += arg2
    if arg1 == 'ㄲ': s1 += arg2
    if arg1 == 'ㅆ': s2 += arg2

def rv(arg1):
    global c1,c2,c3,c4,s1,s2
    if arg1 == 'ㅋ': return c1
    if arg1 == 'ㅌ': return c2
    if arg1 == 'ㅍ': return c3
    if arg1 == 'ㅎ': return c4
    if arg1 == 'ㄲ': return s1
    if arg1 == 'ㅆ': return s2

def decoder(arg1,mode):
    limit = 256
    origin = arg1
    arg1 = rv(arg1)
    if mode == "ㄼ" :
        arg1 = ''
        while limit:
            move();
            if cur == 'ㅒ': break
            arg1 += cur
            limit -= 1
            if not limit : director = 0
        vs(origin,arg1)




while director and test:
    move()
    test -= 1

    if mid == 'ㅗ' : director = 1                                               #process director
    if mid == 'ㅏ' : director = 2
    if mid == 'ㅜ' : director = 3
    if mid == 'ㅓ' : director = 4
    if mid == 'ㅡ' :
        if ini == 'ㄲ' and fin == 'ㅌ' : director = 0;print("  끝  ")


    if mid == 'ㅏ' or 'ㅓ' or 'ㅗ' or 'ㅜ':
        if ini == 'ㅉ' :
            limit = 256
            while limit:
                move()
                if hangul.get_vowel(cur) == 'ㅣ' : break
                limit -= 1
                if not limit : director = 0

    if mid == 'ㅛ' : va(ini,i2n(fin))
    if mid == 'ㅠ' : va(ini,-i2n(fin))

    if mid == 'ㅐ' :
        if ini == 'ㅍ' :
            if fin == 'ㄲ' or fin == 'ㅆ' : print(rv(fin),end='')
            elif fin == 'ㄱ' : print(" ",end='')
            elif fin == 'ㅈ' : print("")
            else : print(chr(rv(fin)),end='')
        if ini == 'ㅅ' :
            if fin == 'ㄱ' :
                move()
                if mid == 'ㅣ': suhak = rv(ini) * rv(fin); move(); vs(fin,suhak)
            if fin == 'ㅁ' :
                move()
                if mid == 'ㅣ': suhak = rv(ini) // rv(fin); move(); vs(fin,suhak)
            if fin == 'ㅎ' :
                move()
                if mid == 'ㅣ': suhak = rv(ini) + rv(fin); move(); vs(fin,suhak)
            if fin == 'ㅇ' :
                move()
                if mid == 'ㅣ': suhak = rv(ini) - rv(fin); move(); vs(fin,suhak)
            if fin == 'ㄴ' :
                move()
                if mid == 'ㅣ': suhak = rv(ini) % rv(fin); move(); vs(fin,suhak)

    if mid == 'ㅢ' :
        if fin == 'ㄼ' : decoder(ini,fin)
        else : vs(ini,rv(fin))




    if mid == 'ㅔ' :
        if ini == 'ㅍ' : print(rv(fin),end='');



print(ss)

