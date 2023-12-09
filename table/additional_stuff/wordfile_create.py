from docxtpl import DocxTemplate
from config import attachments_word
from utils.enums import cells_1
from settings import options
from view import text_collection


def create_doc(word_document, option: int):
    doc = DocxTemplate(word_document)  # открываем шаблон

    ships = create_dict_ships(option)
    table_1 = create_dict_1(option)
    table_2 = create_dict_2(option)

    context = ships | table_1 | table_2

    doc.render(context)
    doc.save(f"спидозные козявки.docx")


def create_dict_ships(option: int):
    ship_1, ship_2, ship_3 = options.your_ships(option)

    ships = {
        'ship_1': ship_1,
        'ship_2': ship_2,
        'ship_3': ship_3,
    }

    return ships


def create_dict_1(option: int):
    port_1, port_2 = options.get_ports(option)
    cargo_1, cargo_2 = list(options.cargo_for_calc(option).values())
    distance = options.get_info_distance(option)

    table = {
        'option': option,
        'port_1': port_1,
        'port_2': port_2,
        'cargo_1': cargo_1,
        'cargo_2': cargo_2,
        'distance': distance,

    }

    return table


def create_dict_2(option: int):
    values = []
    table = {}

    text_names = text_collection.text_names

    for cell in cells_1:
        values = values + [options.get_info_ships(option, cell).get(ship) for ship in options.your_ships(option)]

    for i in range(len(text_names)):
        table[text_names[i]] = values[i]

    return table
