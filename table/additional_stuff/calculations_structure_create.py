from view import text_collection
from table import calculations
from settings import options


def calculation_structure_1(option: int):  # расходы за оборот
    ship_1, ship_2, ship_3 = options.your_ships(option)

    cost_maintaining = calculations.find_cost_maintaining(option)[1]
    crew_expenses = calculations.find_crew_expenses(option)[1]
    ship_fees = calculations.find_ship_fees(option)[1]
    fuel_costs = calculations.find_fuel_costs(option)[1]
    consumptions = calculations.find_consumption(option)[1]
    full_consumption = calculations.find_full_consumption(option)[1]

    text = f"""\n\n{text_collection.cost_maintaining_f}\n[{ship_1}]  {cost_maintaining.get(ship_1)[0]}\n[{ship_2}]  {cost_maintaining.get(ship_2)[0]}\n[{ship_3}]  {cost_maintaining.get(ship_3)[0]}\n
{text_collection.cost_maintaining_r}\n[{ship_1}]  {cost_maintaining.get(ship_1)[1]}\n[{ship_2}]  {cost_maintaining.get(ship_2)[1]}\n[{ship_3}]  {cost_maintaining.get(ship_3)[1]}\n
{text_collection.crew_expenses_f}\n[{ship_1}]  {crew_expenses.get(ship_1)[0]}\n[{ship_2}]  {crew_expenses.get(ship_2)[0]}\n[{ship_3}]  {crew_expenses.get(ship_3)[0]}\n
{text_collection.crew_expenses_r}\n[{ship_1}]  {crew_expenses.get(ship_1)[1]}\n[{ship_2}]  {crew_expenses.get(ship_2)[1]}\n[{ship_3}]  {crew_expenses.get(ship_3)[1]}\n
{text_collection.ship_fees}\n[{ship_1}]  {ship_fees.get(ship_1)}\n[{ship_2}]  {ship_fees.get(ship_2)}\n[{ship_3}]  {ship_fees.get(ship_3)}\n
{text_collection.fuel_costs}\n[{ship_1}]  {fuel_costs.get(ship_1)}\n[{ship_2}]  {fuel_costs.get(ship_2)}\n[{ship_3}]  {fuel_costs.get(ship_3)}\n
{text_collection.consumption_f}\n[{ship_1}]  {consumptions.get(ship_1)[0]}\n[{ship_2}]  {consumptions.get(ship_2)[0]}\n[{ship_3}]  {consumptions.get(ship_3)[0]}\n
{text_collection.consumption_r}\n[{ship_1}]  {consumptions.get(ship_1)[1]}\n[{ship_2}]  {consumptions.get(ship_2)[1]}\n[{ship_3}]  {consumptions.get(ship_3)[1]}\n
{text_collection.full_consumption}\n[{ship_1}]  {full_consumption.get(ship_1)}\n[{ship_2}]  {full_consumption.get(ship_2)}\n[{ship_3}]  {full_consumption.get(ship_3)}\n
    """

    return text


def calculation_structure_2(option: int):  # доходы
    ship_1, ship_2, ship_3 = options.your_ships(option)

    revenue = calculations.find_revenue_turn(option)[1]  # Расчёт доходов за оборот dкр.пр dкр.обр dоб
    cost_cargo_trans = calculations.find_cost_cargo_trans(option)[
        1]  # Определение себестоимости перевозок  Scр Sкр.обр Sкр.пр
    freight_rate = calculations.find_freight_rate(option)[
        1]  # Определение расчётной фрахтовой ставки  f кр.пр f кр.обр f cр

    text = f"""
\n{text_collection.revenue_turn}:
\n[{ship_1}] {revenue.get(ship_1)}\n[{ship_2}] {revenue.get(ship_2)}\n[{ship_3}] {revenue.get(ship_3)}
\n{text_collection.determination_cost}:
\n[{ship_1}]\n{cost_cargo_trans.get(ship_1)[0]}\n{cost_cargo_trans.get(ship_1)[1]}\n{cost_cargo_trans.get(ship_1)[2]}
\n[{ship_2}]\n{cost_cargo_trans.get(ship_2)[0]}\n{cost_cargo_trans.get(ship_2)[1]}\n{cost_cargo_trans.get(ship_2)[2]}
\n[{ship_3}]\n{cost_cargo_trans.get(ship_3)[0]}\n{cost_cargo_trans.get(ship_3)[1]}\n{cost_cargo_trans.get(ship_3)[2]}
\n{text_collection.freight_rate}:
\n[{ship_1}]\n{freight_rate.get(ship_1)[0]}\n{freight_rate.get(ship_1)[1]}\n{freight_rate.get(ship_1)[2]}
\n[{ship_2}]\n{freight_rate.get(ship_2)[0]}\n{freight_rate.get(ship_2)[1]}\n{freight_rate.get(ship_2)[2]}
\n[{ship_3}]\n{freight_rate.get(ship_3)[0]}\n{freight_rate.get(ship_3)[1]}\n{freight_rate.get(ship_3)[2]}
"""
    return text


def calculation_structure_2_1(option: int):  # доходы и расходы за год
    ship_1, ship_2, ship_3 = options.your_ships(option)
    income = calculations.find_income(option)[1]  # расчет доходов Дпер.пр Дпер.обр. Дпер
    expenses = calculations.find_expenses(option)[1]  # расчет расходов Эпер.пр Эпер.обр Эпер

    text = f"""\n{text_collection.income_years}:
\n[{ship_1}]\n{income.get(ship_1)[0]}\n{income.get(ship_1)[1]}\n{income.get(ship_1)[2]}
\n[{ship_2}]\n{income.get(ship_2)[0]}\n{income.get(ship_2)[1]}\n{income.get(ship_2)[2]}
\n[{ship_3}]\n{income.get(ship_3)[0]}\n{income.get(ship_3)[1]}\n{income.get(ship_3)[2]}
\n{text_collection.expenses_years}:
\n[{ship_1}]\n{expenses.get(ship_1)[0]}\n{expenses.get(ship_1)[1]}\n{expenses.get(ship_1)[2]}
\n[{ship_2}]\n{expenses.get(ship_2)[0]}\n{expenses.get(ship_2)[1]}\n{expenses.get(ship_2)[2]}
\n[{ship_3}]\n{expenses.get(ship_3)[0]}\n{expenses.get(ship_3)[1]}\n{expenses.get(ship_3)[2]}
"""
    return text


def calculation_structure_3(option: int):  # работа 4 вычисления
    ships = options.your_ships(option)

    minimum_volume_transportation = (calculations.find_min_volume_transportation(option)[1],
                                     text_collection.minimum_volume_transportation)
    operating_costs = (calculations.find_operating_costs(option)[1],
                       text_collection.operating_costs)
    independent_expenses = (calculations.find_independent_expenses(option)[1],
                            text_collection.independent_expenses)
    expenses_navigation_period = (calculations.find_expenses_nav_period(option)[1],
                                  text_collection.expenses_navigation_period)
    carrying_capacity_navigation_period = (calculations.find_capacity_navigation_period(option)[1],
                                           text_collection.carrying_capacity_navigation_period)
    revenue_transportation = (calculations.find_revenue_transportation(option)[1],
                              text_collection.revenue_transportation)
    factor_annual_capacity = (calculations.find_factor_annual_capacity(option)[1],
                              text_collection.factor_annual_capacity)
    minimum_income = (calculations.find_minimum_income(option)[1],
                      text_collection.minimum_income)

    specifications = (minimum_volume_transportation, operating_costs, independent_expenses, expenses_navigation_period,
                      carrying_capacity_navigation_period, revenue_transportation, factor_annual_capacity,
                      minimum_income)
    text = f''
    for specification in specifications:
        text = text + f'\n\n{specification[1]}: '
        for ship in ships:
            text = text + f'\n[{ship}]  {specification[0].get(ship)}'
    return text


def calculation_structure_4(option: int):  # капитал
    ships = options.your_ships(option)

    share_capital = calculations.find_share_capital(option)[1]
    text = f''
    for ship in ships:
        text = text + f'\n[{ship}]  {share_capital.get(ship)}'

    return text


def calculation_structure_5(option: int):  # таблица работа 2
    ships = options.your_ships(option)

    specific_capacity = calculations.find_specific_capacity(option)[1]
    rate_load = calculations.find_rate_load(option)
    utilization_factor = calculations.find_utilization_factor(option)[1]
    operational_speed = calculations.find_operational_speed(option)[1]
    times_with_cargo = calculations.find_times_with_cargo(option)[1]
    flight_time = calculations.find_flight_time(option)[1]
    duration_turn = calculations.find_duration_turn(option)[1]

    titles = text_collection.table_text_6
    specifications = (specific_capacity, rate_load, utilization_factor, operational_speed,
                      times_with_cargo, flight_time, duration_turn)
    text = f''
    for specification, title in zip(specifications, titles):
        text = text + f'\n{title}'
        if specification is rate_load:
            for ship in ships:
                text = text + f'\n[{ship}]  {specification[2].get(ship)}'
                text = text + f'\n[{ship}]  {specification[3].get(ship)}'
            text = text + '\n '
        elif type(specification.get(ships[0])) is tuple:
            for ship in ships:
                text = text + f'\n[{ship}]  {specification.get(ship)[0]}'
                text = text + f'\n[{ship}]  {specification.get(ship)[1]}'
            text = text + '\n '
        else:
            for ship in ships:
                text = text + f'\n[{ship}]  {specification.get(ship)}'
            text = text + '\n '

    return text


def calculation_structure_6(option: int):  # провозной способности
    ships = options.your_ships(option)
    carrying_capacity = calculations.find_carrying_capacity(option)[1]
    text = f''
    for ship in ships:
        text = text + f'\n[{ship}] {carrying_capacity.get(ship)}'

    return text


def calculation_structure_7(option: int):
    ships = options.your_ships(option)

    charter_equivalent = calculations.find_charter_equivalent(option)[1]  # fтэк = (fср * Qэ – Эссоб – Этоб) / tоб
    income_ships = calculations.find_income_ships(option)[1]  # Дар = (365 – Тэ) * fтэк
    check_charter_equivalent = calculations.find_check_charter_equivalent(option)  # fтэк > Со
    expenses_delivery = calculations.find_expenses_delivery(option)[1]  # Эар = (365 – Тэ) * Со
    gross_profit = calculations.find_gross_profit(option)[1]  # Пв = Дпер + Дар – Эпер – Эар.
    profitability = calculations.find_profitability(option)[1]  # R = Пв / (Эпер + Эар) * 100 %.

    specifications = (charter_equivalent, income_ships, check_charter_equivalent, expenses_delivery,
                      gross_profit, profitability)

    titles = text_collection.table_text_5
    text = f''
    for specification, title in zip(specifications, titles):
        if specification is not check_charter_equivalent:
            text = text + f'\n\n{title}'
            for ship in ships:
                text = text + f'\n[{ship}] {specification.get(ship)}'

        else:
            text = text + f'\n\n'
            for ship in ships:
                text = text + f'\n[{ship}] {specification.get(ship)}'
            text = text + f'\n{title}'

    return text
