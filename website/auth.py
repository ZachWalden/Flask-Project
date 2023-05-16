from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data.get("email"), "PRINTED")
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
    
    #categories can be any var name, 
        if len(email) < 4:
            flash('Email must be at least 5 characters', category='error')
        elif len(firstName) < 2:
            flash('first name must be at least 3 characters', category='error')
        elif password1 != password2:
            flash('Passwords do no match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            flash('Accounted Created', category='success')

    return render_template("register.html")
