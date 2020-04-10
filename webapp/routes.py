from flask import render_template,url_for
from webapp import app

post = [

	{
		'author':'Marco Montez',
		'title': 'Blog Post 1',
		'content':'First post content',
		'date_posted':'April 10,2020'													
	},
	{
		'author':'Jane Doe',
		'title': 'Blog Post 2',
		'content':'Second post content',
		'date_posted':'April 11,2020'														
	}

]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts = post,title='Home')
    
@app.route('/about')
def about():
    return render_template('about.html',posts = post,title='About') 