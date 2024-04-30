"""
running_log.py: A running logger for runners
DS2501: Lab for Intermediate Programming with Data
"""

class RunningLog:

    def __init__(self):
        """ The running log constructor. How you store each run is up to you! """
        pass

    def add_run(self, hms, dist_km):
        """ Record a run.  The time is given as 'hh:mm:ss' and the distance is in kilometers """
        pass

    def num_runs(self):
        """ How many run records are in the database? """
        return 0

    def plot(self):
        """ Generate a line plot showing the average pace (minutes per kilometer) for
        run1, run2, .... run N. The x-axis is the run number, and the y-axis is the average
        pace for that run. """
        pass

    def save(self, filename):
        """ OPTIONAL FOR A FIVE: Save the data to a file. """
        pass

    def load(self, filename):
        """ OPTIONAL FOR A FIVE: Load the data from a file """
        pass

def main():

    # Instantiate a new running log
    logger = RunningLog()

    # This is optional
    logger.load("running.log")

    # Here are 4 sample running events
    logger.add_run("00:32:14", 5.1)
    logger.add_run("00:34:59", 5.5)
    logger.add_run("00:29:01", 4.9)
    logger.add_run("00:30:00", 5.0)

    # Add at least 6 more...

    # Output some data
    print(f"There are {logger.num_runs()} runs in the database")
    logger.plot()

    # This is also optional
    logger.save("running.log")



if __name__ == '__main__':
    main()

