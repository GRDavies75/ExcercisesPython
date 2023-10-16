"""
Due to repeated request for user input during the excercises
A simplified unified user input requestor
"""


def get_user_input(prompt='', *pre_prompts: str) -> str:
    """
    prompt is used at the input itself
    pre_prompts gives the ability for extra sring before the input
    """
    for pre_prompt in pre_prompts:
        print(pre_prompt)
    user_input = input(prompt)

    return user_input