from pages.base_page import BasePage
from pages.create_course_page import CreateCoursePage
from pages.login_page import LoginPage
from pages.personal_data_page import PersonalDataPage
from pages.course_page import CoursePage


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.base_page = BasePage(self)
        self.login = LoginPage(self)
        self.course = CoursePage(self)
        self.create_course = CreateCoursePage(self)
        self.personal_data = PersonalDataPage(self)

    def open_main_page(self):
        self.driver.get(self.url)

    def quit(self):
        self.driver.quit()

    def open_auth_page(self):
        self.driver.get(self.url + "/login/index.php")

    def open_course_page(self):
        self.driver.get(self.url + "/course/index.php")
