#Authors: Nikoo Sabzevar, Sara Ghandehari

from numpy.random import uniform

def find_pi(n):
    """
    find_pi(n) calculates pi number with Monte-Carlo simulation.
    :param n: number of Monte-Carlo runs
    :return: pi number
    """
    inside_count = 0
    for i in range(n):
        x = uniform(0, 1)
        y = uniform(0, 1)
        radious = 1 - x ** 2 - y ** 2
        if radious >= 0 and radious <= 1:
            inside_count += 1
    return round(4 * (inside_count / n), 3)


monte_carlo_runs = 1000
print("The Calculated Pi number with " + str(monte_carlo_runs) +
      " Monte Carlo runs is: " + str(round(find_pi(monte_carlo_runs), 2)))
