API out URL

    URL :/formatted
    View the entries in the database via API

Request Headers
    None

Request

POST
    Mandatory
      -User
        1. id
        2. real_name
        3. tz
      -Activity_periods 
        1. id
        2. user_id(foreignkey User)
        3. start_time
        4. end_time

    Optional
        None

Response
    {"ok":true,
    "members":[
            {"id":"W012A3CDE",
            "real_name":"Egon Spengler",
            "tz":"America/Los_Angeles",
            "Activity_periods":[{"start_time":"2020-02-01T13:33:00Z","end_time":"2020-02-01T13:54:00Z"},{"start_time":"2020-03-01T11:11:00Z","end_time":"2020-03-01T14:00:00Z"},{"start_time":"2020-03-16T17:33:00Z","end_time":"2020-03-16T20:02:00Z"}]
            },
            {"id":"W07QCRPA4",
            "real_name":"Glinda Southgood",
            "tz":"Asia/Kolkata",
            "Activity_periods":[{"start_time":"2020-02-01T13:33:00Z","end_time":"2020-02-01T13:54:00Z"},{"start_time":"2020-03-01T11:11:00Z","end_time":"2020-03-01T14:00:00Z"},{"start_time":"2020-03-16T17:33:00Z","end_time":"2020-03-16T20:02:00Z"}]
            }
        ]
    }