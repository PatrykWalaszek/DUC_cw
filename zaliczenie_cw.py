# -*- coding: utf-8 -*-
"""zaliczenie_cw.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qf3zokLJsFfd5ghDnBqfwbkKfveYZg6b
"""

import math

"""Zadania z cwiczen DUC 2021 (online)

Z1 - Obliczanie prawdopodobieństwa wprowadzenia do użytkowania niezdatnego UC
Oblicz prawdopodobieństwo Pn, że wyprodukowane urządzenie, złożone z **N=200** sztuk układów cyfrowych (o identycznych parametrach niezawodnościowych) będzie niezdatne, jeżeli uzysk podczas produkcji wynosi **90%**  ,a testy produkcyjne wykrywają **95% błędów**. Do obliczeń przyjąć **lambda**=4.

![1.png](data:image/png;base64,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)

**Dane:**
"""

U=0.90;
p=0.95;
l = 4;
N=200;
P=((1-p)*(1-U)*math.exp((l-1)*(-p)))/(U+ (1-p)*(1-U)*math.exp((l-1)*(-p)));
PN=1-((1-P)**N)

print("P= "+"{:.4e}".format(P))
print("P"+str(N)+"= "+"{:.4}".format(PN*100)+"%")