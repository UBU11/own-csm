from transformers import pipeline

try:
    # Using the same model as in senti.py
    pipe = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

    test_sentences = [
        "I love this movie!",
        "This movie was terrible.",
        "It was okay, not great.",
        "Absolute masterpiece.",
        "Waste of time."
    ]

    print("Testing model: sarahai/movie-sentiment-analysis")
    for sentence in test_sentences:
        result = pipe(sentence)[0]
        print(f"Input: {sentence}")
        print(f"Output: {result}")
        print("-" * 20)

except Exception as e:
    print(f"Error loading model: {e}")
