# -*- coding: utf-8 -*-
# ㅐ 의 ㅍ 에서 초성으로 c 조절 문제
import hangul
ㄱ=1;ㄴ=2;ㄷ=3;ㄹ=4;ㅁ=5
ㅂ=6;ㅅ=7;ㅇ=8;ㅈ=9;ㅊ=0
ss = input("input : ")
ss = ss.replace('!','\n')
ss = ss.splitlines()
i = j = 0
cc = c = 65
test = 400;
cur = ss[i][j]                                                                  # cur means current position of process (cursor)
director = 2                                                                    #director is direction of process  1 is up, 2 is right, 3 is down, 4 is left, 0 is end
while director and test:


    if hangul.is_consonant(cur) or hangul.is_vowel(cur):                           #Filtering bad char

        if director == 0 : break
        if director == 1 : i -= 1
        if director == 2 : j += 1
        if director == 3 : i += 1
        if director == 4 : j -= 1

        if i >= len(ss) : i = 0;
        if j >= len(ss[i]) : j = 0;

        cur = ss[i][j]
        test -=1

    else:
        ini = hangul.get_initial(cur)                                               #in first, extract initial,vowel,finish from the cur
        mid = hangul.get_vowel(cur)
        fin = hangul.get_final(cur)

        test -= 1

        if mid == 'ㅗ' : director = 1                                               #process director
        if mid == 'ㅏ' : director = 2
        if mid == 'ㅜ' : director = 3
        if mid == 'ㅓ' : director = 4
        if director == 0 : break
        if director == 1 : i -= 1
        if director == 2 : j += 1
        if director == 3 : i += 1
        if director == 4 : j -= 1

        if mid == 'ㅛ' : c+=1
        if mid == 'ㅠ' : c-=1

        if mid == 'ㅐ' :
            if fin == 'ㅍ' : c+=ini; print(chr(c),end='')

        if i >= len(ss) : i = 0;                                                     #check for out of index
        if j >= len(ss[i]) : j = 0;

        cur = ss[i][j]

