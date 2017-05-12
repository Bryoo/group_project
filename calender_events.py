import requests
import json


url = "https://andela-group-project.firebaseio.com/calender.json"

def get_data(user_id):
    myResponse = requests.get(url)

    print("Response code is " + str(myResponse.status_code))
    # For successful API call, response code will be 200 (OK)

    if myResponse.ok:


        jData = json.loads(myResponse.content)

        # id - id of the event
        # user_id - id of the user
        # date - date of the event
        print("event - event")

        calendar = jData.values()

        l = []
        for key in calendar:

            if key['user_id'] == user_id:
                l.append(key)

        print(l)


    else:
        # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()


def view_last_event(user_id):
    myResponse = requests.get(url)

    print("Response code is " + str(myResponse.status_code))
    # For successful API call, response code will be 200 (OK)


    if (myResponse.ok):
        jData = json.loads(myResponse.content)

        # id - id of the event
        # user_id - id of the user
        # date - date of the event
        # event - event

        calendar = jData.values()

        l = []
        for key in calendar:

            if key['user_id'] == user_id:
                l.append(key)

        print(l[-1])


    else:
        # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()


def create_event(user_id, event, date):
    return requests.post(url, json={
        'user_id': user_id,
        'event': event,
        'date': date,
        })

# create_event('sha', 'this is my event 1', '13/2/1991')
# get_data("bryoo")
