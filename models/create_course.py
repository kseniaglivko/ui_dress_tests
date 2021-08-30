import random

from faker import Faker

from common.constants import CreateCourseConstants

fake = Faker("Ru-ru")


class CreateCourse:
    def __init__(
        self,
        full_course_name=None,
        short_course_name=None,
        end_month=None,
        end_day=None,
        end_year=None,
        end_hour=None,
        end_minute=None,
        course_description=None,
        section_number=None,
        course_language=None,
        max_file_size=None,
        manager_name=None,
        teacher_name=None,
        student_name=None,
    ):
        self.full_course_name = full_course_name
        self.short_course_name = short_course_name
        self.end_month = end_month
        self.end_year = end_year
        self.end_day = end_day
        self.end_hour = end_hour
        self.end_minute = end_minute
        self.course_description = course_description
        self.section_number = section_number
        self.course_language = course_language
        self.max_file_size = max_file_size
        self.manager_name = manager_name
        self.teacher_name = teacher_name
        self.student_name = student_name

    @staticmethod
    def random():
        full_course_name = fake.job()
        short_course_name = fake.word()
        end_month = random.choice(CreateCourseConstants.MONTHS)
        end_day = random.randint(1, CreateCourseConstants.COURSE_DAY)
        end_year = random.randint(
            CreateCourseConstants.CURRENT_YEAR, CreateCourseConstants.LAST_YEAR
        )
        end_hour = random.randint(0, 23)
        end_minute = random.randint(0, 59)
        course_description = fake.text(max_nb_chars=200)
        section_number = random.randint(0, CreateCourseConstants.SECTION_NUMBER)
        course_language = CreateCourseConstants.COURSE_LANGUAGE
        max_file_size = random.choice(CreateCourseConstants.FILE_SIZES)
        manager_name = fake.word()
        teacher_name = fake.word()
        student_name = fake.word()
        return CreateCourse(
            full_course_name,
            short_course_name,
            end_month,
            end_day,
            end_year,
            end_hour,
            end_minute,
            course_description,
            section_number,
            course_language,
            max_file_size,
            manager_name,
            teacher_name,
            student_name,
        )
