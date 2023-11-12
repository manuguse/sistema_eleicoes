from MVC.model import Model
from DAO.arquivo_DAO import ArqDAO
from DAO.data_DAO import DataDAO

import sys
sys.dont_write_bytecode = True

model = Model(DataDAO(), ArqDAO())

def test_candidatos():
    result = model.obter_candidatos()

    assert result == ["Pedro", "Marco", "José", "Mateus"]

def test_regioes():
    result = model.obter_regioes()
    
    assert result == ["sc", "pr", "rs", "am"]

def test_votos_por_regiao():
    result = model.obter_votos_por_regiao("Pedro")

    assert result == {"sc": "50", "pr": "100"}

def test_total_de_votos():
    result = model.obter_total_de_votos("Pedro")

    assert result == 150

def test_votos_em_regioes():
    result = model.obter_votos_em_regiao("Pedro", "sc")

    assert result == 50

def test_nome_de_arquivos():
    model.adicionar_arquivo_a_lista("a")
    model.adicionar_arquivo_a_lista("b")

    result = model.retornar_nome_arquivos()

    assert result == ["a", "b"]

def test_vencedor():
    model.retornar_vencedor()

    result = model.vencedor

    assert result == ["Pedro", "Marco"]



