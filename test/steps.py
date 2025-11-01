import allure

class Steps:

    @allure.step("Пользовательский шаг")
    def custom_step(self):
        pass

    @allure.step("Ещё один шаг")
    def second_step(self):
        pass
