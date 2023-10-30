# Git User Report

Utilizado para criar um relatório sobre um usuário github.

## Requisitos
    - Python 3.10.6
    - Bibliotecas disponíveis no arquivo requirements.txt.
    - VSCode (Opcional)

<br/>

### Preparativos
Instale a biblioteca virtualenv ou venv na sua máquina.

Crie uma virtualenv utilizando o comando:
- python -m venv "Nome_da_virtualenv" 
ou 
- python -m virtualenv "Nome_da_virtualenv"

ative a virtualenv com o seguinte comando (você deve estar no mesmo diretório que sua virtualevn):
- source ./nome_da_virtualenv/bin/activate (No linux)
- nome_da_virtualenv/Scripts/Activate (No windows).

OBS: Lembrando que no Windows você pode ter alguns problemas de políticas para ativar o virtualenv, resolva antes de prosseguir.

Com a virtualenv criada e funcionando, execute o seguinte comando para instalar as dependências:
- pip install -r requirements.txt 

O usuário que terá os dados consultados, deve fornecer o token criado no site do github.

Será necessário criar uma variável de ambiente contendo o token para acessar o perfil do usuário. A variável deve ser nomeada como: 
- GITHUB_TOKEN = "token".

Caso não possa criar uma variável de ambiente, utilize os campos no arquivo run.py desta maneira:

    # github_token = os.environ.get('GITHUB_TOKEN')
    github_token = ('Digite aqui o Token')
    username = input("Digite o nome de usuário do GitHub: ")

Lembre-se de que salvar um token dentro do código, da maneira descrita acima, não é recomendada, pois isso pode gerar problemas de segurança. No fim dos testes remova o token e descomente a linha que busca o token via variável de ambiente.


### Executando o Código
Execute o arquivo run.py para iniciar o código.

No terminal, será solicitado que digite o nome do usuário (Igual ao que está no github).

### Executando os testes
No terminal, enquanto estiver no diretório git_user_report, execute o comando:
- pytest tests/

Ou, se quiser executar exatamente um único teste:
- pytest test/"nome_do_arquivo_test.py"

