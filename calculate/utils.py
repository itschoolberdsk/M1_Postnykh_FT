import calculate_func as calc
import const_locale as const

def result(a: int, b: int, sign: str):
    if sign == const.PLUS:
        return calc.sum(a, b)
    elif sign == const.DIFFERENCE:
        return calc.minus(a, b)
    elif sign == const.MULTIPLIKATION:
        return calc.mult(a, b)
    elif sign == const.DIVISION:
        return calc.dell(a, b)
    elif sign == const.DEGREE:
        return calc.degree(a, b)

def parse_cmd(cmd: str):
    cmd_list = cmd.split()
    type_cmd = len(cmd_list)
    if type_cmd == 3:
        # num_1, sign, num_2
        return (int(cmd_list[0]), cmd_list[1], int(cmd_list[2]))
    elif type_cmd == 2:
        # sign, num_2
        return (cmd_list[0], int(cmd_list[1]))