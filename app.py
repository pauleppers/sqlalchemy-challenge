import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup - create app
# construct an application - instance
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
# define endpoints
@app.route("/")
def index():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/station<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>" 
        f"/api/v1.0/<start>/<end><br/>"
    )

# 1 Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all dates and rain names"""
    # Query all passengers
    results = session.query(Measurement.date, Measurement.prcp).all()
    session.close()

    # Convert list of tuples into normal list
    precip = []
    for date, rain in results:
        precip_dict = {}
        precip_dict[date] = rain
        precip.append(precip_dict)

    return jsonify(precip)

# 2 Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/station")
def station():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of stations data"""
    # Query all stations
    station_data = session.query(Station.name).all()
    session.close()

    # Return a JSON list of stations from the dataset.
    all_stations = list(np.ravel(station_data))
    return jsonify(all_stations)

# Query the dates and temperature observations of the most active station for the last year of data.
# Return a JSON list of temperature observations (TOBS) for the previous year.
# @app.route("/api/v1.0/tobs")
# def tobs():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of all passenger names"""
#     # Query all passengers
#     results = session.query(Station.station).all()

#     session.close()

#     return jsonify(all_passengers)

#Return a JSON list of temperature observations (TOBS) for the previous year.
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
# When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

# @app.route("/api/v1.0/one-date/<date1>")
# def date1(date1):
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of all passenger names"""
#     # Query all passengers
#     results = session.query(Passenger.name).all()

#     session.close()
#     @app.route("/api/v1.0/precipitation")
#     return jsonify(date1)

# def precipitation():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of all passenger names"""
#     # Query all passengers
#     results = session.query(Passenger.name).all()

#     session.close()
#     return jsonify(all_passengers)  

# run app application, debug to True and auto load code after changes
if __name__ == '__main__':
    app.run(debug=True)


#   all_stations = []
#     for name, age, sex in results:
#     #     passenger_dict = {}
#     #     passenger_dict["name"] = name
#     #     passenger_dict["age"] = age
#     #     passenger_dict["sex"] = sex
#     #     all_passengers.append(passenger_dict)
#     station_list = list(np.ravel(results))  # may not need???
#     return jsonify(all_passengers)