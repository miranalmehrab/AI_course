from tkinter import *

root = Tk()
root.geometry("800x500") #window size  
frame = Frame(root) #adding a frame
frame.pack() 

btn_text = [[ '', '' ,'', '', '', '', '', '', '','' ],
            [ '', '' ,'', '', '', '', '', '', '','' ],
            [ '', '' ,'', '', '', '', '', '', '','' ],
            [ '', '' ,'', '', '', '', '', '', '','' ],
            [ '', '' ,'', '', '', '', '', '', '','' ],
            [ '', '' ,'', '', '', '', '', '', '','' ],
            [ '', '' ,'', '', '', '', '', '', '','' ],
            [ '', '' ,'', '', '', '', '', '', '','' ],
            [ '', '' ,'', '', '', '', '', '', '','' ],
            [ '', '' ,'', '', '', '', '', '', '','' ]]
click_counter = -1



def get_counter():
    global click_counter
    click_counter = click_counter + 1
    if(click_counter%2 == 0):
        return 1
    else:
        return 0     



def update_btn_text(index):
    print(click_counter)
    i = int(index[0])
    j = int(index[1])
    if(btn_text[i][j] == ''):
        ch = ''
        if(get_counter() == 0):
            ch = '*'
        else:
            ch = 'o'

        btn_text[i][j] = ch
        print(i,"   ",j,"  ",btn_text[i][j])
        return ch
    else:
        return btn_text[i][j]

#print(btn_text[0])

button00 = Button(frame, fg = 'red',command = lambda: button00.config(text=update_btn_text('00')))
button01 = Button(frame, fg = 'red',command = lambda: button01.config(text=update_btn_text('01')))
button02 = Button(frame, fg = 'red',command = lambda: button02.config(text=update_btn_text('02')))
button03 = Button(frame, fg = 'red',command = lambda: button03.config(text=update_btn_text('03')))
button04 = Button(frame, fg = 'red',command = lambda: button04.config(text=update_btn_text('04')))
button05 = Button(frame, fg = 'red',command = lambda: button05.config(text=update_btn_text('05')))
button06 = Button(frame, fg = 'red',command = lambda: button06.config(text=update_btn_text('06')))
button07 = Button(frame, fg = 'red',command = lambda: button07.config(text=update_btn_text('07')))
button08 = Button(frame, fg = 'red',command = lambda: button08.config(text=update_btn_text('08')))
button09 = Button(frame, fg = 'red',command = lambda: button09.config(text=update_btn_text('09')))

button10 = Button(frame, fg = 'red',command = lambda: button10.config(text=update_btn_text('10')))
button11 = Button(frame, fg = 'red',command = lambda: button11.config(text=update_btn_text('11')))
button12 = Button(frame, fg = 'red',command = lambda: button12.config(text=update_btn_text('12')))
button13 = Button(frame, fg = 'red',command = lambda: button13.config(text=update_btn_text('13')))
button14 = Button(frame, fg = 'red',command = lambda: button14 .config(text=update_btn_text('14')))
button15 = Button(frame, fg = 'red',command = lambda: button15 .config(text=update_btn_text('15')))
button16 = Button(frame, fg = 'red',command = lambda: button16.config(text=update_btn_text('16')))
button17 = Button(frame, fg = 'red',command = lambda: button17.config(text=update_btn_text('17')))
button18 = Button(frame, fg = 'red',command = lambda: button18.config(text=update_btn_text('18')))
button19 = Button(frame, fg = 'red',command = lambda: button19.config(text=update_btn_text('19')))

button20 = Button(frame, fg = 'red',command = lambda: button20.config(text=update_btn_text('20')))
button21 = Button(frame, fg = 'red',command = lambda: button21.config(text=update_btn_text('21')))
button22 = Button(frame, fg = 'red',command = lambda: button22.config(text=update_btn_text('22')))
button23 = Button(frame, fg = 'red',command = lambda: button23.config(text=update_btn_text('23')))
button24 = Button(frame, fg = 'red',command = lambda: button24.config(text=update_btn_text('24')))
button25 = Button(frame, fg = 'red',command = lambda: button25.config(text=update_btn_text('25')))
button26 = Button(frame, fg = 'red',command = lambda: button26.config(text=update_btn_text('26')))
button27 = Button(frame, fg = 'red',command = lambda: button27.config(text=update_btn_text('27')))
button28 = Button(frame, fg = 'red',command = lambda: button28.config(text=update_btn_text('28')))
button29 = Button(frame, fg = 'red',command = lambda: button29.config(text=update_btn_text('29')))

button30 = Button(frame, fg = 'red',command = lambda: button30.config(text=update_btn_text('30')))
button31 = Button(frame, fg = 'red',command = lambda: button31.config(text=update_btn_text('31')))
button32 = Button(frame, fg = 'red',command = lambda: button32.config(text=update_btn_text('32')))
button33 = Button(frame, fg = 'red',command = lambda: button33.config(text=update_btn_text('33')))
button34 = Button(frame, fg = 'red',command = lambda: button34.config(text=update_btn_text('34')))
button35 = Button(frame, fg = 'red',command = lambda: button35.config(text=update_btn_text('35')))
button36 = Button(frame, fg = 'red',command = lambda: button36.config(text=update_btn_text('36')))
button37 = Button(frame, fg = 'red',command = lambda: button37.config(text=update_btn_text('37')))
button38 = Button(frame, fg = 'red',command = lambda: button38.config(text=update_btn_text('38')))
button39 = Button(frame, fg = 'red',command = lambda: button39.config(text=update_btn_text('39')))

button40 = Button(frame, fg = 'red',command = lambda: button40.config(text=update_btn_text('40')))
button41 = Button(frame, fg = 'red',command = lambda: button41.config(text=update_btn_text('41')))
button42 = Button(frame, fg = 'red',command = lambda: button42.config(text=update_btn_text('42')))
button43 = Button(frame, fg = 'red',command = lambda: button43.config(text=update_btn_text('43')))
button44 = Button(frame, fg = 'red',command = lambda: button44.config(text=update_btn_text('44')))
button45 = Button(frame, fg = 'red',command = lambda: button45.config(text=update_btn_text('45')))
button46 = Button(frame, fg = 'red',command = lambda: button46.config(text=update_btn_text('46')))
button47 = Button(frame, fg = 'red',command = lambda: button47.config(text=update_btn_text('47')))
button48 = Button(frame, fg = 'red',command = lambda: button48.config(text=update_btn_text('48')))
button49 = Button(frame, fg = 'red',command = lambda: button49.config(text=update_btn_text('49')))

button50 = Button(frame, fg = 'red',command = lambda: button50.config(text=update_btn_text('50')))
button51 = Button(frame, fg = 'red',command = lambda: button51.config(text=update_btn_text('51')))
button52 = Button(frame, fg = 'red',command = lambda: button52.config(text=update_btn_text('52')))
button53 = Button(frame, fg = 'red',command = lambda: button53.config(text=update_btn_text('53')))
button54 = Button(frame, fg = 'red',command = lambda: button54.config(text=update_btn_text('54')))
button55 = Button(frame, fg = 'red',command = lambda: button55.config(text=update_btn_text('55')))
button56 = Button(frame, fg = 'red',command = lambda: button56.config(text=update_btn_text('56')))
button57 = Button(frame, fg = 'red',command = lambda: button57.config(text=update_btn_text('57')))
button58 = Button(frame, fg = 'red',command = lambda: button58.config(text=update_btn_text('58')))
button59 = Button(frame, fg = 'red',command = lambda: button59.config(text=update_btn_text('59')))

button60 = Button(frame, fg = 'red',command = lambda: button60.config(text=update_btn_text('60')))
button61 = Button(frame, fg = 'red',command = lambda: button61.config(text=update_btn_text('61')))
button62 = Button(frame, fg = 'red',command = lambda: button62.config(text=update_btn_text('62')))
button63 = Button(frame, fg = 'red',command = lambda: button63.config(text=update_btn_text('63')))
button64 = Button(frame, fg = 'red',command = lambda: button64.config(text=update_btn_text('64')))
button65 = Button(frame, fg = 'red',command = lambda: button65.config(text=update_btn_text('65')))
button66 = Button(frame, fg = 'red',command = lambda: button66.config(text=update_btn_text('66')))
button67 = Button(frame, fg = 'red',command = lambda: button67.config(text=update_btn_text('67')))
button68 = Button(frame, fg = 'red',command = lambda: button68.config(text=update_btn_text('68')))
button69 = Button(frame, fg = 'red',command = lambda: button69.config(text=update_btn_text('69')))

button70 = Button(frame, fg = 'red',command = lambda: button70.config(text=update_btn_text('70')))
button71 = Button(frame, fg = 'red',command = lambda: button71.config(text=update_btn_text('71')))
button72 = Button(frame, fg = 'red',command = lambda: button72.config(text=update_btn_text('72')))
button73 = Button(frame, fg = 'red',command = lambda: button73.config(text=update_btn_text('73')))
button74 = Button(frame, fg = 'red',command = lambda: button74.config(text=update_btn_text('74')))
button75 = Button(frame, fg = 'red',command = lambda: button75.config(text=update_btn_text('75')))
button76 = Button(frame, fg = 'red',command = lambda: button76.config(text=update_btn_text('76')))
button77 = Button(frame, fg = 'red',command = lambda: button77.config(text=update_btn_text('77')))
button78 = Button(frame, fg = 'red',command = lambda: button78.config(text=update_btn_text('78')))
button79 = Button(frame, fg = 'red',command = lambda: button79.config(text=update_btn_text('79')))

button80 = Button(frame, fg = 'red',command = lambda: button80.config(text=update_btn_text('80')))
button81 = Button(frame, fg = 'red',command = lambda: button81.config(text=update_btn_text('81')))
button82 = Button(frame, fg = 'red',command = lambda: button82.config(text=update_btn_text('82')))
button83 = Button(frame, fg = 'red',command = lambda: button83.config(text=update_btn_text('83')))
button84 = Button(frame, fg = 'red',command = lambda: button84.config(text=update_btn_text('84')))
button85 = Button(frame, fg = 'red',command = lambda: button85.config(text=update_btn_text('85')))
button86 = Button(frame, fg = 'red',command = lambda: button86.config(text=update_btn_text('86')))
button87 = Button(frame, fg = 'red',command = lambda: button87.config(text=update_btn_text('87')))
button88 = Button(frame, fg = 'red',command = lambda: button88.config(text=update_btn_text('88')))
button89 = Button(frame, fg = 'red',command = lambda: button89.config(text=update_btn_text('89')))

button90 = Button(frame, fg = 'red',command = lambda: button90.config(text=update_btn_text('90')))
button91 = Button(frame, fg = 'red',command = lambda: button91.config(text=update_btn_text('91')))
button92 = Button(frame, fg = 'red',command = lambda: button92.config(text=update_btn_text('92')))
button93 = Button(frame, fg = 'red',command = lambda: button93.config(text=update_btn_text('93')))
button94 = Button(frame, fg = 'red',command = lambda: button94.config(text=update_btn_text('94')))
button95 = Button(frame, fg = 'red',command = lambda: button95.config(text=update_btn_text('95')))
button96 = Button(frame, fg = 'red',command = lambda: button96.config(text=update_btn_text('96')))
button97 = Button(frame, fg = 'red',command = lambda: button97.config(text=update_btn_text('97')))
button98 = Button(frame, fg = 'red',command = lambda: button98.config(text=update_btn_text('98')))
button99 = Button(frame, fg = 'red',command = lambda: button99.config(text=update_btn_text('99')))




def reset_all():
    '''for i in range(0, 9):
        for j in range(0, 9):
            btn_text[i][j] = '''
    button00.config(text='hello')
        
    



icon_replay = PhotoImage(file="/home/miran/Desktop/gomuko/replay.png")
icon_exit = PhotoImage(file="/home/miran/Desktop/gomuko/logout.png")

button_replay = Button(frame, image=icon_replay, command=reset_all())
button_exit = Button(frame,image=icon_exit,command=root.destroy)


button00.grid(row = 0, column=0)
button01.grid(row = 0, column=1)
button02.grid(row = 0, column=2)
button03.grid(row = 0, column=3)
button04.grid(row = 0, column=4)
button05.grid(row = 0, column=5)
button06.grid(row = 0, column=6)
button07.grid(row = 0, column=7)
button08.grid(row = 0, column=8)
button09.grid(row = 0, column=9)

button10.grid(row = 1, column=0)
button11.grid(row = 1, column=1)
button12.grid(row = 1, column=2)
button13.grid(row = 1, column=3)
button14.grid(row = 1, column=4)
button15.grid(row = 1, column=5)
button16.grid(row = 1, column=6)
button17.grid(row = 1, column=7)
button18.grid(row = 1, column=8)
button19.grid(row = 1, column=9)

button20.grid(row =  2, column=0)
button21.grid(row =  2, column=1)
button22.grid(row =  2, column=2)
button23.grid(row =  2, column=3)
button24.grid(row =  2, column=4)
button25.grid(row =  2, column=5)
button26.grid(row =  2, column=6)
button27.grid(row =  2, column=7)
button28.grid(row =  2, column=8)
button29.grid(row =  2, column=9)

button30.grid(row =  3, column=0)
button31.grid(row =  3, column=1)
button32.grid(row =  3, column=2)
button33.grid(row =  3, column=3)
button34.grid(row =  3, column=4)
button35.grid(row =  3, column=5)
button36.grid(row =  3, column=6)
button37.grid(row =  3, column=7)
button38.grid(row =  3, column=8)
button39.grid(row =  3, column=9)

button40.grid(row =  4, column=0)
button41.grid(row =  4, column=1)
button42.grid(row =  4, column=2)
button43.grid(row =  4, column=3)
button44.grid(row =  4, column=4)
button45.grid(row =  4, column=5)
button46.grid(row =  4, column=6)
button47.grid(row =  4, column=7)
button48.grid(row =  4, column=8)
button49.grid(row =  4, column=9)

button50.grid(row =  5, column=0)
button51.grid(row =  5, column=1)
button52.grid(row =  5, column=2)
button53.grid(row =  5, column=3)
button54.grid(row =  5, column=4)
button55.grid(row =  5, column=5)
button56.grid(row =  5, column=6)
button57.grid(row =  5, column=7)
button58.grid(row =  5, column=8)
button59.grid(row =  5, column=9)

button60.grid(row =  6, column=0)
button61.grid(row =  6, column=1)
button62.grid(row =  6, column=2)
button63.grid(row =  6, column=3)
button64.grid(row =  6, column=4)
button65.grid(row =  6, column=5)
button66.grid(row =  6, column=6)
button67.grid(row =  6, column=7)
button68.grid(row =  6, column=8)
button69.grid(row =  6, column=9)

button70.grid(row =  7, column=0)
button71.grid(row =  7, column=1)
button72.grid(row =  7, column=2)
button73.grid(row =  7, column=3)
button74.grid(row =  7, column=4)
button75.grid(row =  7, column=5)
button76.grid(row =  7, column=6)
button77.grid(row =  7, column=7)
button78.grid(row =  7, column=8)
button79.grid(row =  7, column=9)

button80.grid(row =  8, column=0)
button81.grid(row =  8, column=1)
button82.grid(row =  8, column=2)
button83.grid(row =  8, column=3)
button84.grid(row =  8, column=4)
button85.grid(row =  8, column=5)
button86.grid(row =  8, column=6)
button87.grid(row =  8, column=7)
button88.grid(row =  8, column=8)
button89.grid(row =  8, column=9)

button90.grid(row =  9, column=0)
button91.grid(row =  9, column=1)
button92.grid(row =  9, column=2)
button93.grid(row =  9, column=3)
button94.grid(row =  9, column=4)
button95.grid(row =  9, column=5)
button96.grid(row =  9, column=6)
button97.grid(row =  9, column=7)
button98.grid(row =  9, column=8)
button99.grid(row =  9, column=9)

button_replay.grid(row = 10, column = 0)
button_exit.grid(row = 10 , column = 1)

root.mainloop()