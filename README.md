# SQLAlchemy Challenge - Surfs Up!

![image](https://github.com/user-attachments/assets/64c2ab42-8090-4161-b605-0b8b31d6a12a)

This repository is designed to make a climate analysis on Honolulu, Hawaii, to help clients trip planning, and outline when they can plan their vacation.

# Honolulu Climate Analysis and Flask API

# Introduction
This project involves performing a climate analysis of Honolulu, Hawaii, to help with trip planning. It includes analyzing climate data and creating a Flask API to share the findings.

# Getting Started
Follow these instructions to get a copy of the project up and running on your local machine.

# Prerequisites

- Python 3.6 or later

- SQLite

- Flask

- SQLAlchemy

- Pandas

- Matplotlib

# Installation

1. Clone the repository

2. Create a virtual environment

3. Install the dependencies

4. Set up the database:

  - Ensure the hawaii.sqlite file is in the Resources directory.

# Usage

# Running the Climate Analysis

1. Open the Jupyter Notebook

2. Run climate_starter.ipynb:

  - Follow the steps to perform the precipitation and station analysis.

# Running the Flask API

1. Start the Flask server

2. Access the API endpoints:

- Open your browser or use a tool like curl or Postman to access the endpoints listed 
  below.

# API Endpoints

- /api/v1.0/precipitation:

  - Returns JSON representation of the last 12 months of precipitation data.

- /api/v1.0/stations:

  - Returns a JSON list of all stations in the dataset.

- /api/v1.0/tobs:

  - Returns a JSON list of temperature observations for the most-active station for the 
    previous year.

- /api/v1.0/<start>:

  - Returns the minimum, average, and maximum temperatures from the given start date to     the end of the dataset.

- /api/v1.0/<start>/<end>:

  - Returns the minimum, average, and maximum temperatures from the start date to the       end date.

# License

This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments
- Elizabeth Jones

