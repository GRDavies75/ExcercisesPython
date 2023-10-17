"""
Excerise 12-74
Find the nth Fibonacci number using recursion
n and position start at 0 
"""


def give_Fibonacci(n: int) -> int|None:
    """
    Return nth Fibonacci number, for not-negative n (negative n -> None)
    
    n == 0 -> 0, n == 1 -> 1, otherwise Nx = N(x-1) + N(x-2)
    """
    # Cornercase
    if n < 0:
        return None
    
    # Basic step
    if n in {0, 1}:
        return n
    # Otherwise down the rabbit-hole we go
    else:
        return give_Fibonacci(n-1) + give_Fibonacci(n-2)



def main() -> None:
    input_data = [
        0,
        1,
        2,
        3,
        9
    ]

    for entry in input_data:
        print(give_Fibonacci(entry))


if __name__ == "__main__":
    main()
