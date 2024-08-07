# TASK 2: Հայտարարել list, որը բաղկացած է string-ներից:
# List-ում եղած բոլոր string-ների առաջին տառը դարձնել մեծատառ:
# Տպել յուրաքանչյուրի առաջին տառը:

def capitalizeFirstLetters(lst: list[str]) -> list[str]:
    return [s.capitalize() for s in lst]


if __name__ == "__main__":
    test_list = ["tom", "jane", "ann"]
    print(capitalizeFirstLetters(test_list))
