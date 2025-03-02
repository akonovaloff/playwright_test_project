import pytest
import pages
import time


class TestFooter:

    def test_main_page_title(self, page):
        pages.index_page.open_index_page(page)
        assert pages.index_page.get_page_title(page) == "Схема метро Москвы — Яндекс.Метро"

    def test_check_time_estimation(self, page):
        pages.index_page.open_index_page(page)
        time.sleep(5)
        pages.index_page.set_station_from(page, "Красные Ворота")
        pages.index_page.set_station_to(page, "Черкизовская")
        assert pages.index_page.get_estimation_time(page) == "≈\xa013 мин."
        time.sleep(3)

