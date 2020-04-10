from flask import Flask, render_template

app = Flask(__name__)

post = [

	{
		'author':'Marco Montez',
		'title': 'BLog Post 1',
		'content':'First post content',
		'date_posted':'April 10,2020'													
	},
	{
		'author':'Jane Doe',
		'title': 'BLog Post 2',
		'content':'Second post content',
		'date_posted':'April 11,2020'														
	}

]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts = post)
    
@app.route('/about')
def about():
    return render_template('about.html') 