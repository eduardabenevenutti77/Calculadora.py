def calculate():
    operation = input('''
Informe o tipo da operação:
+ = adição
- = subtração
* = multiplicação
/ = divisão
''')

    num1 = int(input('\nInforme o 1º valor: '))
    num2 = int(input('Informe 0 2º valor: '))

    if operation == '+':
        print('{} + {} = {}'.format(num1, num2))
        print(num1 + num2)

    elif operation == '-':
        print('{} - {} = '.format(num1, num2))
        print(num1 - num2)

    elif operation == '*':
        print('{} * {} = '.format(num1, num2))
        print(num1 * num2)

    elif operation == '/':
        print('{} / {} = '.format(num1, num2))
        print(num1 / num2)

    else:
        print('\n O operador informado é inválido! Por favor, insira o tipo da operação novamente..')

    again()

def again():
    calc_again = input('''
Quer continuar calculando?
Coloque S(sim) ou N(não).
''').upper()

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('Até a próxima vez!')
    else:
        again()

calculate()