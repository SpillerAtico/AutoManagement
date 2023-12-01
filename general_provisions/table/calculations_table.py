from general_provisions import options
from general_provisions.options import workbook, sheets
from utils.enum import AttachmentsTable8

ship_count = 3


def share_capital(balance_sell, ship_count):
    capital = int(balance_sell) * ship_count
    return f'{int(balance_sell)} * {ship_count} = {capital}', capital


def find_volume(option: int):
    cargo_1 = (list(options.cargo_for_calc(option).values())[0]).lower()
    cargo_2 = (list(options.cargo_for_calc(option).values())[1]).lower()

    workbook.active = workbook[sheets[3]]  # Приложение 4
    sheet = workbook.active

    cargo_cell_f = {str(cell.coordinate): str(cell.value) for content in sheet['A5':'A30'] for cell in content
                    if cargo_1 in str(cell.value).lower().strip()}.keys()
    cargo_cell_r = {str(cell.coordinate): str(cell.value) for content in sheet['A5':'A30'] for cell in content
                    if cargo_2 in str(cell.value).lower().strip()}.keys()

    volume_f = sheet[list(cargo_cell_f)[0].replace('A', 'B')].value
    volume_r = sheet[list(cargo_cell_r)[0].replace('A', 'B')].value

    return volume_f, volume_r
