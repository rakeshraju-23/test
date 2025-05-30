from github import Github

# Get input from the user
ACCESS_TOKEN = "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"#input("Enter your GitHub access token: "
REPO_OWNER = "rry"#input("Enter the repository owner name: ")
REPO_NAME ="test"# input("Enter the repository name: ")
FILE_PATH = input("Enter the file path (e.g., demo.txt or folder/example.txt): ")

try:
    g = Github(ACCESS_TOKEN)
    repo = g.get_user(REPO_OWNER).get_repo(REPO_NAME)
    file_content = repo.get_contents(FILE_PATH)
    print(file_content.decoded_content.decode())
except Exception as e:
    print(f"Error: {e}")
