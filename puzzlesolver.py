
import random
from urllib.parse import unquote_plus

"""
Preprocess raw_input string to retrieve a seed character(where character=character in input),
and a list sorted by index of the seed.

Input: Raw_string
Output: Seed Character(r_string: str), List(of list) sorted by Seed Character (sorted_list: list)

Ex: 
    Input: "Please+solve+this+puzzle%3A%0A+ABCD%0AA---%3E%0AB%3E---%0AC---%3C%0AD---%3D%0A"
    Output: ('D', ['D---=', 'C---<', 'A--->', 'B>---'])
"""
def get_s_list(r_string):
    # Decode raw string and create string_list with initial logical relations
    r_string = unquote_plus(r_string)
    r_string = r_string[r_string.find("ABCD"):-1]
    string_list = r_string.split("\n")[1:]
    sorted_list = []
    for i in string_list:
        if "=" in i: # Record the Seed where the character == character is already given.
            position = string_list.index(i)
            seed = i[0]
    for index in range(len(string_list)):
        if string_list[index][position+1] != '-': # Sort the output list by the seed character.
            sorted_list.insert(0,string_list[index])
        else:
            sorted_list.append(string_list[index])
    return seed,sorted_list

"""
Take a Seed Character and sorted list to build a dictionary for all characters. 
Value for each character in the dictionary is generated randomly and 
must adhere to Logical Relations expressed in the sorted List

Input: Seed Character (seed: str), Sorted_list (sorted_list: list)
Output: Key,Value Dictionary where 
    Key: all possible characters(A,B,C,D) and 
    Value: Random Integers adhering to Logical Relations

Ex:
    Input: ('D', ['D---=', 'C---<', 'A--->', 'B>---'])
    Output: {'A': 4975, 'B': 5889, 'C': -909, 'D': -661}
"""
def create_relations(seed,sorted_list):
    character = "ABCD" # characters for consideration
    character_dict = {}
    character_dict[str(seed)] = random.randint(-1000,1000) # generate random value for the seed character
    for i in range(len(sorted_list)):
        for j in range(len(sorted_list[i])):
            if sorted_list[i][j] == '>': # generate random values for all other characters based on Logical Relations
                character_dict[sorted_list[i][0]] = random.randint(character_dict[character[j-1]]+1,10000)
            if sorted_list[i][j] == '<':
                character_dict[sorted_list[i][0]] = random.randint(-10000,character_dict[character[j-1]]+1)
    return character_dict
"""
Take Raw Input String and create list with Logical Relations between all characters

Input: Raw_string
Output: List(of list) where each list contains final Logical Relations amongst all characters

Ex:
    Input: "Please+solve+this+puzzle%3A%0A+ABCD%0AA---%3E%0AB%3E---%0AC---%3C%0AD---%3D%0A"
    Output: ['ABCD', 'A=<>>', 'B>=>>', 'C<<=<', 'D<<>=']
"""

def puzzle(raw_string):
    seed, sorted_list = get_s_list(raw_string) # get seed character and sorted list
    character_dict = create_relations(seed,sorted_list) # build dictionary for keys with values adhering to Logical Relations
    outlist = ["ABCD"]
    for current_key in sorted(character_dict):
        cstring = ''
        cstring += str(current_key)
        for other_key in sorted(character_dict): # For each character in the dictionary create string showing Logical Relations with other characters
            if character_dict[current_key] == character_dict[other_key]:
                cstring += '='
            elif character_dict[current_key] > character_dict[other_key]:
                cstring += '>'
            elif character_dict[current_key] < character_dict[other_key]:
                cstring += '<'
        outlist.append(cstring)
    return outlist

"""
Solves the puzzle provided in the raw_string

Input: Raw_string
Output: Final output string with Logical Relations for all characters

Ex:
    Input: "Please+solve+this+puzzle%3A%0A+ABCD%0AA---%3E%0AB%3E---%0AC---%3C%0AD---%3D%0A"
    Output: 'ABCD\nA=<>>\nB>=>>\nC<<=<\nD<<>='
    
"""
def solve_puzzle(d):
    output = puzzle(d) # Solve the puzzle and get list of list for each character with their Logical Relations
    outstring = ''
    for i in output: # Create Final string
        outstring += i+'\n'
    return outstring[:-1]