from time import sleep

from playwright.async_api import async_playwright
import time
from config.config import Settings
from logger.logger import AppLogger


class LinkedInConnect:

    def __init__(self) -> None:
        self._config: Settings = Settings()
        self._linkedin_username: str = self._config.linkedin_username
        self._linkedin_password: str = self._config.linkedin_password
        self._logger = AppLogger.get_logger(self.__class__.__name__)

    async def execute_linkedin_connection(self) -> None:
        try:

            async with async_playwright() as p:
                # Launch browser. 'slow_mo' adds a delay (in ms) between actions to mimic humans.
                browser = await p.chromium.launch(headless=False, slow_mo=100)

                # Create a new browser context with a standard desktop viewport
                context = await browser.new_context(
                    viewport={'width': 1280, 'height': 800},
                    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
                )

                page = await context.new_page()

                self._logger.info("Navigating to LinkedIn login...")
                await page.goto("https://www.linkedin.com/login")

                # Fill in credentials
                # Replace these with your actual details or environment variables
                await page.get_by_role(role="textbox", name="Email or phone").fill(self._linkedin_username)
                await page.get_by_role(role="textbox", name="Password").fill(self._linkedin_password)
                # Click Sign In
                self._logger.info("Logging in...")

                await page.get_by_role(role="button", name="Sign in", exact=True).click()

                # Wait for navigation to complete (LinkedIn home dashboard)
                await page.wait_for_url(url="https://www.linkedin.com/feed/**", timeout=60000)
                self._logger.info("Successfully logged in!")

        except Exception as e:
            self._logger.exception("Connection to LinkedIn API threw an exception")
            raise e
