n = int(input("Введіть розмір масиву: "))
arr = []

for i in range(n):
    a = int(input(f"введіть {i+1}-й елемент масиву: "))
    arr.append(a)

sum = 0

for a in arr:
    if a > 0 and a % 3 == 0:
        sum += a

print("Сума додатніх елементів масиву, кратних трьом:", sum)