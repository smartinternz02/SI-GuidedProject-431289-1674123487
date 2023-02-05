from flask import Flask, render_template, request # Flask is a application
# used to run/serve our application
# request is used to access the file which is uploaded by the user in out application
# render_template is used for rendering the html pages
import pickle # pickle is used for serializing and de-serializing Python object structures

model = pickle.load(open(r'F:/notebook/jojo/prediction/CCPP.pkl','rb'))

app=Flask(__name__)

@app.route('/') # rendering the html template
def home():
    return render_template('index.html')
@app.route('/predict') # rendering the html template
def index():
    return render_template("index.html")

@app.route('/data_predict', methods=['POST']) # route for our prediction 
def predict():
    qa = request.form['qa'] # requesting for age data
    day = request.form['day'] # requesting for gender data
    tp = request.form['tp'] # requesting for Total_Bilirubin data 
    ot = request.form['ot']
    it = request.form['it']
    nsc = request.form['nsc']
    month = request.form['month']
    dp = request.form['dp']
    tm = request.form['tm']
    smv = request.form['smv']
    inc = request.form['inc']
    im = request.form['im']
    now = request.form['now']
    # requesting for Direct_Bilirubin data
    # coverting data into float format
    data = [[float(qa), float(day), float(tp), float(ot),float(it),float(nsc),float(month),float(dp),float(tm),float(smv),float(inc),float(im),float(now)]]
    # Loading model which we saved
    model = pickle.load(open('CCPP.pkl', 'rb'))
    prediction= model.predict(data)[0]
    return render_template('index.html', prediction_text = 'Prediction of electric output is {}'.format(prediction))

if __name__=='__main__':
    app.run()
