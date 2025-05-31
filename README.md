# File:gitextract_with_url_basic.py
**Inputs:**

- **Access token:**  
  - Enter only if you want to access a private repository.  
  - Not needed for public repositories.
- **Repository URL:**  
  - Paste the full web address of the GitHub repository.  
  - Example: `https://github.qualcomm.com/username/repo`.
- **Branch:**  
  - Type the branch name where your file is located.  
  - The default is usually `main`.
- **File path:**  
  - Enter the path to the file inside the repository.  
  - Example: `README.md` or `docs/changelog.txt`.

**Features:**  
- Fetches file content from any GitHub or GitHub Enterprise repository  
- Optionally prints the file content  
- Stores the content for further use
# File:github_extract_url_with_list.py

**Inputs:**

- **Repository URL:**  
  - Enter the full web address of the GitHub repository.  
  - Example: `https://github.com/username/repository`
- **Branch:**  
  - Type the branch name where you want to look for files.  
  - The default is usually `main`.

**During Use:**

- **List Files:**  
  - Choose option `1` to see all files in the repository.
- **Read a File:**  
  - Choose option `2` and enter the file path (e.g., `README.md` or `folder/file.txt`) to view its contents.
- **Quit:**  
  - Choose option `0` to exit the program.

**Features:**  
- Lists all files in any GitHub repository  
- Fetches and displays the contents of any file  
- Easy to use with clear prompts
# File:github_extract_with_access_code.py

## How it works

- **GitHub access token:**  
  - Set once in the code (not asked during runtime).
- **File path:**  
  - Entered as input when the script runs (e.g., `README.md` or `folder/file.txt`).

**Only the file path is entered when prompted; the access token is set in the code.**
# File:github_extract_with_access_url.py
 **Similar to github_extract_url_with_list.py file with extra feature to get access either using url or personal access tokens**  
