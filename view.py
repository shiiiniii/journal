class_db = []

def main_menu() -> int:
    print('Главное меню ')
    menu_list = ['Кто отвечает? ', 
                 'Выход',
                ]
    for i in range(len(menu_list)):
        print(f'    {i+1}.{menu_list[i]}')
    user_input = input('Введите команду >: ')
    if not user_input.isdigit():
        print("Вы должны ввести число, попробуйте снова.")
    else:
        return int(user_input)

def answer():
    pupils = input('Кто пойдет к доске: ')
    while True:
        for s in class_db:
            if s[0] == pupils:
                print(pupils)
        # return pupils
        subject = input('Введите название предмета: ')
        while True:   
            for sbj in class_db:
                if sbj[1] == subject:
                    print(subject)
            print(pupils + ':' + subject)
            break
    


def exit_prog():
    print('Завершение программы.')
    exit()
