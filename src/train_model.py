import pandas as pd
import joblib

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor

df = pd.read_csv("data/students.csv")

X = df[
    [
        "gender",
        "race/ethnicity",
        "parental level of education",
        "lunch",
        "test preparation course"
    ]
]

y = df[
    [
        "math score",
        "reading score",
        "writing score"
    ]
]

preprocessor = ColumnTransformer(
    [
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            X.columns
        )
    ]
)

models = {
    "random_forest.pkl":
    RandomForestRegressor(
        n_estimators=200,
        random_state=42
    ),

    "linear_regression.pkl":
    LinearRegression(),

    "decision_tree.pkl":
    DecisionTreeRegressor(
        random_state=42
    ),

    "gradient_boosting.pkl":
    MultiOutputRegressor(
        GradientBoostingRegressor()
    )
}

for filename, model in models.items():

    pipeline = Pipeline(
        [
            ("preprocessor", preprocessor),
            ("model", model)
        ]
    )

    pipeline.fit(X, y)

    joblib.dump(
        pipeline,
        f"models/{filename}"
    )

    print(f"{filename} saved")