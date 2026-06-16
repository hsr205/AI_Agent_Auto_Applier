from config.config import Settings
from logger.logger import AppLogger


class LinkedInConnect:

    def __init__(self) -> None:
        self._config: Settings = Settings()
        self._api_key: str = self._config.ticketmaster_consumer_key
        self._api_secret: str = self._config.ticketmaster_consumer_secret
        self._logger = AppLogger.get_logger(self.__class__.__name__)

