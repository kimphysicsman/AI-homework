import tkinter as tk

win = tk.Tk()
win.title('계산기')

# 명령어 변수
operator = {'+':1, '-':2, '*':3,
            '/':4, 'C':5, '=':6}
stoValue = 0    # 저장된 값
opPre = ''       # 이전 명령어
disValue = 0    # 결과값 변수
btnPre = 0      # 전에 눌린 버튼의 종류  0:눌린적없음, 1:숫자, 2:명령어

def number_click(value):
    #print('숫자', value)
    global disValue, btnPre
    if btnPre == 1:         # 33
        disValue = (disValue * 10) + value
        if opPre != '':
            str_value.set(str(stoValue) + opPre + str(disValue))
        else:
            str_value.set(str(disValue))
    elif btnPre == 0:       # 3
        disValue = value
        btnPre = 1
        str_value.set(disValue)
    else:                   # 3 + 3
        if opPre != '=':
            disValue = value
            btnPre = 1
            str_value.set(str(stoValue) + opPre + str(disValue))
        else:
            clear()
            number_click(value)

def clear():
    global disValue, operator, stoValue, opPre, btnPre
    stoValue = 0
    opPre = ''
    disValue = 0
    btnPre = 0
    str_value.set(disValue)

def operator_click(value):
    #print('명령', value)
    global disValue, operator, stoValue, opPre, btnPre
    print(stoValue, opPre, disValue, value)
    op = operator[value]    # 현재 눌린 명령어
    if op == 5:             # C 눌린 경우
        clear()
    elif btnPre == 0:       # 눌린적 없는데 명령어가 먼저 눌린 경우
        return
    elif btnPre == 2:       # 명령어가 누른상태로 또 명령어가 눌린 경우
        opPre = value              # 현재 눌린 명령어로 최신화
        if op != 6:
            str_value.set(str(disValue) + value)
    else:                   # 숫자가 눌린 다음 명령어 눌린 경우
        tempValue = disValue
        if opPre == '+':
            disValue = stoValue + disValue
        if opPre == '-':
            disValue = stoValue - disValue
        if opPre == '*':
            disValue = stoValue * disValue
        if opPre == '/':
            try:
                disValue = stoValue / disValue
            except:
                disValue = stoValue

        if op != 6:                     # 3 +
            str_value.set(str(disValue) + value)
        else:                           # 3 + 3 = 6
            if opPre != '':
                str_value.set(str(stoValue) + opPre + str(tempValue)
                            + value + str(disValue))
        opPre = value
        stoValue = disValue
        btnPre = 2

def button_click(value):
    try:
        value = int(value)
        number_click(value)
    except:
        operator_click(value)

str_value = tk.StringVar()
str_value.set(stoValue)
tk.Entry(win, textvariable=str_value, justify='right',
         bg='white', fg='red')\
    .grid(column=0, row=0, columnspan=4, ipadx=80, ipady=30)

# 계산기 버튼
calItem = [
    ['1', '2', '3', '+'],
    ['4', '5', '6', '-'],
    ['7', '8', '9', '*'],
    ['0', '=', 'C', '/']
]
for i, items in enumerate(calItem):
    for j, item in enumerate(items):

        try:
            color = int(item)
            color = 'black'
        except:
            color = 'green'

        bt = tk.Button(win,
                       text=item,
                       width=10,
                       height=5,
                       bg=color,
                       fg='white',
                       command=lambda cmd=item: button_click(cmd))
        bt.grid(column=j, row=i+1)

win.mainloop()