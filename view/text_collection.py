option = f'Введите свой вариант: '

work_number = "Какую работу из (5) вывести? "

table_1 = '🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️Таблица 1.1🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️'
table_2 = '🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️Таблица 1.3🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️'
table_3 = '🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️Таблица 1.4🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️'
table_4 = '🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️Таблица 2.1🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️'
table_5 = '🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️Таблица 2.3🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️'
table_6 = '🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️Таблица 2.4🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️'

distance = "Расстояние, км"

type_cargo = "Род перевозимого груза"

trans_cargo = {
    'forward': "Прямое направление",
    'reverse': "Обратное направление"
}

ports = 'Порты'
type_ports = {
    'departures': "Порт отправления",
    'appointments': "Порт назначения"

}
ship_types = "Варианты типов судов (номера проектов)"

specifications = 'Характеристики'

overall_length = "Длина габаритная, м"
overall_width = "Ширина габаритная, м"
side_height = "Высота борта, м"
draft_cargo = "Осадка в грузу: в море, м"
engine_power = "Мощность главных двигателей, л.с."
empty_speed = "Скорость в грузу & порожнем, км/ч"
autonomy_swim = "Автономность плавания, сут."
crew = "Экипаж"
deadweight = "Дедвейт, т в море & на реке"

deadweight_types = {
    'sea': "Дедвейт, т в море",
    'river': "Дедвейт, т на реке"
}

load_capacity = "Грузоподъёмность (при 100 % запасов) в море, т"
gross_capacity = "Валовая вместимость GT (МК-1969)"
net_capacity = "Чистая вместимость NT (МК-1969)"
holds = "Число трюмов, ед."
hold_capacity = "Вместимость трюмов, м3"
container_capacity = "Контейнеровместимость, ед."

table_text_1 = [overall_length, overall_width, side_height, draft_cargo, engine_power, empty_speed, autonomy_swim, crew,
                deadweight, load_capacity, gross_capacity,
                net_capacity, holds, hold_capacity,
                container_capacity]

type_ship = "Тип судна*"
project_number = "Номер проекта"
book_value = "Балансовая стоимость, тыс. долл."
share_capital = 'Акционерный капитал учредителя, Аакi, тыс. долл.'
count_ship = "Кол-во судов данного проекта, nci"

table_text_2 = [type_ship, project_number, book_value]
table_text_3 = [project_number, book_value, count_ship, share_capital]

calculation_carrying_capacity = "Расчёт провозной способности судов"
calculation_duration_turn = "Расчёт продолжительности оборота cудов"

ship_1 = 'Судно №1'
ship_2 = 'Судно №2'
ship_3 = 'Судно №3'

specific_cargo_capacity = "Удельная грузовместимость судна, куб. м/т"
load_volume_f = "Удельный погрузочный объем в прямом направлении, м3/т"
load_volume_r = "Удельный погрузочный объем в обратном направлении, м3/т"
loading_ship_f = "Норма загрузки судна: в прямом направлении, т"
loading_ship_r = "Норма загрузки судна: в обратном направлении, т"
capacity_factor_f = "Коэффициент использования грузоподъемности судна: в прямом направлении"
capacity_factor_r = "Коэффициент использования грузоподъемности судна: в обратном направлении"
speed_cargo_f = "Скорость хода с грузом: в прямом направлении, км/ч"
speed_cargo_r = "Скорость хода с грузом: в обратном направлении, км/ч"
time_with_cargo_f = "Время хода с грузом: tх гр, час в прямом направлении"
time_with_cargo_r = "Время хода с грузом: tх гр, час в обратном направлении"
flight_time_f = "Время рейса в прямом направлении, сут."
flight_time_r = "Время рейса в обратном  направлении, сут."
duration_turnover = "Продолжительность оборота, сут. "

carrying_capacity = "Расчёт провозной способности судов различных проектов за эксплуатационный период"

specifications_international = "Характеристики судов заграничного плавания"
name_ship = "Название судна"
cost_price = "Себестоимость содержания без топлива – С, долл./сут."
specific_fuel = "Удельный расход топлива – Рт, кг/км"
number_crew = "Экипаж – mэк, чел"

table_text_4 = [name_ship, project_number, cost_price, specific_fuel, number_crew]

structure_turn = "Структура расходов за оборот"
revenue_turn = "Расчёт доходов за оборот"
determination_cost = "Определение себестоимости перевозок грузов в прямом и обратном направлении по каждому судну, долл./т"
freight_rate = "Определение расчётной фрахтовой ставки, долл./т"
income_years = "Определение годовых доходов от перевозки грузов судном"
expenses_years = "Определение годовых расходов от перевозки грузов судном"

cost_maintaining_f = "Затраты судно без учета стоимости топлива в прямом направлении"  # Эокр.пр = Со * tкр.пр
cost_maintaining_r = "Затраты на судно без учета стоимости топлива в обратном направлении"  # Эокр.пр = Со * tкр.пр
abbrev_cost_maintaining = "Затраты на судно без стоимости топлива"
crew_expenses_f = "Расходы содержания экипажа в прямом направлении"  # Ээккр.пр = mэк * 18 * tкрпр
crew_expenses_r = "Расходы содержания экипажа в обратном направлении"  # Ээккр.пр = mэк * 18 * tкрпр
abbrev_crew_expenses = "Расходы на экипажа"
ship_fees = "Cудовые сборы"  # ∑Ссс
fuel_costs = "Расходы на топливо в прямом (обратном) направлении"  # Эткр.пр = 700 * Рт * 712 * 0,00108
abbrev_fuel_costs = "Расходы на топливо"
consumption_f = "Расходы за прямое направление"  # Эокрпр + Ээккрпр + Эсскрпр + Эткрпр
consumption_r = "Расходы за обратное направление"
full_consumption = "Расходы за оборот"

grey_color = "grey"
value_money = "долл"
weight = "bold"
location = "center left"

independent_expenses = "Доля независимых расходов Y"  # Y = Эооб/Эоб
operating_costs = "Эксплуатационные расходы по судну, не зависящие от объёма перевозок Эн"  # Эн = Эi * Y
minimum_volume_transportation = "Минимальный объём перевозок грузов Gmin"  # Gmin = Эн/(fср – Sср  *  (1 – Y))
carrying_capacity_navigation_period = "Провозная способность судна за навигационный период"  # Gi = nобi * (Qэпрi + Qэобрi)
expenses_navigation_period = "Расходы по судну за навигационный период"  # Эперi = Sср * Gi долл
revenue_transportation = "Доходы от перевозок, долл. по каждому судну"  # Дперi = Gперi * fсрi.
utilization_factor_annual_capacity = "Коэффициент использования годовой провозной способности судна"  # Ки.с. = Gmin/Gпер.
minimum_income = "Минимальные доходы (порог рентабельности), долл"  # Дmin = Gmin * fсрi
