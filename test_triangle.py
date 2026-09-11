from triangle import classify_triangle


def test_equilateral_triangle():
    assert classify_triangle(3, 3, 3) == "Equilateral"


def test_isosceles_triangle():
    assert classify_triangle(4, 4, 5) == "Isosceles"


def test_scalene_triangle():
    assert classify_triangle(4, 5, 6) == "Scalene"


def test_scalene_right_triangle():
    assert classify_triangle(3, 4, 5) == "Scalene right triangle"


def test_right_triangle_in_different_order():
    assert classify_triangle(5, 3, 4) == "Scalene right triangle"


def test_isosceles_right_triangle():
    assert classify_triangle(1, 1, 2 ** 0.5) == "Isosceles right triangle"


def test_invalid_triangle_equal_to_longest_side():
    assert classify_triangle(1, 2, 3) == "Not a triangle"


def test_invalid_triangle_negative_side():
    assert classify_triangle(-3, 4, 5) == "Not a triangle"


def test_invalid_triangle_zero_side():
    assert classify_triangle(0, 4, 5) == "Not a triangle"


def test_invalid_triangle_too_short():
    assert classify_triangle(1, 1, 3) == "Not a triangle"