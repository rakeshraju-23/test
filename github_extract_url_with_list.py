import requests

def list_files_in_repo(repo_owner, repo_name, path='', branch='main'):
    """List files in a GitHub repository path using GitHub API."""
    api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{path}?ref={branch}'
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        contents = response.json()
        files = []
        for item in contents:
            files.append({'name': item['name'], 'type': item['type']})
        return files
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def get_github_file(repo_url, file_path, branch='main'):
    """Read a file from a GitHub repository using raw content URL."""
    repo_url = repo_url.rstrip('/').replace('github.com', 'raw.githubusercontent.com')
    raw_url = f"{repo_url}/{branch}/{file_path}"
    try:
        response = requests.get(raw_url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def main():
    print("\nWelcome to GitHub Repository Explorer!")
    print("| Command | Description                        |")
    print("|---------|------------------------------------|")
    print("|    1    | List all files in the repository   |")
    print("|    2    | Read a file from the repository    |")
    print("|    0    | Quit                               |")

    repo_url = input("\nEnter the GitHub repository URL (e.g., https://github.com/username/repository): ")
    branch = input("Enter the branch (default is 'main'): ") or 'main'

    # Parse repo owner and name from URL
    try:
        parts = repo_url.rstrip('/').split('/')
        repo_owner = parts[-2]
        repo_name = parts[-1]
    except IndexError:
        print("Invalid repository URL format.")
        return

    while True:
        choice = input("\nEnter 1 (list), 2 (read), or 0 (quit): ")
        if choice == '0':
            print("\nGoodbye!")
            break
        elif choice == '1':
            files = list_files_in_repo(repo_owner, repo_name, branch=branch)
            if isinstance(files, str):
                print(files)
            else:
                print(f"\nFiles in repository '{repo_owner}/{repo_name}':")
                for f in files:
                    print(f"- {f['name']} ({f['type']})")
        elif choice == '2':
            file_path = input("Enter the file path to read (e.g., README.md or folder/file.txt): ")
            content = get_github_file(repo_url, file_path, branch)
            if content:
                print(f"\nContent of {file_path}:")
                print(content)
            else:
                print("Could not extract the file.")
        else:
            print("Invalid choice. Please enter 1, 2, or 0.")

if __name__ == '__main__':
    main()
