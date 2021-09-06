from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from locators.course_page_locators import CoursePageLocators


class CoursePage(BasePage):
    def go_to_manage_courses(self) -> WebElement:
        return self.click_element(
            self.find_element(CoursePageLocators.MANAGE_COURSES_BUTTON)
        )

    def delete_course(self):
        """Find and delete second element."""
        return self.click_element(
            self.find_elements(CoursePageLocators.DELETE_COURSE_BUTTON)[1]
        )

    def confirm_delete(self) -> WebElement:
        return self.click_element(
            self.find_element(CoursePageLocators.CONFIRM_DELETE_BUTTON)
        )

    def find_fullname_error(self) -> str:
        return self.find_element(CoursePageLocators.FULLNAME_ERROR).text

    def find_shortname_error(self) -> str:
        return self.find_element(CoursePageLocators.SHORTNAME_ERROR).text

    def find_course_full_name(self, course_name) -> WebElement:
        return self.find_element((By.XPATH, f"//a[text()='{course_name}']"))

    def find_delete_confirmation(self) -> str:
        """Find second header at the bottom of the page."""
        return self.find_elements(CoursePageLocators.COURSE_DELETE_CONFIRMATION)[1].text
