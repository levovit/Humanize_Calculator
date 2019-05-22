# Humanize Calculator

## Как запустить?
1. Откройте командную строку в проекте с Humanize_calculator.py
2. Введите:
 
```bash
$python Humanize_calculator.py -s "<Ваша строка>"
```

### Пример:

```bash
$python Humanize_calculator.py -s "99 + 7 =  106"
ninety nine plus seven equals one hundred six
```
```bash
$python Humanize_calculator.py -s "-2 --4 ++4"
minus two minus minus four plus four
```

### Чтобы запустить тесты:

Установите pytest если у вас его нет
```bash
$pip install pytest
```
Запуск тестов
```bash
$py.test -s -v test.py
```
