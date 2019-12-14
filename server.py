from flask import Flask, render_template, request, redirect,session,flash
import random
app = Flask(__name__)
app.number = random.randint(1,100)
app.secret_key = 'secretkey'

@app.route('/')
def index():
    game_info = {
        "message": None,
        "css_class": None
    }
    if 'generated' not in session:
        session['generated'] = random.randint(1,100)
    if "tries" not in session:
        session['tries'] = 0
        
 
    if "guess" not in session:
        game_info["message"] = "Take a guess!"
        game_info['css_class'] = "yellow"
    elif int(session['tries']) > 4:
        game_info["message"] = "You lose!"
        game_info["css_class"] = "red"
    elif int(session["guess"] )> int(session["generated"]):
        game_info["message"] = "Too high!"
        game_info['css_class'] = "red"
    elif int(session["guess"]) < int(session["generated"]):
        game_info["message"] = "Too low!"
        game_info['css_class'] = "red"
    else:
        game_info["message"] = f"{session['generated']} was the number!"
        game_info['css_class'] = "green"
    
    return render_template('index.html',info = game_info)

   

@app.route('/process', methods=['POST'])
def create_user():
    session['guess'] = request.form['guessed_number']    
    session['tries'] += 1
    return redirect("/")

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    session.clear()
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)