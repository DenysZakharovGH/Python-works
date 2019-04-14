import logging
 
logging.basicConfig(filename="sample.log", level=logging.INFO) 
try:
    raise RuntimeError
except RuntimeError:
    log.exception("Error!")