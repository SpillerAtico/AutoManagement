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

    print(
        f'\n\n{text_collection.cost_maintaining_f}\n{cost_maintaining.get(ship_1)[0]}\n{cost_maintaining.get(ship_2)[0]}\n{cost_maintaining.get(ship_3)[0]}\n')
    print(
        f'{text_collection.cost_maintaining_r}\n{cost_maintaining.get(ship_1)[1]}\n{cost_maintaining.get(ship_2)[1]}\n{cost_maintaining.get(ship_3)[1]}\n')
    print(
        f'{text_collection.crew_expenses_f}\n{crew_expenses.get(ship_1)[0]}\n{crew_expenses.get(ship_2)[0]}\n{crew_expenses.get(ship_3)[0]}\n')
    print(
        f'{text_collection.crew_expenses_r}\n{crew_expenses.get(ship_1)[1]}\n{crew_expenses.get(ship_2)[1]}\n{crew_expenses.get(ship_3)[1]}\n')
    print(f'{text_collection.ship_fees}\n{ship_fees.get(ship_1)}\n{ship_fees.get(ship_2)}\n{ship_fees.get(ship_3)}\n')
    print(
        f'{text_collection.fuel_costs}\n{fuel_costs.get(ship_1)}\n{fuel_costs.get(ship_2)}\n{fuel_costs.get(ship_3)}\n')
    print(
        f'{text_collection.consumption_f}\n{consumptions.get(ship_1)[0]}\n{consumptions.get(ship_2)[0]}\n{consumptions.get(ship_3)[0]}\n')
    print(
        f'{text_collection.consumption_r}\n{consumptions.get(ship_1)[1]}\n{consumptions.get(ship_2)[1]}\n{consumptions.get(ship_3)[1]}\n')
    print(
        f'{text_collection.full_consumption}\n{full_consumption.get(ship_1)}\n{full_consumption.get(ship_2)}\n{full_consumption.get(ship_3)}\n')

    return ''


def calculation_structure_2(option: int):
    ship_1, ship_2, ship_3 = options.your_ships(option)

    revenue = calculations.find_revenue_turn(option)[1]  # Расчёт доходов за оборот dкр.пр dкр.обр dоб
    cost_cargo_trans = calculations.find_cost_cargo_trans(option)[
        1]  # Определение себестоимости перевозок  Scр Sкр.обр Sкр.пр
    freight_rate = calculations.find_freight_rate(option)[
        1]  # Определение расчётной фрахтовой ставки  f кр.пр f кр.обр f cр
    income = calculations.find_income(option)[1]  # расчет доходов Дпер.пр Дпер.обр. Дпер
    expenses = calculations.find_expenses(option)[1]  # расчет расходов Эпер.пр Эпер.обр Эпер

    print(f'\n{text_collection.revenue_turn}:')
    print(f'\n[{ship_1}] {revenue.get(ship_1)}\n[{ship_2}] {revenue.get(ship_2)}\n[{ship_3}] {revenue.get(ship_3)}')

    print(f'\n{text_collection.determination_cost}:')
    print(
        f'\n[{ship_1}]\n{cost_cargo_trans.get(ship_1)[0]}\n{cost_cargo_trans.get(ship_1)[1]}\n{cost_cargo_trans.get(ship_1)[2]}')
    print(
        f'\n[{ship_2}]\n{cost_cargo_trans.get(ship_2)[0]}\n{cost_cargo_trans.get(ship_2)[1]}\n{cost_cargo_trans.get(ship_2)[2]}')
    print(
        f'\n[{ship_3}]\n{cost_cargo_trans.get(ship_3)[0]}\n{cost_cargo_trans.get(ship_3)[1]}\n{cost_cargo_trans.get(ship_3)[2]}')

    print(f'\n{text_collection.freight_rate}:')
    print(
        f'\n[{ship_1}]\n{freight_rate.get(ship_1)[0]}\n{freight_rate.get(ship_1)[1]}\n{freight_rate.get(ship_1)[2]}')
    print(
        f'\n[{ship_2}]\n{freight_rate.get(ship_2)[0]}\n{freight_rate.get(ship_2)[1]}\n{freight_rate.get(ship_2)[2]}')
    print(
        f'\n[{ship_3}]\n{freight_rate.get(ship_3)[0]}\n{freight_rate.get(ship_3)[1]}\n{freight_rate.get(ship_3)[2]}')

    print(f'\n{text_collection.income_years}:')
    print(
        f'\n[{ship_1}]\n{income.get(ship_1)[0]}\n{income.get(ship_1)[1]}\n{income.get(ship_1)[2]}')
    print(
        f'\n[{ship_2}]\n{income.get(ship_2)[0]}\n{income.get(ship_2)[1]}\n{income.get(ship_2)[2]}')
    print(
        f'\n[{ship_3}]\n{income.get(ship_3)[0]}\n{income.get(ship_3)[1]}\n{income.get(ship_3)[2]}')

    print(f'\n{text_collection.expenses_years}:')
    print(
        f'\n[{ship_1}]\n{expenses.get(ship_1)[0]}\n{expenses.get(ship_1)[1]}\n{expenses.get(ship_1)[2]}')
    print(
        f'\n[{ship_2}]\n{expenses.get(ship_2)[0]}\n{expenses.get(ship_2)[1]}\n{expenses.get(ship_2)[2]}')
    print(
        f'\n[{ship_3}]\n{expenses.get(ship_3)[0]}\n{expenses.get(ship_3)[1]}\n{expenses.get(ship_3)[2]}')
    return ''
