Pessoas = []

def adicionar():
    nome = input ("Informe seu nome ")
    idade = input ("Informe sua idade ") 
    cidade = input ("Informe sua cidade ")
    Pessoa = {"Nome": nome, "Idade": idade, "Cidade": cidade}
    
    Pessoas.append(Pessoa)
    
while True:
    tem_transporte = input ("Você tem transporte? (sim/não) ")
    if tem_transporte == "sim":
        print ("Serviço indisponível")
        break
    
    elif tem_transporte == "não": 
        adicionar()
    else:
        print ("Opção inválida")
        break
    print(Pessoas)
    
    