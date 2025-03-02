from playwright.sync_api import Page
import config
import time

class IndexPage:

    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    def get_page_title(self, page: Page):
        return page.title()

    def __set_station__(self, page:Page, text:str, locator:str):
        station_from_element = page.locator(locator)
        station_from_element.click()
        station_from_element.fill(text)
        element = page.locator("span", has_text=text)
        element.click()

    def set_station_from(self, page: Page, text: str):
        self.__set_station__(page, text, "//*[@placeholder='Откуда']")


    def set_station_to(self, page: Page, text:str):
        self.__set_station__(page, text,"//*[@placeholder='Куда']")

    def get_estimation_time(self, page: Page) -> str:
        return page.locator("//span[@class = 'route-list-item__time']").text_content()