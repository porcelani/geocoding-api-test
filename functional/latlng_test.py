# coding: utf-8
import json
import os

import requests

geocodingUrl = "https://maps.googleapis.com/maps/api/geocode/json?latlng={latlng}&key={key}"

latlngs = [
    "40.7053762,-73.9335617",
    "-22.9191206,-43.1907328",
    "37.422617,-122.0853839",
    "0,0"

]


def recreate_asserts():
    for latlng in latlngs:
        response = requests.get(geocodingUrl.format(latlng=latlng, key=os.environ['API_KEY']))

        assert response.status_code is 200
        with open('latlng/' + latlng + '.json', 'w') as outfile:
            json.dump(response.json(), outfile, sort_keys=True, indent=4, separators=(',', ': '))


def test_latlng_request():
    for latlng in latlngs:
        response = requests.get(geocodingUrl.format(latlng=latlng, key=os.environ['API_KEY']))

        assert response.status_code is 200
        response_json = json.dumps(response.json(), sort_keys=True, indent=4, separators=(',', ': '))

        with open('latlng/' + latlng + '.json', 'r') as expected:
            assert response_json == expected.read()


if __name__ == "__main__":
    recreate_asserts()
