criancas = []

while True:
    print("\n===> Menu Prontuário digital Pediátrico <===")
    print("1. Cadastrar criança")
    print("2. Exibir crianças")
    print("3. Buscar criança")
    print("4. Cuidados com a Criança")
    print("5. Sair do programa")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        crianca = {}
        crianca['nome'] = input("Nome da criança: ")
        crianca['data_nascimento'] = input("Data de Nascimento (DD/MM/AAAA): ")
        crianca['genero'] = input("Gênero: ")
        crianca['pais_responsaveis'] = input("Nome dos pais/responsáveis: ")
        crianca['endereco'] = input("Endereço: ")
        crianca['telefone_contato'] = input("Telefone de Contato: ")

        historico_medico = input("A criança possui algum histórico médico relevante? (S/N): ").upper()
        if historico_medico == "S":
            print("\n===> Histórico Médico da Criança <===")
            crianca['historico_medico'] = {}
            crianca['historico_medico']['doencas_antigas'] = input("Informe se a criança teve alguma doença anteriormente e os tratamentos realizados: ")
            crianca['historico_medico']['alergias'] = input("Informe se a criança possui alguma alergia conhecida: ")
            crianca['historico_medico']['medicamentos_atuais'] = input("Informe os medicamentos atuais da criança (se houver): ")
            crianca['historico_medico']['cirurgias_anteriores'] = input("Informe se a criança passou por alguma cirurgia anteriormente (se houver): ")
        else:
            crianca['historico_medico'] = None
            print("Nenhum histórico médico relevante registrado para a criança.")

        consultas_anteriores = input("A criança possui exames anteriores? (S/N): ").upper()
        if consultas_anteriores == "S":
            crianca['consultas_exames'] = {}
            crianca['consultas_exames']['ultima_consulta'] = input("Data da Última Consulta (DD/MM/AAAA): ")
        else:
            crianca['consultas_exames'] = None

        crianca['vacinas'] = input("Informe as vacinas já tomadas pela criança: ")
        crianca['habitos_alimentares'] = input("Descreva os hábitos alimentares da criança: ")

        criancas.append(crianca)
        print("\nCriança cadastrada com sucesso!")

    elif opcao == "2":
        print("\nExibindo dados das crianças:")
        for crianca in criancas:
            print("\nNome:", crianca['nome'])
            print("Data de Nascimento:", crianca['data_nascimento'])
            print("Gênero:", crianca['genero'])
            print("Pais/Responsáveis:", crianca['pais_responsaveis'])
            print("Endereço:", crianca['endereco'])
            print("Telefone de Contato:", crianca['telefone_contato'])

            if crianca['historico_medico'] is not None:
                print("\nHistórico Médico:")
                print("Doenças Anteriores e Tratamentos:", crianca['historico_medico']['doencas_antigas'])
                print("Alergias Conhecidas:", crianca['historico_medico']['alergias'])
                print("Medicamentos Atuais:", crianca['historico_medico']['medicamentos_atuais'])
                print("Cirurgias Anteriores:", crianca['historico_medico']['cirurgias_anteriores'])

            if crianca['consultas_exames'] is not None:
                print("\nConsultas e Exames:")
                print("Última Consulta:", crianca['consultas_exames']['ultima_consulta'])

            print("\nVacinas Tomadas:", crianca['vacinas'])
            print("Hábitos Alimentares:", crianca['habitos_alimentares'])

    elif opcao == "3":
        nome_crianca = input("Digite o nome da criança a ser buscada: ")
        encontrada = False
        for crianca in criancas:
            if nome_crianca.lower() in crianca['nome'].lower():
                encontrada = True
                print("\nCriança encontrada. Exibindo informações:")
                print("\nNome:", crianca['nome'])
                print("Data de Nascimento:", crianca['data_nascimento'])
                print("Gênero:", crianca['genero'])
                print("Pais/Responsáveis:", crianca['pais_responsaveis'])
                print("Endereço:", crianca['endereco'])
                print("Telefone de Contato:", crianca['telefone_contato'])

                if crianca['historico_medico'] is not None:
                    print("\nHistórico Médico:")
                    print("Doenças Anteriores e Tratamentos:", crianca['historico_medico']['doencas_antigas'])
                    print("Alergias Conhecidas:", crianca['historico_medico']['alergias'])
                    print("Medicamentos Atuais:", crianca['historico_medico']['medicamentos_atuais'])
                    print("Cirurgias Anteriores:", crianca['historico_medico']['cirurgias_anteriores'])

                if crianca['consultas_exames'] is not None:
                    print("\nConsultas e Exames:")
                    print("Última Consulta:", crianca['consultas_exames']['ultima_consulta'])

                print("\nVacinas Tomadas:", crianca['vacinas'])
                print("Hábitos Alimentares:", crianca['habitos_alimentares'])
                break

        if not encontrada:
            print("Criança não encontrada.")

    elif opcao == "4":
        # Exibindo informações sobre Cuidados com a Criança
        print("\n===> Cuidados com a Criança <===")
        print("\nAlimentação Saudável:")
        print("Ofereça uma variedade de alimentos nutritivos, incluindo frutas, vegetais, proteínas magras e grãos integrais.")
        print("Evite alimentos ricos em açúcar e gorduras saturadas.")
        print("Introduza alimentos sólidos no momento certo, de acordo com as orientações do pediatra.")

        print("\nSono Adequado:")
        print("Estabeleça uma rotina de sono regular.")
        print("Certifique-se de que o ambiente de sono seja seguro e confortável.")
        print("Adapte a quantidade de sono conforme a idade da criança.")

        print("\nAtividade Física:")
        print("Incentive a prática regular de atividades físicas adequadas à idade.")
        print("Proporcione oportunidades para brincadeiras ao ar livre.")
        print("Limite o tempo de tela e promova um equilíbrio saudável entre atividades sedentárias e ativas.")

        print("\nVacinação e Check-ups Regulares:")
        print("Mantenha o calendário de vacinação atualizado conforme as orientações do pediatra.")
        print("Realize check-ups regulares para monitorar o crescimento e desenvolvimento da criança.")

    elif opcao == "5":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")