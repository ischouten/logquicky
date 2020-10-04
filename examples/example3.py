import sys, os

sys.path.insert(1, os.path.join(sys.path[0], ".."))
import logquicky

log = logquicky.load("log", level="INFO")
log.info("Loaded logger with info level")

def test_method():

    """ Shows that you can change the logger level """

    global log
    
    log.debug("Debug msg not shown")

    log.info("Info msg")

    log.error("Error msg")

    log = logquicky.load("log", level="DEBUG")

    log.debug("Debug msg displayed")

if __name__ == "__main__":
    print("hello")
    test_method()
