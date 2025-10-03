import math
import pytest

def solve_quad(a, b, c):

    if not (isinstance(a, int) or isinstance(a, float)) or not (isinstance(b, int) or isinstance(b, float)) or not (isinstance(c, int) or isinstance(c, float)):
        return TypeError

    discriminant = (b ** 2) - (4 * a * c)

    if discriminant < 0:
        return ValueError

    elif discriminant == 0:
        solution_1 = (-b + math.sqrt(discriminant)) / (2 * a)
        solution_1 = round(solution_1, 3)
        return solution_1

    elif discriminant > 0:
        solution_1 = (-b + math.sqrt(discriminant)) / (2 * a)
        solution_1 = round(solution_1, 3)
        solution_2 = (-b - math.sqrt(discriminant)) / (2 * a)
        solution_2 = round(solution_2, 3)
        return solution_1, solution_2
