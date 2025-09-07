
def classify_triangle(a : float, b : float, c : float) -> str:
    """
    Classify a triangle by the lengths of its sides.

    Returns one of:
        - "Equilateral"
        - "Isosceles", "Isosceles and Right"
        - "Scalene", "Scalene and Right"
        - "Not a triangle" (invalid inputs or triangle inequality fails)
    """
    
    sides = sorted([a, b, c])
    # Check for valid triangle using triangle inequality theorem
    if sides[0] + sides[1] <= sides[2]:
        return "Not a triangle"
    # Check for equilateral
    if a == b == c:
        triangle_type = "Equilateral"
    # Check for isosceles
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"
    # Check for right triangle using Pythagoras theorem
    if round(sides[0]**2 + sides[1]**2, 5) == round(sides[2]**2, 5):
        triangle_type += " and Right"
    return triangle_type

if __name__ == "__main__":
    # Example usage
    print("Classify triangle (3, 4, 5): ", classify_triangle(3, 4, 5))  # Scalene and Right
    print("Classify triangle (2, 2, 2): ", classify_triangle(2, 2, 2))  # Equilateral
    print("Classify triangle (2, 2, 3): ", classify_triangle(2, 2, 3))  # Isosceles
    print("Classify triangle (1, 2, 3): ", classify_triangle(1, 2, 3))  # Not a triangle

    # Write welcome message to the CLI and prompt user for triangle sides
    print("Welcome to the Triangle Classifier!")
    try:
        a = float(input("Enter length of side a: "))
        b = float(input("Enter length of side b: "))
        c = float(input("Enter length of side c: "))
        result = classify_triangle(a, b, c)
        print(f"The triangle with sides {a}, {b}, and {c} is classified as: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values for the sides.")