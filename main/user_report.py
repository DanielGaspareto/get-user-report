import requests


class GitHubAPI:
    """Classe que faz a buscar pelos dados do usuário"""
    def __init__(self, token: str):
        self.token = token

    def get_user_data(self, username: str) -> dict:
        """
        Função que retorna os dados em json()

        response: dict
        """
        if not isinstance(username, str):
            raise ValueError("Username deve ser uma string")

        headers = {'Authorization': f'token {self.token}'}
        response = requests.get(f'https://api.github.com/users/{username}', headers=headers)
        response = response.json()
        return response


class GitHubReportGenerator:
    """Classe para criar o relatório.txt"""

    def generate_report(self, username: str, user_data: dict, repositories: list):
        """
        Função que separa, formata os dados em uma string e ecrever em um arquivo txt.
        """
        report = f"Nome: {user_data['name']}\n"
        report += f"Perfil: {user_data['html_url']}\n"
        report += f"Número de repositórios públicos: {user_data['public_repos']}\n"
        report += f"Número de seguidores: {user_data['followers']}\n"
        report += f"Número de usuários seguidos: {user_data['following']}\n"
        report += "Lista de Repositórios:\n"
        for repo in repositories:
            report += f"- {repo['name']}: {repo['html_url']}\n"
    
        with open(f'{username}.txt', 'w') as file:
            # Optei por abrir com w, pois a ideia é pegar apenas um usuário por relatório.
            file.write(report)

        print('Arquvio criado no diretório local')


def run_github_analysis(username: str, token: str):
    """
    Função que gerencia todo o processo.
    """
    api = GitHubAPI(token=token)
    user_data = api.get_user_data(username=username)

    if 'message' in user_data:
        print(f"Erro: {user_data['message']}")
        return

    # Buscando os repositórios públicos do usuário
    response = requests.get(user_data['repos_url'])
    repositories = response.json()

    generator = GitHubReportGenerator()
    generator.generate_report(username=username, user_data=user_data, repositories=repositories)
