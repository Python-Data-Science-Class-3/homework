
text=input("Bir  text  giriniz:")

d = dict()


for x in text:

    x = x.strip()

    x = x.lower()

    words = x.split(" ")

    for kelime in words:
        if kelime in d:
            d[kelime] = d[kelime] + 1
        else:
            d[kelime] = 1
for key in list(d.keys()):
    print(["".join(str(key)),"".join(str(d[key]))],end=" ,")


   