from rapidfuzz import process

def get_top_matches(query, choices, limit=5):
    return process.extract(query, choices, limit=limit)