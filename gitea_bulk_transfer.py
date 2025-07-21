import argparse
import requests

def parse_args():
    parser = argparse.ArgumentParser(description="Transfer all repos from one Gitea user to another.")
    parser.add_argument("--token", required=True, help="Gitea API token")
    parser.add_argument("--url", required=True, help="Base URL of the Gitea instance (e.g. https://gitea.example.com)")
    parser.add_argument("--from-user", required=True, help="Current owner of the repositories")
    parser.add_argument("--to-user", required=True, help="Target owner of the repositories")
    return parser.parse_args()

def get_all_repos(base_url, user, headers):
    repos = []
    page = 1
    per_page = 50
    while True:
        url = f"{base_url}/api/v1/users/{user}/repos?page={page}&limit={per_page}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        batch = response.json()
        if not batch:
            break
        repos.extend(batch)
        page += 1
    return repos

def transfer_repo(base_url, owner, repo_name, new_owner, headers):
    url = f"{base_url}/api/v1/repos/{owner}/{repo_name}/transfer"
    payload = {"new_owner": new_owner}
    response = requests.post(url, headers=headers, json=payload)
    if response.ok:
        print(f"✅ Transferred {repo_name} to {new_owner}")
    else:
        print(f"❌ Failed to transfer {repo_name}: {response.status_code} {response.text}")

def main():
    args = parse_args()
    headers = {
        "Authorization": f"token {args.token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    print(f"🔍 Fetching repositories owned by {args.from_user}...")
    repos = get_all_repos(args.url, args.from_user, headers)

    print(f"🔁 Transferring {len(repos)} repositories to {args.to_user}...\n")
    for repo in repos:
        transfer_repo(args.url, args.from_user, repo["name"], args.to_user, headers)

if __name__ == "__main__":
    main()
