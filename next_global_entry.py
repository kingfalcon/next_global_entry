#!/usr/bin/env python
"""
Check for Global Entry interview openings based on cities and times provided
in the config file
"""

import sys
import datetime
import requests
from twilio.rest import Client
import config


def log(text):
    """Write a one-line log message."""
    print("{dt}\t{msg}".format(dt=datetime.datetime.now(),msg=text))


if __name__ == '__main__':
    count = 0
    for k in config.search_dict.keys():
            try:
                next_time = requests.get(config.global_entry_query_url\
                                             .format(id=config.search_dict[k]['id']))\
                                         .json()[0]['startTimestamp']
                next_time_datetime = datetime.datetime.strptime(next_time,'%Y-%m-%dT%H:%M')
                for j in range(0,len(config.search_dict[k]['times'])):
                    current_time = datetime.datetime.strptime(config.\
                                                              search_dict[k]['times'][j]\
                                                              ,'%Y-%m-%dT%H:%M')
                    if abs(current_time-next_time_datetime)<=datetime.timedelta(hours=2):
                        client = Client(config.twilio_account, config.twilio_token)
                        message = client.messages.create(
                                     to=config.to_number,
                                     from_=config.twilio_from_number,
                                     body="Global Entry interview opportunity in {} \
                                     opened up just now at {}.\
                                     Your flight departs/lands at {}."\
                                     .format(k,next_time_datetime,current_time))
                        count += 1
            except:
                pass
    log("Found {} possible timeslots.".format(count))
    sys.exit(1)