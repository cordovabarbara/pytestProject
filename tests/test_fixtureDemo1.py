import pytest


class TestExample2:
    def test_editProfile(self, dataLoad):
        print(dataLoad)

@pytest.mark.usefixtures("dataLoad") #Solo con usefixtures (si no necesitas los datos)
class TestExample3:
    def test_editProfile(self):
        print("Test executed, dataLoad se ejecutó pero no accedo a sus datos")
