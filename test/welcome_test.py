import allure

from src.test_cases_as_code import get_message


def test_test_cases_as_code():
    with allure.step("Welcome to Allure Report!"):
        assert get_message() == "Hello from test-cases-as-code!"

@allure.title("Демонстрационный ручной тест")
@allure.manual
def test_demo_manual():
    with allure.step("Демонстрационный шаг"):
        pass
    custom_step()


@allure.step("Пользовательский шаг")
def custom_step():
    pass
