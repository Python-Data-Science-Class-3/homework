

list_1 = [1,2,3,4,5]
print("Original list:", list_1)
# Set the number of splits
n_adım = int(input("Bir sayı giriniz:"))

list_1 = (list_1[len(list_1) - n_adım:len(list_1)] + list_1[0:len(list_1) - n_adım])
print("Rotated list:", list_1)


