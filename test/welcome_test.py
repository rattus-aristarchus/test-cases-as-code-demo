import allure
from allure_commons.types import LabelType

from src.test_cases_as_code import get_message


def test_test_cases_as_code():
    with allure.step("Welcome to Allure Report!"):
        assert get_message() == "Hello from test-cases-as-code!"

@allure.title("Демонстрационный ручной тест")
@allure.story("Story")
@allure.feature("Feature")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("example")
@allure.label("owner", "mlankin")
@allure.manual(True)
def test_demo_manual():
    with allure.step("Демонстрационный шаг"):
        pass
    custom_step()


@allure.step("Пользовательский шаг")
def custom_step():
    pass
