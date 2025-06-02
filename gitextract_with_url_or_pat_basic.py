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

def get_github_file(base_url, owner, repo, file_path, branch='main', token=None):
    """Read a file from a GitHub repository using raw content URL."""
    if base_url.startswith('https://github.com'):
        raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{file_path}"
    else:
        # For GitHub Enterprise, construct raw URL based on your enterprise's setup
        # Example: https://github.qualcomm.com/owner/repo/raw/branch/path/to/file
        raw_url = f"{base_url}/{owner}/{repo}/raw/{branch}/{file_path}"
    headers = {}
    if token:
        # For raw content, GitHub Enterprise may require authentication via headers
        headers['Authorization'] = f'token {token}'
    try:
        response = requests.get(raw_url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def main():
    print("\nGitHub File Fetcher")
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
    file_path = input("Enter the file path to read (e.g., README.md or folder/file.txt): ")

    content = get_github_file(base_url, owner, repo, file_path, branch, token)
    if content is None:
        print("Could not extract the file.")
        return

    print("\nFile content has been fetched and stored.")
    print_content = input("Do you want to print the file content? (y/n): ").lower() == 'y'
    if print_content:
        print("\nFile content:")
        print(content)

    # You can now use 'content' for further processing in your script
    # For example, you could return it, write it to a file, etc.

if __name__ == '__main__':
    main()
