from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_plan():

    subjects = request.form['subjects']
    hours = request.form['hours']
    weak_subject = request.form['weak']

    plan = f"""
    Study Plan:
    
    • Focus more on {weak_subject}
    • Study {hours} hours daily
    • Revise important topics every weekend
    • Practice coding/problem-solving daily
    • Maintain short notes for revision
    """

    return render_template('index.html', plan=plan)

if __name__ == '__main__':
    app.run(debug=True)