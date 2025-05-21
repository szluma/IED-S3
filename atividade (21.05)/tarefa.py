usuários_cadastrados = []

while True:
    prosseguir = input ("Outro usuário deseja dizer suas informções? (Sim/Não) ")
    if prosseguir != "Sim":
        break
    
    nome = input ("Qual o seu nome? ")
    cidade = input ("Qual a sua cidade? ")
    meio_de_transporte = input ("Você utiliza algum meio de transporte? ")
    tipo_de_transporte = None
    
    if meio_de_transporte == "Sim":
        tipo_de_transporte = {
            "tipo": input ("Qual meio de transporte você utiliza? "),
            "marca": input ("Qual a marca? "),
            "conforto": input ("Seu transporte é confortável? ")
        }
    
    
    usuário_cadastrado = {
        "nome": nome,
        "cidade": cidade,
        "transporte": tipo_de_transporte
    }
    
    usuários_cadastrados.append(usuário_cadastrado)
    
    print("\n Usuários cadastrados:", nome)
    print("Cidades dos usuários:", cidade)
    print("Meios de transportes dos usuários:", tipo_de_transporte)