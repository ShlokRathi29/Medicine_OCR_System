# Medicine OCR & Information Retrieval System

## Overview

This project is an intelligent system that:

* Extracts text from medicine package images using OCR
* Identifies the medicine name, company, and relevant details
* Matches extracted text with a dataset
* Returns:

  * Best matched medicine
  * Confidence score
  * Top 5 similar suggestions
  * Full medicine details

The system is designed to work even with **partial, noisy, or damaged images**.

---

##  Features

* OCR-based text extraction (EasyOCR)
* Text cleaning and normalization
* Keyword extraction from noisy OCR output
* Fuzzy matching using RapidFuzz
* Weighted scoring system:

  * Medicine name match
  * Company name match
  * Dosage detection (e.g., 500mg)
* Confidence scoring
* Safe failure handling ("Medicine not found")

---

## Project Structure

```
medicine-ocr-system/
│
├── data/
│   └── medicines_cleaned.csv
│
├── src/
│   ├── preprocessing.py
│   ├── ocr.py
│   ├── text_cleaning.py
│   ├── matcher.py
│   ├── pipeline.py
│
├── tests/
│   └── sample.jpg
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone <https://github.com/ShlokRathi29/Medicine_OCR_System.git>
cd medicine-ocr-system
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Usage

1. Place your test image inside:

```
tests/sample.jpg
```

2. Run the system:

```bash
python main.py
```

---

##  Output Example

```json
{
  "medicine_name": "paracip 500 tablet",
  "company": "cipla ltd",
  "confidence": 0.87,
  "top_5": [
    "paracip 500 tablet",
    "paracip 650 tablet",
    "paracip syrup",
    "paracip infusion",
    "paracip suspension"
  ],
  "ocr_text": "raw extracted text from image"
}
```

---

## How It Works

### 1. OCR Extraction

* Uses EasyOCR to extract text from images

### 2. Text Cleaning

* Removes noise, symbols, and unwanted characters

### 3. Keyword Extraction

* Filters meaningful tokens (e.g., `paracip`, `cipla`)

### 4. Matching Engine

* Fuzzy matching (RapidFuzz)
* Weighted scoring:

  * Name similarity
  * Company match
  * Dosage match

### 5. Ranking

* Top 5 matches returned

---

## Limitations

* OCR may fail on:

  * Extremely blurred images
  * Handwritten text
* Similar medicine names can cause confusion
* Accuracy depends on dataset quality

---

##  Future Improvements

*  Embedding-based semantic search
*  Barcode scanning support
*  API integration (FastAPI)
*  Mobile deployment
*  Multi-language OCR support

---

## Tech Stack

* Python
* EasyOCR
* OpenCV
* Pandas
* RapidFuzz

---

## Contribution

Feel free to fork and improve:

* Matching algorithms
* OCR preprocessing
* Dataset quality


```
