from flask import Flask, render_template, request
import torch
from transformers import pipeline

app = Flask(__name__)

hf_name = 'facebook/bart-large-cnn'
summarizer = pipeline(
    "summarization",
    hf_name,
    device=-1  # Force CPU
)

@app.route('/', methods=['GET', 'POST'])
def index():
    print("\n\n--- New Request ---")  # Debug line
    
    if request.method == 'POST':
        print("POST request received!")  # Debug line
        print("Form data:", request.form)  # Debug line
        
        user_input = request.form.get('user_text', '').strip()
        print(f"Input text length: {len(user_input)} chars")  # Debug line
        
        if user_input:
            # For testing, use a hardcoded string
            test_input = "The quick brown fox jumps over the lazy dog. " * 5
            summary = summarizer(test_input, max_length=50)
            return render_template('index.html', summary=summary[0]['summary_text'])
    
    # This handles both:
    # 1. Initial GET requests (first page load)
    # 2. Cases where no user_input was provided
    return render_template('index.html', summary=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)