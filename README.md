# Prophète

Prophète is a simple tool aimed to be a configurable frontend wrapper around Facebook's [Prophet](https://github.com/facebookincubator/prophet) forecasting procedure.

## Dependencies

- [tkinter package](https://docs.python.org/3.5/library/tkinter.html)
-- `apt install python3-tk` on Ubuntu 16.04 / Python 3

## Installation

* clone repository
* `virtualenv prophete --no-site-packages -p /usr/bin/python3.5` (forcing python3.5)
* `cd prophete` (cloned repository root)
* `cp prophete/prophete/settings.example.py prophete/prophete/settings.py`
* update `settings.py` as per your desired configuration (`SECRET_KEY` setting must not be empty, the rest of the defaults should work fine)
* `. bin/activate` to start virtualenv
* `pip install -r requirements.txt` to install pip deps
* `cd prophete` (django project root)
* `python manage.py migrate`
* `python manage.py runserver`
* visit http://127.0.0.1:8000/ in your browser
