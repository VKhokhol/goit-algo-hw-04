
#Відкриття файлу для запису, явно вказане кодування
with open('salaries.txt', 'w', encoding='utf-8') as f:
    f.write('Alex Korp,3000\nNikita Borisenko,2000\nSitarama Roju,1000')

#Створення функції з одним аргументом.   
def total_salary(path):
#Створення двох змінних для виведення середньої та сумарної зарплати
    middle_salary = 0
    sum_salary = 0
#Відкриття файлу для читання з явно визначеним кодуванням
    with open(path, 'r', encoding='utf-8') as f:
#Читання файлу по строкам та очищення від зайвих пробілів та символів
        lines = [line.strip() for line in f.readlines()]
#Цикл по строкам, в якому строка розділяється по знаку ",", при чому частину строки до коми нікуди не записується,
#а після коми, тобто зарплата, записується в змінну
        for line in lines:
            _, sal = line.split(',')
#Перетворення змінної в об'єкт типу int та обрахунок сумарної зарплати
            sum_salary+= int(sal)
#Перевірка на те, чи не пустий файл для того, щоб уникнути ділення на 0 при обрахунку середньої зарплати
        if len(lines) == 0:
            middle_salary = 0
        else:
            middle_salary = sum_salary/len(lines)
#Поверння даних у вигляді кортежу
        return sum_salary, middle_salary
try:
    total, average = total_salary('salaries.txt')
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
#Обробка винятку, який виникає у випадку, коли зарплата написана у текстовому вигляді
except FileNotFoundError:
    print('Файл не знайдений')
