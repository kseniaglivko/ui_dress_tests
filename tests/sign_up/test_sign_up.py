import pytest

from models.auth import AuthData
from models.sign_up import SignUpData


class TestSignUp:
    @pytest.mark.skip(reason="Functionality removed")
    def test_valid_sign_up_data(self, app):
        """
        Steps
        1. Open Login page
        2. Click the "Создать учетную запись" button
        3. Fill in the required fields: Login, Password,
        Email (with mask test@test.te), Email Again,
        First_name, Second_name
        6. Click the "Создать мой новый аккаунт" button
        7. Search text "Отправить вам письмо не удалось!"
        7.1 Check
        8. Click "Продолжить" button
        9. __Login with the entered data__
        9.1 Check
        10. Search "Необходимо подтвердить учетную запись" text
        10.1 Check
        """
        app.open_auth_page()
        app.login.go_to_sign_up_page()
        data = SignUpData().random()
        app.sign_up.sign_up(data)
        assert app.sign_up.check_account_create(), "We are not auth"
        app.sign_up.click_continue()
        app.sign_up.click_log_in()
        data_auth = AuthData(data.login, data.password)
        app.login.auth(data_auth)
        assert app.sign_up.check_new_account_log_in(), "We are not auth"

    @pytest.mark.skip(reason="Functionality removed")
    @pytest.mark.parametrize(
        "field", ["login", "password", "email", "first_name", "last_name"]
    )
    def test_invalid_sign_up_data(self, app, field):
        """
        Steps
        1. Open Login page
        2. Click the "Создать учетную запись" button
        3. Fill in the required fields: Login, Password,
        Email (with mask test@test.te), Email Again,
        First_name, Second_name, Each field separately
        4. Click the "Создать мой новый аккаунт" button
        5. Checking for registration of a new user without empty required fields
        """
        app.open_auth_page()
        app.login.go_to_sign_up_page()
        data = SignUpData().random()
        setattr(data, field, None)
        app.sign_up.sign_up(data)
        assert (
            not app.sign_up.is_sign_upped()
        ), "We are sign up with empty required fields!"
