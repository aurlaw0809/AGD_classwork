import pytest
from class_exercises_.tdd.grade_boundaries import calc_grade


test_data = [(0, "U"),
             (72, "E"),
             (111, "D"),
             (150, "C"),
             (189, "B"),
             (229, "A"),
             (264, "A*"),
             ]

test_data2 = [(71, "U"),
             (110, "E"),
             (149, "D"),
             (188, "C"),
             (228, "B"),
             (263, "A"),
             (350, "A*"),
             ]

@pytest.mark.parametrize("score, grade", test_data)
def test_min_grade_boundaries(score, grade):
    assert calc_grade(score) == grade

@pytest.mark.parametrize("score, grade", test_data2)
def test_max_grade_boundaries(score, grade):
    assert calc_grade(score) == grade

def test_grade_boundaries_normal():
    assert calc_grade(259) == "A"
    assert calc_grade(188) == "C"

#def test_grade_boundaries_erroneous():
 #   assert calc_grade(5000) is None
  #  assert calc_grade(3.5) is None
   # assert calc_grade("howdy") is None
    #assert calc_grade(-5) is None

def test_calc_grade_invalid():
    with pytest.raises(ValueError):
        calc_grade(400)
    with pytest.raises(ValueError):
        calc_grade(20)
    with pytest.raises(TypeError):
        calc_grade("A")