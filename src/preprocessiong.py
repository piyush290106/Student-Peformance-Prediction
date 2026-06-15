from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


def get_preprocessor():

    categorical_features = [
        "gender",
        "race/ethnicity",
        "parental level of education",
        "lunch",
        "test preparation course"
    ]

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_features
            )
        ]
    )

    return preprocessor