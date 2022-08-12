print("Olá você está no notaspocotom, seja bem vindo!")

soma = 0
for n in range(1, 5):
    nota = int(input(f"Digite as notas do {n}° aluno: "))
    soma = nota + soma

if(n == 4):
    media = soma / 4

print(media)
