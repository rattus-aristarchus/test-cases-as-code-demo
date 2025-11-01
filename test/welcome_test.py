import allure
from faker import Faker
from test.steps import Steps

fake = Faker()
steps = Steps()

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
    
    with allure.step(f"Шаг с генерируемым именем: {fake.name()}"):
        pass


@allure.title("Тест с пользовательскими шагами")
@allure.manual(True)
def test_demo_custom_steps():
    steps.custom_step()
    steps.second_step()


@allure.title("Тест с вложением")
@allure.manual(True)
def test_demo_custom_steps():
    with allure.step("Шаг с вложением"):
        allure.attach("text/plain", "Текстовое вложение", name="attachment.txt")
