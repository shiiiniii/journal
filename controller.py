import model
import view

model.read_db('7A.txt')


def input_handler(inp: int):
    match inp:
        case 1:
            model.read_db('7A.txt')
            view.answer()
        case 2:
            view.exit_prog()


def start():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp)
        


