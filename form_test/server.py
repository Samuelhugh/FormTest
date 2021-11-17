from flask import Flask, render_template, request, redirect, session
from env import key
app = Flask(__name__)
app.secret_key = key  # Set a Secret Key for Security Purposes.


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users', methods=['POST']) # METHODS not METHOD, Also Methods can have a number of other values (i.e "GET") because the values are store in a List.
def create_user():
    print('Got Post Info')
    print(request.form)
    # Adding the Two Properties to Session to store the Name and Email.
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    # Never Render a Template on a POST request.
    # Instead I will Redirect to my Index Route.
    return redirect('/show') # Redirecting.


# adding this method
@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("show.html", name_on_template=session['username'], email_on_template=session['useremail'])


if __name__ == '__main__':
    app.run(debug=True)