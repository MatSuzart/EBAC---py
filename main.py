# EXERCICIOS EBAC
import requests
import csv

# URL da API do GitHub para buscar informações de usuário
github_api_url = 'https://api.github.com/users/'

# Solicite o nome de usuário do GitHub ao usuário
username = input("Digite o nome de usuário do GitHub: ")

# Construa a URL completa da API
user_url = github_api_url + username

try:
    # Faça a solicitação à API do GitHub
    response = requests.get(user_url)

    # Verifique se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Obtenha os dados do usuário
        user_data = response.json()

        # Defina o nome do arquivo CSV para salvar as informações
        csv_filename = f'{username}_github_info.csv'

        # Crie um arquivo CSV e escreva as informações do usuário nele
        with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)

            # Escreva o cabeçalho com os nomes das colunas
            writer.writerow(['Nome', 'Login', 'ID', 'Seguidores', 'Repositórios Públicos', 'Localização', 'Bio'])

            # Escreva os dados do usuário no CSV
            writer.writerow([user_data['name'], user_data['login'], user_data['id'],
                             user_data['followers'], user_data['public_repos'],
                             user_data['location'], user_data['bio']])

        print(f"As informações do usuário {username} foram salvas em {csv_filename}.")

    else:
        print(f"Erro ao acessar a API do GitHub. Código de status: {response.status_code}")

except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")
# RODAR SCRIPT -> !PYTHON MAIN.PY