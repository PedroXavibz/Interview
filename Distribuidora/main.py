import json


class Distribuidora:
    _faturamentos = []

    def __init__(self) -> None:
        self._getDataJson()

    def _readJson(self):
        with open('./data.json') as json_file:
            return json.loads(json_file.read())

    def _getDataJson(self):
        data = self._readJson()
        self._faturamentos = data

    def _getValor(self, menor=True):
        valor_atual = self._faturamentos[0].get('valor')
        dia = self._faturamentos[0].get('dia')

        for faturamento in self._faturamentos:
            valor = faturamento.get('valor')

            if valor == 0:
                continue

            if menor and valor <= valor_atual:
                valor_atual = valor
                dia = faturamento.get('dia')
            elif not menor and valor >= valor_atual:
                valor_atual = valor
                dia = faturamento.get('dia')
        return [valor_atual, dia]

    def _calcularMediaMensal(self):
        total_de_dias = 0
        total_mensal = 0

        for faturamento in self._faturamentos:
            valor = faturamento.get('valor')

            if valor == 0:
                continue

            total_mensal += valor
            total_de_dias += 1

        mediaMensal = total_mensal / total_de_dias
        return mediaMensal

    def getMenorFaturamento(self):
        faturamento, dia = self._getValor(menor=True)
        return [faturamento, dia]

    def getMaiorFaturamento(self):
        faturamento, dia = self._getValor(menor=False)
        return [faturamento, dia]

    def getNumeroDeDiasFaturamentoMaiorQueMediaMensal(self):
        mediaMensal = self._calcularMediaMensal()
        numero_de_dias = 0
        for faturamento in self._faturamentos:
            valor = faturamento.get('valor')

            if valor == 0:
                continue

            if valor > mediaMensal:
                numero_de_dias += 1
        return numero_de_dias


print("=============[Faturamento diário de distribuidora]=============")
distribuidora = Distribuidora()

menorFaturamento, diaMenor = distribuidora.getMenorFaturamento()
print("O menor faturamento ocorrido no mês:")
print(f" ・Dia {diaMenor}")
print(f" ・Faturamento de R$:{menorFaturamento}\n")

maiorFaturamento, diaMaior = distribuidora.getMaiorFaturamento()
print("O maior faturamento ocorrido no mês:")
print(f" ・Dia {diaMaior}")
print(f" ・Faturamento de R$:{maiorFaturamento}\n")

numero_de_dias = distribuidora.getNumeroDeDiasFaturamentoMaiorQueMediaMensal()
print("Número de dias em que o faturamento diário e maior que o mensal:")
print(f" ・{numero_de_dias} dias")
