# Name Redirector

A simple Flask application that takes user input and redirects to a custom URL.

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to:
```
http://localhost:5000
```

## How it Works

1. User enters their name in the HTML form
2. Form is submitted to the `/submit` endpoint
3. Python backend redirects to `abc.{name}` where `{name}` is the user input

## Files

- `app.py` - Python Flask backend
- `templates/index.html` - HTML form page
- `requirements.txt` - Python dependencies
