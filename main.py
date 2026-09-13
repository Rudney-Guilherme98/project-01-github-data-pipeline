import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GITHUB_TOKEN")
headers = {
    "Authorization": f"bearer {token}"
}
response = requests.get("https://api.github.com/user", headers=headers)
print (response.status_code)
print (response.json())
repo_url = "https://api.github.com/repos/psf/requests"
repo_reponse = requests.get(repo_url, headers=headers)

repo_data = repo_reponse.json()

print("Nome:", repo_data["full_name"])
print("Estrelas:", repo_data["stargazers_count"])
print("Forks:", repo_data["forks_count"])
print("Linguagem:", repo_data["language"])
print("Criado em:", repo_data["created_at"])
with open("data/raw/psf_requests.json","w") as arquivo:
    json.dump(repo_data, arquivo, indent=4)