import math


def classify_triangle(a, b, c):
    """Return the triangle's side classification and right-triangle status."""

    # Check that the values are positive.
    if a <= 0 or b <= 0 or c <= 0:
        return "Not a triangle"

    # Put the side lengths in order so the largest side is last.
    sides = sorted([a, b, c])
    x, y, z = sides

    # A valid triangle must have two smaller sides that add to more
    # than the largest side.
    if x + y <= z:
        return "Not a triangle"

    # Classify by side length.
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or a == c or b == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    # Check whether x² + y² = z².
    if math.isclose(x * x + y * y, z * z):
        return triangle_type + " right triangle"

    return triangle_type


def main():
    examples = [
        (3, 3, 3),
        (4, 4, 5),
        (4, 5, 6),
        (3, 4, 5),
        (1, 2, 3),
        (0, 4, 5)
    ]

    for a, b, c in examples:
        result = classify_triangle(a, b, c)
        print(f"({a}, {b}, {c}): {result}")


if __name__ == "__main__":
    main()