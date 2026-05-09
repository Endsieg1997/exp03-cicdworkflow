# Session 2 Practice CI/CD

This repository trains a simple linear regression model from `training_data.csv`.

Every push to `main` runs GitHub Actions. If `training_data.csv` changed, the workflow:

1. installs Python dependencies,
2. runs `train_model.py`,
3. generates `linear_model.txt`,
4. pushes `linear_model.txt` to the `release` branch,
5. creates a GitHub Release and uploads `linear_model.txt`.

Local test:

```bash
pip install -r requirements.txt
python train_model.py
```

Final delivery:

Send the GitHub repository URL to the WeChat group after the Actions workflow and Release page work correctly.
