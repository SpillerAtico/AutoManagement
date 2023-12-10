from docxtpl import DocxTemplate
from utils.enums import cells_1, AttachmentsTable2
from utils import switchers
from settings import options
from view import text_collection
from table import calculations
from . import calculations_structure_create


def create_doc(word_document, option: int):
    doc = DocxTemplate(word_document)  # открываем шаблон

    ships = create_dict_ships(option)
    table_1 = create_dict_1(option)
    table_2 = create_dict_2(option)
    table_3 = create_dict_3(option)
    table_4 = create_dict_4(option)

    context = ships | table_1 | table_2 | table_3 | table_4

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
        'port_1': port_1, 'port_2': port_2,
        'cargo_1': cargo_1, 'cargo_2': cargo_2,
        'distance': distance,

    }

    return table


def create_dict_2(option: int):
    values = []
    table = {}

    names = text_collection.text_names

    for cell in cells_1:
        values = values + [options.get_info_ships(option, cell).get(ship) for ship in options.your_ships(option)]

    for i in range(len(names)):
        table[names[i]] = values[i]

    return table


def create_dict_3(option: int):
    ship_1, ship_2, ship_3 = options.your_ships(option)
    ship_count = 2

    balance = options.get_info_table_2(option, AttachmentsTable2.balance)
    type_ship = options.get_info_table_2(option, AttachmentsTable2.type)
    share_capital = calculations.find_share_capital(option)[0]

    share_capital_summa = int(balance.get(ship_1)) * ship_count + int(balance.get(ship_2)) * ship_count + int(
        balance.get(ship_3)) * ship_count

    balance_summa = int(balance.get(ship_1)) + int(balance.get(ship_2)) + int(balance.get(ship_3))

    calc_1 = calculations_structure_create.calculation_structure_4(option)
    table = {
        'balance_1': balance.get(ship_1), 'balance_2': balance.get(ship_2), 'balance_3': balance.get(ship_3),

        'type_ship_1': type_ship.get(ship_1), 'type_ship_2': type_ship.get(ship_2),
        'type_ship_3': type_ship.get(ship_3),

        'share_capital_1': share_capital.get(ship_1), 'share_capital_2': share_capital.get(ship_2),
        'share_capital_3': share_capital.get(ship_3),

        'share_capital_summa': share_capital_summa,
        'balance_summa': balance_summa,

        'calc_1': calc_1
    }

    return table


def create_dict_4(option: int):
    data = []
    table = {}
    ship_1, ship_2, ship_3 = options.your_ships(option)
    names = text_collection.text_names_2
    calc_2 = calculations_structure_create.calculation_structure_5(option)
    for i in range(2, 14):
        data = data + [switchers.choose_def_value(option, i, ship_1)[1],
                       switchers.choose_def_value(option, i, ship_2)[1],
                       switchers.choose_def_value(option, i, ship_3)[1]]

    for i in range(len(names)):
        table[names[i]] = data[i]

    table['calc_2'] = calc_2
    return table
