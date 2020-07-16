<h4 align="center">
  <#Server>
</h4>



## What is this project for

This project was made for only one purpose  - to test my skills and find out if i can deal with new language.

> It's not finished yet, so where will be at least one more version of it

## Usage
My server is able to execute 3 tasks:


- Query, that returns the current day of the week (on server) 

- Query, that returns the day of the week by entered date (year+month+day)

- Query, that returns the day of the week after entered time interval (days+hours+minutes+seconds)

First, ensure you have a python interpreter, that supports python 3+.

Then, run server

    $ uvicorn main:app --reload

`reload` allows you to change the source code.

By default settings your server will be located at http://127.0.0.1:8000, but you can change its port, e.g.

    $ uvicorn main:app --reload --port (enter port number here)

Now the server is launched.
To execute 1 query, you have to enter your server address in internet-browser

    $http://127.0.0.1:8000/return/day
    
To execute 2 query, enter the date

    $
    
To execute 3 query, enter the time interval

    $http://127.0.0.1:8000/DbaD?day=1&hour=1&minute=1&second=1
    

