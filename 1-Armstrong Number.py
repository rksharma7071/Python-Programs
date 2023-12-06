digit = input("Enter Number: ")
n = len(digit)
sum = 0

for i in digit:
    sum = sum + int(i) ** n


if sum == int(digit):
    print(f'{digit} is armstrong number')
else:
    print(f'{digit} is not armstrong number')