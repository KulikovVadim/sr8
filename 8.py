def perevod_chisla(chislo, sistema):
    ost = ""
    while chislo > 0:
        ost = str(ost) + str(chislo % sistema)
        chislo = int(chislo) // sistema
    return ost[::-1]

try:
    chislo = int(input("Введите целое число, которое вы бы хотели перевести: "))
    sistema = int(input("Выберите систему счисления, в которую вы бы хотели перевести число(двоичную либо восьмеричную): "))
except ValueError:
    print("Ошибка, пожалуйста, введите целые числовые значения")
else:
    if sistema == 2 or sistema == 8:
        perevod_chisla(chislo, sistema)
        print(str(chislo) + ' -> ' + str(perevod_chisla(chislo, sistema)))
    else:
        print("Пожалуйста, выберите двоичную либо восьмиричную систему")





