# -*- coding: utf-8 -*-
#디코더에서 숫자 디코딩 문제

"""

hangul 모듈 import
ini = mid = fin 초기화
ss에 초기값 입력
ss가 빈값이면 그냥 종료
ss에서 ㅈ는 CR로 처리
기본 숫자변수 c1~4는 기본값으로 65를 준다
기본 문자열 s1~2는 기본값으로 'Sample'을 준다
Direct 요소 i,j를 오른쪽으로 설정





move() : i 와 j값에 따라 cur을 움직인다. 유효 범위인지 검사하고 유효 문자열인지도 검사한다

rv() : Return Value, ㄱ~ㅊ 까지 1~9,0을 반환 ㅋㅌㅍㅎ가 숫자변수, ㄲㅆ가 문자열변수를 반환한다

vs(arg1,arg2) : Value Setter, arg1에 arg2를 대입한다



"""


import hangul
ini = mid = fin = ''
ss = input("input : ")
if not ss : exit()
ss = ss.replace('ㅈ','\n')
ss = ss.splitlines()
c1 = c2 = c3 = c4 = 65                                                          #c1 for 패
s1 = s2 = 'Sample'
i = 0
j = -1
cur = ss[i][j]                                                                  # cur means current position of process (cursor)
director = 2                                                                    #director is direction of process  1 is up, 2 is right, 3 is down, 4 is left, 0 is end
ttl = 100
cval = ['ㅋ','ㅌ','ㅍ','ㅎ',]
sval = ['ㄲ','ㅆ']

def move():
    global i,j,director,cur,ini,mid,fin

    if director == 1 : i -= 1
    if director == 2 : j += 1
    if director == 3 : i += 1
    if director == 4 : j -= 1

    if i >= len(ss) or i < 0 : i = 0;                                                     #check for out of index
    if j >= len(ss[i]) or j < 0 : j = 0;

    cur = ss[i][j]

    if ord(cur) > 33 and ord(cur) < 128 : ini = mid = fin = ''
    elif hangul.is_consonant(cur) :ini = hangul.get_initial(cur)   #in first, extract initial,vowel,finish from the cur
    elif hangul.is_vowel(cur) :  mid = hangul.get_vowel(cur)
    else : ini = hangul.get_initial(cur); fin = hangul.get_final(cur); mid = hangul.get_vowel(cur)

def rv(arg1) :                                                                  # Return value
    if arg1 == 'ㄱ' or arg1 ==  'ㅏ': return 1
    elif arg1 == 'ㄴ' or arg1 ==  'ㅑ': return 2
    elif arg1 == 'ㄷ' or arg1 ==  'ㅓ': return 3
    elif arg1 == 'ㄹ' or arg1 ==  'ㅕ': return 4
    elif arg1 == 'ㅁ' or arg1 ==  'ㅗ': return 5
    elif arg1 == 'ㅂ' or arg1 ==  'ㅛ': return 6
    elif arg1 == 'ㅅ' or arg1 ==  'ㅜ': return 7
    elif arg1 == 'ㅇ' or arg1 ==  'ㅠ': return 8
    elif arg1 == 'ㅈ' or arg1 ==  'ㅡ': return 9
    elif arg1 == 'ㅊ' or arg1 ==  'ㅣ': return 0
    elif arg1 == 'ㅋ': return c1
    elif arg1 == 'ㅌ': return c2
    elif arg1 == 'ㅍ': return c3
    elif arg1 == 'ㅎ': return c4
    elif arg1 == 'ㄲ': return s1
    elif arg1 == 'ㅆ': return s2
    else : return 0

def vs(arg1,arg2):
    global c1,c2,c3,c4,s1,s2
    if arg1 == 'ㅋ': c1 = float(arg2)
    if arg1 == 'ㅌ': c2 = float(arg2)
    if arg1 == 'ㅍ': c3 = float(arg2)
    if arg1 == 'ㅎ': c4 = float(arg2)
    if arg1 == 'ㄲ': s1 = arg2
    if arg1 == 'ㅆ': s2 = arg2

def va(arg1,arg2):
    global c1,c2,c3,c4,s1,s2
    if arg1 == 'ㅋ': c1 += float(arg2)
    if arg1 == 'ㅌ': c2 += float(arg2)
    if arg1 == 'ㅍ': c3 += float(arg2)
    if arg1 == 'ㅎ': c4 += float(arg2)
    if arg1 == 'ㄲ': s1 += arg2
    if arg1 == 'ㅆ': s2 += arg2

def decoder(arg1,mode):
    global cur,ini,mid,fin,director
    limit = 256
    if mode == "ㄼ" :                                                           # pure string
        origin = arg1
        arg1 = ''
        while limit:
            move()
            if cur == 'ㅒ': break
            arg1 += cur
            limit -= 1
            if not limit : director = 0
        vs(origin,arg1)
    if mode == 'ㄾ' :                                                           # Encoded number
        tempnum = tempnum2 = 0
        while limit:
            move()
            if ini == 'ㅉ' :
                    tempnum2 = tempnum
                    tempnum = 0
                    while limit:
                        move()
                        if ini:tempnum /= 10;tempnum += rv(ini)*0.1
                        if mid:tempnum /= 10;tempnum += rv(mid)*0.1
                        if fin:tempnum /= 10;tempnum += rv(fin)*0.1
                        else : limit = 0;break
                        if cur == 'ㅒ' : limit = 0;break
            if cur == 'ㅒ':
                break
            if ini:tempnum *= 10;tempnum += rv(ini)
            if mid:tempnum *= 10;tempnum += rv(mid)
            if fin:tempnum *= 10;tempnum += rv(fin)
            else :
                move()
                if ini == 'ㅉ' :
                    tempnum2 = tempnum
                    tempnum = 0
                    while limit:
                        move()
                        if ini:tempnum /= 10;tempnum += rv(ini)*0.1
                        if mid:tempnum /= 10;tempnum += rv(mid)*0.1
                        if fin:tempnum /= 10;tempnum += rv(fin)*0.1
                        else : limit = 0;break
                        if cur == 'ㅒ' : limit = 0;break
                else : break
        print(tempnum,tempnum2)
        return vs(arg1,tempnum + tempnum2)





def Cdirector(arg1):                                                            #Change director
    global director
    if arg1 == 'ㅗ' : director = 1
    if arg1 == 'ㅏ' : director = 2
    if arg1 == 'ㅜ' : director = 3
    if arg1 == 'ㅓ' : director = 4

while director and ttl:
    move()
    ttl -= 1

    if mid == 'ㅡ' :
        if ini == 'ㄲ' and fin == 'ㅌ' : director = 0;print("  끝  ")


    if mid == 'ㅏ' or mid == 'ㅓ' or mid ==  'ㅗ' or mid ==  'ㅜ':
        if ini == 'ㅉ' :
            limit = 256
            while limit:
                move()
                if mid == 'ㅣ' : break
                limit -= 1
                if not limit : director = 0
        elif ini in cval or ini in sval :
            if rv(ini) == rv(fin) : Cdirector(mid)
        else : Cdirector(mid)


    if mid == 'ㅛ' : va(ini,rv(fin))
    if mid == 'ㅠ' : va(ini,-rv(fin))

    if mid == 'ㅐ' :
        if ini == 'ㅍ' :
            if fin == 'ㄲ' or fin == 'ㅆ' : print(rv(fin),end='')
            elif fin == 'ㄱ' : print(" ",end='')
            elif fin == 'ㅈ' : print("")
            else : print(chr(int(rv(fin))),end='')
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
            if fin == 'ㅈ' :
                move()
                if mid == 'ㅣ': suhak = rv(ini) / rv(fin); move(); vs(fin,suhak)

    if mid == 'ㅢ' :
        if fin == 'ㄼ' : decoder(ini,fin)
        if fin == 'ㄾ' : decoder(ini,fin)
        else : vs(ini,rv(fin))


    if mid == 'ㅔ' :
        if ini == 'ㅍ' : print(rv(fin),end='');                                 # print pure value
        if ini == 'ㅁ' : ttl = rv(fin)                                          # set time-to-live
        if ini == 'ㅅ' : vs(fin,input(fin +" : "))                              # set value by input


print(ss)

