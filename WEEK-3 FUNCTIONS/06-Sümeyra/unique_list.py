#Write a function that filters all the unique(unrepeated) elements of a given list.
#Example:
#Function call: unique_list([1,2,3,3,3,3,4,5,5])
#Output : [1, 2, 3, 4, 5]

'''
Program calisiyor, algoritma gayet iyi olmus.
Birkac girdi yaptim ara satirda, onlara dikkat edip
bakarsaniz iyi olur.
'''


letters = ["a","a","b","c","c","d","f","e","e","g","h","h","j"] 
'''
Herhangi bir fonksiyon icinde olusturulan degisken 'local variable' olarak adlandirilir,
fonksiyon disindaki variable'lar ise 'global variable' olarak adlandiriyoruz. 
letters, burada global variable olarak ataniyor.
ama daha sonra fonksiyon icinde de ayni isimde baska bir degisken ataniyor,
o da local variable oluyor. Karisiklik olmamasi adina farkli isimlerde variable atanmasi daha uygun olur.

Dongu kullanmadan set() ile de unique elemanlari bulabiliriz. 
Once set() ile liste elemanlari tekrardan kurtulur, sonra sorted() ile liste halinde sirali dondurulebilir.
En altta alternatif bir cozum sundum, inceleyebilirsiniz.
'''
def unrepeated(letters):
    unrepeated_list = []
    s = set(letters)

    for letter in s:
        unrepeated_list.append(letter)
    return sorted(unrepeated_list)  # added sort() for alphabetical order

print(unrepeated(letters))


'''

letters = ["a","z","b","c","c","d","f","e","e","g","h","h","j"]

def unrepeated(first_list):
    last_list = sorted(set(first_list))
    return last_list

print(unrepeated(letters))

'''