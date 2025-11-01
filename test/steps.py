import allure

class Steps:

    @allure.step("Пользовательский шаг")
    def custom_step():
        pass

    @allure.step("Ещё один шаг")
    def second_step():
        pass
