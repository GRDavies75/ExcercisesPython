"""
Excercise 5-26
Determine the difference between 2 lists
better said print all elements of A not in B
Assume len(list A) >= len(list B)
if ListA == ListB print empty list
if list A is empty also print empty list

Update: in hindsight the excercise leaves room
for all sort of implications, probably 
good intentions with a certain lesson to be taught
On the other hand i thought way too difficult
Oh well
"""


def main() -> None:
    input_data = [
        ([1,2,3,4], [1,2]),
        ([1,2,3,4], [1,2,3]),
        ([1,2,3,4], [1,2,3,4]),
        # checking the working of Python
        # I know lists are ordered, but does checking equality
        # Does the order also matter? Probably
        # But you know for sure by experimenting
        # Update: Yes, order does matter when checking for equality
        # ([1,2,3,4], [4,3,2,1]),
        ([], [1,3]),
    ]

    for listA, listB in input_data:
        difference = []
        # Cornercases
        if not listA:
            print(difference)
            continue
        # this should also be handled by default
        # experiment concluded and also this is outside
        # the scope of the excercise
        # ---------------------------------------------
        # elif listA == listB:
        #     print("cornercase2:", [])
        #     continue

        # Default behaviour
        #
        # In hindsight i overengineered it and
        # Probably missed the mark
        # Sets do dismiss duplicates which is not asked
        #
        # My solution:
        # ---------------------------------------------- 
        # print(sorted(set(listA) - set(listB)))
        #
        # in accordance of The Zen of Python
        # Simple is better
        # (This also preserves the order of listA)
        # 
        # Maybe even the cornercase is not needed
        # (But: "Explicit is better then implicit"...Zen of Python)
        for elem in listA:
            if elem not in listB:
                difference.append(elem)
        
        print(difference)

        
if __name__ == "__main__":
    main()
