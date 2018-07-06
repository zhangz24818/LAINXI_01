import allure
class Test_01:
    @allure.step(title = '第一次执行')
    def test_01(self):
        assert 1