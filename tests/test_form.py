import allure
from pages.form_page import FormPage


@allure.feature("Form")
@allure.story("Submit form successfully")
def test_fill_form(driver):
    form = FormPage(driver)

    alert_text = (
        form.open()
            .enter_name("A" * 1000)
            .enter_password("123456")
            .select_drinks()
            .select_color()
            .select_automation()
            .enter_email("name@example.com")
            .enter_message()
            .submit()
            .get_alert_text()
    )

    assert alert_text == "Message received!"