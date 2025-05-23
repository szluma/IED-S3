usuarios_cadastrados = []

while True:

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
    
    usuario_cadastrado = {
        "nome": nome,
        "cidade": cidade,
        "transporte": tipo_de_transporte
    }
    
    usuarios_cadastrados.append(usuario_cadastrado)
    
    prosseguir = input ("Outro usuário deseja dizer suas informções? (Sim/Não) ")
    if prosseguir != "Sim":
        break
    
    print("\n Usuários cadastrados:")
    for i, usuario_cadastrado in enumerate(usuarios_cadastrados):
        print(f"nome:{usuario_cadastrado['nome']}")
        print(f"cidade:{usuario_cadastrado['cidade']}")
    
    for usuario_cadastrado in usuarios_cadastrados:
        print (usuarios_cadastrados)