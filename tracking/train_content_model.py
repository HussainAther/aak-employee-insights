# tracking/train_content_model.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd


def load_labeled_behavior_data():
    """
    Simulated labeled session descriptions for supervised training.
    Replace this with real logs once collected.
    """
    data = [
        ("Wrote clean code with modular structure and comments", "best_practice"),
        ("Clicked randomly and opened multiple non-work tabs", "off_task"),
        ("Consistent typing in VSCode, used testing libraries", "best_practice"),
        ("Idle for long periods, unrelated application in focus", "off_task"),
        ("Integrated API endpoints and documented everything", "best_practice"),
        ("Switching between YouTube and WhatsApp desktop", "off_task")
    ]
    return pd.DataFrame(data, columns=["session_notes", "label"])


def train_behavior_model():
    df = load_labeled_behavior_data()
    X_train, X_test, y_train, y_test = train_test_split(
        df["session_notes"], df["label"], test_size=0.2, random_state=42
    )

    model = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', MultinomialNB())
    ])

    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print("\n🧪 Evaluation Report:\n")
    print(classification_report(y_test, preds))

    return model


if __name__ == "__main__":
    train_behavior_model()
