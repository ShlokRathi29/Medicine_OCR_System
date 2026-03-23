import easyocr

reader = easyocr.Reader(['en'])

def extract_text(image_path):
    result = reader.readtext(image_path)

    texts = []
    confidences = []

    for (_, text, conf) in result:
        texts.append(text)
        confidences.append(conf)

    full_text = " ".join(texts)
    avg_conf = sum(confidences) / len(confidences) if confidences else 0

    return full_text, avg_conf