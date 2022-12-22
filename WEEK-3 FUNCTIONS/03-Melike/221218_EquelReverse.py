""" 
2-equal_reverse.py
Write a function that controls the given inputs whether they are equal to their reversed order or not.

Example:
Input  >>> madam, tacocat, utrecht 
Output >>> True, True, False"""

def equal_reverse():
    word_list = list(map(str, input("Please input words seperated by commas: ").split(",")))       # to take more than one words or phrases (map)
    result = []
    
    for word in word_list:
        new_word = word[::-1]               # to reverse the string by slicing
        if new_word == word:
            result.append(True)             # to add the results to an empty list
        else:
            result.append(False)

    print(result)

equal_reverse()