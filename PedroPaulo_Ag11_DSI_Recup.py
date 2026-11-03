from colorama import Fore, Style, init

# Inicializa o colorama (garante compatibilidade no Windows e no VS Code)
init()

def obter_cor_nivel(nivel):
    """
    Função responsável por definir e retornar a cor correspondente 
    ao nível do reservatório segundo a progressão de risco.
    """
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

def simular_monitoramento():
    """
    Simulação do sistema de monitoramento de níveis de água
    exibindo alertas coloridos no terminal.
    """
    # Lista com as mensagens e situações de cada nível
    niveis_reservatorio = [
        {"nivel": 1, "situacao": "Muito baixo (crítico)"},
        {"nivel": 2, "situacao": "Baixo"},
        {"nivel": 3, "situacao": "Médio"},
        {"nivel": 4, "situacao": "Alto"},
        {"nivel": 5, "situacao": "Muito alto (alerta)"}
    ]

    print("=== SISTEMA DE MONITORAMENTO DE NÍVEL DE ÁGUA ===\n")

    # Percorre a lista exibindo a situação com a cor associada
    for item in niveis_reservatorio:
        num_nivel = item["nivel"]
        situacao = item["situacao"]
        
        cor = obter_cor_nivel(num_nivel)
        
        # Exibe no terminal formatado com a cor correspondente
        print(f"{cor}Nível {num_nivel}: {situacao}")

    # Restaura o estilo padrão do terminal após a exibição das mensagens
    print(Style.RESET_ALL)
    print("=================================================")

if __name__ == "__main__":
    simular_monitoramento()