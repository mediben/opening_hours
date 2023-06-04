# opening-hours

## Part One

An API that takes JSON-formatted opening hours of a restaurant as an input and outputs hours in a more human readable format.

### _Disclaimer_

The candidate has not worked with Python for the last 2 years, he is a bit rusty - Mehdi Ben Taarit -
Please note this work is not configured to run for production. It is only for internal use and for assessment purposes.

### _How to run_

1. Open terminal and go to the root directory `wolt/`.
2. Run `docker compose up` to start the project.
3. Open browser and access endpoint url: `http://127.0.0.1:5230`.
4. It work 🎉 🎉
5. You can post the [Payload example](#payload-example).

### _Additional configuration_

Remember to run `docker compose down` and to remove container and image.
You can run `python -m black app.py ` to apply lint to changes.

### _Run test_

In order to run tests we can use **_pytest-docker-compose_**, however since it was not set up within the deadline we can use a different approach:

1. Run `virtualenv env` to create a virtual environment and then activate by `source env/bin/activate`.
2. Install all required dependencies `pip i requirements.txt`.
3. Finally run `pytest` to run all tests.
4. PS: You can also run the project without docker `python app.py`.

### _Payload example_

```json
{
  "monday": [],
  "tuesday": [
    { "type": "open", "value": 36000 },
    { "type": "close", "value": 64800 }
  ],
  "wednesday": [],
  "thursday": [
    { "type": "open", "value": 36000 },
    { "type": "close", "value": 64800 }
  ],
  "friday": [{ "type": "open", "value": 36000 }],
  "saturday": [
    { "type": "close", "value": 3600 },
    { "type": "open", "value": 36000 }
  ],
  "sunday": [
    { "type": "close", "value": 3600 },
    { "type": "open", "value": 43200 },
    { "type": "close", "value": 75600 }
  ]
}
```

### _Notes to improve_

- Use `@dataclasses` for a better serialization of the input data.
- Update the docker configuration to work with _pytest_.

<br/>
<br/>

## Part Two

New format suggestion for the payload

### _Suggestion One_

No better solution than the appropriate input data being provided. By improving the input to the
expected result data our code will be a lot shorter. “If only life was that easy”.

```json
{
  "monday": [
    {
      "opening_time": "12 PM",
      "closing_time": "12:30 AM"
    }
  ]
}
```

### _Suggestion Two_

With this approach we can standardize the serialization as we will always expect these variables
and we can build our model and have less validation, maybe to just verify if opening_time is
less than closing_time taking into account next_day.

```json
{
  "monday": [
    {
      "opening_time": 32400,
      "closing_time": 3600,
      "next_day": true
    }
  ]
}
```

### _Suggestion Three_

This input data is formatted in a slightly better manner, writing serializer will be also easier as
instead of having the days as keys, we could have a "day" key and its value as the days. Combined with
the previous example I would say to make even better.

```json
[
  {
    "day": "monday",
    "schedule": [
      {
        "opening_time": 32400,
        "closing_time": 3600,
        "next_day": true
      }
    ]
  }
]
```
