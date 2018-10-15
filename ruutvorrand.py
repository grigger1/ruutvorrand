# 1.Looge Githubis repro
# 2.Kopeerige repro aadressi.
# 3.Panete terminali ```git clone (aadress)```
# 4.Teete kloonitud kaustas töö ära.
# 5.Lähete terminalis sama kausta sisse.
# 6.```git add .```
# 7.```git commit -m {suvaline sõnum}```
# 8.```git push```

import math

def ruutvorrand(x1, x2, x3):   
    a = x1
    b = x2
    c = x3
    d = b * b - 4 * a * c
    if d >= 0:
        d=(math.sqrt(d))
        answer1 = ((-b + d) / (2 * a))
        answer2 = ((-b - d) / (2 * a))
        if answer1 == answer2:
            print(answer1)
        else:
            print(answer1, "ja", answer2)
    else:
        print("Ei saa teha")

ruutvorrand(1, 1, -2)
ruutvorrand(0.5, 2.5, 3)
ruutvorrand(-1, 4, -4)
ruutvorrand(1, -3.5, 3.5)