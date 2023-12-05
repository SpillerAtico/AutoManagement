from table import calculations
from settings import options
from utils.enums import AttachmentsTable8


def analysis(option: int):
    ships = options.your_ships(option)
    crews = calculations.find_max_crew_expenses_ship(ships, option)

    average_ship = list(calculations.find_average_load_capacity(option).keys())[0]
    average_capacity = list(calculations.find_average_load_capacity(option).values())[0]

    minimal_ship = options.get_info_ships(option, AttachmentsTable8.load_capacity)

    anal = f"""
    По результатам расчетов можно сделать вывод, что меньшая доля расходов 
    на содержание судна приходится на судно {average_ship}.
    У {average_ship} грузоподъемность и грузовместимость не самые большие - {average_capacity},
    но больше, чем у судна {min(minimal_ship)} - {minimal_ship.get(min(minimal_ship))}.
    Судовые сборы по всем суднам примерно одинаковые. 

    Также:
    Большая доля расходов на содержание экипажа приходится на судно {max(crews)}({crews.get(max(crews))}).
    По итоговому показателю "Расходы за оборот" и по анализу всех показателей и характеристик в целом видно,
    что эффективным является судно {average_ship}.
    """

    return anal
