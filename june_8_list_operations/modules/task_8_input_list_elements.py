# Task 8: Գրել ծրագիր, որը օգտվողին թույլ կտա մուտքագրել ամբողջ թիվ:
# Հայտարարել դատարկ list, որից հետո list-ի մեջ ավելացնել ստացած ամբողջ
# թվի քանակությամբ էլեմենտներ, որոնք նույնպես պետք է մուտքագրվի օգտվողի
# կողմից: Մուտքագրման պահին ստուգել, որ մուտքագրվածը լինի int տիպի:
# Տպել արդյունքը էկրանին:
from typing import List


def input_list_elements() -> List[int]:
    while True:
        try:
            num_elements = int(input('Enter number of elements: '))
            if num_elements < 0:
                print("Number of elements cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    elements = []

    for i in range(num_elements):
        while True:
            try:
                element = int(input(f'Enter element {i + 1}: '))
                elements.append(element)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    return elements


if __name__ == '__main__':
    result_list = input_list_elements()
    print('List of entered elements:', result_list)
