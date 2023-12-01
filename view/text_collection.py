option = f'Введите свой вариант: '

table_1 = 'Таблица 1.1'
table_2 = 'Таблица 1.3'
table_3 = 'Таблица 1.4'
table_4 = 'Таблица 2.1'

separator = '🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️🕸️'
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
empty_speed = "Скорость в грузу порожнем (в балласте), км/ч"
autonomy_swim = "Автономность плавания, сут."
crew = "Экипаж"

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
                list(deadweight_types.values())[0], list(deadweight_types.values())[1], load_capacity, gross_capacity,
                net_capacity, holds, hold_capacity,
                container_capacity]

type_ship = "Тип судна*"
project_number = "Номер проекта"
book_value = "Балансовая стоимость, тыс. долл."
share_capital = 'Акционерный капитал учредителя, Аакi, тыс. долл.'
count_ship = "Кол-во судов данного проекта, nci"

table_text_2 = [type_ship, project_number, book_value]
table_text_3 = [project_number, book_value, count_ship, share_capital]

load_volume_f = "Удельный погрузочный объем в прямом направлении, м3/т"
load_volume_r = "Удельный погрузочный объем в обратном направлении, м3/т"

specific_cargo_capacity = "Удельная грузовместимость судна, куб. м/т"
loading_ship_f = "Норма загрузки судна: в прямом направлении, т"
loading_ship_r = "Норма загрузки судна: в обратном направлении, т"
capacity_factor_f = "Коэффициент использования грузоподъемности судна: в прямом направлении"
capacity_factor_r = "Коэффициент использования грузоподъемности судна: в обратном направлении"
speed_cargo_f = "Скорость хода с грузом: в прямом направлении, км/ч"
speed_cargo_r = "Скорость хода с грузом: в обратном направлении, км/ч"
flight_time_f = "Время рейса в прямом направлении, сут."
flight_time_r = "Время рейса в обратном  направлении, сут."
duration_turnover = "Продолжительность оборота, сут. "