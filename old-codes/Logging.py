import os
import platform
import logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getnev('HOMEPATH'),
                                'logging_file_Logging.log')

else:
    logging_file = os.path.join(os.getnv('HOME'),
                                'log_file_Logging.log')

print("Nge-Log ke", logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file
    filemode='w',
)

logging.debug("DEBUG LOGGING")
logging.info("LOGGING INFO")
logging.warning("WARNING LOGGING")
logging.test("TESTING.....")
