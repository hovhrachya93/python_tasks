# TASK 5: Հայտարարել list, որը բաղկացած է string-ներից:
# Տպել թե քանի անգամ է յուրաքանչյուրը հանդիպում list-ում:

def countStringOccurrences(lst: list[str]) -> dict[str, int]:
    occurrences = {}
    for s in lst:
        if s in occurrences:
            occurrences[s] += 1
        else:
            occurrences[s] = 1
    return occurrences


if __name__ == "__main__":
    test_list = ["apple", "banana", "apple", "cherry", "banana"]
    print(countStringOccurrences(test_list))
