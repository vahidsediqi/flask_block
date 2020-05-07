from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
from models import User, Post




posts = [
    {
        'author': 'Vahid Sediqi',
        'title': 'Python Programming in 2020',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore quasi, tempora minus nesciunt doloremque, harum dolor magnam perspiciatis quas quos ab nemo voluptatum fugit dolores?',

        'date_posted': '20/08/2019',
        'liked': 15
        
    },

    {
        'author': 'Kabir Khan',
        'title': 'Animation with JavaScript',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore quasi, tempora minus nesciunt doloremque, harum dolor magnam perspiciatis quas quos ab nemo voluptatum fugit dolores?',

        'date_posted': '16/12/2018',
        'liked': 250
    },
      {
        'author': 'Ali Khan',
        'title': 'ReactJs VS AngularJs',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore quasi, tempora minus nesciunt doloremque, harum dolor magnam perspiciatis quas quos ab nemo voluptatum fugit dolores?',

        'date_posted': '20/03/2020'
    },
      {
        'author': 'Zaki Khan',
        'title': 'Python for developers',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore quasi, tempora minus nesciunt doloremque, harum dolor magnam perspiciatis quas quos ab nemo voluptatum fugit dolores?',

        'date_posted': '20/03/2020'
    }
]

index_title='Welcome'
@app.route('/')
def index():
    return render_template('index.html', title=index_title)

@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='Welcome to our Blog Posts')



@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created Successfully for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'vahid@gmail.com' and form.password.data == '1122':
            flash('Logged in successfully', 'success ' )
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password!', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)

   
