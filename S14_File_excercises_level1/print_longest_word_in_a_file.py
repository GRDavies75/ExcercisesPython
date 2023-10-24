"""
Excercise 14-87
Find and print the longest word in a file
Originally:
You may assume 1 word per line

But where is the fun in that?
My version of this excercise:
Google a decent sentences containing file
For simplicification a 'word' is:
    encapsulated in spaces (or beginning (^) or end ($) of line)
    only contains letters (.isalpha() == True)

print:
line number
position (index of word, base-1 instead of base-0)
word length
the word itself
(In case of a tie, print the first word, but also print the number of ties)
"""


def print_report(ln: int, pos: int, wl: int, wrd: str, numt: int=0) -> None:
    """
    print a report containing:

    line_number, position, word_length, word, number_of_ties (if any)
    """
    report = [
        f"{('(First instance) l' if numt else 'L')}inenumber: {ln}",
        f"Position: {pos}",
        f"Word length: {wl}",
        f"{('(First) w' if numt else 'W')}ord: {wrd}",
        f"There were {numt} ties for biggest word length",
    ]
    report_string = '\n'.join(report if numt > 0 else report[:-1])

    print(report_string)


def main() -> None:
    FILE_NAME = "sentences.txt"
    HEADER = f"Longest word report for file: '{FILE_NAME}'"
    content = []
    max_word_length = 0
    biggest_word = ""
    line_number = None
    position = None
    ties_dict = {0: 0} # in case of a file only containing non-exclusive letterwords

    with open(FILE_NAME, encoding='utf-8') as sentence_file:
        content = sentence_file.readlines()

    for ln, line in enumerate(content, 1):
        words = line.split(" ")

        for pos, word in enumerate(words, 1):
            # Skip to new iteration/next word if not only letters
            if not word.isalpha():
                continue

            word_length = len(word)
            if word_length > max_word_length:
                max_word_length = word_length
                biggest_word = word
                position = pos
                line_number = ln
                # For efficiency purposes, always make a dict entry (for 0 value)
                ties_dict[word_length] = ties_dict.get(word_length, 0)
            elif word_length == max_word_length:
                ties_dict[word_length] += 1

    print(HEADER)
    print_report(line_number, position, max_word_length, biggest_word, ties_dict[max_word_length])


if __name__ == "__main__":
    main()
