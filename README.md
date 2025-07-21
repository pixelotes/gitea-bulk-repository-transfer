# Gitea Bulk Repository Transfer

A simple Python script to transfer all repositories from one Gitea user or organization to another using the Gitea API.

## Features

- Transfers **all repositories** from a source account to a target account
- Supports **pagination** to process more than 50 repos
- Fully configurable via **command-line arguments**

## Requirements

- Python 3
- `requests` library (`pip install requests`)
- A Gitea **admin API token** with sufficient permissions

## Usage

```bash
python3 transfer_repos.py \
  --token <your_gitea_token> \
  --url <https://gitea.example.com> \
  --from-user <source_user> \
  --to-user <target_user>
```

## License

This repository and its contents are licensed under the [MIT license](./LICENSE).
