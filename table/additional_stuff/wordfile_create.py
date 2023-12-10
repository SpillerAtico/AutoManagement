from docxtpl import DocxTemplate
from utils.enums import cells_1, AttachmentsTable2, AttachmentsTable6
from utils import switchers
from settings import options
from view import text_collection
from table import calculations
from table.additional_stuff import calculations_structure_create


def create_doc(word_document, option: int):
    doc = DocxTemplate(word_document)  # открываем шаблон

    ships = create_dict_ships(option)
    table_1 = create_dict_1(option)
    table_2 = create_dict_2(option)
    table_3 = create_dict_3(option)
    table_4 = create_dict_4(option)
    table_5 = create_dict_5(option)
    table_6 = create_dict_6(option)

    calculations = create_dict_calculations(option)

    context = ships | table_1 | table_2 | table_3 | table_4 | table_5 | table_6 | calculations

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

    for i in range(2, 14):
        data = data + [switchers.choose_def_value(option, i, ship_1)[1],
                       switchers.choose_def_value(option, i, ship_2)[1],
                       switchers.choose_def_value(option, i, ship_3)[1]]

    for i in range(len(names)):
        table[names[i]] = data[i]

    return table


def create_dict_5(option: int):
    ship_1, ship_2, ship_3 = options.your_ships(option)

    cost = options.get_info_ships_6(option, AttachmentsTable6.cost_price)
    specific_fuel = options.get_info_ships_6(option, AttachmentsTable6.specific_fuel)
    crew = options.get_info_ships_6(option, AttachmentsTable6.number_crew)

    table = {
        'cost_1': cost.get(ship_1), 'cost_2': cost.get(ship_2),
        'cost_3': cost.get(ship_3),

        'specific_fuel_1': specific_fuel.get(ship_1), 'specific_fuel_2': specific_fuel.get(ship_2),
        'specific_fuel_3': specific_fuel.get(ship_3),

        'crew_1': crew.get(ship_1), 'crew_2': crew.get(ship_2),
        'crew_3': crew.get(ship_3)
    }

    return table


def create_dict_calculations(option: int):
    calc_2 = calculations_structure_create.calculation_structure_5(option)
    calc_3 = calculations_structure_create.calculation_structure_6(option)
    calc_4 = calculations_structure_create.calculation_structure_1(option)
    calc_5 = calculations_structure_create.calculation_structure_2(option)
    calc_6 = calculations_structure_create.calculation_structure_2_1(option)
    calc_7 = calculations_structure_create.calculation_structure_3(option)
    calc_8 = calculations_structure_create.calculation_structure_7(option)

    calculations = {
        'calc_2': calc_2,
        'calc_3': calc_3,
        'calc_4': calc_4,
        'calc_5': calc_5,
        'calc_6': calc_6,
        'calc_7': calc_7,
        'calc_8': calc_8
    }

    return calculations


def create_dict_6(option: int):
    data = []
    table = {}
    ships = options.your_ships(option)
    ship_1, ship_2, ship_3 = options.your_ships(option)

    names = ('revenue_1', 'revenue_2', 'revenue_3')
    for ship, name in zip(ships, names):
        table[name] = switchers.choose_def_value(option, 29, ship)[1]  # Дпер = Gi * fсрi.

    names = ('expenses_period_1', 'expenses_period_2', 'expenses_period_3')
    for ship, name in zip(ships, names):
        table[name] = switchers.choose_def_value(option, 27, ship)[1]  # Эпер = Sср * Gi долл

    names = ('income_ships_1', 'income_ships_2', 'income_ships_3',
             'expenses_delivery_1', 'expenses_delivery_2', 'expenses_delivery_3',
             'gross_profit_1', 'gross_profit_2', 'gross_profit_3',
             'profitability_1', 'profitability_2', 'profitability_3')

    for case in range(32, 36):
        data = data + [switchers.choose_def_value(option, case, ship_1)[1],
                       switchers.choose_def_value(option, case, ship_2)[1],
                       switchers.choose_def_value(option, case, ship_3)[1]]

    for i in range(len(names)):
        table[names[i]] = data[i]

    return table
