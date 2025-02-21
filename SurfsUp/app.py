from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
import datetime as dt

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create and bind the session
Session = sessionmaker(bind=engine)
session = Session()

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route('/')
def welcome():
    return """
        Welcome to the Climate App API!<br/>
        Available Routes:<br/>
        /api/v1.0/precipitation<br/>
        /api/v1.0/stations<br/>
        /api/v1.0/tobs<br/>
        /api/v1.0/<start><br/>
        /api/v1.0/<start>/<end>
        """

@app.route('/api/v1.0/precipitation')
def precipitation():
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.date, Measurement.prcp)\
        .filter(Measurement.date >= one_year_ago)\
        .order_by(Measurement.date.desc())\
        .all()
    precipitation_dict = {date: prcp for date, prcp in results}
    session.close()
    return jsonify(precipitation_dict)

@app.route('/api/v1.0/stations')
def stations():
    session = Session()
    results = session.query(Station.station, Station.name).all()
    session.close()
    stations_list = [{'station': station, 'name': name} for station, name in results]
    return jsonify(stations_list)

@app.route('/api/v1.0/tobs')
def tobs():
    session = Session()
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    most_active_station = session.query(Measurement.station)\
        .group_by(Measurement.station)\
        .order_by(func.count(Measurement.station).desc())\
        .first()[0]
    results = session.query(Measurement.date, Measurement.tobs)\
        .filter(Measurement.station == most_active_station)\
        .filter(Measurement.date >= one_year_ago)\
        .all()
    session.close()
    tobs_list = [{'date': date, 'tobs': tobs} for date, tobs in results]
    return jsonify(tobs_list)

@app.route('/api/v1.0/<start>')
def temperature_stats(start):
    session = Session()
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    results = session.query(*sel).filter(Measurement.date >= start).all()
    session.close()
    temps = list(results[0])
    return jsonify(temps)

@app.route('/api/v1.0/<start>/<end>')
def temperature_stats_range(start, end):
    session = Session()
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    results = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    session.close()
    temps = list(results[0])
    return jsonify(temps)

if __name__ == '__main__':
    app.run(debug=True)

