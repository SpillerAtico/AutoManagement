import matplotlib.pyplot as plt
import numpy as np
from view import text_collection
from general_provisions.table import calculations_table
from general_provisions import options


def diagramma(ship, cost_maintaining, crew_expenses, ship_fees, fuel_costs):
    cars = ['Затраты судно без учета стоимости топлива', 'Расходы содержания экипажа', 'Cудовые сборы',
            'Расходы на топливо']

    data = [cost_maintaining, crew_expenses, ship_fees, fuel_costs]

    explode = (0.1, 0.0, 0.2, 0.3)

    colors = ("orange", "cyan", "brown",
              "grey", "indigo", "beige")

    # Wedge properties
    wp = {'linewidth': 1, 'edgecolor': "green"}

    def func(pct, allvalues):
        absolute = int(pct / 100. * np.sum(allvalues))
        return "{:.1f}%\n({:d} долл)".format(pct, absolute)

    fig, ax = plt.subplots(figsize=(8, 3))
    wedges, texts, autotexts = ax.pie(data,
                                      autopct=lambda pct: func(pct, data),
                                      explode=explode,
                                      labels=cars,
                                      shadow=True,
                                      colors=colors,
                                      startangle=90,
                                      wedgeprops=wp,
                                      textprops=dict(color="magenta"))

    ax.legend(wedges, cars,
              title=text_collection.specifications,
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")
    ax.set_title(ship)

    # show plot
    plt.show()
    return ''


def get_diagrams(option: int):
    ship = options.your_ships(option)
    cost_maintaining = list(calculations_table.summa_cost_maintaining(option).values())
    crew_expenses = list(calculations_table.summa_crew_expenses(option).values())
    ship_fees = list(calculations_table.find_ship_fees(option)[0].values())
    fuel_costs = list(calculations_table.find_fuel_costs(option)[0].values())

    for i in range(3):
        print(diagramma(ship[i], cost_maintaining[i], crew_expenses[i], ship_fees[i], fuel_costs[i]))
    return ''
