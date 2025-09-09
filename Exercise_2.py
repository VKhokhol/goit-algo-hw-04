#Відкриття файлу в режимі запису даних
with open('cats_info.txt', 'w', encoding='utf-8') as f:
    f.write('60b90c1c13067a15887e1ae1,Tayson,3\n' \
    '60b90c2413067a15887e1ae2,Vika,1\n' \
    '60b90c2e13067a15887e1ae3,Barsik,2\n' \
    '60b90c3b13067a15887e1ae4,Simon,12\n' \
    '60b90c4613067a15887e1ae5,Tessi,5')

def get_cats_info(path):
#Створення списку для подальшого додавання туда словників
    info_cats = []
#Відкриття файлу в режимі читання даних
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
#Обробка кожної зі стрічок. Спочатку видалення зайвих символів, потім розділення по комам
            cat_id, name, age = line.strip().split(',')
#Створення словників та додавання до списку
            info = {'id': cat_id, 'name': name, 'age': age}
            info_cats.append(info)
    return info_cats


try:
    cats = get_cats_info('cats_info.txt') 
    print(cats)

#Обробк винятку на випадок відсутності файлу
except FileNotFoundError:
    print('Файл не знайдений')
#Обробка винятку, якщо запис і читання файлу відбувалося в різних кодуваннях
except UnicodeDecodeError:
    print('Неправильно встановлено кодування')
#Обробка винятку, якщо дані записано в неправильному форматі, наприклад не 3 параметри, а 4
except ValueError:
    print('Неправильний формат даних')