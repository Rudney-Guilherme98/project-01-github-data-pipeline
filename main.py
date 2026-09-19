import os
import requests
import json
from dotenv import load_dotenv
def buscar_repositorio (owner, repo, headers):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url, headers=headers)
    return response.json()

load_dotenv()
token = os.getenv("GITHUB_TOKEN")
headers = {
    "Authorization": f"bearer {token}"
}
response = requests.get("https://api.github.com/user", headers=headers)
print (response.status_code)
print (response.json())
repositorios = [
    ("psf", "requests"),
    ("pallets", "flask"),
    ("pandas-dev", "pandas"),
]
def exibir_repositorio(repo_data):
    print("Nome:", repo_data["full_name"])
    print("Estrelas:", repo_data["stargazers_count"])
    print("Forks:", repo_data["forks_count"])
    print("Linguagem:", repo_data["language"])
    print("Criado em:", repo_data["created_at"])
    print("---")

for owner, repo in repositorios:
    repo_data = buscar_repositorio(owner, repo, headers)
    exibir_repositorio(repo_data)
    nome_arquivo = f"data/raw/{owner}_{repo}.json"
    with open(nome_arquivo, "w") as arquivo:
        json.dump(repo_data, arquivo, indent=4)