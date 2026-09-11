import math


def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Not a triangle"

    sides = sorted([a, b, c])
    x, y, z = sides

    if x + y <= z:
        return "Not a triangle"

    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or a == c or b == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

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