import pytest
import allure
from allure_commons.types import AttachmentType

from common.constants import CourseConstants
from models.auth import AuthData
from models.create_course import CreateCourse


class TestCourseCreation:
    def test_valid_course_creation(self, app):
        """
        Steps
        1. Authorize under admin.
        2. Go to Administration page.
        3. Go to Courses tab.
        4. Go to Create Course page.
        3. Fill in fields: «Полное название курса», «Краткое название курса».
        4. Enter day, month, year and time for course end date.
        5. In section "Общие" fill in fields:  «Дата окончания курса», «Описание».
        6. In section "Формат курса" choose number in  «Количество секций».
        7. In section "Внешний вид" choose Russian language
            in dropdown «Принудительный язык».
        8. In section "Файлы и загрузки" choose value
            in dropdown «Максимальный размер загружаемого файла».
        9. In section "Переименование Ролей" fill in fields:
            «Ваше слово вместо «Управляющий»»,
             «Ваше слово вместо «Учитель»»,
             «Ваше слово вместо «Студент»».
        10. Click button «Сохранить и показать».
        11. Click button «Перейти к курсу».
        12. Check if the created course name is in the page header.
        13. Go to https://qacoursemoodle.innopolis.university/course/index.php.
        14. Click button «Управление курсами».
        15. Find the created course name on the page.
        16. Click delete button next to the new course name.
        17. Confirm deletion by clicking «Удалить».
        18. Check for text "{the new course name} был полностью удален".
        """
        app.open_main_page()
        if not app.login.is_auth():
            app.open_auth_page()
            data = AuthData(login="admin", password="Vjcrdf2!")
            app.login.auth(data)
            assert app.login.is_auth(), "You are not auth"
        app.login.go_to_administration_page()
        app.login.go_to_course_page()
        app.login.go_to_create_course_page()
        course_info = CreateCourse.random()
        app.create_course.create_course(course_info)
        allure.attach(
            app.personal_data.make_screenshot(),
            name="Course_creation_valid_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        assert (
            app.create_course.new_course_page() == course_info.full_course_name
        ), "The course was not created!"
        app.open_course_page()
        app.course.go_to_manage_courses()
        app.course.find_course_full_name(course_info.full_course_name)
        app.course.delete_course()
        app.course.confirm_delete()
        delete_confirmation = (
            f"{course_info.short_course_name} {CourseConstants.DELETED_COURSE}"
        )
        allure.attach(
            app.personal_data.make_screenshot(),
            name="Course_deletion_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        assert (
            app.course.find_delete_confirmation() == delete_confirmation
        ), "The course was not deleted!"

    @pytest.mark.parametrize("field", ["full_course_name"])
    def test_invalid_course_creation_no_full_name(self, app, field):
        """
        Steps
        1. Authorize under admin.
        2. Go to Administration page.
        3. Go to Courses tab.
        4. Go to Create Course page.
        3. Do not fill in the required field  «Полное название курса».
        4. Fill in field «Краткое название курса».
        5. Click button «Сохранить и показать».
        6. Check for text "- Заполните поле".
        """
        app.open_main_page()
        if not app.login.is_auth():
            app.open_auth_page()
            data = AuthData(login="admin", password="Vjcrdf2!")
            app.login.auth(data)
            assert app.login.is_auth(), "You are not auth"
        app.login.go_to_administration_page()
        app.login.go_to_course_page()
        app.login.go_to_create_course_page()
        course_info = CreateCourse.random()
        setattr(course_info, field, None)
        app.create_course.create_course(course_info)
        allure.attach(
            app.personal_data.make_screenshot(),
            name="Invalid-course_creation_no_fullname_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        assert (
            app.course.find_fullname_error() == CourseConstants.FULLNAME_ERROR
        ), "The course was created without fullname!"

    @pytest.mark.parametrize("field", ["short_course_name"])
    def test_invalid_course_creation_no_short_name(self, app, field):
        """
        Steps
        1. Authorize under admin.
        2. Go to Administration page.
        3. Go to Courses tab.
        4. Go to Create Course page.
        3. Fill in field «Полное название курса».
        4. Do not fill in the required field «Краткое название курса».
        5. Click button «Сохранить и показать».
        6. Check for text "- Не указано краткое название".
        """
        app.open_main_page()
        if not app.login.is_auth():
            app.open_auth_page()
            data = AuthData(login="admin", password="Vjcrdf2!")
            app.login.auth(data)
            assert app.login.is_auth(), "You are not auth"
        app.login.go_to_administration_page()
        app.login.go_to_course_page()
        app.login.go_to_create_course_page()
        course_info = CreateCourse.random()
        setattr(course_info, field, None)
        app.create_course.create_course(course_info)
        allure.attach(
            app.personal_data.make_screenshot(),
            name="Invalid-course_creation_no_shortname_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        assert (
            app.course.find_shortname_error() == CourseConstants.SHORTNAME_ERROR
        ), "The course was created without shortname!"
