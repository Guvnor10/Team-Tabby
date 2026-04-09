import unittest
from unittest.mock import patch, MagicMock
from bot.bot import create_driver, simulate_user, URL

class TestBot(unittest.TestCase):

    @patch("bot.bot.webdriver.Chrome")
    def test_create_driver(self, mock_chrome):
        create_driver()
        mock_chrome.assert_called_once()

    @patch("bot.bot.webdriver.Chrome")
    def test_simulate_user_no_links(self, mock_chrome):
        mock_driver = MagicMock()
        mock_driver.find_elements.return_value = []
        mock_chrome.return_value = mock_driver

        simulate_user()
        mock_driver.get.assert_called_with(URL)
        mock_driver.quit.assert_called_once()

if __name__ == "__main__":
    unittest.main()