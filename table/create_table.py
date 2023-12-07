from view import text_collection
from settings import options
from settings.options import workbook, sheets
from utils.enums import cells_1, AttachmentsTable8, AttachmentsTable2, AttachmentsTable6
from prettytable import PrettyTable
from . import calculations
from utils import switchers
from .additional_stuff import diagramm_create, analysis_create, calculations_structure_create


def get_table_1(option: int):
    ship_1, ship_2, ship_3 = options.your_ships(option)
    cargo_1, cargo_2 = list(options.cargo_for_calc(option).values())
    port = options.get_ports(option)
    distance = options.get_info_distance(option)

    mydata = [text_collection.ports,
              text_collection.type_cargo,
              text_collection.ship_types,
              text_collection.distance]
    pups = PrettyTable(mydata)
    navigation = f"{text_collection.type_ports['departures']} - {port[0]}\n{text_collection.type_ports['appointments']} - {port[1]}"
    cargos = f"{text_collection.trans_cargo['forward']} - {cargo_1}\n{text_collection.trans_cargo['reverse']} - {cargo_2}"
    ships = f"1 - {ship_1}\n2 - {ship_2}\n3 - {ship_3}"
    distance_swim = f"{distance}"

    pups.add_row([navigation,
                  cargos,
                  ships,
                  distance_swim])

    print(text_collection.table_1)
    print(pups)


def get_table_2(option: int):
    ship_1, ship_2, ship_3 = options.your_ships(option)

    mydata = [text_collection.specifications, ship_1, ship_2, ship_3]

    pups = PrettyTable(mydata)

    for specification, cell in zip(text_collection.table_text_1, cells_1):
        tits = [specification] + [options.get_info_ships(option, cell).get(ship) for ship in options.your_ships(option)]
        pups.add_row(tits)

    print(text_collection.table_2)
    print(pups)


def get_table_3(option: int, action):
    summa = 0

    your_ships = options.your_ships(option)

    mydata = text_collection.table_text_3
    pups = PrettyTable(mydata)

    ship_count = options.get_info_ships(option, AttachmentsTable8.ship_count)
    balance = options.get_info_table_2(option, AttachmentsTable2.balance)
    share_capital = calculations.find_share_capital(option)[0]
    if action == text_collection.no:
        for ship in your_ships:
            pups.add_row([ship, balance.get(ship), ship_count.get(ship), share_capital.get(ship)])
            summa = summa + int(balance.get(ship)) * int(ship_count.get(ship))
        pups.add_row([' ', ' ', ' ', ' '])
        pups.add_row([text_collection.resulte, ' ', ' ', summa])

        print(text_collection.table_4)
        print(pups)
    elif action == text_collection.yes:
        for ship in your_ships:
            pups.add_row([ship, balance.get(ship), ship_count.get(ship), share_capital.get(ship)])
            summa = summa + int(balance.get(ship)) * int(ship_count.get(ship))

        pups.add_row([' ', ' ', ' ', ' '])
        pups.add_row([text_collection.resulte, ' ', ' ', summa])

        print(text_collection.table_4)
        print(pups)
        calculations_structure_create.calculation_structure_4(option)
    else:
        print(text_collection.only_yes_and_no)


def get_table_4(option: int, action):
    ship_1, ship_2, ship_3 = options.your_ships(option)

    mydata = [text_collection.specifications, ship_1, ship_2, ship_3]
    pups = PrettyTable(mydata)

    if action == text_collection.no:
        for i in range(2, 14):
            pups.add_row([switchers.choose_def_value(option, i, ship_1)[0],
                          switchers.choose_def_value(option, i, ship_1)[1],
                          switchers.choose_def_value(option, i, ship_2)[1],
                          switchers.choose_def_value(option, i, ship_3)[1]])
        print()
        print(text_collection.table_5)
        print(pups)

    elif action == text_collection.yes:
        for i in range(2, 14):
            pups.add_row([switchers.choose_def_value(option, i, ship_1)[0],
                          switchers.choose_def_value(option, i, ship_1)[1],
                          switchers.choose_def_value(option, i, ship_2)[1],
                          switchers.choose_def_value(option, i, ship_3)[1]])
        print()
        print(text_collection.table_5)
        print(pups)
        calculations_structure_create.calculation_structure_5(option)

    else:
        print(text_collection.only_yes_and_no)


def get_carrying_capacity(option: int, action):
    ship_1, ship_2, ship_3 = options.your_ships(option)

    mydata = [ship_1, ship_2, ship_3]
    pups = PrettyTable(mydata)

    if action == text_collection.no:
        pups.add_row([switchers.choose_def_value(option, 14, ship_1)[1],
                      switchers.choose_def_value(option, 14, ship_2)[1],
                      switchers.choose_def_value(option, 14, ship_3)[1]])

        print()
        print(switchers.choose_def_value(option, 14, ship_1)[0])
        print(pups)
    elif action == text_collection.yes:
        pups.add_row([switchers.choose_def_value(option, 14, ship_1)[1],
                      switchers.choose_def_value(option, 14, ship_2)[1],
                      switchers.choose_def_value(option, 14, ship_3)[1]])

        print()
        print(switchers.choose_def_value(option, 14, ship_1)[0])
        print(pups)
        calculations_structure_create.calculation_structure_6(option)

    else:
        print(text_collection.only_yes_and_no)


def get_table_5(option: int):
    ships = options.your_ships(option)

    type_ship = options.get_info_ships_6(option, AttachmentsTable6.type_ship)
    cost = options.get_info_ships_6(option, AttachmentsTable6.cost_price)
    specific_fuel = options.get_info_ships_6(option, AttachmentsTable6.specific_fuel)
    crew = options.get_info_ships_6(option, AttachmentsTable6.number_crew)

    mydata = text_collection.table_text_4
    pups = PrettyTable(mydata)
    for ship in ships:
        pups.add_row([type_ship.get(ship), ship, cost.get(ship), specific_fuel.get(ship), crew.get(ship)])
    print()
    print(text_collection.table_6)
    print(pups)


def get_structure_turn(option: int, action):
    ship_1, ship_2, ship_3 = options.your_ships(option)

    mydata = [text_collection.specifications] + [ship_1, ship_2, ship_3]
    pups = PrettyTable(mydata)

    if action == text_collection.no:
        for i in range(15, 24):
            pups.add_row([switchers.choose_def_value(option, i, ship_1)[0],
                          switchers.choose_def_value(option, i, ship_1)[1],
                          switchers.choose_def_value(option, i, ship_2)[1],
                          switchers.choose_def_value(option, i, ship_3)[1]])
        print()
        print(text_collection.structure_turn)
        print(pups)
    elif action == text_collection.yes:
        for i in range(15, 24):
            pups.add_row([switchers.choose_def_value(option, i, ship_1)[0],
                          switchers.choose_def_value(option, i, ship_1)[1],
                          switchers.choose_def_value(option, i, ship_2)[1],
                          switchers.choose_def_value(option, i, ship_3)[1]])
        print()
        print(text_collection.structure_turn)
        print(pups)
        calculations_structure_create.calculation_structure_1(option)  # вывод вычислений
        calculations_structure_create.calculation_structure_2(option)
    else:
        print(text_collection.only_yes_and_no)


def get_analysis(option: int, operand):
    if operand == text_collection.yes:
        print(analysis_create.analysis(option))
    elif operand == text_collection.no:
        print(text_collection.analysis_not_print)
    else:
        print(text_collection.only_yes_and_no)


def get_diagrams(option: int, operand):
    if operand == text_collection.yes:
        diagramm_create.get_diagrams(option)
    elif operand == text_collection.no:
        print(text_collection.diagrams_not_print)
    else:
        print(text_collection.only_yes_and_no)


def work_4(option: int, action):
    ship_1, ship_2, ship_3 = options.your_ships(option)

    mydata = [text_collection.specifications] + [ship_1, ship_2, ship_3]
    pups = PrettyTable(mydata)

    if action == text_collection.no:
        for i in range(24, 32):
            pups.add_row([switchers.choose_def_value(option, i, ship_1)[0],
                          switchers.choose_def_value(option, i, ship_1)[1],
                          switchers.choose_def_value(option, i, ship_2)[1],
                          switchers.choose_def_value(option, i, ship_3)[1]])
        print()
        print(text_collection.title_work_4)
        print(pups)
    elif action == text_collection.yes:
        for i in range(24, 32):
            pups.add_row([switchers.choose_def_value(option, i, ship_1)[0],
                          switchers.choose_def_value(option, i, ship_1)[1],
                          switchers.choose_def_value(option, i, ship_2)[1],
                          switchers.choose_def_value(option, i, ship_3)[1]])

        print()
        print(text_collection.title_work_4)
        print(pups)
        calculations_structure_create.calculation_structure_3(option)
    else:
        print(text_collection.only_yes_and_no)
