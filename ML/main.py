from flask import Flask, render_template, request
import torch
from transformers import pipeline

app = Flask(__name__)

hf_name = 'facebook/bart-large-cnn'
summarizer = pipeline(
    "summarization",
    hf_name,
    device=-1  # forces CPU
)

@app.route('/', methods=['GET', 'POST'])
def index():
    print("\n=== New Request ===")  # debugging
    
    if request.method == 'POST':
        print("POST request received")
        print(f" form data: {request.form}")
        
        user_input = request.form.get('user_text', '').strip()
        print(f"🔠 input text length: {len(user_input)} characters")
        
        if user_input:
            try:
                print("starting summary")
                summary = summarizer(
                    user_input,
                    max_length=1000,      
                    min_length=30,       
                    do_sample=False      #adds randomness/diversity to txt
                )
                print("summarization complete!")
                return render_template('index.html', 
                                     summary=summary[0]['summary_text'],
                                     original_text=user_input)
                
            except Exception as e:
                error_msg = f" error: {str(e)}"
                print(error_msg)
                return render_template('index.html', 
                                     summary=error_msg,
                                     original_text=user_input)
    
    # Default return for GET requests or empty POST
    return render_template('index.html', 
                         summary=None,
                         original_text=None)

if __name__ == '__main__':
    # debugging / progress
    print("!!!warming up model...")
    summarizer("warmup", max_length=30, min_length=10)
    
    # running the app
    print("!!!server starting at http://127.0.0.1:5002")
    app.run(host='0.0.0.0', port=5002, debug=True)