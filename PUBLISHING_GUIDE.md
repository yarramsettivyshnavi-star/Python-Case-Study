# Publish and ZIP guide

## Before publishing

1. Open the folder `Python-Activity-Based-Learning` in VS Code.
2. Edit `README.md` and fill in your name, roll number, branch, and section.
3. Review the personal details before making the repository public. Public repository contents can be viewed by anyone.
4. Keep the PDF and programs together in the project folder.

## Create or refresh the ZIP

The ZIP is already provided beside the project folder. If you edit the README or other files, open VS Code's integrated terminal in the parent `outputs` folder and run:

```powershell
Compress-Archive -Path .\Python-Activity-Based-Learning -DestinationPath .\Python-Activity-Based-Learning.zip -Force
```

This makes a ZIP containing the complete project folder.

## Publish a new public GitHub repository from VS Code

1. Open the project folder in VS Code.
2. Open the Command Palette with **Ctrl+Shift+P**.
3. Run **Publish to GitHub** and sign in if VS Code asks.
4. Enter the repository name exactly: `Python-Activity-Based-Learning`.
5. Choose **Public**.
6. Include the project files when prompted, review the file list, then confirm publishing. VS Code creates the GitHub repository, connects it as the remote, and pushes the commit.
7. Open the repository on GitHub and check that the README, ten programs, case-study documents, PDF, and screenshots are visible. Copy the repository page link for submission.

The GitHub ZIP download is separate from the prepared local ZIP. For your assignment, submit the public repository URL if that is what your instructor requests.
