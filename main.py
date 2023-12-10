from table import create_table
from config import your_option, work_number, attachments_word

if __name__ == '__main__':
    if work_number == 'create':
        print('Документ.docx создается...')
        create_table.create_doc(attachments_word, your_option)
        print('Документ.docx создан')

    if work_number == 'a/d':
        action = input('Выводим анализ? (да/нет): ')
        create_table.get_analysis(your_option, action)

        action = input('Выводим диаграммы? (да/нет): ')
        create_table.get_diagrams(your_option, action)
