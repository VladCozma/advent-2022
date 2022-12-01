from typing import List, Dict
from collections import Counter

def read_file(filename):
    """
    Reading an input file
  
    Parameters:
    filename (str): path of file to be loaded
  
    Returns:
    list(str): a list with lines contents
    
    """
    with open(filename) as f:
        contents = f.readlines()
    return contents

def count_calories(calories: List) -> Dict:
    """
    Counts the backpack calories for every elf
  
    Parameters:
    calories (List[str]): list of items with calories. Each item is on a ne line. Elf backpack divided by new line
  
    Returns:
    Dict(int, int): a dictionary with elf number and total calories load
    
    """
    elf_backpack = 0
    elf_load = {}
    i = 0
    for list_item in calories:
        if list_item != "\n":
            elf_backpack += int(list_item)
        else:
            elf_load[i]=elf_backpack
            i+=1
            elf_backpack = 0
    elf_load[i]=elf_backpack
    return elf_load


if __name__ == "__main__":

    # day 1
    filename = "./data/day1.txt"
    calories = read_file(filename=filename)
    elf_load = count_calories(calories=calories)
    
    # Maximum load
    print(f"max load:{max(elf_load.values())}")

    k = Counter(elf_load)
    # First 3
    print(f"first 3 loads:{k.most_common(3)}")
    # Sum of first 3
    print(f"sum of first 3:{[x for x in map(sum, zip(*k.most_common(3)))][1]}")