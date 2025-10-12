array = ['I', 'II', "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
num = int(input())

if num <= 10 and num >= 1:
    print(array[num - 1])
else:
    print("ошибка")