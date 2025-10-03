import pytest
from class_exercises_.tdd.quadratic_solver import solve_quad

normal_data = [(1, 5, 6, (-2, -3)),
               (2, -7, -15, (5, -1.5)),
               (4, 9, -2, (0.204, -2.454)),
               (-2, 1, 6, (-1.5, 2)),
               (2.5, 5, 1, (-0.225, -1.775))
               ]

edge_data = [(1, 4, 4, -2),
             (4, 12, 9, -1.5),
             ]

erroneous_value_data = [(1, 1, 2),
                        (4, -5, 5),
                        ]

erroneous_type_data = [(4, 2, 'hi'),
                       (5, '!', 6),
                       ]

@pytest.mark.parametrize("a, b, c, result", normal_data)
def test_normal_data(a, b, c, result):
    assert solve_quad(a, b, c) == result

@pytest.mark.parametrize("a, b, c, result", edge_data)
def test_edge_data(a, b, c, result):
    assert solve_quad(a, b, c) == result

@pytest.mark.parametrize("a, b, c", erroneous_value_data)
def test_edge_data(a, b, c):
    assert solve_quad(a, b, c) is ValueError

@pytest.mark.parametrize("a, b, c", erroneous_type_data)
def test_edge_data(a, b, c):
    assert solve_quad(a, b, c) is TypeError