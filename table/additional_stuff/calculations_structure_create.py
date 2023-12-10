from view import text_collection
from table import calculations
from settings import options


def calculation_structure_1(option: int):
    ship_1, ship_2, ship_3 = options.your_ships(option)

    cost_maintaining = calculations.find_cost_maintaining(option)[1]
    crew_expenses = calculations.find_crew_expenses(option)[1]
    ship_fees = calculations.find_ship_fees(option)[1]
    fuel_costs = calculations.find_fuel_costs(option)[1]
    consumptions = calculations.find_consumption(option)[1]
    full_consumption = calculations.find_full_consumption(option)[1]

    text = f"""\n\n{text_collection.cost_maintaining_f}\n{cost_maintaining.get(ship_1)[0]}\n{cost_maintaining.get(ship_2)[0]}\n{cost_maintaining.get(ship_3)[0]}\n
{text_collection.cost_maintaining_r}\n{cost_maintaining.get(ship_1)[1]}\n{cost_maintaining.get(ship_2)[1]}\n{cost_maintaining.get(ship_3)[1]}\n
{text_collection.crew_expenses_f}\n{crew_expenses.get(ship_1)[0]}\n{crew_expenses.get(ship_2)[0]}\n{crew_expenses.get(ship_3)[0]}\n
{text_collection.crew_expenses_r}\n{crew_expenses.get(ship_1)[1]}\n{crew_expenses.get(ship_2)[1]}\n{crew_expenses.get(ship_3)[1]}\n
{text_collection.ship_fees}\n{ship_fees.get(ship_1)}\n{ship_fees.get(ship_2)}\n{ship_fees.get(ship_3)}\n
{text_collection.fuel_costs}\n{fuel_costs.get(ship_1)}\n{fuel_costs.get(ship_2)}\n{fuel_costs.get(ship_3)}\n
{text_collection.consumption_f}\n{consumptions.get(ship_1)[0]}\n{consumptions.get(ship_2)[0]}\n{consumptions.get(ship_3)[0]}\n
{text_collection.consumption_r}\n{consumptions.get(ship_1)[1]}\n{consumptions.get(ship_2)[1]}\n{consumptions.get(ship_3)[1]}\n
{text_collection.full_consumption}\n{full_consumption.get(ship_1)}\n{full_consumption.get(ship_2)}\n{full_consumption.get(ship_3)}\n
    """

    return text


def calculation_structure_2(option: int):
    ship_1, ship_2, ship_3 = options.your_ships(option)

    revenue = calculations.find_revenue_turn(option)[1]  # Расчёт доходов за оборот dкр.пр dкр.обр dоб
    cost_cargo_trans = calculations.find_cost_cargo_trans(option)[
        1]  # Определение себестоимости перевозок  Scр Sкр.обр Sкр.пр
    freight_rate = calculations.find_freight_rate(option)[
        1]  # Определение расчётной фрахтовой ставки  f кр.пр f кр.обр f cр
    income = calculations.find_income(option)[1]  # расчет доходов Дпер.пр Дпер.обр. Дпер
    expenses = calculations.find_expenses(option)[1]  # расчет расходов Эпер.пр Эпер.обр Эпер

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
\n{text_collection.income_years}:
\n[{ship_1}]\n{income.get(ship_1)[0]}\n{income.get(ship_1)[1]}\n{income.get(ship_1)[2]}
\n[{ship_2}]\n{income.get(ship_2)[0]}\n{income.get(ship_2)[1]}\n{income.get(ship_2)[2]}
\n[{ship_3}]\n{income.get(ship_3)[0]}\n{income.get(ship_3)[1]}\n{income.get(ship_3)[2]}
\n{text_collection.expenses_years}:
\n[{ship_1}]\n{expenses.get(ship_1)[0]}\n{expenses.get(ship_1)[1]}\n{expenses.get(ship_1)[2]}
\n[{ship_2}]\n{expenses.get(ship_2)[0]}\n{expenses.get(ship_2)[1]}\n{expenses.get(ship_2)[2]}
\n[{ship_3}]\n{expenses.get(ship_3)[0]}\n{expenses.get(ship_3)[1]}\n{expenses.get(ship_3)[2]}
"""
    return text


def calculation_structure_3(option: int):
    ships = options.your_ships(option)

    minimum_volume_transportation = (calculations.find_min_volume_transportation(option)[1],
                                     text_collection.minimum_volume_transportation)
    operating_costs = (calculations.find_operating_costs(option)[1],
                       text_collection.minimum_volume_transportation)
    independent_expenses = (calculations.find_independent_expenses(option)[1],
                            text_collection.operating_costs)
    expenses_navigation_period = (calculations.find_expenses_nav_period(option)[1],
                                  text_collection.independent_expenses)
    carrying_capacity_navigation_period = (calculations.find_capacity_navigation_period(option)[1],
                                           text_collection.expenses_navigation_period)
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


def calculation_structure_5(option: int): # таблица работа 2
    ships = options.your_ships(option)

    specific_capacity = calculations.find_specific_capacity(option)[1]
    rate_load = calculations.find_rate_load(option)
    utilization_factor = calculations.find_utilization_factor(option)[1]
    operational_speed = calculations.find_operational_speed(option)[1]
    times_with_cargo = calculations.find_times_with_cargo(option)[1]
    flight_time = calculations.find_flight_time(option)[1]
    duration_turn = calculations.find_duration_turn(option)[1]

    specifications = (specific_capacity, rate_load, utilization_factor, operational_speed,
                      times_with_cargo, flight_time, duration_turn)
    text = f''
    for specification in specifications:
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


def calculation_structure_6(option: int):
    ships = options.your_ships(option)
    carrying_capacity = calculations.find_carrying_capacity(option)[1]
    text = f''
    for ship in ships:
        text = text + f'\n[{ship}] {carrying_capacity.get(ship)}'

    return text
