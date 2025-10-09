import allure

from src.test_cases_as_code import get_message


def test_test_cases_as_code():
    with allure.step("Welcome to Allure Report!"):
        assert get_message() == "Hello from test-cases-as-code!"

@allure.title("Demo manual test")
@allure.label("manual", "true")
def test_demo_manual():
    with allure.step("First step"):
        pass
