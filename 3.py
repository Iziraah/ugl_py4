# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


bank = 0
count = 0

def add_bank(cash:int):
    global bank,count
    bank += cash
    count +=1
    print('Ваш баланс: ', bank)
    

def take_bank(cash:int):
    global bank, count
    if cash <=2000:
        cash -=30
    elif 2001 <= cash <= 40000:
        cash *= 0.0985
    else:
        cash -= 600
    bank -= cash
    count +=1
    print('Ваш баланс: ', bank)

def exit_bank():
    print('Рады будем витеть Вас снова!.')
    exit()

# cash = int(input("Введите сумму, кратную 50: "))

def make_dict(id, string, cash):
    dict = {}
    di = {id:{string: cash}}
    # dict.update(di)

    return di


def wellcome():
    # cash
    dict = {}
    id = 1
    while True:
        global bank,count
        action = int(input('1 - Снять\n2 - Пополнить\n3 - Выйти\n'))
        if bank >= 5000000:
            bank *= 0.9
        match action:
            case 1:
                cash = int(input("Введите сумму, кратную 50: "))
                dict.update(make_dict(id, 'take', cash)) 
                id += 1
                # print('yo')
                if cash := cash < bank:
                    take_bank(cash)                                    
                else:
                    print('Нет денег!')
                
            case 2:
                cash = int(input("Введите сумму, кратную 50: "))
                add_bank(cash)
                dict.update(make_dict(id, 'add', cash))
                id += 1
                # di = {'add': cash}
                # dict.update(di)
            case 3:
                print(dict)
                exit_bank()
                
        if count ==3:
            bank *=1.03
            count = 0
wellcome()