import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkPresenceWait(self,text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def test_getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        # It will take fine handler object - File Location for log file
        filehandler = logging.FileHandler("C:/Users/abhis/PycharmProjects/PyTestFramework/Test_Reports/logfile.log")

        # Foramt of Logs to be print
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        # asctime : time

        logger.addHandler(filehandler)
        # set level - whichever we want to see logs level - error or warning or critical
        logger.setLevel(logging.INFO)

        logger.debug("A debug statement is executed")
        logger.info("Information statement")
        logger.warning("Alert - Pass a warning message")
        logger.error("Error has happened")
        logger.critical("Critical Issue")

        return  logger
