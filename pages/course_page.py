import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from locators.course_page_locators import CoursePageLocators

logger = logging.getLogger("moodle")


class CoursePage(BasePage):
    def go_to_manage_courses(self) -> WebElement:
        return self.click_element(
            self.find_element(CoursePageLocators.MANAGE_COURSES_BUTTON)
        )

    def delete_course(self):
        """Find and delete second element."""
        logger.info("Deleting course.")
        return self.click_element(
            self.find_elements(CoursePageLocators.DELETE_COURSE_BUTTON)[1]
        )

    def confirm_delete(self) -> WebElement:
        return self.click_element(
            self.find_element(CoursePageLocators.CONFIRM_DELETE_BUTTON)
        )

    def delete_course_by_full_name(self, full_course_name):
        self.app.open_course_page()
        self.go_to_manage_courses()
        self.find_course_by_full_name(full_course_name)
        self.delete_course()
        self.confirm_delete()

    def is_full_course_name_error(self) -> bool:
        element = self.find_elements(CoursePageLocators.FULLNAME_ERROR)
        if len(element) > 0:
            return True
        return False

    def is_short_course_name_error(self) -> bool:
        element = self.find_elements(CoursePageLocators.SHORTNAME_ERROR)
        if len(element) > 0:
            return True
        return False

    def is_course_name_error(self):
        if self.is_short_course_name_error() or self.is_full_course_name_error():
            return True
        return False

    def find_course_by_full_name(self, course_name) -> WebElement:
        return self.find_element((By.XPATH, f"//a[text()='{course_name}']"))

    def find_delete_confirmation(self) -> str:
        """Find second header at the bottom of the page."""
        return self.find_elements(CoursePageLocators.COURSE_DELETE_CONFIRMATION)[1].text
