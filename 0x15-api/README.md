# API - Application Programming Interface

This repository deals with experimenting with REST API's using pythons `requests` module<br>
To install request use:
```
pip3 install requests
```

## Directory Files

* [responses](./responses) - contains mock responses
* [0-gather_data_from_an_API.py](0-gather_data_from_an_API.py) - Writing a Python script that, using this [REST API](https://jsonplaceholder.typicode.com/), for a given employee ID, returns information about his/her TODO list progress.
* [1-export_to_CSV.py](1-export_to_CSV.py) - Using *0-\*.py*, extend the Python script to export data in the CSV format.
* [2-export_to_JSON.py](2-export_to_JSON.py) - extend your Python script to export data in the JSON format.
* [3-dictionary_of_list_of_dictionaries.py](3-dictionary_of_list_of_dictionaries.py) - extend your Python script to export data in the JSON format of ALL employees.

## What is an API?

Alot of applications today are made from decentralized and modulated components, and API's help us achieve that. API's provide a set of rules for two systems to communicate with each other. The API will produce a response whether it's data or authentication. 

The advantage is that the system requesting the service does not need to know how the API serves it's content in the background, only the rules to request the content. These rules occur at an **End point** where there are protocols that define what input is required an what response is produced. Sometimes an **API Key** is required for a request to identify who's interacting with the API. This is useful for API service's that require subscription fees.

An example of API is a Weather API that serves live updates of weather data depending on what exact data you request. One free weather API service you can test is [open-meteo](https://open-meteo.com/). API's have documentation that provides information of the rules in which you can interact with their services, see [open-meteo documentation](https://open-meteo.com/en/docs).

## REST API's

`REST -> Representational State Transfer`

REST API's are the most used API's across the web. They can make their services available through a simple URL. See more information on [postmans blog](https://blog.postman.com/rest-api-examples/)
