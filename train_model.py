import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression


def main():
    data = pd.read_csv("training_data.csv")
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]

    model = LinearRegression()
    model.fit(X, y)

    joblib.dump(model, "linear_model.pkl")

    with open("linear_model.txt", "w", encoding="utf-8") as f:
        f.write(f"Coefficients: {model.coef_}\n")
        f.write(f"Intercept: {model.intercept_}\n")


if __name__ == "__main__":
    main()
