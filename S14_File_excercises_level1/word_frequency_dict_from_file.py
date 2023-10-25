"""
Excercise 14-88
Create and print a word frequency dict
Originally:
You may assume 1 word per line

But where is the fun in that?
My version of this excercise:
Google a decent sentences containing file
For simplicification a 'word' is:
    encapsulated in spaces (or beginning (^) or end ($) of line)
    only contains letters (.isalpha() == True)

frequency_dict = {str: int} (word: freq)
"""


def main() -> None:
    FILE_NAME = "sentences.txt"
    HEADER = f"Word frequency dict report for file: '{FILE_NAME}'"
    content = []
    frequency_dict = {} # {[str]word: [int]freqeuncy}

    with open(FILE_NAME, encoding='utf-8') as sentence_file:
        content = sentence_file.readlines()

    for line in content:
        words = line.split(" ")

        for word in words:
            # Skip to new iteration/next word if not only letters
            if not word.isalpha():
                continue

            word = word.casefold()
            word = word.strip("\n")
            frequency_dict[word] = frequency_dict.get(word, 0) + 1


    print(HEADER)
    for w, f in sorted(frequency_dict.items()):
        print(f"{w} - {f}")
    

if __name__ == "__main__":
    main()
