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
          coordinates: { latitude: 59.96050414081307, longitude: 11.040338686322317 }
          name: "Stockfleths gate 38B"
        }
        to: {
          place: "NSR:StopPlace:385"
          name: "Økern, Oslo"
        }
        numTripPatterns: 3
        dateTime: "2026-10-15T09:33:53.756+02:00"
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