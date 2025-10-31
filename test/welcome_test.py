import allure
from faker import Faker

fake = Faker()

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

    with allure.step(f"Шаг с генерируемым именем: {fake.name()}"):
        pass


@allure.step("Пользовательский шаг")
def custom_step():
    pass
