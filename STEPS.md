# Steps to Finish the CI/CD Practice

1. Create a new empty GitHub repository.
2. Add it as the remote for this local project.
3. Push `main`.
4. Create and push the empty `release` branch if it does not exist.
5. Edit `training_data.csv`, commit, and push again.
6. Check the GitHub Actions tab.
7. Check the `release` branch and GitHub Releases page.
8. Send the repository URL to the WeChat group.

Commands after creating the GitHub repository:

```bash
git remote add origin https://github.com/YOUR-USERNAME/session2-practice-ci-cd.git
git push -u origin main

git checkout --orphan release
git rm -rf .
git commit --allow-empty -m "create empty release branch"
git push origin release
git checkout main
```
