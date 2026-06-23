import math

import streamlit as st

from components.app_data import METRIC_ROWS
from components.ui_helpers import metric_card, render_navigation, render_page_header


IRIS_EVAL_ROWS = [
    {"sepal_length": 5.1, "petal_length": 1.4, "actual": "setosa", "predicted": "setosa"},
    {"sepal_length": 4.9, "petal_length": 1.4, "actual": "setosa", "predicted": "setosa"},
    {"sepal_length": 5.8, "petal_length": 1.2, "actual": "setosa", "predicted": "setosa"},
    {"sepal_length": 6.0, "petal_length": 4.5, "actual": "versicolor", "predicted": "versicolor"},
    {"sepal_length": 5.7, "petal_length": 4.2, "actual": "versicolor", "predicted": "versicolor"},
    {"sepal_length": 6.3, "petal_length": 4.7, "actual": "versicolor", "predicted": "virginica"},
    {"sepal_length": 6.5, "petal_length": 5.8, "actual": "virginica", "predicted": "virginica"},
    {"sepal_length": 7.2, "petal_length": 6.1, "actual": "virginica", "predicted": "virginica"},
    {"sepal_length": 6.1, "petal_length": 5.1, "actual": "virginica", "predicted": "versicolor"},
]


REGRESSION_EVAL_ROWS = [
    {"home_sqft": 900, "actual_price_k": 310, "predicted_price_k": 300},
    {"home_sqft": 1150, "actual_price_k": 390, "predicted_price_k": 410},
    {"home_sqft": 1400, "actual_price_k": 465, "predicted_price_k": 450},
    {"home_sqft": 1800, "actual_price_k": 610, "predicted_price_k": 640},
    {"home_sqft": 2200, "actual_price_k": 760, "predicted_price_k": 700},
]


def classification_metrics(rows, positive_label):
    """Calculate binary metrics for one class treated as positive."""
    tp = sum(row["actual"] == positive_label and row["predicted"] == positive_label for row in rows)
    fp = sum(row["actual"] != positive_label and row["predicted"] == positive_label for row in rows)
    fn = sum(row["actual"] == positive_label and row["predicted"] != positive_label for row in rows)
    tn = sum(row["actual"] != positive_label and row["predicted"] != positive_label for row in rows)
    total = tp + fp + fn + tn

    return {
        "tp": tp,
        "fp": fp,
        "fn": fn,
        "tn": tn,
        "accuracy": (tp + tn) / total if total else 0,
        "precision": tp / (tp + fp) if tp + fp else 0,
        "recall": tp / (tp + fn) if tp + fn else 0,
    }


def confusion_matrix(rows):
    """Return a display-friendly multiclass confusion matrix."""
    labels = ["setosa", "versicolor", "virginica"]
    matrix = []
    for actual in labels:
        row = {"actual species": actual}
        for predicted in labels:
            row[f"predicted {predicted}"] = sum(
                item["actual"] == actual and item["predicted"] == predicted for item in rows
            )
        matrix.append(row)
    return matrix


def regression_metrics(rows):
    """Calculate MSE and RMSE for the regression example."""
    enriched_rows = []
    squared_errors = []

    for row in rows:
        error = row["predicted_price_k"] - row["actual_price_k"]
        squared_error = error ** 2
        squared_errors.append(squared_error)
        enriched_rows.append({**row, "error_k": error, "squared_error": squared_error})

    mse = sum(squared_errors) / len(squared_errors)
    rmse = math.sqrt(mse)
    return enriched_rows, mse, rmse


render_page_header(1)

st.header("Metrics You May Already Know")
st.write(
    "These metrics are useful because they compress many examples into a small signal. "
    "They become dangerous when the number is treated as complete proof that the system is ready."
)
st.dataframe(METRIC_ROWS, hide_index=True, use_container_width=True)

st.header("Dataset Walkthrough: Iris Classification")
st.write(
    "The Iris dataset is a classic small classification dataset. Each flower belongs to one "
    "of three species. Here we use a tiny Iris-style sample with actual labels and model "
    "predictions so the metrics have something concrete to count."
)
st.dataframe(IRIS_EVAL_ROWS, hide_index=True, use_container_width=True)

positive_label = st.selectbox(
    "Treat this species as the positive class",
    ["setosa", "versicolor", "virginica"],
    index=1,
)
iris_metrics = classification_metrics(IRIS_EVAL_ROWS, positive_label)

iris_col1, iris_col2, iris_col3 = st.columns(3)
with iris_col1:
    metric_card("Accuracy", f"{iris_metrics['accuracy']:.1%}", "Correct examples across this one-vs-rest view")
with iris_col2:
    metric_card("Precision", f"{iris_metrics['precision']:.1%}", f"Predicted {positive_label} and was right")
with iris_col3:
    metric_card("Recall", f"{iris_metrics['recall']:.1%}", f"Found the real {positive_label} examples")

with st.expander("Iris confusion matrix", expanded=True):
    st.dataframe(confusion_matrix(IRIS_EVAL_ROWS), hide_index=True, use_container_width=True)
    st.write(
        "Rows are the true species. Columns are the predicted species. The diagonal cells are "
        "correct predictions; off-diagonal cells are mistakes."
    )

st.header("Dataset Walkthrough: Regression Errors")
st.write(
    "For regression, the prediction is a number instead of a class. This tiny home-price example "
    "shows why MSE and RMSE care about the size of the error."
)
regression_rows, mse, rmse = regression_metrics(REGRESSION_EVAL_ROWS)
st.dataframe(regression_rows, hide_index=True, use_container_width=True)

reg_col1, reg_col2 = st.columns(2)
with reg_col1:
    metric_card("MSE", f"{mse:.1f}", "Average squared error in thousands-of-dollars squared")
with reg_col2:
    metric_card("RMSE", f"{rmse:.1f}k", "Typical error size back in thousands of dollars")

with st.expander("Why squared errors matter"):
    st.write(
        "MSE squares each error, so a miss of 60 counts much more than six misses of 10. "
        "That is useful when large misses are especially painful, but it can also let outliers "
        "dominate the story."
    )

st.header("Try It: Confusion Matrix Tradeoffs")
st.write("Change the counts and watch how accuracy, precision, and recall move differently.")

col1, col2, col3, col4 = st.columns(4)
with col1:
    tp = st.number_input("True positives", min_value=0, value=42)
with col2:
    fp = st.number_input("False positives", min_value=0, value=8)
with col3:
    fn = st.number_input("False negatives", min_value=0, value=15)
with col4:
    tn = st.number_input("True negatives", min_value=0, value=135)

total = tp + fp + fn + tn
accuracy = (tp + tn) / total if total else 0
precision = tp / (tp + fp) if tp + fp else 0
recall = tp / (tp + fn) if tp + fn else 0

m1, m2, m3 = st.columns(3)
with m1:
    metric_card("Accuracy", f"{accuracy:.1%}", "Overall correctness")
with m2:
    metric_card("Precision", f"{precision:.1%}", "How many predicted positives were right")
with m3:
    metric_card("Recall", f"{recall:.1%}", "How many real positives were found")

with st.expander("What this teaches", expanded=True):
    st.write(
        "Accuracy can look strong when the negative class is large. Precision and recall force "
        "you to ask which mistake is more expensive: false positives or false negatives. For AI "
        "systems, this same habit applies to hallucinations, format errors, latency, and cost."
    )

render_navigation(1)
