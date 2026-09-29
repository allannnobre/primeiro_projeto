nome = 'Carlos'
sobrenome = 'Oliveira'
idade = 42
ano_nascimento = 2026 - idade -1
maior_de_idade = idade >= 18
altura_metros = 1.78

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)


nome = str(input('Qual o seu nome: '))
sobrenome = str(input('Qual seu sobrenome: '))
idade = int(input('Qual a Sua idade: '))
ano_nascimento = int(input('Qual o ano do seu Nascimento: '))
maior_de_idade = idade >= 18
altura = float(input('Qual sua altura: '))

print(
    'Nome:', nome ,
    'Sobrenome:', sobrenome ,
    'idade:', idade ,
    'Você nasceu em: ', ano_nascimento ,
    'É maior de Idade: ', maior_de_idade ,
    'Você tem: de Altura', altura

)