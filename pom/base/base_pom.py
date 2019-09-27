from abc import ABC, abstractmethod
from manager.driver_wrapper import DriverWrapper


class BasePOM(ABC):
    def __init__(self, driver_wrapper, is_displayed=True):
        """
        :type driver_wrapper: DriverWrapper
        """
        self.driver_wrapper = driver_wrapper
        super().__init__()

        if is_displayed:
            assert self.is_displayed()

    @abstractmethod
    def is_displayed(self):
        """
        :return: True if the page is displaying conditions are met
                 False otherwise
        """
        pass
