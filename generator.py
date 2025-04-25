
from flask import Flask, render_template_string
import random

app = Flask(__name__)

quotes = ['The only way to do great work is to love what you do. - Steve Jobs',
       'In the middle of every difficulty lies opportunity. - Albert Einstein', 
       'The best way to predict the future is to create it. - Peter Drucker',
       'Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill',
       'The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt',
       "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
       'The secret of getting ahead is getting started. - Mark Twain',
       'Well done is better than well said. - Benjamin Franklin',
       'You miss 100% of the shots you don\'t take. - Wayne Gretzky']

template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Quote Generator</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            max-width: 800px; 
            margin: 40px auto; 
            padding: 20px;
            text-align: center;
        }
        .quote {
            font-size: 24px;
            padding: 20px;
            margin: 20px 0;
            background: #f5f5f5;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        button {
            padding: 10px 20px;
            font-size: 18px;
            background: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background: #0056b3;
        }
    </style>
</head>
<body>
    <h1>Inspirational Quote Generator</h1>
    <div class="quote">{{ quote }}</div>
    <form method="get">
        <button type="submit">Generate New Quote</button>
    </form>
</body>
</html>
'''

@app.route('/')
def home():
    quote = random.choice(quotes)
    return render_template_string(template, quote=quote)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
