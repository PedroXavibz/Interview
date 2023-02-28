distribuidora = [
    {
        "estado": "SP",
        "faturamento": 67836.43,
        "percentual": 0
    },
    {
        "estado": "RJ",
        "faturamento": 36678.66,
        "percentual": 0
    },
    {
        "estado": "MG",
        "faturamento": 29229.88,
        "percentual": 0
    },
    {
        "estado": "ES",
        "faturamento": 27165.48,
        "percentual": 0
    },
    {
        "estado": "outros",
        "faturamento": 19849.53,
        "percentual": 0
    },
]


def calcValorMensal(distribuidora):
    total_mensal = 0
    for dados in distribuidora:
        total_mensal += dados.get('faturamento')
    return total_mensal


def calcularPercentual(distribuidora):
    total_mensal = calcValorMensal(distribuidora)
    for dados in distribuidora:
        faturamento = dados.get('faturamento')
        percentual = (faturamento * 100) / total_mensal
        dados.update({'percentual': percentual})


def exibirDados(distribuidora):
    calcularPercentual(distribuidora)
    titulo = "| Estado | Faturamento | Percentual de faturamento |"
    line = "|" + ("-" * (len(titulo) - 2)) + "|"

    print("==================[ DISTRIBUIDORA ]==================\n")
    print(line)
    print(titulo)
    print(line)

    for dados in distribuidora:
        estado = dados.get('estado')
        faturamento = dados.get('faturamento')
        percentual = dados.get('percentual')

        print(f"| {str(estado).ljust(6)} | R${str(faturamento).ljust(9)} | {percentual:.2f}% {' '.ljust(18)} |")
        print(line)


exibirDados(distribuidora)
