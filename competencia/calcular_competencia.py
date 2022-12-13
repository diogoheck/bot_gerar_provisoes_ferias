import datetime


def calcular_competencia_geracao(data=None):
    if not data:
        data = datetime.date.today()

    if data.month - 1 == 0:
        competencia = f"12{data.year-1}"
    elif data.month - 1 <= 9:
        competencia = f"0{data.month - 1}{data.year}"
    else:
        competencia = f"{data.month - 1}{data.year}"

    return competencia


def calcular_competencia_geracao_anterior(mes_ano):

    mes = int(mes_ano[0:2])
    ano = int(mes_ano[2:6])

    if mes - 1 == 0:
        competencia = f"12{str(ano-1)}"
    else:
        competencia = f"0{str(mes - 1)}{str(ano)}"

    return competencia


# print(calcular_competencia_geracao())
