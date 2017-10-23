from flask import Flask, render_template
#import urllib2
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
import json

app = Flask(__name__)

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
@app.route('/')
def index():

    response        = urllib2.urlopen('https://data.pa.gov/resource/kbfj-5adf.json')
    data  = json.load(response)
    SchoolYear	              = data["SchoolYear"]
    SchoolYearEndDate         = data["SchoolYearEndDate"]
    LocalEducationalAgency    = data["LocalEducationalAgency"]
    SchoolName	              = data["SchoolName"]
    AdministrativeUnitNumber  = data["AdministrativeUnitNumber"]
    SchoolNumber	          = data["SchoolNumber"]
    DataElement	              = data["DataElement"]
    DisplayValue               = data["DisplayValue"]

    SchoolRecords = []

    for school_record in data:
        record_tuple = (timestamp, school_record["SchoolYear"], school_record["SchoolYearEndDate"], school_record["LocalEducationalAgency"], school_record["SchoolName"])
        SchoolRecords.append(record_tuple)

    return render_template('index.html', records=SchoolRecords)


if __name__ == '__main__':
    # Starts the Flask application server
    app.run(debug=True)
