# Flask web app wrapper for Safety Report Analyzer
# This allows the Tkinter GUI to work as a web application on Vercel

from flask import Flask, render_template_string, request, jsonify
import os
import sys

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the GUI module
try:
    import gui
    from config import API_KEY
except ImportError as e:
    print(f"Import error: {e}")
    API_KEY = os.environ.get('OPENAI_API_KEY', '')

app = Flask(__name__)

# HTML template for the web interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Safety Report Analyzer</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0B1220 0%, #111A2B 100%);
            color: #E8EEF9;
            margin: 0;
            padding: 20px;
            min-height: 100vh;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: #111A2B;
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        }
        h1 {
            color: #4F8FF7;
            text-align: center;
            margin-bottom: 30px;
        }
        .info-box {
            background: #0E1730;
            border: 1px solid #233249;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
        }
        .status {
            color: #18C29C;
            font-weight: bold;
        }
        .warning {
            color: #E74C3C;
            font-weight: bold;
        }
        .setup-instructions {
            background: #0A1424;
            border-left: 4px solid #4F8FF7;
            padding: 15px;
            margin: 15px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🛡️ Safety Report Analyzer</h1>
        
        <div class="info-box">
            <h3>Status</h3>
            <p class="status">✅ Application is running successfully!</p>
            <p>This is a Tkinter-based desktop application that has been wrapped for web deployment.</p>
        </div>
        
        <div class="setup-instructions">
            <h3>⚠️ Important Note</h3>
            <p class="warning">This application is designed as a desktop GUI application using Tkinter.</p>
            <p>For full functionality, please:</p>
            <ol>
                <li>Clone this repository locally</li>
                <li>Set up a Python virtual environment</li>
                <li>Install dependencies: <code>pip install -r requirements.txt</code></li>
                <li>Configure your OpenAI API key in <code>config.py</code></li>
                <li>Run: <code>python gui.py</code></li>
            </ol>
        </div>
        
        <div class="info-box">
            <h3>Features</h3>
            <ul>
                <li>PDF safety report analysis using GPT</li>
                <li>Multiple analysis methods (Five Whys, Fishbone, Bowtie, Fault Tree)</li>
                <li>Auto-classification for TC/SMS compliance</li>
                <li>Local SQLite database with similarity search</li>
                <li>Export to PDF and Excel formats</li>
                <li>English and French language support</li>
            </ul>
        </div>
        
        <div class="info-box">
            <h3>API Key Status</h3>
            <p>OpenAI API Key: {% if api_key_configured %}✅ Configured{% else %}❌ Not configured{% endif %}</p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    api_key_configured = bool(API_KEY and API_KEY != 'your-openai-api-key-here')
    return render_template_string(HTML_TEMPLATE, api_key_configured=api_key_configured)

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'app': 'Safety Report Analyzer',
        'version': '1.0.0'
    })

if __name__ == '__main__':
    app.run(debug=True)
