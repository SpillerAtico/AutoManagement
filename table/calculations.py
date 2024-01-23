from settings import options
from settings.options import workbook, sheets
from utils.enums import AttachmentsTable8, AttachmentsTable6, AttachmentsTable2


def find_share_capital(option: int):
    ships = options.your_ships(option)

    ship_count = 2
    balance = options.get_info_table_2(option, AttachmentsTable2.balance)

    capital = {ship: int(balance.get(ship)) * ship_count for ship in ships}
    calculate = {
        ship: f'{int(balance.get(ship))} * {ship_count} = {int(balance.get(ship)) * ship_count}'
        for ship in ships
    }

    return capital, calculate


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

    cargo_cell_f = {str(cell.coordinate): str(cell.value) for content in sheet['A3':'A42'] for cell in content
                    if cargo_1 in str(cell.value).lower().strip()}.keys()
    cargo_cell_r = {str(cell.coordinate): str(cell.value) for content in sheet['A3':'A42'] for cell in content
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
        ship: f'{float(hold_capacity_val.get(ship))} / {float(load_capacity_val.get(ship))} = {float(hold_capacity_val.get(ship)) / float(load_capacity_val.get(ship))}'
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

    speeds = {ship: options.get_info_ships(option, AttachmentsTable8.speed).get(ship).split('&') for ship in ships}

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


def find_duration_stay(option: int) -> dict:  # Продолжительность стоянки судна в морском порту, ч
    ships = options.your_ships(option)

    rate_f = find_rate_load(option)[0]
    rate_r = find_rate_load(option)[1]

    volume_f, volume_r = find_volume_foreign(option)

    duration_stay = {ship: (round(float(rate_f.get(ship)) / float(volume_f), 2),
                            round(float(rate_r.get(ship)) / float(volume_r), 2)) for ship in ships}

    return duration_stay


def find_flight_time(option: int):  # Время рейса: tкр
    ships = options.your_ships(option)
    duration_stay = find_duration_stay(option)

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

    duration_turn = {ship: round(time.get(ship)[0] + time.get(ship)[1], 2) for ship in ships}
    calculate = {
        ship: f'{time.get(ship)[0]} + {time.get(ship)[1]} = {(time.get(ship)[0] + time.get(ship)[1])} суток'
        for ship in ships}

    return duration_turn, calculate


def find_period_operation(option: int):  # nобi = Тэ/tобi
    ships = options.your_ships(option)

    duration_turn = find_duration_turn(option)[0]
    time = 305

    period_operation = {ship: round(time / duration_turn.get(ship), 2) for ship in ships}
    calculate = {ship: f'{time} / {duration_turn.get(ship)} = {time / duration_turn.get(ship)}'
                 for ship in ships}

    return period_operation, calculate


def find_carrying_capacity(option: int):
    ships = options.your_ships(option)

    period_operation = find_period_operation(option)[0]
    rate_f, rate_r = find_rate_load(option)[0], find_rate_load(option)[1]
    ship_count = options.get_info_ships(option, AttachmentsTable8.ship_count)

    carrying_capacity = {ship: int(ship_count.get(ship)) * int(period_operation.get(ship)) * (
            round(int(rate_f.get(ship))) + round(int(rate_r.get(ship))))
                         for ship in ships}

    calculate = {
        ship: f'{int(ship_count.get(ship))} * {int(period_operation.get(ship))} * ({int(rate_f.get(ship))} + {int(rate_r.get(ship))}) = {int(ship_count.get(ship)) * int(period_operation.get(ship)) * (int(rate_f.get(ship)) + int(rate_r.get(ship)))}'
        for ship in ships}

    return carrying_capacity, calculate


def find_cost_maintaining(
        option: int):  # Затраты на судно без учета стоимости топлива в прямом направлении Эо кр = Со * tкр пр
    ships = options.your_ships(option)

    costs = options.get_info_ships_6(option, AttachmentsTable6.cost_price)
    times = find_flight_time(option)[0]

    cost_maintaining = {ship: (round(float(costs.get(ship)) * float(times.get(ship)[0]), 1),
                               round(float(costs.get(ship)) * float(times.get(ship)[1]), 1)) for ship in ships}

    calculate = {
        ship: (
            f'{float(costs.get(ship))} * {float(times.get(ship)[0])} = {float(costs.get(ship)) * float(times.get(ship)[0])}',
            f'{float(costs.get(ship))} * {float(times.get(ship)[1])} = {float(costs.get(ship)) * float(times.get(ship)[1])}')
        for ship in ships}

    return cost_maintaining, calculate


def find_crew_expenses(option: int):
    ships = options.your_ships(option)

    number_crew = options.get_info_ships_6(option, AttachmentsTable6.number_crew)
    times = find_flight_time(option)[0]

    crew_expenses = {ship: (round(float(number_crew.get(ship)) * 18 * float(times.get(ship)[0]), 1),
                            round(float(number_crew.get(ship)) * 18 * float(times.get(ship)[1]), 1))
                     for ship in ships}

    calculate = {
        ship: (
            f'{float(number_crew.get(ship))} * 18 * {float(times.get(ship)[0])} = {float(number_crew.get(ship)) * 18 * float(times.get(ship)[0])}',
            f'{float(number_crew.get(ship))} * 18 * {float(times.get(ship)[1])} = {float(number_crew.get(ship)) * 18 * float(times.get(ship)[1])}')
        for ship in ships}

    return crew_expenses, calculate


def find_ship_fees(option: int):  # Эсс
    ships = options.your_ships(option)
    fees = options.ship_fees_table_7(option)

    if len(fees.get(ships[0])) == 3:
        ship_fees = {ship: round(fees.get(ship)[0] + fees.get(ship)[1] + fees.get(ship)[2], 2) for ship in ships}
        calculate = {ship: {
            f'{fees.get(ship)[0]} + {fees.get(ship)[1]} + {fees.get(ship)[2]} = {fees.get(ship)[0] + fees.get(ship)[1] + fees.get(ship)[2]}'}
            for ship in ships}
        return ship_fees, calculate
    elif len(fees.get(ships[0])) == 2:
        ship_fees = {ship: round(fees.get(ship)[0] + fees.get(ship)[1], 2) for ship in ships}
        calculate = {ship: f'{fees.get(ship)[0]} + {fees.get(ship)[1]} = {fees.get(ship)[0] + fees.get(ship)[1]}'
                     for ship in ships}
        return ship_fees, calculate


def find_fuel_costs(option: int):  # Этоб
    ships = options.your_ships(option)
    specific_fuel = options.get_info_ships_6(option, AttachmentsTable6.specific_fuel)

    fuel_costs = {ship: round(700 * float(specific_fuel.get(ship)) * 712 * 0.00108, 2) for ship in ships}
    calculate = {
        ship: f'700 * {float(specific_fuel.get(ship))} * 712 * 0.00108 = {700 * float(specific_fuel.get(ship)) * 712 * 0.00108}'
        for ship in ships}

    return fuel_costs, calculate


def find_consumption(option: int):
    ships = options.your_ships(option)

    one = find_cost_maintaining(option)[0]
    two = find_crew_expenses(option)[0]
    three = find_ship_fees(option)[0]
    four = find_fuel_costs(option)[0]

    consumption = {ship: (round(one.get(ship)[0] + two.get(ship)[0] + three.get(ship) + four.get(ship)),
                          round(one.get(ship)[1] + two.get(ship)[1] + three.get(ship) + four.get(ship)))
                   for ship in ships}

    calculate = {
        ship: (
            f'{one.get(ship)[0]} + {two.get(ship)[0]} + {three.get(ship)} + {four.get(ship)} = {one.get(ship)[0] + two.get(ship)[0] + three.get(ship) + four.get(ship)}',
            f'{one.get(ship)[1]} + {two.get(ship)[1]} + {three.get(ship)} + {four.get(ship)} = {one.get(ship)[1] + two.get(ship)[1] + three.get(ship) + four.get(ship)}')
        for ship in ships}

    return consumption, calculate


def find_full_consumption(option: int):
    ships = options.your_ships(option)
    one = find_consumption(option)[0]

    full_consumption = {ship: round(one.get(ship)[0] + one.get(ship)[1], 2) for ship in ships}
    calculate = {
        ship: f'{float(one.get(ship)[0])} + {float(one.get(ship)[1])} = {float(one.get(ship)[0] + one.get(ship)[1])}'
        for ship in ships}

    return full_consumption, calculate


def summa_cost_maintaining(option: int):
    ships = options.your_ships(option)

    cost_maintaining = {}
    for ship in ships:
        cost_maintaining[ship] = (
            round(find_cost_maintaining(option)[0].get(ship)[0] + find_cost_maintaining(option)[0].get(ship)[1], 1))

    return cost_maintaining


def summa_crew_expenses(option: int):
    ships = options.your_ships(option)

    crew_expenses = {}
    for ship in ships:
        crew_expenses[ship] = (
            round(find_crew_expenses(option)[0].get(ship)[0] + find_crew_expenses(option)[0].get(ship)[1], 1))

    return crew_expenses


def find_max_crew_expenses_ship(ships, option):
    crew_expenses = find_crew_expenses(option)[0]

    crew_expenses = {ship: crew_expenses.get(ship)[0] + crew_expenses.get(ship)[1] for ship in ships}

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
    rentable = 1.30
    ships = options.your_ships(option)

    consumption = find_consumption(option)[0]

    revenue_turn = {ship: (round(consumption.get(ship)[0] * rentable, 1),
                           round(consumption.get(ship)[1] * rentable, 1),
                           round(consumption.get(ship)[0] * rentable + consumption.get(ship)[1] * rentable, 1))
                    for ship in ships}
    calculate = {
        ship: f'{consumption.get(ship)[0]} * {rentable} + {consumption.get(ship)[1]} * {rentable} = {consumption.get(ship)[0] * rentable + consumption.get(ship)[1] * rentable}'
        for ship in ships}

    return revenue_turn, calculate


def find_cost_cargo_trans(option: int):  # Определение себестоимости перевозок  Scр Sкр.обр Sкр.пр
    ships = options.your_ships(option)

    rate_load = find_rate_load(option)
    consumptions = find_consumption(option)[0]
    full_consumption = find_full_consumption(option)[0]

    rate_load_f, rate_load_r = rate_load[0], rate_load[1]

    cost_trans = {ship: (round(consumptions.get(ship)[0] / float(rate_load_f.get(ship)), 1),
                         round(consumptions.get(ship)[1] / float(rate_load_r.get(ship)), 1),
                         round(
                             full_consumption.get(ship) / (float(rate_load_f.get(ship)) + float(rate_load_r.get(ship))),
                             1))
                  for ship in ships}

    calculate = {ship: (
        f'{consumptions.get(ship)[0]} / {float(rate_load_f.get(ship))} = {consumptions.get(ship)[0] / float(rate_load_f.get(ship))}',
        f'{consumptions.get(ship)[1]} / {float(rate_load_r.get(ship))} = {consumptions.get(ship)[1] / float(rate_load_r.get(ship))}',
        f'{full_consumption.get(ship)} / ({float(rate_load_f.get(ship))} + {float(rate_load_r.get(ship))}) = {full_consumption.get(ship) / (float(rate_load_f.get(ship)) + float(rate_load_r.get(ship)))}')
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


def find_independent_expenses(option: int):  # Y = Эооб / Эоб
    ships = options.your_ships(option)

    cost_maintaining = summa_cost_maintaining(option)  # Эо кр пр + Эо кр обр

    full_consumption = find_full_consumption(option)[0]  # Эоб
    independent_expenses = {ship: round(cost_maintaining.get(ship) / full_consumption.get(ship), 2)
                            for ship in ships}

    calculate = {
        ship: f'{cost_maintaining.get(ship)} / {full_consumption.get(ship)} = {cost_maintaining.get(ship) / full_consumption.get(ship)}'
        for ship in ships
    }

    return independent_expenses, calculate


def find_operating_costs(option: int):  # Эн = Э пер * Y
    ships = options.your_ships(option)

    expenses = find_expenses(option)[0]  # Эпер
    independent_expenses = find_independent_expenses(option)[0]  # Y = Эооб / Эоб

    operating_costs = {
        ship: round(expenses.get(ship)[2] * independent_expenses.get(ship), 2)
        for ship in ships
    }

    calculate = {
        ship: f'{expenses.get(ship)[2]} * {independent_expenses.get(ship)} = {expenses.get(ship)[2] * independent_expenses.get(ship)}'
        for ship in ships
    }

    return operating_costs, calculate


def find_min_volume_transportation(option: int):  # Gmin = Эн/(fср – Sср  *  (1 – Y))
    ships = options.your_ships(option)

    operating_costs = find_operating_costs(option)[0]  # Эн = Эпер * Y
    independent_expenses = find_independent_expenses(option)[0]  # Y = Эооб / Эоб

    freight_rate = find_freight_rate(option)[0]  # fср
    cost_cargo_trans = find_cost_cargo_trans(option)[0]  # Sср

    volume_transportation = {
        ship:
            round(operating_costs.get(ship) / (freight_rate.get(ship)[2] - cost_cargo_trans.get(ship)[2] * (
                    1 - independent_expenses.get(ship))), 2)
        for ship in ships
    }

    calculate = {
        ship: f'{operating_costs.get(ship)} / ({freight_rate.get(ship)[2]} - {cost_cargo_trans.get(ship)[2]} * ({1} - {independent_expenses.get(ship)})) = {operating_costs.get(ship) / (freight_rate.get(ship)[2] - cost_cargo_trans.get(ship)[2] * (1 - independent_expenses.get(ship)))}'
        for ship in ships
    }

    return volume_transportation, calculate


def find_capacity_navigation_period(option: int):  # Gi = nоб * (Qэпр + Qэобр)
    ships = options.your_ships(option)

    period_operation = find_period_operation(option)[0]  # nоб
    rate_load = find_rate_load(option)

    rate_load_f, rate_load_r = rate_load[0], rate_load[1]  # Qэпр & Qэобр

    capacity_navigation_period = {
        ship: round(period_operation.get(ship) * (float(rate_load[0].get(ship)) + float(rate_load[1].get(ship))), 2)
        for ship in ships
    }

    calculate = {
        ship: f'{period_operation.get(ship)} * ({rate_load[0].get(ship)} + {rate_load[1].get(ship)}) = {period_operation.get(ship) * (float(rate_load[0].get(ship)) + float(rate_load[1].get(ship)))}'
        for ship in ships
    }

    return capacity_navigation_period, calculate


def find_expenses_nav_period(option: int):  # Эпер = Sср * Gi долл
    ships = options.your_ships(option)

    cost_cargo_trans = find_cost_cargo_trans(option)[0]  # Sср
    navigation_period = find_capacity_navigation_period(option)[0]  # Gi = nоб * (Qэпр + Qэобр)

    expenses_nav_period = {
        ship: round(cost_cargo_trans.get(ship)[2] * navigation_period.get(ship), 2)
        for ship in ships
    }

    calculate = {
        ship: f'{cost_cargo_trans.get(ship)[2]} * {navigation_period.get(ship)} = {cost_cargo_trans.get(ship)[2] * navigation_period.get(ship)}'
        for ship in ships

    }
    return expenses_nav_period, calculate


def find_revenue_transportation(option: int):  # Дпер = Gi * fсрi
    ships = options.your_ships(option)

    navigation_period = find_capacity_navigation_period(option)[0]  # Gi = nоб * (Qэпр + Qэобр)
    freight_rate = find_freight_rate(option)[0]  # fср

    revenue_transportation = {
        ship: round(navigation_period.get(ship) * freight_rate.get(ship)[2], 2)
        for ship in ships
    }

    calculate = {
        ship: f'{navigation_period.get(ship)} * {freight_rate.get(ship)[2]} = {navigation_period.get(ship) * freight_rate.get(ship)[2]}'
        for ship in ships
    }

    return revenue_transportation, calculate


def find_factor_annual_capacity(option: int):  # Ки.с. = Gmin/Gi.
    ships = options.your_ships(option)

    min_volume_transportation = find_min_volume_transportation(option)[0]  # Gmin
    navigation_period = find_capacity_navigation_period(option)[0]  # Gi = nоб * (Qэпр + Qэобр)

    factor_annual_capacity = {
        ship: round(min_volume_transportation.get(ship) / navigation_period.get(ship), 2)
        for ship in ships
    }
    calculate = {
        ship: f'{min_volume_transportation.get(ship)} / {navigation_period.get(ship)} = {min_volume_transportation.get(ship) / navigation_period.get(ship)}'
        for ship in ships
    }
    return factor_annual_capacity, calculate


def find_minimum_income(option: int):  # Дmin = Gmin * fсрi
    ships = options.your_ships(option)

    min_volume_transportation = find_min_volume_transportation(option)[0]  # Gmin
    freight_rate = find_freight_rate(option)[0]  # fср

    minimum_income = {
        ship: round(min_volume_transportation.get(ship) * freight_rate.get(ship)[2], 2)
        for ship in ships
    }

    calculate = {
        ship: f'{min_volume_transportation.get(ship)} * {freight_rate.get(ship)[2]} = {min_volume_transportation.get(ship) * freight_rate.get(ship)[2]}'
        for ship in ships
    }

    return minimum_income, calculate


def find_charter_equivalent(option: int):  # fтэк = (fср * Qэ – Эссоб – Этоб) / tоб
    ships = options.your_ships(option)

    rate_load = find_rate_load(option)  # Qэпр & Qэобр
    freight_rate = find_freight_rate(option)[0]  # fср
    duration_turn = find_duration_turn(option)[0]  # tоб
    ship_fees = find_ship_fees(option)[0]  # Эссоб
    fuel_costs = find_fuel_costs(option)[0]  # Этоб

    charter_equivalent = {
        ship: round((freight_rate.get(ship)[2] * (
                float(rate_load[0].get(ship)) + float(rate_load[1].get(ship))) - ship_fees.get(
            ship) - fuel_costs.get(ship)) / duration_turn.get(ship), 2)
        for ship in ships
    }

    calculate = {
        ship: f'({freight_rate.get(ship)[2]} * ({float(rate_load[0].get(ship))} + {float(rate_load[1].get(ship))}) - {ship_fees.get(ship)} - {fuel_costs.get(ship)}) / {duration_turn.get(ship)} = {(freight_rate.get(ship)[2] * (float(rate_load[0].get(ship)) + float(rate_load[1].get(ship))) - ship_fees.get(ship) - fuel_costs.get(ship)) / duration_turn.get(ship)}'
        for ship in ships
    }

    return charter_equivalent, calculate


def find_income_ships(option: int):  # Дар = (365 – Тэ) * fтэк;
    time = 305  # Тэ
    charter_equivalent = find_charter_equivalent(option)[0]
    ships = options.your_ships(option)

    income_ships = {
        ship: round((365 - time) * charter_equivalent.get(ship), 2)
        for ship in ships
    }

    calculate = {
        ship: f'(365 - {time}) * {charter_equivalent.get(ship)} = {(365 - time) * charter_equivalent.get(ship)}'
        for ship in ships
    }

    return income_ships, calculate


def find_check_charter_equivalent(option: int):  # fтэк > Со
    ships = options.your_ships(option)

    charter_equivalent = find_charter_equivalent(option)[0]  # fтэк
    costs = options.get_info_ships_6(option, AttachmentsTable6.cost_price)  # Со

    calculate = {
        ship: f'{charter_equivalent.get(ship)} > {costs.get(ship)}'
        for ship in ships
    }

    return calculate


def find_expenses_delivery(option: int):  # Эар = (365 – Тэ) * Со
    ships = options.your_ships(option)
    time = 305  # Тэ

    costs = options.get_info_ships_6(option, AttachmentsTable6.cost_price)  # Со

    expenses_delivery = {
        ship: round((365 - time) * float(costs.get(ship)), 2)
        for ship in ships
    }

    calculate = {
        ship: f'(365 - {time}) * {costs.get(ship)} = {(365 - time) * float(costs.get(ship))}'
        for ship in ships
    }

    return expenses_delivery, calculate


def find_gross_profit(option: int):  # Пв = Дпер + Дар – Эпер – Эар.
    ships = options.your_ships(option)

    revenue_transportation = find_revenue_transportation(option)[0]  # Дпер
    expenses_nav_period = find_expenses_nav_period(option)[0]  # Эпер
    income_ships = find_income_ships(option)[0]  # Дар
    expenses_delivery = find_expenses_delivery(option)[0]  # Эар

    gross_profit = {
        ship: round(revenue_transportation.get(ship) + income_ships.get(ship) - expenses_nav_period.get(
            ship) - expenses_delivery.get(ship), 2)
        for ship in ships
    }

    calculate = {
        ship: f'{revenue_transportation.get(ship)} + {income_ships.get(ship)} - {expenses_nav_period.get(ship)} - {expenses_delivery.get(ship)} = {revenue_transportation.get(ship) + income_ships.get(ship) - expenses_nav_period.get(ship) - expenses_delivery.get(ship)}'
        for ship in ships
    }

    return gross_profit, calculate


def find_profitability(option: int):  # R = Пв / (Эпер + Эар) * 100 %.
    ships = options.your_ships(option)

    gross_profit = find_gross_profit(option)[0]  # Пв
    expenses_nav_period = find_expenses_nav_period(option)[0]  # Эпер
    expenses_delivery = find_expenses_delivery(option)[0]  # Эар

    profitability = {
        ship: f'{round(gross_profit.get(ship) / (expenses_nav_period.get(ship) + expenses_delivery.get(ship)) * 100, 1)}%'
        for ship in ships
    }

    calculate = {
        ship: f'{gross_profit.get(ship)} / ({expenses_nav_period.get(ship)} + {expenses_delivery.get(ship)}) * 100% = {gross_profit.get(ship) / (expenses_nav_period.get(ship) + expenses_delivery.get(ship)) * 100}%'
        for ship in ships
    }

    return profitability, calculate
