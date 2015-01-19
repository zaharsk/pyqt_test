"""
Пользовательские слоты для виджетов.
"""
# Импортируем модуль времени
from datetime import datetime
# Импортируем класс интерфейса из созданного конвертером модуля
from test_ui import Ui_Form


# Создаём собственный класс, наследуясь от автоматически сгенерированного
class MainWindowSlots(Ui_Form):

    # Определяем пользовательский слот
    def set_time(self):
        # Получаем текущую метку времени в формате 'Ч:М:С'
        str_time = datetime.now().strftime('%H:%M:%S')
        # Присваиваем надписи на кнопке метку времени
        self.pushButton.setText(str_time)
        return None
