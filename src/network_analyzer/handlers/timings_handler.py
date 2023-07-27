import configparser
import datetime

from handlers.models import Count


config = configparser.ConfigParser() # create a parser object
config.read("./src/network_analyzer/settings.ini") # read data from cfg

def timings():
    """
    This function create a list with class Count object to store count of 
    internet traffic in certain intervals of time
    Returns:
        list: list with class object, which store count of packets in a 
        certain amount of time
    """
    try:
        timings = [x.strip() for x in config["traffic"]["timings"].split(',')]
        count_timings = []
        for timing in range(len(timings)): # create necessary number of objects
            _ = Count(datetime.datetime.now())
            _.timing = int(timings[timing])
            count_timings.append(_)
        return count_timings
    except Exception as err:
        print("Something wrong with setting.ini. Fix it and try again.")
        print(err)
        

if __name__ == "__main__":
    timings()