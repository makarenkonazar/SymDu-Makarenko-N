t = str(input("Введіть слово: "))

ascii_sum = 0

for i in range(len(t)):
    ascii_sum += ord(t[i])

print("Сума ASCII-кодів символів у слові ", t, " дорівнює", ascii_sum)