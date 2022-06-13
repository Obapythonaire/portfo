from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        
        file = database.write(f"\n{name}, {email}, {subject}, {message}")

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]     
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,subject,message])

@app.route('/')
def home2():
    return render_template('/index.html')

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Data not saved in the database'
    else:
        return 'Something went wrong, try again'

@app.route('/<username>')
def any_user(username=None):
    return render_template('/thankyou.html', name=username)

"""
@app.route('/<username>/<int:post_id>')
def any_user2(username=None, post_id=None):
    return render_template('/index.html', name=username, post_id=post_id)


@app.route('/index.html')
def home():
    return render_template('/index.html')

@app.route('/')
def home2():
    return render_template('/index.html')

@app.route('/about.html')
def about():
    return render_template('/about.html')

@app.route('/work.html')
def work():
    return render_template('/work.html')

@app.route('/works.html')
def works():
    return render_template('/works.html')

@app.route('/contact.html')
def contact():
    return render_template('/contact.html')

@app.route('/')
def hello_world():
    return render_template('/index.html')


@app.route('/<username>')
def any_user(username=None):
    return render_template('/index.html', name=username)

@app.route('/<username>/<int:post_id>')
def any_user2(username=None, post_id=None):
    return render_template('/index.html', name=username, post_id=post_id)

@app.route('/about')
def about():
    return render_template('/about.html')

@app.route('/favicon')
def fav():
    return render_template('/favicon.ico')


@app.route('/blog')
def blog():
    return 'This is another blog post'


@app.route('/blog/2020/dogs')
def blog2():
    return 'This is my dog'

"""