# -*- coding: utf-8 -*-
import tkinter as tki
import hangul
class App(object):

    def __init__(self):
        self.root = tki.Tk()

    # create a Frame for the Text and Scrollbar
        txt_frm = tki.Frame(self.root, width=200, height=200)
        txt_frm.pack(fill="both", expand=True)

        # ensure a consistent GUI size
        txt_frm.grid_propagate(False)

        # implement stretchability
        txt_frm.grid_rowconfigure(0, weight=1)
        txt_frm.grid_columnconfigure(0, weight=1)

    # create a Text widget
        self.txt = tki.Text(txt_frm, borderwidth=3, relief="sunken")
        self.txt.config(font=("consolas", 12), undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        self.text = tki.Text()
        self.text.pack()


    # create a Scrollbar and associate it with txt
        scrollb = tki.Scrollbar(txt_frm, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set

        tki.Button(txt_frm, text='Retrieve input', command=self.retrieve_input).grid(row=1, column=0)

    def retrieve_input(self):
        lines = self.txt.get("1.0", tki.END)
        Processor(lines)

    def printf(self,arg1):
        self.text.insert(tki.INSIDE,arg1)


def Processor(arg1) :
    global i,j,director,cur,ini,mid,fin
    ini = mid = fin = ''
    ss = arg1
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
        elif hangul.is_consonant(cur) :ini = hangul.get_initial(cur); mid = fin = ''   #in first, extract initial,vowel,finish from the cur
        elif hangul.is_vowel(cur) :  mid = hangul.get_vowel(cur); ini = fin = ''
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
                        digit = 1
                        while limit:
                            move()
                            if ini:digit *= 0.1;tempnum += rv(ini)*digit
                            if mid:digit *= 0.1;tempnum += rv(mid)*digit
                            if fin:digit *= 0.1;tempnum += rv(fin)*digit
                            else : limit = 0;break
                            if cur == 'ㅒ' : limit = 0;break
                else :
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
                            digit = 1
                            while limit:
                                move()
                                if ini:digit *= 0.1;tempnum += rv(ini)*digit
                                if mid:digit *= 0.1;tempnum += rv(mid)*digit
                                if fin:digit *= 0.1;tempnum += rv(fin)*digit
                                else : limit = 0;break
                                if cur == 'ㅒ' : limit = 0;break
                        else : break
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
            elif fin == 'ㄵ' :
                skipblock = rv(ini)+1
                while skipblock:
                    move()
                    skipblock -= 1
            elif ini in cval or ini in sval:
                if rv(ini) == rv(fin) : Cdirector(mid);print('D')
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
                    if mid == 'ㅣ': suhak = rv(ini) * rv(fin); move(); vs(ini,suhak)
                if fin == 'ㅁ' :
                    move()
                    if mid == 'ㅣ': suhak = rv(ini) // rv(fin); move(); vs(ini,suhak)
                if fin == 'ㅎ' :
                    move()
                    if mid == 'ㅣ': suhak = rv(ini) + rv(fin); move(); vs(ini,suhak)
                if fin == 'ㅇ' :
                    move()
                    if mid == 'ㅣ': suhak = rv(ini) - rv(fin); move(); vs(ini,suhak)
                if fin == 'ㄴ' :
                    move()
                    if mid == 'ㅣ': suhak = rv(ini) % rv(fin); move(); vs(ini,suhak)
                if fin == 'ㅈ' :
                    move()
                    if mid == 'ㅣ': suhak = rv(ini) / rv(fin); move(); vs(ini,suhak)

        if mid == 'ㅢ' :
            if fin == 'ㄼ' : decoder(ini,fin)
            if fin == 'ㄾ' : decoder(ini,fin)
            else : vs(ini,rv(fin))


        if mid == 'ㅔ' :
            if ini == 'ㅍ' : App.text.insert(tki.INSERT,rv(fin))                                 # print pure value
            if ini == 'ㅈ' : print(int(rv(fin)),end='');                            # print int value
            if ini == 'ㅁ' : ttl = rv(fin)                                          # set time-to-live
            if ini == 'ㅅ' : vs(fin,input(fin +" : "))                              # set value by input
    print(arg1)


app = App()
app.root.mainloop()
