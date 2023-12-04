from general_provisions.table import func_table
from config import your_option

if __name__ == '__main__':
    func_table.get_table_1(your_option)
    func_table.get_table_2(your_option)
    func_table.get_table_3(your_option)
    func_table.get_table_4(your_option, action=input('Выводим таблицу с вычислениями? (да/нет): '))



