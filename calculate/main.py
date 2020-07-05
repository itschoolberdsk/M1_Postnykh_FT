import const_locale as const
import utils as utils

def startText():
    print("Возможные операции: ")
    print("1 Сложение '+'.")
    print("2 Вычитание '-'.")
    print("3 Деление '/'.")
    print("4 Умножение '*'.")
    print("5 Возведение в квадрат/куб '**'.")
    print("Чтобы завершить работу с калькулятором, пропишите 'end'.")
    print("Вводите математическое выражение через пробел.")

def updateCache(a: int, b: int, sign: str):
    global cache
    cache = utils.result(a, b, sign)

startText()

cache = 0
while True:
    math_task = input()
    if math_task == const.END_WORKING:
        print(const.PHRASE_PROGRAM_END)
        break   

    operation_data = utils.parse_cmd(math_task)
    operation_data_len = len(operation_data)

    if operation_data_len == 3:
        updateCache(operation_data[0], operation_data[2], operation_data[1])
    elif operation_data_len == 2 and cache != 0:
        updateCache(cache, operation_data[1], operation_data[0])
    
    print(cache)