import os
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'kyara_secret'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    print(f"New message from {name} ({email}): {message}")

    flash('Thanks for contacting us! We’ll get back to you soon.')
    return redirect('/')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


