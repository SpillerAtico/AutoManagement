from view import text_collection
from general_provisions import options
from general_provisions.options import workbook, sheets
from utils.enum import cells_1, AttachmentsTable8, AttachmentsTable2, AttachmentsTable6
from prettytable import PrettyTable
from . import calculations_table
import switcher


def get_table_1(option: int):
    workbook.active = workbook[sheets[2]]  # Приложение 3
    sheet = workbook.active
    cell_option = options.get_table_options_3(option, sheet)

    your_ship = options.your_ships(option)
    cargo = options.get_cargos(cell_option, sheet)
    port = options.get_ports(option)
    distance = options.get_distance(cell_option, sheet)

    mydata = [text_collection.ports, text_collection.type_cargo, text_collection.ship_types,
              text_collection.distance]

    navigation = f"{text_collection.type_ports['departures']} - {port[0]}\n{text_collection.type_ports['appointments']} - {port[1]}"
    cargos = f"{text_collection.trans_cargo['forward']} - {cargo[0]}\n{text_collection.trans_cargo['reverse']} - {cargo[1]}"
    ships = f"1 - {your_ship[0]}\n2 - {your_ship[1]}\n3 - {your_ship[2]}"
    distance_swim = f"{distance}"

    pups = PrettyTable(mydata)
    pups.add_row([navigation, cargos, ships, distance_swim])

    print(text_collection.table_1)
    print(pups)


def get_table_2(option: int):
    workbook.active = workbook[sheets[8]]  # Приложение 8, теперь взаимодействуем с полученными корабликами
    sheet = workbook.active

    your_ships = options.your_ships(option)
    ship_cells = options.get_ships_table_8(your_ships, sheet)

    mydata = [text_collection.specifications,
              list(options.get_attachments_8(ship_cells, sheet, AttachmentsTable8.length).keys())[0],
              list(options.get_attachments_8(ship_cells, sheet, AttachmentsTable8.length).keys())[1],
              list(options.get_attachments_8(ship_cells, sheet, AttachmentsTable8.length).keys())[2]]

    pups = PrettyTable(mydata)

    for spec, cell in zip(text_collection.table_text_1, cells_1):
        tits = [spec] + [list(options.get_attachments_8(ship_cells, sheet, cell).values())[i] for i in range(3)]
        pups.add_row(tits)

    print(text_collection.table_2)
    print(pups)


def get_table_3(option: int):
    workbook.active = workbook[sheets[1]]  # Приложение 2
    sheet = workbook.active
    summa = 0

    your_ships = options.your_ships(option)
    ship_cells = options.get_ships_table_2(your_ships, sheet)

    ship_count = list(options.get_info_ships(option, AttachmentsTable8.ship_count).values())

    balance = list(options.get_attachments_2(ship_cells, sheet, AttachmentsTable2.balance).values())

    mydata = text_collection.table_text_3
    pups = PrettyTable(mydata)

    for i in range(3):
        count_ship_keys = list(calculations_table.share_capital(balance[i], ship_count[i], option)[1].keys())
        calculate = calculations_table.share_capital(balance[i], ship_count[i], option)[0]

        pups.add_row([count_ship_keys[i], balance[i], ship_count[i], calculate])

        summa = summa + int(balance[i]) * int(ship_count[i])

    pups.add_row([' ', ' ', ' ', ' '])
    pups.add_row(['Итого', ' ', ' ', summa])

    print(text_collection.table_4)
    print(pups)


def get_table_4(option: int, action):
    mydata = [text_collection.specifications] + [switcher.choose_def_calc(option, 1)[1][0]] + [
        switcher.choose_def_calc(option, 1)[1][1]] + [switcher.choose_def_calc(option, 1)[1][2]]
    pups = PrettyTable(mydata)
    if action == 'да':
        for i in range(2, 14):
            pups.add_row([switcher.choose_def_calc(option, i)[0]] + [switcher.choose_def_calc(option, i)[1][0]] + [
                switcher.choose_def_calc(option, i)[1][1]] + [switcher.choose_def_calc(option, i)[1][2]])
        print(text_collection.table_5)
        print(pups)

    elif action == 'нет':
        for i in range(2, 14):
            pups.add_row([switcher.choose_def_calc(option, i)[0]] + [switcher.choose_def_value(option, i)[1][0]] + [
                switcher.choose_def_value(option, i)[1][1]] + [switcher.choose_def_value(option, i)[1][2]])
        print(text_collection.table_5)
        print(pups)

    else:
        print('Только да или нет')


def get_carrying_capacity(option: int, action):
    mydata = [switcher.choose_def_calc(option, 1)[1][0]] + [switcher.choose_def_calc(option, 1)[1][1]] + [
        switcher.choose_def_calc(option, 1)[1][2]]
    pups = PrettyTable(mydata)

    if action == 'да':
        pups.add_row([switcher.choose_def_calc(option, 14)[1][0]] + [switcher.choose_def_calc(option, 14)[1][1]] + [
            switcher.choose_def_calc(option, 14)[1][2]])
        print(switcher.choose_def_value(option, 14)[0])
        print(pups)

    elif action == 'нет':
        pups.add_row([switcher.choose_def_value(option, 14)[1][0]] + [switcher.choose_def_value(option, 14)[1][1]] + [
            switcher.choose_def_value(option, 14)[1][2]])
        print(switcher.choose_def_value(option, 14)[0])
        print(pups)

    else:
        print('Только да или нет')


def get_table_5(option: int):
    ships = list(options.get_info_ships_6(option, AttachmentsTable6.type_ship).keys())
    type_ship = list(options.get_info_ships_6(option, AttachmentsTable6.type_ship).values())
    cost = list(options.get_info_ships_6(option, AttachmentsTable6.cost_price).values())
    specific_fuel = list(options.get_info_ships_6(option, AttachmentsTable6.specific_fuel).values())
    crew = list(options.get_info_ships_6(option, AttachmentsTable6.number_crew).values())

    mydata = text_collection.table_text_4
    pups = PrettyTable(mydata)
    for i in range(3):
        pups.add_row([type_ship[i], ships[i], cost[i], specific_fuel[i], crew[i]])

    print(text_collection.table_6)
    print(pups)


def get_structure_turn(option: int, action):
    mydata = [text_collection.specifications] + [switcher.choose_def_calc(option, 1)[1][0]] + [
        switcher.choose_def_calc(option, 1)[1][1]] + [switcher.choose_def_calc(option, 1)[1][2]]
    pups = PrettyTable(mydata)
    if action == "нет":
        for i in range(15, 24):
            pups.add_row([switcher.choose_def_value(option, i)[0]] + [switcher.choose_def_value(option, i)[1][0]] + [
                switcher.choose_def_value(option, i)[1][1]] + [switcher.choose_def_value(option, i)[1][2]])
    elif action == "да":
        for i in range(15, 24):
            pups.add_row([switcher.choose_def_value(option, i)[0]] + [switcher.choose_def_value(option, i)[1][0]] + [
                switcher.choose_def_value(option, i)[1][1]] + [switcher.choose_def_value(option, i)[1][2]])
        print(calculations_table.calculation_structure_turn(option))
    else:
        print('Только да или нет')

    print(text_collection.structure_turn)
    print(pups)
    print(calculations_table.canalization(option))
