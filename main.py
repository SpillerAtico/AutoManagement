from table import create_table
from config import your_option, work_number, attachments_word
from view import text_collection
from table.additional_stuff import wordfile_create

if __name__ == '__main__':
    if work_number == 'create':
        print('Документ.docx создается...')
        wordfile_create.create_doc(attachments_word, your_option)
        print('Документ.docx создан')

    if work_number == '0':
        create_table.get_table_1(your_option)
        create_table.get_table_2(your_option)
        action = text_collection.yes
        create_table.get_table_3(your_option, action)

        action = text_collection.yes
        create_table.get_table_4(your_option, action)
        create_table.get_carrying_capacity(your_option, action)

        action = text_collection.yes
        create_table.get_table_5(your_option)
        create_table.get_structure_turn(your_option, action)

        action = input('Выводим анализ? (да/нет): ')
        create_table.get_analysis(your_option, action)

        action = input('Выводим диаграммы? (да/нет): ')
        create_table.get_diagrams(your_option, action)

        action = text_collection.yes
        create_table.work_4(your_option, action)

    if work_number == '1':
        create_table.get_table_1(your_option)
        create_table.get_table_2(your_option)
        action = input('Выводим таблицу вместе с вычислениями? (да/нет): ')
        create_table.get_table_3(your_option, action)

    if work_number == '2':
        action = input('Выводим таблицы вместе с вычислениями? (да/нет): ')
        create_table.get_table_4(your_option, action)
        create_table.get_carrying_capacity(your_option, action)

    if work_number == '3':
        action = input('Выводим таблицу вместе с вычислениями? (да/нет): ')
        create_table.get_table_5(your_option)
        create_table.get_structure_turn(your_option, action)

        action = input('Выводим анализ? (да/нет): ')
        create_table.get_analysis(your_option, action)

        action = input('Выводим диаграммы? (да/нет): ')
        create_table.get_diagrams(your_option, action)

    if work_number == '4':
        action = input('Выводим таблицу вместе с вычислениями? (да/нет): ')
        create_table.work_4(your_option, action)
