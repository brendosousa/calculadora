
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

operacao = input('Digite o símbilo da operação (+ - * /): ')

def resultado(n1, n2):
    if operacao == '+':
        return n1 + n2
    elif operacao == '-':
        return n1 - n2
    elif operacao == '*':
        return n1 * n2
    elif operacao == '/':
        return n1 * n2
    else:
        return "Operação não encontrada"

print("O resultado da operação é: ", resultado(n1,n2))                    
                     