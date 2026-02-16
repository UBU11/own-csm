from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
import uvicorn
from jinja2 import Template


try:
    from models.Text.sentimental_analysis.senti import analyze_sentiment
except ImportError:
    print("Error importing sentiment analysis module. Make sure 'models' is in the python path.")
    def analyze_sentiment(text):
        return {'label': 'NEUTRAL', 'score': 0.5}

app = FastAPI()


html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Movie Review Sentiment Analysis</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f4f9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            width: 100%;
            max-width: 500px;
            text-align: center;
        }
        h1 {
            color: #333;
            margin-bottom: 1.5rem;
        }
        textarea {
            width: 100%;
            height: 150px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            resize: vertical;
            margin-bottom: 1rem;
            font-size: 16px;
        }
        button {
            background-color: #007bff;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #0056b3;
        }
        .result {
            margin-top: 2rem;
            padding-top: 1rem;
            border-top: 1px solid #eee;
        }
        .stars {
            font-size: 2rem;
            color: #ccc;
        }
        .stars .filled {
            color: #ffc107;
        }
        .rating-text {
            font-size: 1.2rem;
            font-weight: bold;
            color: #555;
            margin-top: 0.5rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Movie Review Analyzer</h1>
        <form action="/sentiment" method="post">
            <textarea name="comment" placeholder="Write your movie review here..." required>{{ comment }}</textarea>
            <br>
            <button type="submit">Analyze Sentiment</button>
        </form>

        {% if rating is not none %}
        <div class="result">
            <div class="stars">
                {% for i in range(1, 6) %}
                    <span class="{% if i <= rating %}filled{% endif %}">★</span>
                {% endfor %}
            </div>
            <div class="rating-text">Rating: {{ rating }}/5</div>
            <p>Sentiment: <strong>{{ label }}</strong></p>
            <p>Normalized Score: <strong>{{ normalized_score }}</strong> (Model Confidence: {{ (score * 100)|round(1) }}%)</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def read_root():
    template = Template(html_template)
    return HTMLResponse(content=template.render(rating=None, comment=""), status_code=200)

@app.get("/sentiment", response_class=HTMLResponse)
async def get_sentiment():
    template = Template(html_template)
    return HTMLResponse(content=template.render(rating=None, comment=""), status_code=200)

@app.post("/sentiment", response_class=HTMLResponse)
async def analyze_sentiment_post(comment: str = Form(...)):

    result = analyze_sentiment(comment)
    label = result['label']
    score = result['score']




    normalized_score = score if label == "POSITIVE" else (1 - score)



    if normalized_score <= 0.2:
        rating = 1
    elif normalized_score <= 0.4:
        rating = 2
    elif normalized_score <= 0.6:
        rating = 3
    elif normalized_score <= 0.8:
        rating = 4
    else:
        rating = 5

    template = Template(html_template)
    rendered_html = template.render(
        comment=comment,
        rating=rating,
        label=label,
        score=score,
        normalized_score=round(normalized_score, 4)
    )

    return HTMLResponse(content=rendered_html, status_code=200)

@app.get("/api/v1/hello")
def read_hello():
    return {"message": "Hello form FastAPI"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
