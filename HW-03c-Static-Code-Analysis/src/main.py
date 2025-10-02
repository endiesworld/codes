"""
Module for triangle classification and CLI interaction.
"""

def classify_triangle(side_a: float, side_b: float, side_c: float) -> str:
    """
    Classify a triangle by the lengths of its sides.

    Returns one of:
        - "Equilateral"
        - "Isosceles", "Isosceles and Right"
        - "Scalene", "Scalene and Right"
        - "Not a triangle" (invalid inputs or triangle inequality fails)
    """
    sides = sorted([side_a, side_b, side_c])
    # Check for valid triangle using triangle inequality theorem
    if sides[0] + sides[1] <= sides[2]:
        return "Not a triangle"
    # Check for equilateral
    if side_a == side_b == side_c:
        triangle_type = "Equilateral"
    # Check for isosceles
    elif side_a == side_b or side_b == side_c or side_a == side_c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"
    # Check for right triangle using Pythagoras theorem
    if round(sides[0]**2 + sides[1]**2, 5) == round(sides[2]**2, 5):
        triangle_type += " and Right"
    return triangle_type

def main():
    """
    Command-line interface for triangle classification.
    """
    print("Welcome to the Triangle Classifier!")
    try:
        side_a = float(input("Enter length of side a: "))
        side_b = float(input("Enter length of side b: "))
        side_c = float(input("Enter length of side c: "))
        classification_result = classify_triangle(side_a, side_b, side_c)
        print(f"The triangle with sides {side_a}, {side_b}, and {side_c} is classified as: {classification_result}")
    except ValueError:
        print("Invalid input. Please enter numeric values for the sides.")

if __name__ == "__main__":
    # Example usage
    print("Classify triangle (3, 4, 5): ", classify_triangle(3, 4, 5))  # Scalene and Right
    print("Classify triangle (2, 2, 2): ", classify_triangle(2, 2, 2))  # Equilateral
    print("Classify triangle (2, 2, 3): ", classify_triangle(2, 2, 3))  # Isosceles
    print("Classify triangle (1, 2, 3): ", classify_triangle(1, 2, 3))  # Not a triangle

    main()