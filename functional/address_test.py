# coding: utf-8
import json
import os

import requests

geocodingUrl = "https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={key}"

addresses = [
    "49+bogart+St,+San+brooklyn,+Ny",
    "Santa+Teresa,+Rio+de+Janeiro+-+RJ",
    "1600+Amphitheatre+Parkway,+Mountain+View,+CA",
    "+"
]


def recreate_asserts():
    for address in addresses:
        response = requests.get(geocodingUrl.format(address=address, key=os.environ['API_KEY']))

        assert response.status_code is 200
        with open('addresses/' + address + '.json', 'w') as outfile:
            json.dump(response.json(), outfile, sort_keys=True, indent=4, separators=(',', ': '))


def test_address_request():
    for address in addresses:
        response = requests.get(geocodingUrl.format(address=address, key=os.environ['API_KEY']))

        assert response.status_code is 200
        response_json = json.dumps(response.json(), sort_keys=True, indent=4, separators=(',', ': '))

        with open('addresses/' + address + '.json', 'r') as expected:
            assert response_json == expected.read()


if __name__ == "__main__":
    recreate_asserts()
