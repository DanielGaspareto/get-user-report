import sys
import os
import pytest

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from main.user_report import GitHubAPI, GitHubReportGenerator


@pytest.fixture
def github_api():
    github_token = os.environ.get('GITHUB_TOKEN')
    return GitHubAPI(github_token)

def test_get_user_data(github_api):
    # Testando a busca pelo usuario
    user_data = github_api.get_user_data('DanielGaspareto')
    assert 'login' in user_data

def test_get_user_data_fields(github_api):
    # Garantindo que um erro deve acontecer caso mude o tipo da string
    with pytest.raises(ValueError):
        user_data = github_api.get_user_data(username=1)


@pytest.fixture
def github_report_generator():
    return GitHubReportGenerator()

def test_generate_report_fields(github_report_generator):
    # Criando um exemplo de resposta da API
    user_data = {
        'name': 'Daniel da Silva Gaspareto',
        'html_url': 'https://github.com/DanielGaspareto',
        'public_repos': 3,
        'followers': 2,
        'following': 3
    }
    repositories = [
        {'name': 'get_asn', 'html_url': 'https://github.com/DanielGaspareto/get_asn'},
        {'name': 'simple_game', 'html_url': 'https://github.com/DanielGaspareto/simple_game'},
        {'name': 'to-do-list', 'html_url': 'https://github.com/DanielGaspareto/to-do-list'}
    ]
    
    # Chama a função para gerar o relatório
    username = 'DanielGaspareto'
    github_report_generator.generate_report(username=username, user_data=user_data, repositories=repositories)
    
    # Lê o conteúdo do arquivo gerado
    with open(f'{username}.txt', 'r') as file:
        report = file.read()
    
    # Verifica se o relatório gerado contém informações esperadas
    assert 'Nome: Daniel da Silva Gaspareto' in report
    assert 'Perfil: https://github.com/DanielGaspareto' in report
    assert 'Número de repositórios públicos: 3' in report
    assert 'Número de seguidores: 2' in report
    assert 'Número de usuários seguidos: 3' in report
    assert '- get_asn: https://github.com/DanielGaspareto/get_asn' in report
    assert '- simple_game: https://github.com/DanielGaspareto/simple_game' in report
    assert '- to-do-list: https://github.com/DanielGaspareto/to-do-list' in report

    os.remove(f'{username}.txt')
