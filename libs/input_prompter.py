"""
Due to repeated request for user input during the excercises
A simplified unified user input requestor / prompter
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