from flask import Flask, render_template, request, redirect
import flask
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('database.csv',mode='a',newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2,delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'






# @app.route('/projects.html')
# def my_projects():
#     return render_template('projects.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')
    
# @app.route('/work.html')
# def work():
#     return render_template('work.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
