from openpyxl import load_workbook
import os
CAMINHO = f'R:\Compartilhado\DP\lista_clientes_dp_provisoes'


def ler_excel(nome_arquivo, dic):
    dados_cliente_excel = load_workbook(nome_arquivo)

    for planilha in dados_cliente_excel:
        if planilha.title != 'RELAÇÃO DE EMPRESAS' and planilha.title != 'ASSESSORIAS':
            # print(planilha.title)
            cabecalho = True
            for linha in planilha.values:
                # print(linha[0])
                if not cabecalho:
                    dic.update({linha[0]: linha})

                cabecalho = False
                #         nova_data = str(linha[1])[0:10].split('-')
                #         nova_data = nova_data[2] + nova_data[1] + nova_data[0]
                #         dicionario_admissoes.update(
                #             {linha[0]: nova_data})
                #     else:
                #         dicionario_admissoes.update({linha[0]: str(linha[1])})

    return dic


def ler_pasta():
    dic = {}
    for diretorio, subpastas, arquivos in os.walk(CAMINHO):

        for arquivo in arquivos:

            formato = os.path.join(diretorio, arquivo).split('.')[-1]
            if formato == 'xlsx' or formato == 'xls':
                # nome_arquivo = os.path.join(diretorio, arquivo).split('\\')[-1]
                nome_arquivo = os.path.join(diretorio, arquivo)
                # print(nome_arquivo)
                # ler_excel(nome_arquivo, dic)
                dic = ler_excel(
                    nome_arquivo, dic)
    return dic


if __name__ == '__main__':
    dados_funcionario = ler_pasta()
    # ler_pasta()
    print(dados_funcionario)
    # data = dados_funcionario.get('NASCIMENTO')[0:10].split('-')
    # nova_data = data[2] + data[1] + data[0]
    # print(nova_data)
