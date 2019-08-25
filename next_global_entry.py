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
   
def test_and_send(time,j,k):
    current_time = datetime.datetime.strptime(config.\
                                              search_dict[k]['times'][j]\
                                              ,'%Y-%m-%dT%H:%M')
    if abs(current_time-time)<=datetime.timedelta(hours=2):
        client = Client(config.twilio_account, config.twilio_token)
        message = client.messages.create(
                     to=config.to_number,
                     from_=config.twilio_from_number,
                     body="Global Entry interview opportunity in {} \
                     opened up just now at {}.\
                     Your flight departs/lands at {}."\
                     .format(k,time,current_time))


if __name__ == '__main__':
    for k in config.search_dict.keys():
            try:
                next_time = requests.get(config.global_entry_query_url\
                                             .format(id=config.search_dict[k]['id']))\
                                         .json()[0]['startTimestamp']
                next_time_datetime = datetime.datetime.strptime(next_time,'%Y-%m-%dT%H:%M')
                for j in range(0,len(config.search_dict[k]['times'])):
                    if k in config.exclusion_dict.keys():
                        if config.search_dict[k]['times'][j] in config.exclusion_dict[k]['times']:
                            continue
                        else:
                            test_and_send(next_time_datetime,j,k)
                    else:
                        test_and_send(next_time_datetime,j,k)
            except:
                continue
    sys.exit(1)