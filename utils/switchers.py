from settings import options
from table import calculations
from view import text_collection


def choose_def_value(option, case, ship) -> tuple:
    if case == 1:  # Виды кораблей
        type_ship = text_collection.type_ship
        your_ships = options.your_ships(option)
        return type_ship, your_ships

    if case == 2:  # Удельная грузовместимость судна Wc куб.м/т
        specific_cargo_capacity = text_collection.specific_cargo_capacity
        find_specific_capacity = calculations.find_specific_capacity(option)[0]
        return specific_cargo_capacity, find_specific_capacity.get(ship)

    if case == 3:  # Норма загрузки судна: Qэ, т в прямом направлении Qэ пр
        loading_ship_f = text_collection.loading_ship_f
        rate_f = calculations.find_rate_load(option)[0]
        return loading_ship_f, rate_f.get(ship)

    if case == 4:  # Норма загрузки судна: Qэ, т в обратном Qэ пр
        loading_ship_r = text_collection.loading_ship_r
        rate_r = calculations.find_rate_load(option)[1]
        return loading_ship_r, rate_r.get(ship)

    if case == 5:  # Коэффициент использования грузоподъемности судна: Ео в прямом направлении Ео пр
        capacity_factor_f = text_collection.capacity_factor_f
        utilization_factor = calculations.find_utilization_factor(option)[0]

        return capacity_factor_f, utilization_factor.get(ship)[0]

    if case == 6:  # Коэффициент использования грузоподъемности судна: Ео в обратном направлении Ео пр
        capacity_factor_r = text_collection.capacity_factor_r
        utilization_factor = calculations.find_utilization_factor(option)[0]

        return capacity_factor_r, utilization_factor.get(ship)[1]

    if case == 7:  # Скорость хода с грузом: Vе, км/ч в прямом направлении Vе пр
        speed_cargo_f = text_collection.speed_cargo_f
        speed_cargo = calculations.find_operational_speed(option)[0]

        return speed_cargo_f, speed_cargo.get(ship)[0]

    if case == 8:  # Скорость хода с грузом: Vе, км/ч в обратном направлении Vе пр
        speed_cargo_r = text_collection.speed_cargo_r
        speed_cargo = calculations.find_operational_speed(option)[0]

        return speed_cargo_r, speed_cargo.get(ship)[1]

    if case == 9:  # Время хода с грузом: tх гр, час в прямом направлении tх гр пр
        time_with_cargo_f = text_collection.time_with_cargo_f
        times_with_cargo = calculations.find_times_with_cargo(option)[0]

        return time_with_cargo_f, times_with_cargo.get(ship)[0]

    if case == 10:  # Время хода с грузом: tх гр, час в обратном направлении tх гр пр
        time_with_cargo_r = text_collection.time_with_cargo_r
        times_with_cargo = calculations.find_times_with_cargo(option)[0]

        return time_with_cargo_r, times_with_cargo.get(ship)[1]

    if case == 11:  # Время рейса: tкр, час в прямом направлении tкр пр
        flight_time_f = text_collection.flight_time_f
        flight_time = calculations.find_flight_time(option)[0]

        return flight_time_f, flight_time.get(ship)[0]

    if case == 12:  # Время рейса: tкр, час в обратном направлении tкр пр
        flight_time_r = text_collection.flight_time_r
        flight_time = calculations.find_flight_time(option)[0]

        return flight_time_r, flight_time.get(ship)[1]

    if case == 13:  # Продолжительность рейса: tоб, час
        duration_turnover = text_collection.duration_turnover
        duration_turn = calculations.find_duration_turn(option)[0]
        return duration_turnover, duration_turn.get(ship)

    if case == 14:  # Расчёт провозной способности судов
        capacity_carrying = text_collection.carrying_capacity
        carrying_capacity = calculations.find_carrying_capacity(option)[0]
        return capacity_carrying, carrying_capacity.get(ship)

    if case == 15:  # Затраты судно без учета стоимости топлива в прямом направлении
        cost_maintaining_f = text_collection.cost_maintaining_f
        answer = calculations.find_cost_maintaining(option)[0]

        return cost_maintaining_f, answer.get(ship)[0]

    if case == 16:  # Затраты судно без учета стоимости топлива в обратном направлении
        cost_maintaining_r = text_collection.cost_maintaining_r
        answer = calculations.find_cost_maintaining(option)[0]
        return cost_maintaining_r, answer.get(ship)[1]

    if case == 17:  # Расходы содержания экипажа в прямом направлении
        crew_expenses_f = text_collection.crew_expenses_f
        answer = calculations.find_crew_expenses(option)[0]
        return crew_expenses_f, answer.get(ship)[0]

    if case == 18:  # Расходы содержания экипажа в обратном направлении
        crew_expenses_r = text_collection.crew_expenses_r
        answer = calculations.find_crew_expenses(option)[0]
        return crew_expenses_r, answer.get(ship)[1]

    if case == 19:  # Cудовые сборы
        ship_fees = text_collection.ship_fees
        answer = calculations.find_ship_fees(option)[0]
        return ship_fees, answer.get(ship)

    if case == 20:  # Расходы на топливо в прямом (обратном) направлении
        fuel_costs = text_collection.fuel_costs
        answer = calculations.find_fuel_costs(option)[0]
        return fuel_costs, answer.get(ship)

    if case == 21:  # Расходы за прямое направление
        consumption_f = text_collection.consumption_f
        answer = calculations.find_consumption(option)[0]
        return consumption_f, answer.get(ship)[0]

    if case == 22:  # Расходы за обратное направление
        consumption_r = text_collection.consumption_r
        answer = calculations.find_consumption(option)[0]
        return consumption_r, answer.get(ship)[1]

    if case == 23:  # Расходы за оборот
        full_consumption = text_collection.full_consumption
        answer = calculations.find_full_consumption(option)[0]
        return full_consumption, answer.get(ship)

    if case == 24:  # Gmin = Эн/(fср – Sср  *  (1 – Y))
        minimum_volume_transportation = text_collection.minimum_volume_transportation
        answer = calculations.find_min_volume_transportation(option)[0]
        return minimum_volume_transportation, answer.get(ship)

    if case == 25:  # Эн = Эi * Y
        operating_costs = text_collection.operating_costs
        answer = calculations.find_operating_costs(option)[0]
        return operating_costs, answer.get(ship)

    if case == 26:  # Y = Эооб/Эоб
        independent_expenses = text_collection.independent_expenses
        answer = calculations.find_independent_expenses(option)[0]
        return independent_expenses, answer.get(ship)

    if case == 27:  # Эпер = Sср * Gi долл
        expenses_navigation_period = text_collection.expenses_navigation_period
        answer = calculations.find_expenses_nav_period(option)[0]
        return expenses_navigation_period, answer.get(ship)

    if case == 28:  # Gi = nобi * (Qэпрi + Qэобрi)
        carrying_capacity_navigation_period = text_collection.carrying_capacity_navigation_period
        answer = calculations.find_capacity_navigation_period(option)[0]
        return carrying_capacity_navigation_period, answer.get(ship)

    if case == 29:  # Дпер = Gi * fсрi.
        revenue_transportation = text_collection.revenue_transportation
        answer = calculations.find_revenue_transportation(option)[0]
        return revenue_transportation, answer.get(ship)

    if case == 30:  # Дmin = Gmin * fсрi
        factor_annual_capacity = text_collection.factor_annual_capacity
        answer = calculations.find_factor_annual_capacity(option)[0]
        return factor_annual_capacity, answer.get(ship)

    if case == 31:  # # fтэк = (fср * Qэ – Эссоб – Этоб) / tоб, где Qэ = Qэпр + Qэобр
        charter_equivalent = text_collection.charter_equivalent
        answer = calculations.find_charter_equivalent(option)[0]
        return charter_equivalent, answer.get(ship)

    if case == 32:  # Дар = (365 – Тэ) * fтэк;
        income_ships = text_collection.income_ships
        answer = calculations.find_income_ships(option)[0]
        return income_ships, answer.get(ship)

    if case == 33:  # Эар = (365 – Тэ) * Со
        expenses_delivery = text_collection.expenses_delivery
        answer = calculations.find_expenses_delivery(option)[0]
        return expenses_delivery, answer.get(ship)

    if case == 34:  # Пв = Дпер + Дар – Эпер – Эар
        gross_profit = text_collection.gross_profit
        answer = calculations.find_gross_profit(option)[0]
        return gross_profit, answer.get(ship)

    if case == 35:  # R = Пв / (Эпер + Эар) * 100%
        profitability = text_collection.profitability
        answer = calculations.find_profitability(option)[0]
        return profitability, answer.get(ship)
