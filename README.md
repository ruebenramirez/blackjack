Host dependencies
-----------------

Please make sure to install these dependencies on your linux environment:

* make
* docker

App dependencies
----------------

* our runtime container is based on the alpine:3.12 container
* tests are ran via `pytest` (installed in the container through automation)

Development Journal/notes
-------------------------

I kept some notes [here](https://docs.google.com/document/d/1wO-xEMoQwp3TiPYaeCp4rmLFIhbTEyOypmQzVn9Y4S0/edit#heading=h.8z06b4vtvw26) as I was writing code to solve this challenge


How to run the blackjack game simulation:
-----------------------------------------

To run the simulation run this command:

```
make play
```

How to run the tests:
---------------------

run the tests with this command:

```
make test
```
