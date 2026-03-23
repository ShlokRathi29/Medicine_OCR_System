from src.pipeline import MedicinePipeline

pipeline = MedicinePipeline("data/medicines_cleaned.csv")

result = pipeline.predict("tests/sample.jpg")

print("\nFINAL RESULT:")
print(result)