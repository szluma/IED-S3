nome = [] # array []
cidade = {} # objeto {}
meio_de_transporte = {} # dicionário com as informações

nomes = input("Informe seu nome:")

cidades = input("Qual a sua cidade?:")

uso_transporte = input ("Você utiliza algum meio de transporte? (Sim/Não)")

if uso_transporte == "Sim":
    uso_transporte = input ("Qual meio de transporte você utiliza?")
    uso_transporte = input ("Ele é confortável?")
    uso_transporte = input ("O transporte utilizado é posse sua?")
    meio_de_transporte[nomes] = {
        'meio_transporte': meio_transporte,
        'conforto': conforto,
        'posse': posse
    }
else:
    meio_de_transporte[nome] = print ("Não uso meios de transportes")

nome.append(nomes)
cidades[nome] = cidade

print ("\n Informações do usuário")
print ("Nomes dos usuários:", nome)
print ("Cidades dos usuários:", cidade)
print ("Utilização de transporte:")

for nomes in nome:
    print (f"{nomes}: {meio_de_transporte[nomes]}")

 # Armazenando as informações de transporte no dicionário
    meio_de_transporte[nomes] = {
        'meio_transporte': meio_transporte,
        'conforto': conforto,
        'posse': posse
    }
    
