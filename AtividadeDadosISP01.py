# Comando limpa o terminal
import os
os.system("cls")

# Importando bibliotecas necessárias para análise de dados
import pandas as pd
import numpy as np

# Execute os comando abaixo "try", exceto, se ocorrer ERRO
# Comandos abaixo realizaram a conexão com o bando de dados

# "ENDERECO_DADOS" está escrito em maiuculo por se tratar de uma constante (convenção no python)
try:
    print("Carregando dados ISP... Aguarde!")
    ENDERECO_DADOS = "https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv"
    df = pd.read_csv(ENDERECO_DADOS, sep=";",encoding="iso-8859-1")

# Delimitando a atividade no tipo "roubo_celular"
    df_roubo_celular = df[["roubo_celular","mes_ano"]]
    print(df_roubo_celular.head())
    print(df_roubo_celular)

# Em casos de erro, executar as instruções abaixo, até o EXIT()
except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()

print(80*"#")

# Executando os camandos abaixo, exceto, se ocorrer ERRO

try:
# Casos de roubos de celulares organizados anualmente
    df_roubo_celular_data =  df_roubo_celular.groupby(["mes_ano"]).sum().reset_index()
    print(df_roubo_celular_data)

    array_roubo_celular_data = np.array(df_roubo_celular_data["roubo_celular"])

# Calculando a méida e a mediana das ocorrências "roubo de celuar" mensalmente

    media_casos = np.mean(array_roubo_celular_data)
    mediana_casos = np.median(array_roubo_celular_data)

    distancia_relativa = abs(media_casos - mediana_casos) / mediana_casos
    print(90*"=")
    print(f'Mensalmente a média de roubo de celulares é: {media_casos}')
    print(f'Mensalmente a mediana de roubo de celulares é: {mediana_casos}')
    print(f'A distânicia relativa entre a média e a mediana, no banco em análise é; {distancia_relativa}')

# Em caso de ERRO, executar as instruções abaixo, até o exit()

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()
print(90*"=")
print("Conclusão: Os dados indicam uma pequena assimetria na distribuição (diferença entre média e mediana).")
