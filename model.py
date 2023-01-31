class_db = {}
path = ''
name = ''
class_dict = {}

def read_db(path: str):
    global class_dict
    with open(path, 'r', encoding='UTF-8') as file:
        class_list = file.readlines()
        class_db = []
        for line in class_list:
            pupils_marks = line.strip().split('|')
            class_db.append(pupils_marks)
        for i, item in enumerate(class_db):
            pupils = item[1].split(';')
            marks = [pupils[j] for j in range(1, len(pupils), 2)]
            names = [pupils[j] for j in range(0, len(pupils), 2)]
            pupils_dict = dict(zip(names, marks))
            class_dict[item[0]] = pupils_dict
    return class_dict
read_db('7A.txt')
