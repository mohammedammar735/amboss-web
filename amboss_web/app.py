
from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_account', methods=['POST'])
def create_account():
    try:
        result = subprocess.run(["python3", "amboss_signup.py"], capture_output=True, text=True)
        return jsonify({"output": result.stdout.strip(), "error": result.stderr.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
