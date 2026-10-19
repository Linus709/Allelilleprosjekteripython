from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def reisen():
    url = "https://api.entur.io/journey-planner/v3/graphql"
    headers = {
        "ET-Client-Name": "mitt-skoleprosjekt-app"
    }

    query = """
    {
      trip(
        from: {
          name: "Stockfleths gate 38B"
          coordinates: { latitude: 59.9333, longitude: 10.7529 }
        }
        to: {
          name: "Aker Brygge, Oslo"
          coordinates: {
            latitude: 59.9114
            longitude: 10.7291
          }
        }
        numTripPatterns: 3
        dateTime: "2026-10-16T09:38:00.999+02:00"
        walkSpeed: 1.3
        arriveBy: false
      ) {
        tripPatterns {
          expectedStartTime
          duration
          streetDistance
          legs {
            mode
            distance
            line {
              id
              publicCode
            }
          }
        }
      }
    }
    """

    response = requests.post(url, json={'query': query}, headers=headers)

    if response.status_code == 200:
        api_data = response.json()
    else:
        api_data = {"feil": "fikk ikke hentet data"}

    return render_template("design.html", data=api_data)

if __name__ == "__main__":
    app.run(debug=True)