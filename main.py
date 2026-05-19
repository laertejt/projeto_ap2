import streamlit as st
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
# gravando o excel em uma variaveldf
df = pd.read_excel("planilhao.xlsx", sheet_name="Sheet1")
# titulo do Dashboar
st.header("Meu Dashbord")
menu = st.tabs(["Tabela", "Barra", "Pizza"])
with menu[0]:
        st.dataframe(df)# expondo o df no dashboard
with menu[1]:
        # # grafico de barras vertical
        fig = plt.figure(figsize=(10,6)) # tamanho do grafico
        sn.countplot(data=df, x="setor", 
                order=df['setor'].value_counts().index,
                palette='viridis')
        plt.title("Grafico de Barras por setor")
        plt.xlabel("Numero de empresas")
        plt.ylabel("Setor")
        plt.xticks(rotation=45)
        plt.show()
        st.pyplot(fig)
with menu[2]:
        # #Grafico de Pizza
        setor = df["setor"].value_counts()
        cores = sn.color_palette("Blues_r", len(setor)) # Paleta degradê profissional
        fig = plt.figure(figsize=(10,6)) # tamanho do grafico
        plt.pie(setor, 
                labels=setor.index,
                # autopct='%1.1f%%',
                startangle=140,
                colors=cores,
                pctdistance=0.85, # Afasta a porcentagem do centro
                wedgeprops={'linewidth': 3, 'edgecolor': 'white'})
        plt.show()
        st.pyplot(fig)


# import pandas as pd
# import seaborn as sn
# import matplotlib.pyplot as plt
# # gravando o excel em uma df
# df = pd.read_excel("planilhao.xlsx", sheet_name="Sheet1")
# df.columns
# # grafico de barras vertical
# plt.figure(figsize=(10,6)) # tamanho do grafico
# sn.countplot(data=df, x="setor", 
#              order=df['setor'].value_counts().index,
#              palette='viridis')
# plt.title("Grafico de Barras por setor")
# plt.xlabel("Numero de empresas")
# plt.ylabel("Setor")
# plt.xticks(rotation=45)
# plt.show()
# # grafico de barras horizontal
# plt.figure(figsize=(10,6)) # tamanho do grafico
# sn.countplot(data=df, y="setor", 
#              order=df['setor'].value_counts().index,
#              palette='viridis')
# plt.title("Grafico de Barras por setor")
# plt.xlabel("Numero de empresas")
# plt.ylabel("Setor")
# plt.xticks(rotation=45)
# plt.show()
# #Grafico de Pizza
# setor = df["setor"].value_counts()
# cores = sn.color_palette("Blues_r", len(setor)) # Paleta degradê profissional
# plt.figure(figsize=(10,6)) # tamanho do grafico
# plt.pie(setor, 
#         labels=setor.index,
#         # autopct='%1.1f%%',
#         startangle=140,
#         colors=cores,
#         pctdistance=0.85, # Afasta a porcentagem do centro
#         wedgeprops={'linewidth': 3, 'edgecolor': 'white'})
# plt.show()
# # Grafico de Histograma
# filtro = df["setor"] == 'consumo'
# df_setor = df[filtro]
# sn.histplot(df["roe"], bins=20, kde=True, color='blue')



# # # Importar a biblioteca
# # import pandas as pd
# # # Le o excel
# # df = pd.read_excel("planilhao.xlsx", sheet_name="Planilha1")
# # # Selecionando as coluna que tenha o valor "EBIT"
# # filtro = df["Conta"]=="EBIT"
# # df.columns
# # # Selecionando as colunas
# # colunas = [
# #     '20254T', '20252T','20251T', '20244T', '20243T', '20242T', 
# #     '20241T', '20234T', '20233T','20232T', '20231T', '20224T', 
# #     '20223T', '20222T', '20221T', '20214T','20213T', '20212T',
# #     '20211T', '20204T', '20203T'
# #     ]
# # colunas = sorted(colunas)
# # # Instlar a bibioteca matplotlib (uv add matplotlib)
# # ebit = df[filtro][colunas].iloc[0]

# # import seaborn as sn
# # sn.lineplot(ebit)
# # sn.histplot(ebit)
# # sn.boxplot(ebit)










# # import pandas as pd
# # df = pd.read_csv("study_performance.csv")
# # # selecionar apenas as 3 colunas
# # colunas = ["math_score","reading_score","writing_score"]
# # df[colunas]
# # # selecionar apenas as 7 primeiras linhas
# # df[0:7]
# # # selecionar as 7 linas e as 3 colunas
# # df[0:7][colunas]
# # # estatisticas descritivas
# # df.describe()
# # df.to_excel



