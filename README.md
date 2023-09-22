# clean-school-base
Учебный проект для редактирования данных в https://github.com/devmanorg/e-diary.git

### Запуск
1) Скопировать scripts.py в корневую папку проекта.
2) Выполнить команду
```
python .\manage.py shell 
```
3) Заполнить ФИО. Далее скопировать в терминал.

```
import scripts
child = scripts.get_child("ФИО")
scripts.fix_marks(child) # Исправляет оценки
scripts.remove_chastisements(child) # Удаляет замечания 
scripts.create_commendation(child, "Математика") # Создает похвалы на уроки
```
