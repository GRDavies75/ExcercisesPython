"""
A module for input related code
for consistency and related motives
"""


def get_user_input(prompt: str='', *pre_prompts: str) -> str:
    """
    prompt is for at the input itself

    pre_prompts gives the ability for extra strings before the input
    
    (can be loose strings or a list of strings)
    """
    for pre_prompt in pre_prompts:
        if isinstance(pre_prompt, list):
            for inner_elem in pre_prompt:
                print(inner_elem)
        else:
            print(pre_prompt)
    user_input = input(prompt)

    return user_input


def sanetize_input_to_numerical_value(input: str) -> int|float|None:
    """
    apparently input is interpreted char by char

    and a . isnt a float so float(input) doesn't work

    return None if input not been able to convert to int or float

    TODO: integrate locale, now this works only for American numberformat
    """
    # Cornercase - users can be unpredictable
    if input[-1] == '.':
        input = input + '0'
    # (Potential) float
    if input.count(".") == 1:
        parts = input.split(".")
        whole = parts[0]
        fraction = parts[1]

        if whole.isdigit() and fraction.isdigit():
            return int(whole) + float(int(fraction) / 10 ** len(fraction))
        
        return None

    # (Potential) integer 
    if input.isdigit():
        return int(input)
    
    # apparently not a numerical value
    return None
