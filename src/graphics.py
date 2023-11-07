import PySimpleGUI as sg
import json
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image


# Função para criar um gráfico de pizza
def create_pie_chart(data):
    votes_by_state = {}
    for item in data:
        for state, votes in item["votos"].items():
            votes_by_state[state] = votes_by_state.get(state, 0) + int(votes)

    labels = votes_by_state.keys()
    sizes = votes_by_state.values()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Gráfico de Pizza')

# Função para criar um gráfico de barras
def create_bar_chart(data):
    names = [item["nome"] for item in data]
    total_votes = [sum(int(votes) for votes in item["votos"].values()) for item in data]

    plt.barh(names, total_votes)
    plt.xlabel('Votos Totais')
    plt.ylabel('Candidatos')
    plt.title('Gráfico de Colunas')

    # Salvar o gráfico em uma imagem e converter em bytes
    img_data = BytesIO()
    plt.savefig(img_data, format='png')
    img_data.seek(0)

    # Converter a imagem em formato bytes para exibir no PySimpleGUI
    return sg.Image(data=img_data.getvalue())