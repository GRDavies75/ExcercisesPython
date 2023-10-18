"""
Excercise 13-78
Given 2 (positive) integers, determine their
Greatest Common Denominator
"""

def grd_gcd(a: int, b: int, current_gcd: int=1) -> int|None:
    """
    return the Greatest Common Divisor of given 2 positivie ints
    
    return None if both are 0 (one 0 is allowed), also if both < 0
    """
    # Cornercase(s)
    if (a < 0 or b < 0) or (a == 0 and b == 0):
        return None
    elif a == 0 or b == 0:
        # Read the wikipedia wrong, returned intially 0,
        # But should have been the non-zero value
        return max(a, b)
    
    # Base step
    if a == 1 or b == 1:
        return current_gcd
    # recursion part
    for i in range (2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            current_gcd *= i
            a //= i
            b //= i
            return grd_gcd(a, b, current_gcd)
    else: # for loop, not hitting any common denominator
        return current_gcd
    

# Again it looks like i produced something workable (beside the a XOR b == 0 -> max(a,b) little bug)
# But the actual solution is way shorter and more elegant/efficient (asummed perfect input)
# This is not my code!
def find_gcd(a, b):
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)

# And there is also the math library, which has math.gcd(a, b)


def main() -> None:
    input_data = [
        (48, 60),
        (60, 48),
        (0, 9),
        (9, 0),
        (42, 56),
        (3, 7),
        (6, 2),
    ]

    for entry in input_data:
        a, b = entry
        print(grd_gcd(a, b))


if __name__ == "__main__":
    main()
