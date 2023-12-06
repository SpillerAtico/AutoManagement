import matplotlib.pyplot as plt
import numpy as np
from view import text_collection
from table import calculations
from settings import options


def create_diagram(ship, cost_maintaining, crew_expenses, ship_fees, fuel_costs):
    specific = [text_collection.abbrev_cost_maintaining,
                text_collection.abbrev_crew_expenses,
                text_collection.ship_fees,
                text_collection.abbrev_fuel_costs]

    data = [cost_maintaining, crew_expenses, ship_fees, fuel_costs]

    explode = (0.1, 0.0, 0.2, 0.3)

    colors = (text_collection.grey_color,
              text_collection.grey_color,
              text_collection.grey_color,
              text_collection.grey_color)

    # Wedge properties
    wp = {'linewidth': 1, 'edgecolor': text_collection.grey_color}

    def func(pct, allvalues):
        absolute = int(pct / 100. * np.sum(allvalues))
        return "{:.1f}%\n({:d} долл)".format(pct, absolute)

    fig, ax = plt.subplots(figsize=(8, 3))
    wedges, texts, autotexts = ax.pie(data,
                                      autopct=lambda pct: func(pct, data),
                                      explode=explode,
                                      labels=specific,
                                      shadow=True,
                                      colors=colors,
                                      startangle=90,
                                      wedgeprops=wp,
                                      textprops=dict(color="magenta"))

    ax.legend(wedges,
              specific,
              title=text_collection.specifications,
              loc=text_collection.location,
              bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight=text_collection.weight)
    ax.set_title(ship)

    plt.show()
    return


def get_diagrams(option: int):
    ship = options.your_ships(option)
    cost_maintaining = list(calculations.summa_cost_maintaining(option).values())
    crew_expenses = list(calculations.summa_crew_expenses(option).values())
    ship_fees = list(calculations.find_ship_fees(option)[0].values())
    fuel_costs = list(calculations.find_fuel_costs(option)[0].values())

    for i in range(3):
        print(create_diagram(ship[i], cost_maintaining[i], crew_expenses[i], ship_fees[i], fuel_costs[i]))
    return ''
