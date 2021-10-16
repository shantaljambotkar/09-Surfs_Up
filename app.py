# import dependencies
import datetime as dt
import numpy as np
import pandas as pd


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite") # create the engine to get in touch with the database

Base = automap_base() #map the tables

Base.prepare(engine, reflect=True) # to reflect the code

Measurement = Base.classes.measurement # call the class and get the tables
Station = Base.classes.station

session = Session(engine)

app = Flask(__name__)

@app.route("/")
# Our welcome function
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
@app.route("/api/v1.0/precipitation")

def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()    #the date and precipitation for the previous year.
   precip = {date: prcp for date, prcp in precipitation}  #dictionary comprehension
   return jsonify(precip)

@app.route("/api/v1.0/stations")

def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results)) # convert the results in array form to list form
    return jsonify(stations=stations) # jasonify the stations 

@app.route("/api/v1.0/tobs")

def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
    filter(Measurement.date >= prev_year).\
    filter(Measurement.station == 'USC00519281').all() #the primary station for all the temperature observations from the previous year
    temps = list(np.ravel(results)) # convert the results in array form to list form
    return jsonify(temps=temps)

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        #Here the asterisk is used to indicate there will be multiple results for our query: minimum, average, and maximum temperatures.
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)
    # results based on a range of dates
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
    
   


