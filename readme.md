## A basic Subscription App to emulate yearly website subscription.

**Test**

[![Build Status](https://travis-ci.com/rexeze/subscription.svg?token=HykhQiNSsLiLzFfvd6fi&branch=master)](https://travis-ci.com/rexeze/subscription)

## Setup

clone the repo and install the dependencies
```shell
git clone https://github.com/rexeze/subscription.git 

```
Create a virtual environment and actvate it 
```shell
virtualenv venv && source venv/bin/activate
```
install dependencies

```shell
pip install -r requirements.txt
```
The peewee ORM was used so we need to run migrations
Run
```shell
pem migrate
```

Set up is complete. Run test.
```shell
python3 -m inittest
```

boom, you can play around with the app


