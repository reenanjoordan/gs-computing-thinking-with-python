# Sistema de Monitoramento de Energia Solar
# Desenvolvedores: [Renan Urtado Challó de Oliveira Jordão - RM: 560618 e Matheus Mallet - RM: 560491]

def calcular_energia_gerada(horas_sol, eficiencia, area_painel):
    """Calcula a energia gerada em kWh."""
    energia_por_m2 = 1  # Constante: 1 kWh por m² por hora de sol
    return horas_sol * eficiencia * area_painel * energia_por_m2

def monitorar_consumo(consumos):
    """Calcula o total de energia consumida."""
    return sum(consumos)

def calcular_economia_carbono(energia_gerada):
    """Calcula a economia de carbono com base na energia gerada."""
    fator_carbono = 0.5  # Emissões evitadas (kg CO2 por kWh)
    return energia_gerada * fator_carbono

def exibir_relatorio(energia_gerada, consumo_total, economia_carbono):
    """Exibe o relatório diário de energia."""
    print("\n--- Relatório Diário de Energia ---")
    print(f"Energia Gerada: {energia_gerada:.2f} kWh")
    print(f"Consumo Total: {consumo_total:.2f} kWh")
    print(f"Economia de Carbono: {economia_carbono:.2f} kg CO2")
    if energia_gerada >= consumo_total:
        print("Status: Energia suficiente para atender ao consumo.")
    else:
        print("Status: Déficit de energia. Considere economizar ou expandir o sistema.")

def main():
    print("Bem-vindo ao Sistema de Monitoramento de Energia Solar!")
    
    # Entrada de dados
    horas_sol = float(input("Digite o número de horas de sol no dia: "))
    eficiencia = float(input("Digite a eficiência dos painéis (0 a 1): "))
    area_painel = float(input("Digite a área total dos painéis (m²): "))
    
    energia_gerada = calcular_energia_gerada(horas_sol, eficiencia, area_painel)
    
    consumos = []
    print("\nInsira os consumos diários de energia (em kWh). Digite '0' para finalizar.")
    while True:
        consumo = float(input("Consumo (kWh): "))
        if consumo == 0:
            break
        consumos.append(consumo)
    
    consumo_total = monitorar_consumo(consumos)
    economia_carbono = calcular_economia_carbono(energia_gerada)
    
    # Exibição do relatório
    exibir_relatorio(energia_gerada, consumo_total, economia_carbono)

# Execução do programa
if __name__ == "__main__":
    main()