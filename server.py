from flask import Flask, render_template, request, redirect,session,flash
import random
app = Flask(__name__)
app.number = random.randint(1,100)
app.secret_key = 'secretkey'

@app.route('/')
def index():
    if 'generated' not in session:
        session['generated'] = random.randint(1,100)
    else:
        pass
    if "tries" not in session:
        session['tries'] = 0
    if session['tries'] == 5:
         flash('You lose', 'game_lost')
    
    return render_template('index.html')

   

@app.route('/guess_number', methods=['POST'])
def create_user():
    guess = request.form['guessed_number']
    print(session['generated'])
    if int(guess) == int(session['generated']):
        flash('Correct', 'success')
        return redirect('/')
    elif int(guess) > int(session['generated']):
        flash('Too high', 'error')
    else:
        flash('Too low', 'error')
 
    
    session['tries'] = session['tries'] + 1
    return redirect("/")

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    session.clear()
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)