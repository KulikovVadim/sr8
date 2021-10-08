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
    if chislo == 0:
        print("0 в любой системе счисления 0")
        quit()
    if sistema == 2 and (chislo <= 0 or chislo >= 256):
        print("Пожалуйста, задайте число от 0 до 255")
        quit()
    elif sistema == 8 or sistema == 2:
        perevod_chisla(chislo, sistema)
        print(str(chislo) + ' -> ' + str(perevod_chisla(chislo, sistema)))
    else:
        print("Пожалуйста, выберите двоичную либо восьмиричную систему")




