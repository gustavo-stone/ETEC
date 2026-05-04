from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

# Lista com os níveis do reservatório
niveis = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]

# Função que define a cor conforme o nível
def definir_cor(nivel):
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

# Simulação do monitoramento
def exibir_niveis():
    print("=== Monitoramento do Reservatório ===\n")
    
    for i in range(len(niveis)):
        nivel = i + 1
        cor = definir_cor(nivel)
        print(cor + niveis[i])

    # Restaura estilo padrão (opcional por causa do autoreset)
    print(Style.RESET_ALL)

# Execução
if __name__ == "__main__":
    exibir_niveis()