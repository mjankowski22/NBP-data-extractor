# NBP data extractor

API written with Flask framework providing processed data got from NBP API

### How to run the server
Build the Docker image by cloning the git repo

```
$ git clone https://github.com/mjankowski22/NBP-data-extractor.git
$ docker image build -t nbp_data_extractor .
```

It is also possible to download the existing image from [DockerHub](https://hub.docker.com/r/mjankowski22/nbp_data_extractor)
```
$ docker pull mjankowski22/nbp_data_extractor
```

Then run container with:
```
$ docker run -i -p 5000:5000 -d nbp_data_extractor
```

It is also possible to run the server without using Docker by a command:
```
$ python3 app.py
```

The server will be availble on localhost:5000

### Examples
There are three available endpoints: /exchanges , /max_min , /major_diff .
Each endpoint returns the answer in the JSON format.
Each endpoint can be tested using the simple UI available on localhost:5000/swagger\

![image](https://user-images.githubusercontent.com/106553136/233865825-ad67c304-39e7-4250-92e7-e1c1a2e1ce1a.png)

Or by commands provided in the description of each funcionality.

The /exchanges endpoint provides the average exchange rate of the given currency in a particular day.
To query the operation the command is:
```
$ curl localhost/5000/{currency_code}/{date}
```
The date should be in format: YYYY-MM-DD
For example command

```
$ curl localhost:5000/exchanges/GBP/2023-01-02
```
returns

```javascript
{"currency": "funt szterling", "code": "GBP", "date": "2023-01-02", "average_exchange_rate": 5.2768}
```

The average exchange rate is available in the field "average_exchange_rate"


The /max_min endpoint provides the maximum and minimum average exchange rate of the given currency in the number of last quatotations.
To query the operation the command is:

```
$ curl localhost/5000/max_min/{currency_code}/{number_of_last_quatoations}
```
The number of last quotations should be less than 255.
For example command

```
$ curl localhost:5000/max_min/EUR/200
```
returns

```javascript
{"currency": "euro", "code": "EUR", "max_min": {"min": {"value": 4.6039, "date": "2023-04-21"}, "max": {"value": 4.8711, "date": "2022-10-11"}}}
```

The answer contains the values of minimum and maximum exchange rate and the date of their occurence.

The /major_diff endpoint provides the major difference between the buy and ask rate of the given currency in the number of last quatotations.
To query the operation the command is:

```
$ curl localhost/5000/major_diff/{currency_code}/{number_of_last_quatoations}
```

The number of last quotations should be less than 255.
For example command

```
$ curl localhost:5000/major_diff/AUD/100
```

returns

```javascript
{"currency": "dolar australijski", "code": "AUD", "major_difference": {"date": "2023-02-14", "bid_value": 3.0792, "ask_value": 3.1414, "difference": 0.0622}}
```

The answer contains the values of a bid and ask values, the differecne and the date of its occurence.



## How it works
The application is divided into few files. Each of them has its own funcionalities described shortly below.

#### app.py
Sets up and run the server 

#### get_data.py
Makes a request to the NBP API and returns the data

#### process_data.py 
Processes the date gotten from NBP API to extract particular data. Then prepares and returns the answer in JSON format.

#### resources.py
Prepares each endpoint using flask-restful library. Defines the functions called after making the request to the server.

#### validator.py
Contains few simple validators checking if the data provided by the user is correct.

#### constants.py
Contains few constant values used in the application.

#### test_api.py
Contains unit test for the application. The tests can be run using:

```
$ pytest
```

In static folder there is also swagger.json file which sets up the UI.





