# Global Entry Interview Openings Checker

Uses an undocumented API and a (provided) dictionary of the user's availability to search for Global Entry appointments within two hours. If one is found, the user receives a text, powered by Twilio. Heavily influenced and inspired by [another project] (https://github.com/mvexel/next_global_entry) on GitHub. 

## Setup

- If you don't have a Twilio account, [create one]() for free, and create a free [phone number](https://www.twilio.com/console/phone-numbers). This is where your texts will originate from
- Install the dependencies `pip install -r requirements.txt`
- Copy `config.py.template` to a new file `config.py`
- Edit `config.py`:
  - Enter your Twilio [tokens](https://www.twilio.com/console)
  - Enter your Twilio ['from' phone number](https://www.twilio.com/console/phone-numbers)
  - Enter your desired destination cell number, amount of weeks to look ahead, and your city search string
- Add this script to your crontab (see [virtualenv notes](https://stackoverflow.com/questions/3287038/cron-and-virtualenv)) or use Windows' Task Scheduler.
- Wait.
