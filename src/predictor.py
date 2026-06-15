import joblib
import pandas as pd

model = joblib.load(
    "models/random_forest.pkl"
)


def predict_student(data):

    df = pd.DataFrame([data])

    prediction = model.predict(df)

    math = prediction[0][0]
    reading = prediction[0][1]
    writing = prediction[0][2]

    avg = (
        math +
        reading +
        writing
    ) / 3

    if avg >= 90:
        category = "Excellent"

    elif avg >= 75:
        category = "Good"

    elif avg >= 65:
        category = "Average"

    else:
        category = "Needs Improvement"

    status = (
        "PASS"
        if avg >= 65
        else "FAIL"
    )

    return {
        "Math": round(math, 2),
        "Reading": round(reading, 2),
        "Writing": round(writing, 2),
        "Average": round(avg, 2),
        "Category": category,
        "Status": status
    }