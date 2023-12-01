from view import text_collection
from general_provisions import options
from general_provisions.options import workbook, sheets
from utils.enum import cells_1, cells_2, AttachmentsTable8, AttachmentsTable2
from prettytable import PrettyTable
from . import calculations_table


def get_table_1(option: int):
    workbook.active = workbook[sheets[2]]  # Приложение 3
    sheet = workbook.active
    cell_option = options.get_table_options_3(option, sheet)

    your_ship = options.your_ships(option)
    cargo = options.get_cargos(cell_option, sheet)
    port = options.get_ports(cell_option, sheet)
    distance = options.get_distance(cell_option, sheet)

    mydata = [text_collection.ports, text_collection.type_cargo, text_collection.ship_types,
              text_collection.distance]

    navigation = f"{text_collection.type_ports['departures']} - {port[0]}\n{text_collection.type_ports['appointments']} - {port[1]}"
    cargos = f"{text_collection.trans_cargo['forward']} - {cargo[0]}\n{text_collection.trans_cargo['reverse']} - {cargo[1]}"
    ships = f"1 - {your_ship[0]}\n2 - {your_ship[1]}\n3 - {your_ship[2]}"
    distance_swim = f"{distance}"

    pups = PrettyTable(mydata)
    pups.add_row([navigation, cargos, ships, distance_swim])

    print(text_collection.separator)
    print(text_collection.table_1)
    print(pups)


def get_table_2(option: int):
    workbook.active = workbook[sheets[7]]  # Приложение 8, теперь взаимодействуем с полученными корабликами
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

    your_ships = options.your_ships(option)
    ship_cells = options.get_ships_table_2(your_ships, sheet)

    type_ship = list(options.get_attachments_2(ship_cells, sheet, AttachmentsTable2.type).values())
    balance = list(options.get_attachments_2(ship_cells, sheet, AttachmentsTable2.balance).values())

    mydata = text_collection.table_text_2
    pups = PrettyTable(mydata)

    for i in range(3):
        pups.add_row([type_ship[i], your_ships[i], balance[i]])

    print(text_collection.table_2)
    print(pups)


def get_table_4(option: int):
    workbook.active = workbook[sheets[1]]  # Приложение 2
    sheet = workbook.active
    summa = 0

    your_ships = options.your_ships(option)
    ship_cells = options.get_ships_table_2(your_ships, sheet)

    type_ship = list(options.get_attachments_2(ship_cells, sheet, AttachmentsTable2.type).values())
    balance = list(options.get_attachments_2(ship_cells, sheet, AttachmentsTable2.balance).values())

    mydata = text_collection.table_text_3
    pups = PrettyTable(mydata)

    count_ship = calculations_table.ship_count
    for i in range(3):
        pups.add_row([your_ships[i], balance[i], count_ship,
                      calculations_table.share_capital(int(balance[i]), count_ship)[0]])
        summa = summa + int(calculations_table.share_capital(int(balance[i]), count_ship)[1])

    pups.add_row([' ', ' ', ' ', ' '])
    pups.add_row(['Итого', ' ', ' ', summa])

    print(text_collection.table_4)
    print(pups)
