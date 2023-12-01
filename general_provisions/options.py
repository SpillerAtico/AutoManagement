from openpyxl import load_workbook
from typing import List
from config import attachments, your_option
from view import text_collection
from utils.enum import AttachmentsTable8

workbook = load_workbook(attachments)
sheets = load_workbook(attachments).sheetnames


def get_table_options_3(option: int, sheet) -> str:
    options = {cell.coordinate: cell.value for content in sheet['A5':'A94'] for cell in content if
               cell.value is not None}

    key_list, val_list = list(options.keys()), list(options.values())
    return key_list[val_list.index(option)]


def get_ships_table_2(ships: list, sheet) -> dict:
    options = {str(cell.coordinate): str(cell.value) for content in sheet['B6':'B23'] for cell in content if
               cell.value is not None}

    key_list, val_list = list(options.keys()), list(options.values())

    return {str(sheet[key_list[val_list.index(ship)]].value): str(key_list[val_list.index(ship)]) for ship in ships}


def your_ships(option: int):
    workbook.active = workbook[sheets[2]]  # Приложение 3
    sheet = workbook.active
    cell_option = get_table_options_3(option, sheet)

    your_ship = get_ships(cell_option, sheet)
    your_ships = [your_ship[0], your_ship[1], your_ship[2]]
    return your_ships


def get_ships_table_8(ships: list, sheet) -> dict:
    options = {str(cell.coordinate): str(cell.value) for content in sheet['B4':'S4'] for cell in content if
               cell.value is not None}

    key_list, val_list = list(options.keys()), list(options.values())

    return {str(sheet[key_list[val_list.index(ship)]].value): str(key_list[val_list.index(ship)]) for ship in ships}


def get_ships(cell_option, sheet) -> List[str]:
    ship_cells = [cell_option.replace('A', order) for order in ('E', 'F', 'G')]
    ships = [str(sheet[ship].value) for ship in ship_cells]

    return ships


def get_cargos(cell_option, sheet) -> List[str]:
    cargo_forward = cell_option.replace('A', 'D')

    old_num_option = cargo_forward[1:]
    new_num_option = int(cargo_forward[1:]) + 1
    # word_cell_option = type_cargo_1[:1]

    cargo_reverse = cargo_forward.replace(old_num_option, str(new_num_option))

    cargo = [str(sheet[cargo_forward].value), str(sheet[cargo_reverse].value)]

    return cargo


def cargo_for_calc(option):
    workbook.active = workbook[sheets[2]]  # Приложение 3
    sheet = workbook.active
    cell_option = get_table_options_3(option, sheet)

    cargo_forward = cell_option.replace('A', 'D')

    old_num_option = cargo_forward[1:]
    new_num_option = int(cargo_forward[1:]) + 1

    cargo_reverse = cargo_forward.replace(old_num_option, str(new_num_option))

    cargo = {text_collection.load_volume_f: str(sheet[cargo_forward].value),
             text_collection.load_volume_r: str(sheet[cargo_reverse].value)}

    return cargo


def get_ports(cell_option, sheet) -> List[str]:
    cell_ports = [cell_option.replace('A', order) for order in ('B', 'C')]
    ports = [str(sheet[port].value) for port in cell_ports]

    return ports


def get_type_ship(cell_option, sheet):
    cell_ports = [cell_option.replace('B', 'A')]
    type = [str(sheet[port].value) for port in cell_ports]

    return type


def get_distance(cell_option, sheet) -> str:
    cell_distance = cell_option.replace('A', 'H')

    distance = str(sheet[cell_distance].value)

    return distance


def get_attachments_8(ship_cells, sheet, enum):
    ships = list(ship_cells.values())
    option = {str(sheet[ship].value): str(sheet[ship.replace('4', enum)].value) for ship in ships}

    return option


def get_info_ships(option: int, enum):
    workbook.active = workbook[sheets[7]]  # Приложение 8, теперь взаимодействуем с полученными корабликами
    sheet = workbook.active

    your_ship = your_ships(option)
    ship_cells = get_ships_table_8(your_ship, sheet)

    ships = list(ship_cells.values())
    data = {str(sheet[ship].value): str(sheet[ship.replace('4', enum)].value) for ship in ships}

    return data


def get_info_distance(option: int):
    workbook.active = workbook[sheets[2]]  # Приложение 3
    sheet = workbook.active
    cell_option = get_table_options_3(option, sheet)

    distance = get_distance(cell_option, sheet)
    return distance




def get_attachments_2(ship_cells, sheet, enum):
    ships = list(ship_cells.values())
    option = {str(sheet[ship].value): str(sheet[ship.replace('B', enum)].value) for ship in ships}

    return option
