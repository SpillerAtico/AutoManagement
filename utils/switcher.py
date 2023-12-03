from general_provisions import options
from general_provisions.table import calculations_table
from view import text_collection


def choose_def(option, case) -> tuple:
    if case == 1:  # Виды кораблей
        type_ship = text_collection.type_ship
        your_ships = options.your_ships(option)
        return type_ship, your_ships
    if case == 2:  # Удельная грузовместимость судна Wc куб.м/т
        specific_cargo_capacity = text_collection.specific_cargo_capacity
        find_specific_capacity = calculations_table.find_specific_capacity(option)[1]
        return specific_cargo_capacity, find_specific_capacity
    if case == 3:  # Норма загрузки судна: Qэ, т в прямом направлении Qэ пр
        loading_ship_f = text_collection.loading_ship_f
        rate_f = calculations_table.find_rate_load(option)[2]
        return loading_ship_f, rate_f
    if case == 4:  # Норма загрузки судна: Qэ, т в обратном Qэ пр
        loading_ship_r = text_collection.loading_ship_r
        rate_r = calculations_table.find_rate_load(option)[3]
        return loading_ship_r, rate_r
    if case == 5:  # Коэффициент использования грузоподъемности судна: Ео в прямом направлении Ео пр
        capacity_factor_f = text_collection.capacity_factor_f
        utilization_factor = calculations_table.find_rate_load(option)[2]
        return capacity_factor_f, utilization_factor
    if case == 6:  # Коэффициент использования грузоподъемности судна: Ео в обратном направлении Ео пр
        capacity_factor_r = text_collection.capacity_factor_r
        utilization_factor = calculations_table.find_rate_load(option)[3]
        return capacity_factor_r, utilization_factor
    if case == 7:  # Скорость хода с грузом: Vе, км/ч в прямом направлении Vе пр
        speed_cargo_f = text_collection.speed_cargo_f
        speed_cargo = calculations_table.find_operational_speed(option)[2]
        return speed_cargo_f, speed_cargo
    if case == 8:  # Скорость хода с грузом: Vе, км/ч в обратном направлении Vе пр
        speed_cargo_r = text_collection.speed_cargo_r
        speed_cargo = calculations_table.find_operational_speed(option)[3]
        return speed_cargo_r, speed_cargo
    if case == 9:  # Время хода с грузом: tх гр, час в прямом направлении tх гр пр
        time_with_cargo_f = text_collection.time_with_cargo_f
        flight_time = calculations_table.find_times_with_cargo(option)[2]
        return time_with_cargo_f, flight_time
    if case == 10:  # Время хода с грузом: tх гр, час в обратном направлении tх гр пр
        time_with_cargo_r = text_collection.time_with_cargo_r
        flight_time = calculations_table.find_times_with_cargo(option)[3]
        return time_with_cargo_r, flight_time
    if case == 11:  # Время рейса: tкр, час в прямом направлении tкр пр
        flight_time_f = text_collection.flight_time_f
        flight_time = calculations_table.find_times_with_cargo(option)[2]
        return flight_time_f, flight_time
    if case == 12:  # Время рейса: tкр, час в обратном направлении tкр пр
        flight_time_r = text_collection.flight_time_r
        flight_time = calculations_table.find_times_with_cargo(option)[3]
        return flight_time_r, flight_time
    if case == 13:  # Продолжительность рейса: tоб, час
        duration_turnover = text_collection.duration_turnover
        duration_turn = calculations_table.find_duration_turn(option)[1]
        return duration_turnover, duration_turn
