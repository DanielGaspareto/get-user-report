# Inicia o código
import os

from main.user_report import run_github_analysis


if __name__ == '__main__':
    github_token = os.environ.get('GITHUB_TOKEN')
    username = input("Digite o nome de usuário do GitHub: ")

    if not github_token:
        print("Por favor, configure a variável de ambiente GITHUB_TOKEN com seu token de acesso.")
    else:
        run_github_analysis(username=username, token=github_token)
