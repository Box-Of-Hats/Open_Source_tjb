from flask import Flask, render_template, request, flash
from forms import DataForm

 
app = Flask(__name__) 
#app.secret_key = 'development key' #Can be changed. Should be hard to guess. Allows authentication


app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html')
 
@app.route('/one')
def one():
    return render_template('one.html')

@app.route('/datarequest', methods=['GET', 'POST'])
def contact():
    form = DataForm(csrf_enabled=False)

    if request.method == 'POST':
        return 'Name: {} Username: {}'.format(request.form['name'], request.form['username'])
        #return 'Form posted.'
 
    elif request.method == 'GET':
        return render_template('dataform.html', form=form)


if __name__ == '__main__':
  app.run(debug=True)