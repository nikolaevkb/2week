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
        a = input("a = ")
        b = input("b = ")

        if s == "#":
            print(int(b) % int(a))

        elif s == '!':

            sum_one = 0
            sum_two = 0
            for letters in str(a):
                sum_one += int(letters)
            for letters in str(b):
                sum_two += int(letters)
            if sum_one > sum_two:
                print(a)
            else:
                print(b)

        elif s == "@":
            print(max(int(a), int(b)))

        elif s == "$":
            count_one = 0
            count_two = 0
            for letters in str(a):
                count_one += len(letters)
            for letters in str(b):
                count_two += len(letters)
            if count_one > count_two:
                print(a)
            else:
                print(b)

    else:
        print("Неверный знак операции!")
