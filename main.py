from general_provisions.table import func_table
from config import your_option, work_number

if __name__ == '__main__':
    if work_number == 1:
        func_table.get_table_1(your_option)
        func_table.get_table_2(your_option)
        func_table.get_table_3(your_option)

    if work_number == 2:
        action = input('Выводим таблицы с вычислениями? (да/нет): ')
        func_table.get_table_4(your_option, action)
        func_table.get_carrying_capacity(your_option, action)

    if work_number == 3:
        action = input('Выводим таблицы с вычислениями? (да/нет): ')
        func_table.get_table_5(your_option)
        func_table.get_structure_turn(your_option, action)
