"""
Excercise 9-54
Given are quadratic equations (ax**2 + bx + c = 0)
https://en.wikipedia.org/wiki/Quadratic_equation

To solve such equations:
x = (-b + root(b**2 - 4ac))/2a or x = (-b - root(b**2 - 4ac))/2a
Note: the 'b**2 - 4ac' part is called the Discriminant

Solutions are/have:
2 solutions, print the negative one first
1 solution, Dicrimant == 0, print x
'no solution' aka Discriminant < 0 and solves only when making use
of i (imaginary numbers) because of rooting negative numbers

Personal note: 
I'm a numberphile, but not a mathematician persé
Where or when to use quadratic equations?
- If given a finite amount of Materials (square foot/cm/whatever, x in the same measurement)
    and given known desired Ratio (length (x) vs width (?x))
    determine x => Rx**2 + 0x <= M, normalized to Rx**2 - M = 0 (a = R, b = 0, c = -M)
- For all the scholars, know the solution(s) and you know where the graph 
    of the quadratic equation intersects the x-as (aka y == 0) 
    if any, in case of the Discrimant < 0

Enough theory, back to the excercise
"""


def determine_discriminant(a: float, b: float, c: float) -> float:
    """
    a, b, c as in a (normalized) quadratic equation:
    
    a * x**2 + b * x + c == 0
    
    The Discrimant is a part for solving for x

    See also https://en.wikipedia.org/wiki/Quadratic_equation
    """
    return b**2 - 4 * a * c


def solve_qe_for_not_negative_discriminant(a: float, b: float, d: float) -> tuple[float,...]:
    """
    Given a (normalized) quadratic equation a * x**2 + b * x + c == 0

    And an already determined discriminant (b**2 - 4 * a * c)
    
    x = (-b plus/minus root(Discrimant))/(2*a)

    (c is omitted because not needed anymore because of known discriminant)

    2 x's if the Discriminant > 0

    1 x if Discriminant == 0

    (3rd scenario, Discriminant < 0 makes of of i, imaginary numbers, is omitted,
    don't feed a negative d!)
    """
    if d == 0:
        the_answer = -b / (2 * a)

        return (the_answer)
    elif d > 0:
        rooted_discriminant = d ** 0.5 
        minus_answer = (-b - rooted_discriminant) / (2 * a)
        positive_answer = (-b + rooted_discriminant) / (2 * a)

        return (minus_answer, positive_answer)
    else: # doo-doo in, doo-doo out, if you break it, you buy it
        raise TypeError("We don't need no negative Discriminants")


def main() -> None:
    # a, b, c
    input_data = [
        (1, 2, 1),
        (2, 5, -3),
        (3, 4, 5),
    ]

    for entry in input_data:
        a, b, c = entry
        discriminant = determine_discriminant(a, b, c)

        # Cornercase
        if discriminant < 0:
            print("Complex Roots")
            continue

        print(solve_qe_for_not_negative_discriminant(a, b, discriminant))


if __name__ == "__main__":
    main()
