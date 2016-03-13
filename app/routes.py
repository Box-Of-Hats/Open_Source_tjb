from flask import Flask, render_template, request, flash
from forms import DataForm

from flask import request, jsonify

app = Flask(__name__) 
#app.secret_key = 'development key' #Can be changed. Should be hard to guess. Allows authentication

@app.route('/')
def home():
  return render_template('home.html')
 
@app.route('/results', methods=['GET', 'POST'])
def one():
    if request.method == 'POST':
        imgs = ['static/img/eximg1.png',
                'static/img/eximg2.png',
                'static/img/eximg3.png']
        return render_template('results.html', form=request.form, imglist=imgs)

    elif request.method == 'GET':
        return render_template('dataform.html')

@app.route('/datarequest', methods=['GET', 'POST'])
def input_form():
    def build_page(request):
            return request.form['name']

    form = DataForm(csrf_enabled=False)

    if request.method == 'POST':
        #return 'Name: {} Username: {}'.format(request.form['name'], request.form['username'])
        #return 'Form posted.'
        return build_page(request)
 
    elif request.method == 'GET':
        return render_template('dataform.html', form=form)



if __name__ == '__main__':
  app.run(debug=True)