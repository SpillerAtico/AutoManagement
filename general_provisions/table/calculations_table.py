from general_provisions import options
from general_provisions.options import workbook, sheets
from utils.enum import AttachmentsTable8, AttachmentsTable6
from general_provisions import options
from view import text_collection
from random import randint


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
        f'{distance} / ({operational_speed_vals_r[i]} * 0.85) = {distance / (operational_speed_vals_r[i] * 0.85)}'
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
    flight_time_f = {ships[i]: (time_cargo_f[i] + duration_stay_time_f[i] + duration_stay_time_f[i]) / 24 for i in
                     range(3)}
    flight_time_r = {ships[i]: (time_cargo_r[i] + duration_stay_time_r[i] + duration_stay_time_r[i]) / 24 for i in
                     range(3)}

    calculate_f = [
        f'{time_cargo_f[i]} + {duration_stay_time_f[i]} ч. + {duration_stay_time_f[i]} ч. = {(time_cargo_f[i] + duration_stay_time_f[i] + duration_stay_time_f[i]) / 24} суток'
        for i in range(3)]
    calculate_r = [
        f'{time_cargo_r[i]} + {duration_stay_time_r[i]} ч. + {duration_stay_time_r[i]} ч. = {(time_cargo_r[i] + duration_stay_time_r[i] + duration_stay_time_r[i]) / 24} суток'
        for i in range(3)]
    return flight_time_f, flight_time_r, calculate_f, calculate_r


def find_duration_turn(option: int):
    ships = list(options.get_info_ships(option, AttachmentsTable8.ship_count).keys())

    forward_time_f = list(find_flight_time(option)[0].values())
    forward_time_r = list(find_flight_time(option)[1].values())

    duration_turn = {ships[i]: forward_time_f[i] + forward_time_r[i] for i in range(3)}
    calculate = [
        f'{forward_time_f[i]} ч. + {forward_time_r[i]} ч. = {(forward_time_f[i] + forward_time_r[i]) / 24} суток'
        for i in range(3)]
    return duration_turn, calculate


def find_carrying_capacity(option: int):
    ship_count = list(options.get_info_ships(option, AttachmentsTable8.ship_count).values())
    ships = list(options.get_info_ships(option, AttachmentsTable8.ship_count).keys())

    duration_turn = list(find_duration_turn(option)[0].values())

    rate_f = list(find_rate_load(option)[0].values())
    rate_r = list(find_rate_load(option)[1].values())

    carrying_capacity = {
        ships[i]: int(ship_count[i]) * int(duration_turn[i]) * (round(int(rate_f[i])) + round(int(rate_r[i])))
        for i in range(3)}

    calculate = {ships[
                     i]: f'{int(ship_count[i])} * {int(duration_turn[i])} * ({round(int(rate_f[i]))} + {round(int(rate_r[i]))}) = {int(ship_count[i]) * int(duration_turn[i]) * (round(int(rate_f[i])) + round(int(rate_r[i])))}'
                 for i in range(3)}

    return carrying_capacity, calculate


def find_cost_maintaining(option: int):
    ships = options.your_ships(option)

    costs = options.get_info_ships_6(option, AttachmentsTable6.cost_price)
    times_f, times_r = find_flight_time(option)[0], find_flight_time(option)[1]

    cost_maintaining_f = {ship: round(float(costs.get(ship)) * float(times_f.get(ship)), 1) for ship in ships}
    cost_maintaining_r = {ship: round(float(costs.get(ship)) * float(times_r.get(ship)), 1) for ship in ships}

    calculate_f = {
        ship: f'{float(costs.get(ship))} * {float(times_f.get(ship))} = {float(costs.get(ship)) * float(times_f.get(ship))} долл'
        for ship in ships}
    calculate_r = {
        ship: f'{float(costs.get(ship))} * {float(times_r.get(ship))} = {float(costs.get(ship)) * float(times_r.get(ship))} долл'
        for ship in ships}

    return cost_maintaining_f, cost_maintaining_r, calculate_f, calculate_r


def find_crew_expenses(option: int):
    ships = options.your_ships(option)

    number_crew = options.get_info_ships_6(option, AttachmentsTable6.number_crew)
    times_f, times_r = find_flight_time(option)[0], find_flight_time(option)[1]

    crew_expenses_f = {ship: round(float(number_crew.get(ship)) * 18 * float(times_f.get(ship)), 1) for ship in ships}
    crew_expenses_r = {ship: round(float(number_crew.get(ship)) * 18 * float(times_r.get(ship)), 1) for ship in ships}

    calculate_f = {
        ship: f'{float(number_crew.get(ship))} * 18 * {float(times_f.get(ship))} = {float(number_crew.get(ship)) * 18 * float(times_f.get(ship))}  долл'
        for ship in ships}
    calculate_r = {
        ship: f'{float(number_crew.get(ship))} * 18 * {float(times_r.get(ship))} = {float(number_crew.get(ship)) * 18 * float(times_r.get(ship))}  долл'
        for ship in ships}

    return crew_expenses_f, crew_expenses_r, calculate_f, calculate_r


def find_ship_fees(option: int):
    ships = options.your_ships(option)
    fees = options.ship_fees_table_7(option)

    if len(fees.get(ships[0])) == 3:
        ship_fees = {ship: round(fees.get(ship)[0] + fees.get(ship)[1] + fees.get(ship)[2], 2) for ship in ships}
        calculate = {ship: {
            f'{fees.get(ship)[0]} + {fees.get(ship)[1]} + {fees.get(ship)[2]} = {fees.get(ship)[0] + fees.get(ship)[1] + fees.get(ship)[2]} долл'}
            for ship in ships}
        return ship_fees, calculate
    elif len(fees.get(ships[0])) == 2:
        ship_fees = {ship: fees.get(ship)[0] + fees.get(ship)[1] for ship in ships}
        calculate = {ship: {f'{fees.get(ship)[0]} + {fees.get(ship)[1]} = {fees.get(ship)[0] + fees.get(ship)[1]} долл'}
                     for ship in ships}
        return ship_fees, calculate


def find_fuel_costs(option: int):
    ships = options.your_ships(option)
    specific_fuel = options.get_info_ships_6(option, AttachmentsTable6.specific_fuel)

    fuel_costs = {ship: round(700 * float(specific_fuel.get(ship)) * 712 * 0.00108, 1) for ship in ships}
    calculate = {
        ship: f'700 * {float(specific_fuel.get(ship))} * 712 * 0.00108 = {700 * float(specific_fuel.get(ship)) * 712 * 0.00108} долл'
        for ship in ships}

    return fuel_costs, calculate


def find_consumption(option: int):
    ships = options.your_ships(option)

    one_f, one_r = find_cost_maintaining(option)[0], find_cost_maintaining(option)[1]
    two_f, two_r = find_crew_expenses(option)[0], find_crew_expenses(option)[1]
    three = find_ship_fees(option)[0]
    four = find_fuel_costs(option)[0]

    consumption_f = {ship: round(one_f.get(ship) + two_f.get(ship) + three.get(ship) + four.get(ship))
                     for ship in ships}
    consumption_r = {ship: round(one_r.get(ship) + two_r.get(ship) + three.get(ship) + four.get(ship))
                     for ship in ships}
    calculate_f = {
        ship: f'{one_f.get(ship)} + {two_f.get(ship)} + {three.get(ship)} + {four.get(ship)} = {one_f.get(ship) + two_f.get(ship) + three.get(ship) + four.get(ship)}'
        for ship in ships}
    calculate_r = {
        ship: f'{one_r.get(ship)} + {two_r.get(ship)} + {three.get(ship)} + {four.get(ship)} = {one_r.get(ship) + two_r.get(ship) + three.get(ship) + four.get(ship)}'
        for ship in ships}

    return consumption_f, consumption_r, calculate_f, calculate_r


def find_full_consumption(option: int):
    ships = options.your_ships(option)
    one_f, one_r = find_consumption(option)[0], find_consumption(option)[1]

    full_consumption = {ship: one_f.get(ship) + one_r.get(ship) for ship in ships}
    calculate = {
        ship: f'{float(one_f.get(ship))} + {float(one_r.get(ship))} = {float(one_f.get(ship) + one_r.get(ship))}'
        for ship in ships}

    return full_consumption, calculate


def calculation_structure_turn(option: int):
    cost_maintaining_f = list(find_cost_maintaining(option)[2].values())
    cost_maintaining_r = list(find_cost_maintaining(option)[3].values())
    crew_expenses_f = list(find_crew_expenses(option)[2].values())
    crew_expenses_r = list(find_crew_expenses(option)[3].values())
    ship_fees = list(find_ship_fees(option)[1].values())
    fuel_costs = list(find_fuel_costs(option)[1].values())
    consumption_f = list(find_consumption(option)[2].values())
    consumption_r = list(find_consumption(option)[3].values())
    full_consumption = list(find_full_consumption(option)[1].values())

    print(
        f'{text_collection.cost_maintaining_f}\n{cost_maintaining_f[0]}\n{cost_maintaining_f[1]}\n{cost_maintaining_f[2]}\n')
    print(
        f'{text_collection.cost_maintaining_r}\n{cost_maintaining_r[0]}\n{cost_maintaining_r[1]}\n{cost_maintaining_r[2]}\n')
    print(f'{text_collection.crew_expenses_f}\n{crew_expenses_f[0]}\n{crew_expenses_f[1]}\n{crew_expenses_f[2]}\n')
    print(f'{text_collection.crew_expenses_r}\n{crew_expenses_r[0]}\n{crew_expenses_r[1]}\n{crew_expenses_r[2]}\n')
    print(f'{text_collection.ship_fees}\n{ship_fees[0]}\n{ship_fees[1]}\n{ship_fees[2]}\n')
    print(f'{text_collection.fuel_costs}\n{fuel_costs[0]}\n{fuel_costs[1]}\n{fuel_costs[2]}\n')
    print(f'{text_collection.consumption_f}\n{consumption_f[0]}\n{consumption_f[1]}\n{consumption_f[2]}\n')
    print(f'{text_collection.consumption_r}\n{consumption_r[0]}\n{consumption_r[1]}\n{consumption_r[2]}\n')
    print(f'{text_collection.full_consumption}\n{full_consumption[0]}\n{full_consumption[1]}\n{full_consumption[2]}\n')
    return ''


def find_max_crew_expenses_ship(ships, option):
    crew_expenses_f = find_crew_expenses(option)[0]
    crew_expenses_r = find_crew_expenses(option)[1]

    crew_expenses = {ship: crew_expenses_f.get(ship) + crew_expenses_r.get(ship) for ship in ships}

    return crew_expenses


def find_average_load_capacity(option):
    average_capacity = options.get_info_ships(option, AttachmentsTable8.load_capacity)

    del average_capacity[max(average_capacity)]
    del average_capacity[min(average_capacity)]

    return average_capacity


def find_min_load_capacity(option):
    average_capacity = options.get_info_ships(option, AttachmentsTable8.load_capacity)

    return average_capacity


def canalization(option: int):
    ships = options.your_ships(option)
    crews = find_max_crew_expenses_ship(ships, option)

    average_ship = list(find_average_load_capacity(option).keys())[0]
    average_capacity = list(find_average_load_capacity(option).values())[0]

    minimal_ship = options.get_info_ships(option, AttachmentsTable8.load_capacity)

    anal = f"""
    По результатам расчетов можно сделать вывод, что меньшая доля расходов 
    на содержание судна приходится на судно {average_ship}.
    У {average_ship} грузоподъемность и грузовместимость не самые большие - {average_capacity},
    но больше, чем у судна {min(minimal_ship)} - {minimal_ship.get(min(minimal_ship))}.
    Судовые сборы по всем суднам примерно одинаковые. 
    
    Также:
    Большая доля расходов на содержание экипажа приходится на судно {max(crews)}({crews.get(max(crews))}).
    По итоговому показателю "Расходы за оборот" и по анализу всех показателей и характеристик в целом видно, что эффективным является судно {average_ship}.
    """

    print(anal)
    return ''

