from selenium.webdriver.common.by import By


class CoursePageLocators:
    COURSES_HEADER = (By.XPATH, "//a[@href='#linkcourses']")
    CREATE_COURSE_LINK = (
        By.XPATH,
        "//a[@href='https://qacoursemoodle.innopolis.university/course/edit.php"
        "?category=0']",
    )
    MANAGE_COURSES_BUTTON = (By.XPATH, "//button[text()='Управление курсами']")
    DELETE_COURSE_BUTTON = (By.CLASS_NAME, "action-delete")
    CONFIRM_DELETE_BUTTON = (By.XPATH, "//button[text()='Удалить']")
    FULLNAME_ERROR = (By.ID, "id_error_fullname")
    SHORTNAME_ERROR = (By.ID, "id_error_shortname")
    COURSE_DELETE_CONFIRMATION = (By.TAG_NAME, "h2")
