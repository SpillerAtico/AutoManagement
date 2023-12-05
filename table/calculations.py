from settings import options
from settings.options import workbook, sheets
from utils.enums import AttachmentsTable8, AttachmentsTable6
from view import text_collection


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


def find_volume_foreign(option: int):  # Усреднённая валовая норма обработки судов в зарубежных портах
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


def find_specific_capacity(option: int) -> tuple:  # Удельная грузовместимость судна Wc куб.м/т
    load_capacity_val = options.get_info_ships(option, AttachmentsTable8.load_capacity)
    hold_capacity_val = options.get_info_ships(option, AttachmentsTable8.hold_capacity)

    ships = options.your_ships(option)

    specific_capacity = {ship: round(float(hold_capacity_val.get(ship)) / float(load_capacity_val.get(ship)), 1) for
                         ship in ships}
    calculate = {
        ship: f'{ship} / {hold_capacity_val.get(ship)} = {float(hold_capacity_val.get(ship)) / float(load_capacity_val.get(ship))}'
        for ship in ships}

    return specific_capacity, calculate


def find_rate_load(option: int) -> tuple:  # Норма загрузки судна: Qэ, т

    specific_capacity = find_specific_capacity(option)[0]  # удельная грузовместимость судна
    hold_capacity_val = options.get_info_ships(option,
                                               AttachmentsTable8.hold_capacity)
    load_capacity_val = options.get_info_ships(option,
                                               AttachmentsTable8.load_capacity)  # грузоподъёмность, т (при 100 % запасов)

    ships = options.your_ships(option)
    volume = find_volume(option)

    rate_load_f, rate_load_r, calculate_1, calculate_2 = {}, {}, {}, {}

    for ship in ships:
        if float(volume[0]) > float(specific_capacity.get(ship)):
            rate_load_f[ship] = round(float(hold_capacity_val.get(ship)) / float(volume[0]), 1)
            calculate_1[
                ship] = f'{float(hold_capacity_val.get(ship))} / {float(volume[0])} = {float(hold_capacity_val.get(ship)) / float(volume[0])}'
        else:
            rate_load_f[ship] = load_capacity_val.get(ship)
            calculate_1[ship] = f'{load_capacity_val.get(ship)}'

        if float(volume[1]) > float(specific_capacity.get(ship)):
            rate_load_r[ship] = round(float(hold_capacity_val.get(ship)) / float(volume[1]), 1)
            calculate_2[
                ship] = f'{float(hold_capacity_val.get(ship))} / {float(volume[1])} = {float(hold_capacity_val.get(ship)) / float(volume[1])}'
        else:
            rate_load_r[ship] = load_capacity_val.get(ship)
            calculate_2[ship] = f'{load_capacity_val.get(ship)}'

    return rate_load_f, rate_load_r, calculate_1, calculate_2


def find_utilization_factor(option: int):  # Коэффициент использования грузоподъемности судна Ео

    load_capacity_val = options.get_info_ships(option,
                                               AttachmentsTable8.load_capacity)  # грузоподъёмность, т (при 100 % запасов)
    rate_load_dict = find_rate_load(option)  # норма загрузки судна грузом

    ships = options.your_ships(option)
    rate_load_f = rate_load_dict[0]  # норма загрузки судна грузом прямое
    rate_load_r = rate_load_dict[1]  # норма загрузки судна грузом обратное

    utilization_factor = {ship: (round(float(rate_load_f.get(ship)) / float(load_capacity_val.get(ship)), 2),
                                 round(float(rate_load_r.get(ship)) / float(load_capacity_val.get(ship)), 2))
                          for ship in ships}

    calculate = {ship: (
        f'{float(rate_load_f.get(ship))} / {float(load_capacity_val.get(ship))} = {float(rate_load_f.get(ship)) / float(load_capacity_val.get(ship))}',
        f'{float(rate_load_r.get(ship))} / {float(load_capacity_val.get(ship))} = {float(rate_load_r.get(ship)) / float(load_capacity_val.get(ship))}')
        for ship in ships}

    return utilization_factor, calculate


def find_operational_speed(option: int):  # Скорость хода с грузом Vе, км/ч
    ships = options.your_ships(option)

    speeds = {ship: speed.split('&') for speed in
              tuple(options.get_info_ships(option, AttachmentsTable8.speed).values()) for ship in ships}

    speed = {ship: (float(speeds.get(ship)[0].strip().replace(',', '.')),
                    float(speeds.get(ship)[1].strip().replace(',', '.')))
             for ship in ships}  # load и empty скорости

    utilization_factor = find_utilization_factor(option)[0]

    operational_speed = {
        ship: (
            round(speed.get(ship)[1] - utilization_factor.get(ship)[0] * (speed.get(ship)[1] - speed.get(ship)[0]), 2),
            round(speed.get(ship)[1] - utilization_factor.get(ship)[1] * (speed.get(ship)[1] - speed.get(ship)[0]), 2))
        for ship in ships}

    calculate = {ship: (
        f'{speed.get(ship)[1]} - {utilization_factor.get(ship)[0]} * ({speed.get(ship)[1]} - {speed.get(ship)[0]}) = {speed.get(ship)[1] - utilization_factor.get(ship)[0] * (speed.get(ship)[1] - speed.get(ship)[0])}',
        f'{speed.get(ship)[1]} - {utilization_factor.get(ship)[1]} * ({speed.get(ship)[1]} - {speed.get(ship)[0]}) = {speed.get(ship)[1] - utilization_factor.get(ship)[1] * (speed.get(ship)[1] - speed.get(ship)[0])}')
        for ship in ships}

    return operational_speed, calculate


def find_times_with_cargo(option: int) -> tuple:  # Время хода с грузом tх гр, час
    ships = options.your_ships(option)
    operational_speed = find_operational_speed(option)[0]
    distance = float(options.get_info_distance(option))

    times = {ship: (round(distance / (operational_speed.get(ship)[0] * 0.85), 2),
                    round(distance / (operational_speed.get(ship)[1] * 0.85), 2)) for ship in ships}

    calculate = {ship:
        (
            f'{distance} / ({operational_speed.get(ship)[0]} * 0.85) = {distance / (operational_speed.get(ship)[0] * 0.85)}',
            f'{distance} / ({operational_speed.get(ship)[1]} * 0.85) = {distance / (operational_speed.get(ship)[1] * 0.85)}')
        for ship in ships}

    return times, calculate


def find_duration_stay(option: int) -> tuple:  # Продолжительность стоянки судна в морском порту, ч
    ships = options.your_ships(option)

    rate_f = find_rate_load(option)[0]
    rate_r = find_rate_load(option)[1]

    volume_f, volume_r = find_volume_foreign(option)

    duration_stay = {ship: (round(float(rate_f.get(ship)) / float(volume_f), 2),
                            round(float(rate_r.get(ship)) / float(volume_r), 2)) for ship in ships}

    calculate = {ship: (f'{float(rate_f.get(ship))} / {float(volume_f)} = {float(rate_f.get(ship)) / float(volume_f)}',
                        f'{float(rate_r.get(ship))} / {float(volume_r)} = {float(rate_r.get(ship)) / float(volume_r)}')
                 for ship in ships}

    return duration_stay, calculate


print(find_duration_stay(3)[1])


def find_flight_time(option: int):  # Время рейса: tкр
    ships = options.your_ships(option)

    duration_stay = find_duration_stay(option)[0]

    time_cargo = find_times_with_cargo(option)[0]

    flight_time = {
        ship: (round((time_cargo.get(ship)[0] + duration_stay.get(ship)[0] + duration_stay.get(ship)[0]) / 24, 1),
               round((time_cargo.get(ship)[1] + duration_stay.get(ship)[1] + duration_stay.get(ship)[1]) / 24, 1)) for
        ship in ships}

    calculate = {ship:
        (
            f'{time_cargo.get(ship)[0]} ч. + {duration_stay.get(ship)[0]} ч. + {duration_stay.get(ship)[0]} ч. = {(time_cargo.get(ship)[0] + duration_stay.get(ship)[0] + duration_stay.get(ship)[0]) / 24} суток',
            f'{time_cargo.get(ship)[1]} ч. + {duration_stay.get(ship)[1]} ч. + {duration_stay.get(ship)[1]} ч. = {(time_cargo.get(ship)[1] + duration_stay.get(ship)[1] + duration_stay.get(ship)[1]) / 24} суток')
        for ship in ships}

    return flight_time, calculate


def find_duration_turn(option: int):  # Продолжительность оборота, сут. tоб
    ships = options.your_ships(option)

    time = find_flight_time(option)[0]

    duration_turn = {ship: time.get(ship)[0] + time.get(ship)[1] for ship in ships}
    calculate = {
        ship: f'{time.get(ship)[0]} + {time.get(ship)[1]} = {(time.get(ship)[0] + time.get(ship)[1])} суток'
        for ship in ships}

    return duration_turn, calculate


def find_period_operation(option: int):  # nобi = Тэ/tобi
    ships = options.your_ships(option)

    duration_turn = find_duration_turn(option)[0]
    time = 365 * 3

    period_operation = {ship: time / duration_turn.get(ship) for ship in ships}
    calculate = {ship: f'{time} / {duration_turn.get(ship)} = {time / duration_turn.get(ship)}'
                 for ship in ships}

    return period_operation, calculate


def find_carrying_capacity(option: int):
    ship_count = list(options.get_info_ships(option, AttachmentsTable8.ship_count).values())
    ships = list(options.get_info_ships(option, AttachmentsTable8.ship_count).keys())

    period_operation = list(find_period_operation(option)[0].values())

    rate_f = list(find_rate_load(option)[0].values())
    rate_r = list(find_rate_load(option)[1].values())

    carrying_capacity = {
        ships[i]: int(ship_count[i]) * int(period_operation[i]) * (round(int(rate_f[i])) + round(int(rate_r[i])))
        for i in range(3)}

    calculate = {ships[
                     i]: f'{int(ship_count[i])} * {int(period_operation[i])} * ({round(int(rate_f[i]))} + {round(int(rate_r[i]))}) = {int(ship_count[i]) * int(period_operation[i]) * (round(int(rate_f[i])) + round(int(rate_r[i])))}'
                 for i in range(3)}

    return carrying_capacity, calculate


def find_cost_maintaining(option: int):
    ships = options.your_ships(option)

    costs = options.get_info_ships_6(option, AttachmentsTable6.cost_price)
    times = find_flight_time(option)[0]

    cost_maintaining_f = {ship: round(float(costs.get(ship)) * float(times.get(ship)[0]), 1) for ship in ships}
    cost_maintaining_r = {ship: round(float(costs.get(ship)) * float(times.get(ship)[1]), 1) for ship in ships}

    calculate_f = {
        ship: f'{float(costs.get(ship))} * {float(times.get(ship)[0])} = {float(costs.get(ship)) * float(times.get(ship)[0])}'
        for ship in ships}
    calculate_r = {
        ship: f'{float(costs.get(ship))} * {float(times.get(ship)[1])} = {float(costs.get(ship)) * float(times.get(ship)[1])}'
        for ship in ships}

    return cost_maintaining_f, cost_maintaining_r, calculate_f, calculate_r


def find_crew_expenses(option: int):
    ships = options.your_ships(option)

    number_crew = options.get_info_ships_6(option, AttachmentsTable6.number_crew)
    times = find_flight_time(option)[0]

    crew_expenses_f = {ship: round(float(number_crew.get(ship)) * 18 * float(times.get(ship)[0]), 1) for ship in ships}
    crew_expenses_r = {ship: round(float(number_crew.get(ship)) * 18 * float(times.get(ship)[1]), 1) for ship in ships}

    calculate_f = {
        ship: f'{float(number_crew.get(ship))} * 18 * {float(times.get(ship)[0])} = {float(number_crew.get(ship)) * 18 * float(times.get(ship)[0])}'
        for ship in ships}
    calculate_r = {
        ship: f'{float(number_crew.get(ship))} * 18 * {float(times.get(ship)[1])} = {float(number_crew.get(ship)) * 18 * float(times.get(ship)[1])}'
        for ship in ships}

    return crew_expenses_f, crew_expenses_r, calculate_f, calculate_r


def find_ship_fees(option: int):
    ships = options.your_ships(option)
    fees = options.ship_fees_table_7(option)

    if len(fees.get(ships[0])) == 3:
        ship_fees = {ship: round(fees.get(ship)[0] + fees.get(ship)[1] + fees.get(ship)[2], 2) for ship in ships}
        calculate = {ship: {
            f'{fees.get(ship)[0]} + {fees.get(ship)[1]} + {fees.get(ship)[2]} = {fees.get(ship)[0] + fees.get(ship)[1] + fees.get(ship)[2]}'}
            for ship in ships}
        return ship_fees, calculate
    elif len(fees.get(ships[0])) == 2:
        ship_fees = {ship: fees.get(ship)[0] + fees.get(ship)[1] for ship in ships}
        calculate = {ship: {f'{fees.get(ship)[0]} + {fees.get(ship)[1]} = {fees.get(ship)[0] + fees.get(ship)[1]}'}
                     for ship in ships}
        return ship_fees, calculate


def find_fuel_costs(option: int):
    ships = options.your_ships(option)
    specific_fuel = options.get_info_ships_6(option, AttachmentsTable6.specific_fuel)

    fuel_costs = {ship: round(700 * float(specific_fuel.get(ship)) * 712 * 0.00108, 1) for ship in ships}
    calculate = {
        ship: f'700 * {float(specific_fuel.get(ship))} * 712 * 0.00108 = {700 * float(specific_fuel.get(ship)) * 712 * 0.00108}'
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
    ship_1, ship_2, ship_3 = options.your_ships(option)

    cost_maintaining_f = find_cost_maintaining(option)[2]
    cost_maintaining_r = find_cost_maintaining(option)[3]
    crew_expenses_f = find_crew_expenses(option)[2]
    crew_expenses_r = find_crew_expenses(option)[3]
    ship_fees = find_ship_fees(option)[1]
    fuel_costs = find_fuel_costs(option)[1]
    consumption_f = find_consumption(option)[2]
    consumption_r = find_consumption(option)[3]
    full_consumption = find_full_consumption(option)[1]

    print(
        f'{text_collection.cost_maintaining_f}\n{cost_maintaining_f.get(ship_1)}\n{cost_maintaining_f.get(ship_2)}\n{cost_maintaining_f.get(ship_3)}\n')
    print(
        f'{text_collection.cost_maintaining_r}\n{cost_maintaining_r.get(ship_1)}\n{cost_maintaining_r.get(ship_2)}\n{cost_maintaining_r.get(ship_3)}\n')
    print(
        f'{text_collection.crew_expenses_f}\n{crew_expenses_f.get(ship_1)}\n{crew_expenses_f.get(ship_2)}\n{crew_expenses_f.get(ship_3)}\n')
    print(
        f'{text_collection.crew_expenses_r}\n{crew_expenses_r.get(ship_1)}\n{crew_expenses_r.get(ship_2)}\n{crew_expenses_r.get(ship_3)}\n')
    print(f'{text_collection.ship_fees}\n{ship_fees.get(ship_1)}\n{ship_fees.get(ship_2)}\n{ship_fees.get(ship_3)}\n')
    print(
        f'{text_collection.fuel_costs}\n{fuel_costs.get(ship_1)}\n{fuel_costs.get(ship_2)}\n{fuel_costs.get(ship_3)}\n')
    print(
        f'{text_collection.consumption_f}\n{consumption_f.get(ship_1)}\n{consumption_f.get(ship_2)}\n{consumption_f.get(ship_3)}\n')
    print(
        f'{text_collection.consumption_r}\n{consumption_r.get(ship_1)}\n{consumption_r.get(ship_2)}\n{consumption_r.get(ship_3)}\n')
    print(
        f'{text_collection.full_consumption}\n{full_consumption.get(ship_1)}\n{full_consumption.get(ship_2)}\n{full_consumption.get(ship_3)}\n')

    return ''


def calculations_structure_turn(option: int):
    return


def summa_cost_maintaining(option: int):
    ships = options.your_ships(option)

    cost_maintaining = {}
    for ship in ships:
        cost_maintaining[ship] = (
            round(find_cost_maintaining(option)[0].get(ship) + find_cost_maintaining(option)[1].get(ship), 1))

    return cost_maintaining


def summa_crew_expenses(option: int):
    ships = options.your_ships(option)

    crew_expenses = {}
    for ship in ships:
        crew_expenses[ship] = (
            round(find_crew_expenses(option)[0].get(ship) + find_crew_expenses(option)[1].get(ship), 1))

    return crew_expenses


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


def find_revenue_turn(option: int):  # Расчёт доходов за оборот dоб dкр.пр dкр.обр
    rentable = 1.40
    ships = options.your_ships(option)

    consumption = find_consumption(option)

    consumption_f = consumption[0]
    consumption_r = consumption[1]

    revenue_turn = {ship: (round(consumption_f.get(ship) * rentable, 1),
                           round(consumption_r.get(ship) * rentable, 1),
                           round(consumption_f.get(ship) * rentable + consumption_r.get(ship) * rentable, 1))
                    for ship in ships}
    calculate = {
        ship: f'{consumption_f.get(ship)} * {rentable} + {consumption_r.get(ship)} * {rentable} = {consumption_f.get(ship) * rentable + consumption_r.get(ship) * rentable}'
        for ship in ships}

    return revenue_turn, calculate


def find_cost_cargo_trans(option: int):  # Определение себестоимости перевозок  Scр Sкр.обр Sкр.пр
    ships = options.your_ships(option)

    rate_load = find_rate_load(option)
    consumption = find_consumption(option)
    full_consumption = find_full_consumption(option)[0]

    rate_load_f, rate_load_r = rate_load[0], rate_load[1]
    consumption_f, consumption_r = consumption[0], consumption[1]

    cost_trans = {ship: (round(consumption_f.get(ship) / float(rate_load_f.get(ship)), 1),
                         round(consumption_r.get(ship) / float(rate_load_r.get(ship)), 1),
                         round(
                             full_consumption.get(ship) / (float(rate_load_f.get(ship)) + float(rate_load_r.get(ship))),
                             1))
                  for ship in ships}

    calculate = {ship: (
        f'{consumption_f.get(ship)} / {float(rate_load_f.get(ship))} = {consumption_f.get(ship) / float(rate_load_f.get(ship))}',
        f'{consumption_r.get(ship)} / {float(rate_load_r.get(ship))} = {consumption_r.get(ship) / float(rate_load_r.get(ship))}',
        f'{full_consumption.get(ship)} / {float(rate_load_f.get(ship))} + {float(rate_load_r.get(ship))} = {full_consumption.get(ship) / (float(rate_load_f.get(ship)) + float(rate_load_r.get(ship)))}')
        for ship in ships}

    return cost_trans, calculate


def find_freight_rate(option: int):  # Определение расчётной фрахтовой ставки f cр f кр.пр f кр.обр
    ships = options.your_ships(option)

    revenue_turn = find_revenue_turn(option)

    rate_load = find_rate_load(option)
    rate_load_f, rate_load_r = rate_load[0], rate_load[1]

    freight_rate = {
        ship: (round(revenue_turn[0].get(ship)[0] / float(rate_load_f.get(ship)), 1),  # fкр.пр = (dкр.пр)/(Qэ.кр.пр.);
               round(revenue_turn[0].get(ship)[1] / float(rate_load_r.get(ship)), 1),
               # fкр.обр. = (dкр.обр.)/(Qэ.кр.обр.);
               round(revenue_turn[0].get(ship)[2] / (float(rate_load_f.get(ship)) + float(rate_load_r.get(ship))), 1))
        # fср = (dоб)/(Qэ.кр.пр + Qэ.кр.обр).
        for ship in ships}

    calculate = {
        ship: (
            f'{revenue_turn[0].get(ship)[0]} / {float(rate_load_f.get(ship))} = {round(revenue_turn[0].get(ship)[0] / float(rate_load_f.get(ship)), 1)}',
            f'{revenue_turn[0].get(ship)[1]} / {float(rate_load_r.get(ship))} = {round(revenue_turn[0].get(ship)[1] / float(rate_load_r.get(ship)), 1)}',
            f'{revenue_turn[0].get(ship)[2]} / ({float(rate_load_f.get(ship))} + {float(rate_load_r.get(ship))}) = {round(revenue_turn[0].get(ship)[2] / (float(rate_load_f.get(ship)) + float(rate_load_r.get(ship))), 1)}')
        for ship in ships}

    return freight_rate, calculate


def find_income(option: int):  # расчет доходов Дпер.пр Дпер.обр. Дпер
    ships = options.your_ships(option)

    rate_load = find_rate_load(option)
    rate_load_f, rate_load_r = rate_load[0], rate_load[1]

    freight_rate = find_freight_rate(option)[0]
    period_operation = find_period_operation(option)[0]

    income = {ship: (round(freight_rate.get(ship)[0] * period_operation.get(ship) * float(rate_load_f.get(ship)), 1),
                     round(freight_rate.get(ship)[1] * period_operation.get(ship) * float(rate_load_r.get(ship)), 1),
                     round(freight_rate.get(ship)[0] * period_operation.get(ship) * float(rate_load_f.get(ship)) +
                           freight_rate.get(ship)[1] * period_operation.get(ship) * float(rate_load_r.get(ship)), 1))
              for ship in ships}

    calculate = {ship: (
        f'{freight_rate.get(ship)[0]} * {period_operation.get(ship)} * {float(rate_load_f.get(ship))} = {freight_rate.get(ship)[0] * period_operation.get(ship) * float(rate_load_f.get(ship))}',
        f'{freight_rate.get(ship)[1]} * {period_operation.get(ship)} * {float(rate_load_r.get(ship))} = {freight_rate.get(ship)[1] * period_operation.get(ship) * float(rate_load_r.get(ship))}',
        f'{freight_rate.get(ship)[0] * period_operation.get(ship) * float(rate_load_f.get(ship))} + {freight_rate.get(ship)[1] * period_operation.get(ship) * float(rate_load_r.get(ship))} = {freight_rate.get(ship)[0] * period_operation.get(ship) * float(rate_load_f.get(ship)) + freight_rate.get(ship)[1] * period_operation.get(ship) * float(rate_load_r.get(ship))}')
        for ship in ships}
    return income, calculate


def find_expenses(option: int):  # расчет расходов Эпер.пр Эпер.обр Эпер
    ships = options.your_ships(option)

    rate_load = find_rate_load(option)
    rate_load_f, rate_load_r = rate_load[0], rate_load[1]

    cost_trans = find_cost_cargo_trans(option)[0]
    period_operation = find_period_operation(option)[0]

    expenses = {ship: (round(cost_trans.get(ship)[0] * period_operation.get(ship) * float(rate_load_f.get(ship)), 1),
                       round(cost_trans.get(ship)[1] * period_operation.get(ship) * float(rate_load_r.get(ship)), 1),
                       round(cost_trans.get(ship)[0] * period_operation.get(ship) * float(rate_load_f.get(ship)) +
                             cost_trans.get(ship)[1] * period_operation.get(ship) * float(rate_load_r.get(ship)), 1))
                for ship in ships}

    calculate = {ship: (
        f'{cost_trans.get(ship)[0]} * {period_operation.get(ship)} * {float(rate_load_f.get(ship))} = {cost_trans.get(ship)[0] * period_operation.get(ship) * float(rate_load_f.get(ship))}',
        f'{cost_trans.get(ship)[1]} * {period_operation.get(ship)} * {float(rate_load_r.get(ship))} = {cost_trans.get(ship)[1] * period_operation.get(ship) * float(rate_load_r.get(ship))}',
        f'{cost_trans.get(ship)[0] * period_operation.get(ship) * float(rate_load_f.get(ship))} + {cost_trans.get(ship)[1] * period_operation.get(ship) * float(rate_load_r.get(ship))} = {cost_trans.get(ship)[0] * period_operation.get(ship) * float(rate_load_f.get(ship)) + cost_trans.get(ship)[1] * period_operation.get(ship) * float(rate_load_r.get(ship))}')
        for ship in ships}

    return expenses, calculate
