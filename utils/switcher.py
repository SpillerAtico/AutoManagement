from settings import options
from table import calculations
from view import text_collection


def choose_def_calc(option, case) -> tuple:
    if case == 1:  # Виды кораблей
        type_ship = text_collection.type_ship
        your_ships = options.your_ships(option)
        return type_ship, your_ships
    if case == 2:  # Удельная грузовместимость судна Wc куб.м/т
        specific_cargo_capacity = text_collection.specific_cargo_capacity
        find_specific_capacity = calculations.find_specific_capacity(option)[1]
        return specific_cargo_capacity, find_specific_capacity
    if case == 3:  # Норма загрузки судна: Qэ, т в прямом направлении Qэ пр
        loading_ship_f = text_collection.loading_ship_f
        rate_f = list(calculations.find_rate_load(option)[2].values())
        return loading_ship_f, rate_f
    if case == 4:  # Норма загрузки судна: Qэ, т в обратном Qэ пр
        loading_ship_r = text_collection.loading_ship_r
        rate_r = list(calculations.find_rate_load(option)[3].values())
        return loading_ship_r, rate_r
    if case == 5:  # Коэффициент использования грузоподъемности судна: Ео в прямом направлении Ео пр
        capacity_factor_f = text_collection.capacity_factor_f
        utilization_factor = calculations.find_utilization_factor(option)[2]
        return capacity_factor_f, utilization_factor
    if case == 6:  # Коэффициент использования грузоподъемности судна: Ео в обратном направлении Ео пр
        capacity_factor_r = text_collection.capacity_factor_r
        utilization_factor = calculations.find_utilization_factor(option)[3]
        return capacity_factor_r, utilization_factor
    if case == 7:  # Скорость хода с грузом: Vе, км/ч в прямом направлении Vе пр
        speed_cargo_f = text_collection.speed_cargo_f
        speed_cargo = calculations.find_operational_speed(option)[2]
        return speed_cargo_f, speed_cargo
    if case == 8:  # Скорость хода с грузом: Vе, км/ч в обратном направлении Vе пр
        speed_cargo_r = text_collection.speed_cargo_r
        speed_cargo = calculations.find_operational_speed(option)[3]
        return speed_cargo_r, speed_cargo
    if case == 9:  # Время хода с грузом: tх гр, час в прямом направлении tх гр пр
        time_with_cargo_f = text_collection.time_with_cargo_f
        times_with_cargo = calculations.find_times_with_cargo(option)[2]
        return time_with_cargo_f, times_with_cargo
    if case == 10:  # Время хода с грузом: tх гр, час в обратном направлении tх гр пр
        time_with_cargo_r = text_collection.time_with_cargo_r
        times_with_cargo = calculations.find_times_with_cargo(option)[3]
        return time_with_cargo_r, times_with_cargo
    if case == 11:  # Время рейса: tкр, час в прямом направлении tкр пр
        flight_time_f = text_collection.flight_time_f
        flight_time = calculations.find_flight_time(option)[2]
        return flight_time_f, flight_time
    if case == 12:  # Время рейса: tкр, час в обратном направлении tкр пр
        flight_time_r = text_collection.flight_time_r
        flight_time = calculations.find_flight_time(option)[3]
        return flight_time_r, flight_time
    if case == 13:  # Продолжительность рейса: tоб, час
        duration_turnover = text_collection.duration_turnover
        duration_turn = calculations.find_duration_turn(option)[1]
        return duration_turnover, duration_turn
    if case == 14:
        capacity_carrying = text_collection.carrying_capacity
        carrying_capacity = list(calculations.find_carrying_capacity(option)[1].values())
        return capacity_carrying, carrying_capacity


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
        cost = calculations.find_cost_maintaining(option)[0]

        return cost_maintaining_f, cost.get(ship)[0]

    if case == 16:  # Затраты судно без учета стоимости топлива в обратном направлении
        cost_maintaining_r = text_collection.cost_maintaining_r
        cost = calculations.find_cost_maintaining(option)[0]
        return cost_maintaining_r, cost.get(ship)[1]

    if case == 17:  # Расходы содержания экипажа в прямом направлении
        crew_expenses_f = text_collection.crew_expenses_f
        cost = calculations.find_crew_expenses(option)[0]
        return crew_expenses_f, cost.get(ship)[0]

    if case == 18:  # Расходы содержания экипажа в обратном направлении
        crew_expenses_r = text_collection.crew_expenses_r
        cost = calculations.find_crew_expenses(option)[0]
        return crew_expenses_r, cost.get(ship)[1]

    if case == 19:  # Cудовые сборы
        ship_fees = text_collection.ship_fees
        cost = calculations.find_ship_fees(option)[0]
        return ship_fees, cost.get(ship)

    if case == 20:  # Расходы на топливо в прямом (обратном) направлении
        fuel_costs = text_collection.fuel_costs
        cost = calculations.find_fuel_costs(option)[0]
        return fuel_costs, cost.get(ship)

    if case == 21:  # Расходы за прямое направление
        consumption_f = text_collection.consumption_f
        cost = calculations.find_consumption(option)[0]
        return consumption_f, cost.get(ship)[0]

    if case == 22:  # Расходы за обратное направление
        consumption_r = text_collection.consumption_r
        cost = calculations.find_consumption(option)[0]
        return consumption_r, cost.get(ship)[1]

    if case == 23:  # Расходы за оборот
        full_consumption = text_collection.full_consumption
        cost = calculations.find_full_consumption(option)[0]
        return full_consumption, cost.get(ship)
