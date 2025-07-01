ano_nascimento = 1981
ano_atual = 2025
idade = ano_atual - ano_nascimento
print("Idade", idade)

num = int(input("Digite um numero inteiro"))
resultado = 10 / num
print(f"Resulatdo da divisão: {resultado}")
except zeroDivisionError:
print("Erro: Não e possivel dividir por zero.")
except ValueError:
print("Erro: digite um numero inteiro valido.")
