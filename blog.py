from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '39dc2832779e81ccbf7b64f70f4c9eaa'

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

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)

   
