from func_math import MathFunc

def main():
    while True:
        print("\n1. Somar\n2. Subtrair\n3. Multiplicar\n4. Dividir\n5.Porcento\n")
        try:
            funcSelect = int(input("Olá. Selecione qual função você quer: "))
            match funcSelect:
                case 1:
                    newFunc = MathFunc.sum
                    break
                case 2:
                    newFunc = MathFunc.minus
                    break
                case 3:
                    newFunc = MathFunc.multiply
                    break
                case 4:
                    newFunc = MathFunc.division
                    break
                case 5:
                    newFunc = MathFunc.percent
                    break
                case _:
                    print("Ops...parece que você não selecionou uma opção válida. Tente novamente\n")

        except ValueError:
            print("ops...")

    firstValue = int(input("Agora selecione um primeiro valor: "))
    while True:
        try:
            secondValue = int(input("E um segundo valor: "))
            if secondValue != 0:
                break
            else:
                print("Não é possível dividir um número por zero, tente novamente.\n")
        except ZeroDivisionError:
            print("Não é possível dividir um número por zero, tente novamente.")

    print(f"\nO resultado é: {newFunc(firstValue, secondValue)}")

main()
