from transformers import pipeline



pipe = pipeline("text-classification", model="sarahai/movie-sentiment-analysis")

def analyze_sentiment(text):

    result = pipe(text)[0]
    label = result['label']


    if label == 'LABEL_1':
        result['label'] = 'POSITIVE'
    elif label == 'LABEL_0':
        result['label'] = 'NEGATIVE'

    return result

if __name__ == "__main__":
    ans = analyze_sentiment("I love this movie!")
    print(ans)
    ans = analyze_sentiment("this direct cinamatic angles are so good")
    print(ans)
