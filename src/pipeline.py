import pandas as pd
import re
from rapidfuzz import fuzz

from src.ocr import extract_text
from src.text_cleaning import clean_text


def extract_keywords(text):
    tokens = text.split()

    stopwords = [
        "mg", "ml", "tablet", "tab", "capsule",
        "for", "of", "the", "and", "with", "in"
    ]

    keywords = []

    for t in tokens:
        if (
            t not in stopwords
            and len(t) > 3
            and not t.isdigit()
            and not any(char.isdigit() for char in t)
        ):
            keywords.append(t)

    return list(set(keywords))


class MedicinePipeline:

    def __init__(self, dataset_path):
        self.df = pd.read_csv(dataset_path)

    def predict(self, image_path):
        # OCR
        raw_text, ocr_conf = extract_text(image_path)
        print("RAW OCR:", raw_text)

        # Clean
        cleaned = clean_text(raw_text)
        print("CLEANED:", cleaned)

        # Extract keywords
        keywords = extract_keywords(cleaned)
        print("KEYWORDS:", keywords)

        # Extract numbers (dosage)
        numbers = re.findall(r'\d+', cleaned)

        # Matching
        scores = []

        for _, row in self.df.iterrows():
            name = row["clean_name"]
            company = row["company"]

            score = 0

            for word in keywords:
                # 🔥 FUZZY MATCH (MAIN FIX)
                similarity = fuzz.partial_ratio(word, name)

                if similarity > 85:
                  score += 2
                elif similarity > 70:
                  score += 1

                # company match
                if word in company:
                    score += 4

                # priority boost
                if word in ["para", "cipla"]:
                    score += 2

            # dosage boost
            for num in numbers:
                if num in name:
                    score += 2

            scores.append((name, score))

        # Sort matches
        scores = sorted(scores, key=lambda x: x[1], reverse=True)

        top_matches = scores[:5]
        print("MATCHES:", top_matches)

        best_match, best_score = top_matches[0]

        # Threshold
        if best_score < 3:
            return {
                "error": "Medicine not found",
                "confidence": 0
            }

        # Get row
        row = self.df[self.df["clean_name"] == best_match].iloc[0]

        # Confidence
        confidence = round(min(best_score / 6, 1.0), 2)

        return {
            "medicine_name": row["medicine_name"],
            "company": row["company"],
            "confidence": confidence,
            "top_5": [m[0] for m in top_matches],
            "ocr_text": raw_text
        }