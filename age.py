drive = input('請問你是否開過車 : ')
age   = int(input('請問目前年齡 : '))
if drive == '有':
    if age >=18:
        print('你通過測驗了')
    else:
        print('阿你無照喔?')
elif drive == '沒有':
    if age >18:
        print('你可以去考駕照囉!')
    else:
        print('再過幾年再去考吧!')
else:
    print('不要亂回答好ㄇ?')
