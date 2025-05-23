# Интегратор с графической визуализацией

Этот проект представляет собой программу для численного вычисления площади под графиком функции методом трапеций, а также для отображения графика функции с визуализацией метода интегрирования. Программа использует библиотеку `matplotlib` для построения графика и `numpy` для численных вычислений.

## Описание

Программа принимает на вход:

- Математическое выражение для функции от переменной `x` (например, `x**2`, `sqrt(x**3 + 1)`).
- Левую и правую границы интегрирования.
- Количество шагов для численного интегрирования.

Результатом работы программы является площадь под графиком функции на заданном интервале, а также графическое отображение функции и разбиения на трапеции, используемые для вычисления интеграла.

## Установка

Установите необходимые зависимости с помощью `pip`:

```bash
pip install -r requirements.txt
```

## Использование

Запуск программы
Чтобы запустить программу, используйте следующую команду:

```bash
python3 Calculeted.py
```

## Разработка

### Структура проекта:

- `Calculeted.py`: Основной скрипт программы.
- `requirements.txt`: Файл с зависимостями.
- `README.md`: Этот файл.

## Важные замечания

- Функция для вычисления интеграла может содержать стандартные математические операции, такие как возведение в степень (`**`), корни (`sqrt`), синус (`sin`), косинус (`cos`), экспонента (`exp`), логарифм (`log`).
- Важно, чтобы количество шагов было положительным числом.
- Если левая граница не меньше правой, программа выведет ошибку.

## Использование

### Запуск программы

Чтобы запустить программу, используйте следующую команду:

```bash
python3 Calculeted.py
