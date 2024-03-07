from collections import Counter
import math
import matplotlib.pyplot as plt


def task_1():
    # Входные данные
    string = "hello, world!"
    # Объект счётчика для подсчёта количества символов
    frequency = Counter(string)
    # Количество символов
    total = sum(frequency.values())

    entropies = {}
    for char, count in frequency.items():
        # Вероятность появления символа
        probability = count / total
        # Подсчёт энтропии по формуле Шеннона
        entropy = -probability * math.log(probability, 2)
        entropies[char] = entropy
    # Подсчёт общей энтропии сообщения
    total_entropy = sum(entropies.values())

    # Построение диаграммы по ключам и значениям (символы и энтропия)
    plt.bar(entropies.keys(), entropies.values())
    plt.title(f"Общая энтропия: {total_entropy:.2f} бит")
    plt.xlabel("Символ")
    plt.ylabel("Энтропия")

    for char, entropy in entropies.items():
        # Отображение энтропии каждого символа на диаграмме
        plt.text(char, entropy - 0.25, f"{entropy:.2f}", ha="center")

    # Отображение диаграммы
    plt.show()


def task_2():
    # Входные данные
    binary_code = "010101011110101001010101"

    # Количество нулей в сообщении
    count_0 = binary_code.count('0')
    # Количество единиц в сообщении
    count_1 = binary_code.count('1')

    # Подсчёт количества символов сообщения
    total = count_0 + count_1

    # Подсчёт вероятности появления нуля
    p_0 = count_0 / total
    # Подсчёт вероятности появления единицы
    p_1 = count_1 / total

    # Подсчёт энтропии сообщения по формуле Хартли
    entropy = -p_0 * math.log2(p_0) - p_1 * math.log2(p_1)

    print(f"Энтропия бинарного алфавита: {entropy:.2f} бит")


def task_3():
    # Входные данные
    text = "Юров Максим Дмитриевич"

    # Подсчёт количества информации, которое передаёт сообщение по русскому алфавиту
    rus_i = len(text) * math.log(33, 2)
    # Подсчёт количества информации, которое передаёт сообщение по ASCII
    ascii_i = len(text) * math.log(128, 2)

    print(f'На основе исходного алфавита моё ФИО будет передавать {rus_i:.2f} бит информации')
    print(f'На основе ASCII кодировки моё ФИО будет передавать {ascii_i:.2f} бит информации')

    # Вероятность ошибки
    error_1 = 0.1
    # Вероятность ошибки
    error_2 = 0.5
    # Вероятность ошибки
    error_3 = 1.0

    print()

    print(f'На основе исходного алфавита, учитывая вероятность ошибки ({error_1}) моё ФИО '
          f'будет передавать {rus_i * (1 - error_1):.2f} бит информации')
    print(f'На основе исходного алфавита, учитывая вероятность ошибки ({error_2}) моё ФИО '
          f'будет передавать {rus_i * (1 - error_2):.2f} бит информации')
    print(f'На основе исходного алфавита, учитывая вероятность ошибки ({error_3}) моё ФИО '
          f'будет передавать {rus_i * (1 - error_3):.2f} бит информации')

    print()

    print(f'На основе ASCII кодировки, учитывая вероятность ошибки ({error_1}) моё ФИО '
          f'будет передавать {ascii_i * (1 - error_1):.2f} бит информации')
    print(f'На основе ASCII кодировки, учитывая вероятность ошибки ({error_2}) моё ФИО '
          f'будет передавать {ascii_i * (1 - error_2):.2f} бит информации')
    print(f'На основе ASCII кодировки, учитывая вероятность ошибки ({error_3}) моё ФИО '
          f'будет передавать {ascii_i * (1 - error_3):.2f} бит информации')


task_1()
print()
task_2()
print()
task_3()
