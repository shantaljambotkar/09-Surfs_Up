from flask import Flask
app = Flask(__name__)
@app.route('/') # decorator # run this in anaconda promt - (flask run)

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation \n
    /api/v1.0/stations \n
    /api/v1.0/tobs \n
    /api/v1.0/temp/start/end
    ''')

@app.route('/api/v1.0/precipitation') # to create another tab
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()                        #the date and precipitation for the previous year
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)


# @app.route('/api/v1.0/stations') # to create another tab
# def stations():
#     return 'stations check'


# @app.route('/api/v1.0/tobs') # to create another tab
# def MonthlyTemperature():
#     return 'Monthly Temperature check'


# @app.route('/api/v1.0/temp/start/end') # to create another tab
# def statistics():
#     return 'statistics check'


if __name__ =='__main__':
    app.run(debug == 'True')

