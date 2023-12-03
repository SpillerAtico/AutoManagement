from general_provisions import options
from general_provisions.options import workbook, sheets
from utils.enum import AttachmentsTable8
from general_provisions import options


def share_capital(balance_sell, ship_count, option):
    ships = list(options.get_info_ships(option, AttachmentsTable8.ship_count).keys())

    capital = {ships[i]: int(balance_sell) * int(ship_count) for i in range(3)}
    value = int(balance_sell) * int(ship_count)
    return f'{int(balance_sell)} * {ship_count} = {value}', capital


def find_volume(option: int):
    cargo_1 = (list(options.cargo_for_calc(option).values())[0]).lower()
    cargo_2 = (list(options.cargo_for_calc(option).values())[1]).lower()

    workbook.active = workbook[sheets[3]]  # Приложение 4
    sheet = workbook.active

    cargo_cell_f = {str(cell.coordinate): str(cell.value) for content in sheet['A5':'A31'] for cell in content
                    if cargo_1 in str(cell.value).lower().strip()}.keys()
    cargo_cell_r = {str(cell.coordinate): str(cell.value) for content in sheet['A5':'A31'] for cell in content
                    if cargo_2 in str(cell.value).lower().strip()}.keys()

    volume_f = sheet[list(cargo_cell_f)[0].replace('A', 'B')].value
    volume_r = sheet[list(cargo_cell_r)[0].replace('A', 'B')].value

    return volume_f, volume_r


def find_volume_foreign(option: int):  # усреднённая валовая норма обработки судов в зарубежных портах
    cargo_1 = (list(options.cargo_for_calc(option).values())[0]).lower()
    cargo_2 = (list(options.cargo_for_calc(option).values())[1]).lower()

    workbook.active = workbook[sheets[4]]  # Приложение 5
    sheet = workbook.active

    cargo_cell_f = {str(cell.coordinate): str(cell.value) for content in sheet['A3':'A41'] for cell in content
                    if cargo_1 in str(cell.value).lower().strip()}.keys()
    cargo_cell_r = {str(cell.coordinate): str(cell.value) for content in sheet['A3':'A41'] for cell in content
                    if cargo_2 in str(cell.value).lower().strip()}.keys()

    volume_f = sheet[list(cargo_cell_f)[0].replace('A', 'B')].value
    volume_r = sheet[list(cargo_cell_r)[0].replace('A', 'B')].value

    return volume_f, volume_r


def find_specific_capacity(option: int) -> tuple:  # Удельная грузовместимость судна
    load_capacity_val = list(options.get_info_ships(option, AttachmentsTable8.load_capacity).values())
    hold_capacity_val = list(options.get_info_ships(option, AttachmentsTable8.hold_capacity).values())
    load_capacity_key = list(options.get_info_ships(option, AttachmentsTable8.load_capacity).keys())

    specific_capacity = {load_capacity_key[i]: float(hold_capacity_val[i]) / float(load_capacity_val[i]) for i in
                         range(3)}
    calculate = [
        f'{hold_capacity_val[i]} / {load_capacity_val[i]} = {float(hold_capacity_val[i]) / float(load_capacity_val[i])}'
        for i in range(3)]

    return specific_capacity, calculate


def find_rate_load(option: int) -> tuple:  # Норма загрузки судна: Qэ, т
    specific_capacity = list(find_specific_capacity(option)[0].values())  # удельная грузовместимость судна
    hold_capacity_val = list(options.get_info_ships(option,
                                                    AttachmentsTable8.hold_capacity).values())
    load_capacity_val = list(options.get_info_ships(option,
                                                    AttachmentsTable8.load_capacity).values())  # грузоподъёмность, т (при 100 % запасов)
    ships = list(find_specific_capacity(option)[0].keys())
    volume = find_volume(option)

    rate_load_f = {}
    rate_load_r = {}
    calculate_1 = {}
    calculate_2 = {}
    for i in range(3):
        if float(volume[0]) > float(specific_capacity[i]):
            rate_load_f[ships[i]] = float(hold_capacity_val[i]) / float(volume[0])
            calculate_1[ships[
                i]] = f'{float(hold_capacity_val[i])} / {float(volume[0])} = {float(hold_capacity_val[i]) / float(volume[0])}'
        else:
            rate_load_f[ships[i]] = load_capacity_val[i]
            calculate_1[ships[i]] = f'{load_capacity_val[i]}'

        if float(volume[1]) > float(specific_capacity[i]):
            rate_load_r[ships[i]] = float(hold_capacity_val[i]) / float(volume[1])
            calculate_2[ships[
                i]] = f'{float(hold_capacity_val[i])} / {float(volume[1])} = {float(hold_capacity_val[i]) / float(volume[1])}'
        else:
            rate_load_r[ships[i]] = load_capacity_val[i]
            calculate_2[ships[i]] = f'{load_capacity_val[i]}'
    return rate_load_f, rate_load_r, calculate_1, calculate_2


def find_utilization_factor(option: int):
    load_capacity_val = list(options.get_info_ships(option,
                                                    AttachmentsTable8.load_capacity).values())  # грузоподъёмность, т (при 100 % запасов)
    rate_load_dict = find_rate_load(option)  # норма загрузки судна грузом
    rate_load_keys = list(rate_load_dict[0].keys())
    rate_load_f = list(rate_load_dict[0].values())  # норма загрузки судна грузом прямое
    rate_load_r = list(rate_load_dict[1].values())  # норма загрузки судна грузом обратное

    utilization_factor_f = {rate_load_keys[i]: float(rate_load_f[i]) / float(load_capacity_val[i]) for i in range(3)}
    utilization_factor_r = {rate_load_keys[i]: float(rate_load_r[i]) / float(load_capacity_val[i]) for i in range(3)}

    calculate_1 = [
        f'{float(rate_load_f[i])} / {float(load_capacity_val[i])} = {float(rate_load_f[i]) / float(load_capacity_val[i])}'
        for i in range(3)]
    calculate_2 = [
        f'{float(rate_load_r[i])} / {float(load_capacity_val[i])} = {float(rate_load_r[i]) / float(load_capacity_val[i])}'
        for i in range(3)]

    return utilization_factor_f, utilization_factor_r, calculate_1, calculate_2


def find_operational_speed(option: int):
    ships = tuple(options.get_info_ships(option, AttachmentsTable8.speed).keys())
    speeds = {ship: speed.split('&')
              for speed in tuple(options.get_info_ships(option, AttachmentsTable8.speed).values()) for ship in ships}
    speed_load_dict = {list(speeds.keys())[i]: float(list(speeds.values())[i][0].strip().replace(',', '.'))
                       for i in range(3)}
    speed_empty_dict = {list(speeds.keys())[i]: float(list(speeds.values())[i][1].strip().replace(',', '.'))
                        for i in range(3)}
    utilization_factor_f_dict, utilization_factor_r_dict = find_utilization_factor(option)[0], \
        find_utilization_factor(option)[1]

    speed_load = list(speed_load_dict.values())
    speed_empty = list(speed_empty_dict.values())

    utilization_factor_f = list(utilization_factor_f_dict.values())
    utilization_factor_r = list(utilization_factor_r_dict.values())

    operational_speed_f = {ships[i]: speed_empty[i] - utilization_factor_f[i] * (speed_empty[i] - speed_load[i])
                           for i in range(3)}
    operational_speed_r = {ships[i]: speed_empty[i] - utilization_factor_r[i] * (speed_empty[i] - speed_load[i])
                           for i in range(3)}
    calculate_f = [
        f'{speed_empty[i]} - {utilization_factor_f[i]} * ({speed_empty[i]} - {speed_load[i]}) = {speed_empty[i] - utilization_factor_f[i] * (speed_empty[i] - speed_load[i])}'
        for i in range(3)]
    calculate_r = [
        f'{speed_empty[i]} - {utilization_factor_r[i]} * ({speed_empty[i]} - {speed_load[i]}) = {speed_empty[i] - utilization_factor_r[i] * (speed_empty[i] - speed_load[i])}'
        for i in range(3)]

    return operational_speed_f, operational_speed_r, calculate_f, calculate_r


def find_times_with_cargo(option: int) -> tuple:
    operational_speed_vals_f = list(find_operational_speed(option)[0].values())
    operational_speed_keys_f = list(find_operational_speed(option)[0].keys())
    operational_speed_vals_r = list(find_operational_speed(option)[1].values())
    operational_speed_keys_r = list(find_operational_speed(option)[1].keys())

    distance = float(options.get_info_distance(option))

    times_forward = {operational_speed_keys_f[i]: distance / (operational_speed_vals_f[i] * 0.85) for i in range(3)}
    times_reverse = {operational_speed_keys_r[i]: distance / (operational_speed_vals_r[i] * 0.85) for i in range(3)}

    calculate_f = [
        f'{distance} / ({operational_speed_vals_f[i]} * 0.85) = {distance / (operational_speed_vals_f[i] * 0.85)}'
        for i in range(3)]
    calculate_r = [
        f'{distance} / ({operational_speed_keys_r[i]} * 0.85) = {distance / (operational_speed_vals_r[i] * 0.85)}'
        for i in range(3)]

    return times_forward, times_reverse, calculate_f, calculate_r


def find_duration_stay(option: int) -> tuple:
    rate_f, rate_f_keys = list(find_rate_load(option)[0].values()), list(find_rate_load(option)[0].keys())
    rate_r, rate_r_keys = list(find_rate_load(option)[1].values()), list(find_rate_load(option)[1].keys())

    volume_f, volume_r = find_volume_foreign(option)

    duration_stay_f = {rate_f_keys[i]: float(rate_f[i]) / float(volume_f) for i in range(3)}
    duration_stay_r = {rate_r_keys[i]: float(rate_r[i]) / float(volume_r) for i in range(3)}

    calculate_f = [f'{float(rate_f[i])} / {float(volume_f)} = {float(rate_f[i]) / float(volume_f)}'
                   for i in range(3)]
    calculate_r = [f'{float(rate_r[i])} / {float(volume_r)} = {float(rate_r[i]) / float(volume_r)}'
                   for i in range(3)]
    return duration_stay_f, duration_stay_r, calculate_f, calculate_r


def find_flight_time(option: int):
    ships = list(options.get_info_ships(option, AttachmentsTable8.ship_count).keys())

    duration_stay_time_f = list(find_duration_stay(option)[0].values())
    duration_stay_time_r = list(find_duration_stay(option)[1].values())

    time_cargo_f, time_cargo_r = (list(find_times_with_cargo(option)[0].values()),
                                  list(find_times_with_cargo(option)[1].values()))
    flight_time_f = {ships[i]: time_cargo_f[i] + duration_stay_time_f[i] + duration_stay_time_f[i] for i in range(3)}
    flight_time_r = {ships[i]: time_cargo_r[i] + duration_stay_time_r[i] + duration_stay_time_r[i] for i in range(3)}

    calculate_f = [
        f'{time_cargo_f[i]} + {duration_stay_time_f[i]} + {duration_stay_time_f[i]} = {(time_cargo_f[i] + duration_stay_time_f[i] + duration_stay_time_f[i]) / 24} суток'
        for i in range(3)]
    calculate_r = [
        f'{time_cargo_r[i]} + {duration_stay_time_r[i]} + {duration_stay_time_r[i]} = {(time_cargo_r[i] + duration_stay_time_r[i] + duration_stay_time_r[i]) / 24} суток'
        for i in range(3)]
    return flight_time_f, flight_time_r, calculate_f, calculate_r


def find_duration_turn(option: int):
    ships = list(options.get_info_ships(option, AttachmentsTable8.ship_count).keys())

    forward_time_f = list(find_flight_time(option)[0].values())
    forward_time_r = list(find_flight_time(option)[1].values())

    duration_turn = {ships[i]: forward_time_f[i] + forward_time_r[i] for i in range(3)}
    calculate = [f'{forward_time_f[i]} + {forward_time_r[i]} = {(forward_time_f[i] + forward_time_r[i]) / 24} суток' for i in
                 range(3)]
    return duration_turn, calculate
