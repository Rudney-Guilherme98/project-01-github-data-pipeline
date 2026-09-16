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
repo_data = buscar_repositorio("psf", "requests", headers)

print("Nome:", repo_data["full_name"])
print("Estrelas:", repo_data["stargazers_count"])
print("Forks:", repo_data["forks_count"])
print("Linguagem:", repo_data["language"])
print("Criado em:", repo_data["created_at"])
with open("data/raw/psf_requests.json","w") as arquivo:
    json.dump(repo_data, arquivo, indent=4)