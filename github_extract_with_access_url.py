import requests

def get_repo_info_from_url(url):
    """Extract owner and repo name from GitHub or GitHub Enterprise URL."""
    url = url.rstrip('/')
    parts = url.split('/')
    if len(parts) < 2:
        return None, None
    owner = parts[-2]
    repo = parts[-1]
    return owner, repo

def get_base_url_from_repo_url(url):
    """Extract base URL for API calls (github.com or github.qualcomm.com, etc.)."""
    url = url.rstrip('/')
    parts = url.split('/')
    if len(parts) < 3:
        return "https://github.com"
    base = parts[0] + "//" + parts[2]
    return base

def list_files_in_repo(base_url, owner, repo, path='', branch='main', token=None):
    """List files in a GitHub repository using API."""
    api_url = f"{base_url}/api/v3/repos/{owner}/{repo}/contents/{path}?ref={branch}"
    headers = {}
    if token:
        headers['Authorization'] = f'token {token}'
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        contents = response.json()
        files = []
        for item in contents:
            files.append({'name': item['name'], 'type': item['type']})
        return files
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def get_github_file(base_url, owner, repo, file_path, branch='main', token=None):
    """Read a file from a GitHub repository using raw content URL."""
    if base_url.startswith('https://github.com'):
        raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{file_path}"
    else:
        # For GitHub Enterprise, construct raw URL based on your enterprise's setup
        # This may vary; adjust as needed for your enterprise
        # Example: https://github.qualcomm.com/name/repo/raw/branch/path/to/file
        raw_url = f"{base_url}/{owner}/{repo}/raw/{branch}/{file_path}"
    headers = {}
    if token:
        # For raw content, GitHub Enterprise may require authentication via headers or basic auth
        # Adjust as needed for your enterprise
        headers['Authorization'] = f'token {token}'
    try:
        response = requests.get(raw_url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def main():
    print("\nWelcome to GitHub Repository Explorer!")
    print("You can use a GitHub access token for private repos or just the URL for public repos.")

    use_token = input("Do you want to use an access token? (y/n): ").lower() == 'y'
    token = None
    if use_token:
        token = input("Enter your GitHub access token: ")

    repo_url = input("Enter the repository URL (e.g., https://github.com/owner/repo or https://github.qualcomm.com/owner/repo): ")
    base_url = get_base_url_from_repo_url(repo_url)
    owner, repo = get_repo_info_from_url(repo_url)
    if not owner or not repo:
        print("Invalid repository URL format.")
        return

    branch = input("Enter the branch (default is 'main'): ") or 'main'

    while True:
        print("\n| Command | Description                        |")
        print("|---------|------------------------------------|")
        print("|    1    | List all files in the repository   |")
        print("|    2    | Read a file from the repository    |")
        print("|    0    | Quit                               |")

        choice = input("\nEnter 1 (list), 2 (read), or 0 (quit): ")
        if choice == '0':
            print("\nGoodbye!")
            break
        elif choice == '1':
            files = list_files_in_repo(base_url, owner, repo, branch=branch, token=token)
            if isinstance(files, str):
                print(files)
            else:
                print(f"\nFiles in repository '{owner}/{repo}':")
                for f in files:
                    print(f"- {f['name']} ({f['type']})")
        elif choice == '2':
            file_path = input("Enter the file path to read (e.g., README.md or folder/file.txt): ")
            content = get_github_file(base_url, owner, repo, file_path, branch, token)
            if content:
                print(f"\nContent of {file_path}:")
                print(content)
            else:
                print("Could not extract the file.")
        else:
            print("Invalid choice. Please enter 1, 2, or 0.")

if __name__ == '__main__':
    main()
