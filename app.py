import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt


#generates the engine to the correct sqlite file
engine = create_engine("sqlite:///Resources/hawaii.sqlite?check_same_thread=False")

# Uses automap_base() and reflects the database schema
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the tables in the sqlite file (measurement and station)
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask Setup - create app construct an application - instance
app = Flask(__name__)

# Flask Routes define endpoints
@app.route("/")
def index():
    """List all available api routes."""
    return (
        f"Available Routes-format for dates: 2014-05-02<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/station<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/<start><br/>" 
        f"/api/v1.0/temp2/<start>/<end><br/>"
    )

# 1 Precipitation route 
#  Returns the jsonified precipitation data for the last year in the database
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link),
    # binds the session between the python app and database
    session = Session(engine)

    # Return a list of all dates and rain names, query last year of rain
    minus_year = str(dt.date(2017, 8, 23) - dt.timedelta(days=365))
    #minus_year = str(dt.date(int(max_date_split[0]), int(max_date_split[1]), int(max_date_split[2])) - dt.timedelta(days=365))

    # Perform a query to retrieve the date and precipitation scores
    ###  results for the last year of data (note that the last day in the dataset is 8/23/2017)
    precipitation = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date > minus_year)\
        .filter(Measurement.prcp>=0).order_by(Measurement.date).all()
    session.close()

    # Convert list of tuples into normal list json with the date as the key and the value as the precipitation
    precip = []
    for date, rain in precipitation:
        precip_dict = {}
        precip_dict[date] = rain
        precip.append(precip_dict)

    return jsonify(precip)

# 2 Stations route
# Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/station")
def station():
    # Create our session (link) 
    # and binds the session between the python app and database
    session = Session(engine)

    # Query all stations
    station_data = session.query(Station.name).all()
    session.close()

    # Return a JSON list of stations from the dataset.
    all_stations = list(np.ravel(station_data))
    return jsonify(all_stations)

# 3 Tobs route
#  Returns jsonified data for the most active station (USC00519281) for the last year of data
@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) 
    # and binds the session between the python app and database
    session = Session(engine)
    # Query all temp
    minus_year = str(dt.date(2017, 8, 23) - dt.timedelta(days=365))
    temp_query = session.query(Measurement.date, Measurement.prcp, Measurement.tobs).filter(Measurement.date >= minus_year)\
    .filter(Measurement.tobs>=0).filter(Measurement.station== 'USC00519281').all()
    # results = session.query(Measurement.date, Measurement.tobs).all()

    session.close()
    all_data = []
    for date, prcp, tobs in temp_query:
        data_dict = {}
        data_dict["Date"] = date
        data_dict["Precipitation"] = prcp
        data_dict["Temperature"] = tobs
        all_data.append(data_dict)
 #   station_list = list(np.ravel(results))  # may not need???
    return jsonify(all_data)

# 4-5 Start route
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
# When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.
# 4 Route accepts the start dateas a parameter from the URL
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp2/<start>/<end>")
def stats(start=None, end=None):
    """Return TMIN, TAVG, TMAX."""
    # Create our session (link) 
    # and binds the session between the python app and database
    session = Session(engine)
    
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    
    if not end:
        #  Returns the min, max, and average temperatures calculated from the given start date to the end of the dataset
        route = session.query(*sel).filter(Measurement.date >= start).all()
        # Return a JSON list from the dataset, unravel
        temps = list(np.ravel(route))
        return jsonify(temps)
# Returns the min, max, and average temperatures calculated from the given start date to the given end date
    else:
        route = session.query(*sel).filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
        # Return a JSON list from the dataset.
        temps = list(np.ravel(route))
        return jsonify(temps)

# run app application, debug to True and auto load code after changes
if __name__ == '__main__':
    app.run(debug=True)


