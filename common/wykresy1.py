# import matplotlib.pyplot as plt
#
# x = [1,2,3,4,5]
# y = [10,15,13,17,20]
#
# # Wykres liniowy
#
# # plt.plot(
# #     x,
# #     y,
# #     color="red",
# #     linewidth=3,
# #     marker="o",
# #     markersize=10,
# #     linestyle="-.",
# # )
# # plt.title("Wykres liniowy")
# # plt.xlabel("Numer dnia")
# # plt.ylabel("Wartość sprzedaży")
# # plt.grid(True)
# # plt.show()
#
#
# oceny = [2,2,5,5,4,3,2,5,4,3]
#
# plt.hist(oceny, bins=4)
# plt.title("Histogram ocen")
# plt.xlabel("Ocena")
# plt.ylabel("Liczba wystąpień")
#
# plt.ylim([0,100])
#
# plt.show()
import matplotlib.pyplot as plt

dni = ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Nd"]
sprzedaz = [120, 150, 180, 160, 170, 210, 190]

plt.plot(dni, sprzedaz, marker='o')

plt.title("Sprzedaż w tygodniu")
plt.xlabel("Dni tygodnia")
plt.ylabel("Sprzedaż")

plt.show()

import matplotlib.pyplot as plt

produkty = ["Laptop", "Tablet", "Telefon", "Monitor"]
sprzedaz = [25, 18, 40, 12]

plt.bar(produkty, sprzedaz)

plt.title("Sprzedaż produktów")
plt.xlabel("Produkty")
plt.ylabel("Liczba sprzedanych sztuk")

plt.show()

import matplotlib.pyplot as plt

wyniki = [45, 50, 52, 48, 60, 70, 65, 55, 58, 62, 75, 80, 78, 85, 90]

plt.hist(wyniki, bins=5)

plt.title("Rozkład wyników testu")
plt.xlabel("Wynik")
plt.ylabel("Liczba studentów")

plt.show()