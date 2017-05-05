# -*- coding: utf-8 -*-

import hangul
from tkinter import *
ini = mid = fin = ''
c1 = c2 = c3 = c4 = 0                                                         #c1 for 패
s1 = s2 = 'Sample'
i = 0
j = -1
ss = 'Sample'
cur = ss[i][j]                                                                  # cur means current position of process (cursor)
director = 0                                                                    #director is direction of process  1 is up, 2 is right, 3 is down, 4 is left, 0 is end
ttl = 0
cval = ['ㅋ','ㅌ','ㅍ','ㅎ',]
sval = ['ㄲ','ㅆ']


def move():
        global i,j,director,cur,ini,mid,fin,ss
        ini = mid = fin = ''
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

def rv(arg1) :
    global c1,c2,c3,c4,s1,s2,ttl                                                            # Return value
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
    elif arg1 == 'ㄳ': return ttl
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
    limit = 64
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
            elif mid == 'ㅒ':
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
        print(tempnum, tempnum2)
        return vs(arg1,tempnum + tempnum2)




class MyApp:

    def __init__(self, parent):
        self.myParent = parent
        self.myParent['bg'] = 'gray'
        self.TopContainer = Frame(self.myParent, padx = 20, pady = 20, bg ='grey')
        self.TopContainer.pack()
        self.BottomContainer = Frame(self.myParent, pady = 10, bg ='grey')
        self.BottomContainer.pack()
        self.myParent.resizable(False, False)


        self.Input = Text(self.TopContainer, width = 35, height = 20, relief = SUNKEN, bd = 7, bg= 'black', fg = 'green', undo = TRUE, insertbackground = 'green', selectbackground = 'white',selectforeground = 'black')
        self.Input.insert(END,"Input")
        self.Input.bind("<FocusIn>", self.InputFocusIn)
        self.Input.bind("<Control-Key-a>", self.InputFocusIn)
        self.Input.pack(side = LEFT, fill = BOTH)

        self.MiddleContainer = Frame(self.TopContainer)
        self.MiddleContainer.pack(side = LEFT, fill = BOTH)
        self.ButtonContainer = Frame(self.MiddleContainer, padx = 20, bg ='grey')
        self.ButtonContainer.pack(side = TOP, ipady = 10)
        self.DecodeLabel = Label(self.MiddleContainer, text = "<Decode Option>")
        self.DecodeLabel.pack()

        DecodeVar = IntVar()

        self.DecodeOpt_1 = Radiobutton(self.MiddleContainer, text="KOR -> NUM", value = 0, variable = DecodeVar, state = 'normal')
        self.DecodeOpt_1.pack()
        self.DecodeOpt_2 = Radiobutton(self.MiddleContainer, text="KOR -> ASC", value = 1, variable = DecodeVar, state = 'normal')
        self.DecodeOpt_2.pack()



        self.Compile = Button(self.ButtonContainer, text = "Compile", width = 7, command = self.CompileClick)
        self.Compile.pack(side = TOP)
        self.Decode = Button(self.ButtonContainer, text = "Decode", width = 7, command = self.DecodeClick)
        self.Decode.pack(side = TOP)
        self.Quit = Button(self.ButtonContainer, text = "Quit", command = self.QuitClick)
        self.Quit.pack(side = BOTTOM)
        self.Debug = Button(self.ButtonContainer, text = "Debug", width = 7, command = self.DebugClick)
        self.Debug.pack(side = TOP)

        self.RightLabel = Label(self.BottomContainer, text = "Powerd by Python 3, JDH -GFLH Nerd-  ver 0.1", bg = 'grey', fg = 'red')
        self.RightLabel.pack(side = TOP)

        self.Decoder = Text(self.TopContainer, width = 35, height = 20, relief = SUNKEN, bd = 7, bg = 'black', fg = 'green', undo = TRUE, insertbackground = 'green', selectbackground = 'white',selectforeground = 'black')
        self.Decoder.insert(END,"Decoder or Debugger")
        self.Decoder.bind("<FocusIn>", self.DecodeFocusIn)
        self.Decoder.bind("<Control-Key-a>", self.DecodeFocusIn)
        self.Decoder.pack(side = LEFT, fill = BOTH)

        self.Interpreter = Text(self.BottomContainer, height = 20, relief = SUNKEN, bd = 7, bg = 'black', fg = 'green', undo = TRUE, insertbackground = 'green', selectbackground = 'white',selectforeground = 'black')
        self.Interpreter.insert(END,"Interpreter")
        self.Interpreter.pack(side = BOTTOM , fill = BOTH, expand = 1)

    def DecodeClick(self):
        self.Decoder.insert(END,"D")

    def DebugClick(self):
        global director, ttl, ini, mid, fin, ss, c1,c2,c3,c4, s1,s2, cur, cval , sval, ss, i, j

        self.CompileClick()
        self.Decoder.delete(1.0,END)

        self.Decoder.insert(END,"디버깅..\n"+(self.Input.index(INSERT)).split(".")[0] + "줄의 " + str(int((self.Input.index(INSERT)).split(".")[1])+1) + "번째 문자 처리..\n")
        i = int((self.Input.index(INSERT)).split(".")[0])
        j = int((self.Input.index(INSERT)).split(".")[1])-1
        move()
        self.Decoder.insert(END,"\ndirector : "+str(director))
        self.Decoder.insert(END,"\nttl : "+str(ttl))
        self.Decoder.insert(END,"\ncur : "+cur)
        self.Decoder.insert(END,"\nc1 : %f\nc2 : %f\nc3 : %f\nc4 : %f"%(c1,c2,c3,c4))
        self.Decoder.insert(END,"\nini : "+ini)
        self.Decoder.insert(END,"\nmid : "+mid)
        self.Decoder.insert(END,"\nfin : "+fin)
        self.Decoder.insert(END,"\nss : "+str(ss))

    def InputFocusIn(self, event):
        self.Input.tag_add(SEL,1.0,END);
        self.Input.mark_set(INSERT, "1.0")
        self.Input.see(INSERT)
        return 'break'

    def DecodeFocusIn(self, event):
        self.Decoder.tag_add(SEL,1.0,END);
        self.Decoder.mark_set(INSERT, "1.0")
        self.Decoder.see(INSERT)
        return 'break'

    def QuitClick(self):
        self.myParent.destroy()

    def CompileClick(self):
        global director, ttl, ini, mid, fin, ss, c1,c2,c3,c4, s1,s2, cur, cval , sval, ss, i, j
        self.Interpreter.delete(1.0,END)
        ss = self.Input.get(1.0,END)
        if len(ss) == 1 : self.Interpreter.insert(END,"컴파일 하시기 전에 Input 칸을 입력하시오"); return

        ss = ss.splitlines()

        ini = mid = fin = ''
        c1 = c2 = c3 = c4 = 0                                                         #c1 for 패
        s1 = s2 = 'Sample'
        i = 0
        j = -1
        cur = ss[i][j]                                                                  # cur means current position of process (cursor)
        director = 2                                                                    #director is direction of process  1 is up, 2 is right, 3 is down, 4 is left, 0 is end
        ttl = 100

        while director and ttl:

            move()
            ttl -= 1

            if mid == 'ㅡ' :
                if ini == 'ㄲ' and fin == 'ㅌ' : director = 0;self.Interpreter.insert(END,"  끝  ")


            if mid == 'ㅏ' or mid == 'ㅓ' or mid ==  'ㅗ' or mid ==  'ㅜ':
                if ini == 'ㅉ' :
                    limit = 256
                    if mid == 'ㅗ' : director = 1
                    if mid == 'ㅏ' : director = 2
                    if mid == 'ㅜ' : director = 3
                    if mid == 'ㅓ' : director = 4
                    while limit:
                        move()
                        if mid == 'ㅣ' and (director == 2 or director == 4) : break
                        if mid == 'ㅡ' and (director == 1 or director == 3) : break
                        limit -= 1
                        if not limit : director = 0
                elif ini in cval or ini in sval :
                    if rv(ini) == rv(fin) :
                        if mid == 'ㅗ' : director = 1
                        if mid == 'ㅏ' : director = 2
                        if mid == 'ㅜ' : director = 3
                        if mid == 'ㅓ' : director = 4
                else :
                    if mid == 'ㅗ' : director = 1
                    if mid == 'ㅏ' : director = 2
                    if mid == 'ㅜ' : director = 3
                    if mid == 'ㅓ' : director = 4


            if mid == 'ㅛ' : va(ini,rv(fin))
            if mid == 'ㅠ' : va(ini,-rv(fin))

            if mid == 'ㅐ' :
                if ini == 'ㅍ' :
                    if fin in sval : self.Interpreter.insert(END,rv(fin))
                    elif fin == 'ㄱ' : self.Interpreter.insert(END," ")
                    elif fin == 'ㅈ' : self.Interpreter.insert(END,"\n")
                    else : self.Interpreter.insert(END,(chr(int(rv(fin)))))
                if ini == 'ㅅ' :

                    if mid == 'ㅣ':

                        if fin == 'ㄱ' :
                            move()
                            suhak = rv(ini) * rv(fin); move(); vs(fin,suhak)
                        elif fin == 'ㅁ' :
                            move()
                            suhak = rv(ini) // rv(fin); move(); vs(fin,suhak)
                        elif fin == 'ㅎ' :
                            move()
                            suhak = rv(ini) + rv(fin); move(); vs(fin,suhak)
                        elif fin == 'ㅇ' :
                            move()
                            suhak = rv(ini) - rv(fin); move(); vs(fin,suhak)
                        elif fin == 'ㄴ' :
                            move()
                            suhak = rv(ini) % rv(fin); move(); vs(fin,suhak)
                        elif fin == 'ㅈ' :
                            move()
                            suhak = rv(ini) / rv(fin); move(); vs(fin,suhak)
                    else :
                        self.Interpreter.insert(END,"'새' 함수는 ㅣ로 두 변수를 구분합니다")

            if mid == 'ㅢ' :
                if fin == 'ㄼ' : decoder(ini,fin)
                if fin == 'ㄾ' : decoder(ini,fin)
                else : vs(ini,rv(fin))


            if mid == 'ㅔ' :
                if ini == 'ㅍ' : self.Interpreter.insert(END,str(rv(fin)))                                 # print pure value
                if ini == 'ㅈ' : self.Interpreter.insert(END,int(rv(fin)))
                if ini == 'ㅁ' :
                    if fin == '' : ttl = -1
                    elif fin == 'ㄲ' : self.Interpreter.insert(END,ttl)
                    else : ttl = rv(fin)                                          # set time-to-live
                if ini == 'ㅅ' : vs(fin,input(fin +" : "))                              # set value by input

        self.Interpreter.insert(END,"\n--------------------------------------------------------------------------------\n\n" + str(ss) + "의 컴파일이 끝났습니다")


root = Tk()
myapp = MyApp(root)
root.mainloop()


#--------------------------------------------------------TK GUI에 Kor Programming을 이식중...-------------------------------------------------------------------------------------------------------------


#디코더에서 숫자 디코딩 문제

"""
hangul 모듈 import
ini = mid = fin 초기화
ss에 초기값 입력
ss가 빈값이면 그냥 종료
ss에서 ㅈ는 CR로 처리
기본 숫자변수 c1~4는 기본값으로 65를 준다
기본 문자열 s1~2는 기본값으로 'Sample'을 준다
Director 요소 i,j를 오른쪽으로 설정
무한 루프를 방지하기 위해 ttl(Time To Live,100)를 넣음

move() : i 와 j값에 따라 cur을 움직인다. 유효 범위인지 검사하고 유효 문자열인지도 검사한다
rv() : Return Value, ㄱ~ㅊ 까지 1~9,0을 반환 ㅋㅌㅍㅎ가 숫자변수, ㄲㅆ가 문자열변수를 반환한다 또 ㄳ은 ttl을 반환한다
vs(arg1,arg2) : Value Setter, arg1에 arg2를 대입한다
va(arg1,arg2) : Value Adjuster, arg1에 arg2를 가감한다
decoder(arg1,mode):
    mode가 ㄼ면 ㅒ까지 순수 문자열로 디코딩
    mode가 ㄾ면 ㅒ까지 인코딩된 숫자로 디코딩 (ㅉ으로 소수점)

director 또는 ttl이 0이면 컴파일 종료

'끝' -> Exit()   'ㅡㅣ' -> 울타리   'c1 c2 c3 c4 s1 s2' -> cval, sval

'ㅏㅓㅗㅜ'로 Director의 방향 설정 만약 초성이 ㅉ라면 그 방향으로 울타리까지 쩜프
    혹은 초성과 종성이 cval 혹은 sval 이면 이 둘을 비교하고 같을시 Director 방향 변경
    이외의 모음만 달랑 있을 경우 그대로 Director 방향 변경

'ㅛㅠ' 초성에다가 종성값을 더하고 뺀다

'ㅐ'
    만약 초성이 ㅍ라면 이는 프린트 함수. 종성이 'ㄲㅆ'은 문자열 그대로 출력, ㄱ은 공백 ㅈ은 빈줄, 그 이외에는 해당 아스키값을 문자로 출력
    만약 초성이 ㅅ라면 이는 수학 함수. 종성이 ㄱ는 곱하기 ㅁ는 몫 ㅎ합 ㅇ빼기 ㄴ나머지 ㅈ나누기

'ㅢ' 디코더 역할을 한다 종성을 decoder에 mode값으로 준다

'ㅔ' 초성이 ㅍ라면 순수한 종성값 출력, ㅁ라면 ttl를 종성값으로 설정 ㅅ라면 종성에 값을 입력 받는다

"""

#피보나치 : 쿅ㅏ쿝젴팩ㅜㅈㅇㅗ팩젵툨ㅓ
# 걍 테스트용 : 쿅틡즞멪짜팾젵팾ㅣ젴팩쿜쩌
