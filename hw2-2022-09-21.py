print("Выберите один из следующих знаков и введите данные:"
      "\n# - возвращает остаток от деления второго числа на первое;"
      "\n! - возвращает число, у которого сумма цифр больше;"
      "\n@ - возвращает большее число из двух;"
      "\n$ - возвращает число, у которого больше цифр."
      "\nDEL в качестве знака операции завершит работу программы")
while True:
    s = input("Знак (#,!,@,$): ")
    if s == "DEL":
        break
    if s in ('#', '!', '@', '$'):
        a = int(input("a = "))
        b = int(input("b = "))
        if s == "#":
            print(b % a)

        elif s == '!':

            num1 = a
            num2 = b
            sum1 = 0
            sum2 = 0
            while (num1 != 0, num2 != 0):
                sum1 = sum1 + num1 % 10
                num1 = num1 // 10
                sum2 = sum2 + num2 % 10
                num2 = num2 // 10

                print(max(sum1, sum2))

        elif s == "@":
            print(max(a, b))

        elif s == "$":
            print(max(str(a), str(b)))

    else:
        print("Неверный знак операции!")
