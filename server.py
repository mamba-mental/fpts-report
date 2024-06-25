from flask import Flask, request, jsonify, render_template_string
import subprocess
import os
import json
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return render_template_string('<h1>Welcome to the Fundability Report Generator</h1>')

@app.route('/execute', methods=['POST'])
def execute_script():
    data = request.json
    logging.info(f'Received data: {data}')
    
    personal_profile = data.get('personal_profile', {})
    business_profile = data.get('business_profile', {})
    client_name = data.get('client_name', "Client Name")
    company_name = data.get('company_name', "Company Name")
    user_name = data.get('user_name', "User Name")
    date = data.get('date', "Date")

    with open('personal_profile.json', 'w') as f:
        json.dump(personal_profile, f)
    with open('business_profile.json', 'w') as f:
        json.dump(business_profile, f)

    logging.info('Running main.py script...')
    result = subprocess.run(['python', 'main.py', client_name, company_name, user_name, date], capture_output=True, text=True)
    
    logging.info(f'Script output: {result.stdout}')
    logging.error(f'Script error output: {result.stderr}')

    os.remove('personal_profile.json')
    os.remove('business_profile.json')

    return jsonify({'result': result.stdout})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
