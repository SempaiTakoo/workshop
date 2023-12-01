from cProfile import label
from functools import reduce
from collections import defaultdict
import random
from datetime import datetime, timedelta

def generate_dates(start_date, end_date):
    """
    Генерирует список дат между указанными начальной и конечной датами.

    Параметры
    ----------
    start_date : str
        Начальная дата в формате ГГГГ-ММ-ДД.
    end_date : str
        Конечная дата в формате ГГГГ-ММ-ДД.

    Возвращает
    -------
    list
        Список дат (в виде строк в формате ГГГГ-ММ-ДД) между начальной и конечной датами.
    """

    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    date_list = [(start + timedelta(days=x)).strftime("%Y-%m-%d") for x in range((end - start).days + 1)]
    return date_list

def choose_city(cities):
    """
    Случайно выбирает город из списка городов.

    Параметры
    ----------
    cities : list
        Список названий городов.

    Возвращает
    -------
    str
        Случайно выбранный город из списка.
    """
    return random.choice(cities)

def generate_weather_data(temp_range, humidity_range, precipitation_range):
    """
    Генерирует случайные данные о погоде, включая температуру, влажность и осадки.

    Параметры
    ----------
    temp_range : tuple
        Кортеж (минимальная температура, максимальная температура), задающий диапазон температур.
    humidity_range : tuple
        Кортеж (минимальная влажность, максимальная влажность), задающий диапазон влажности.
    precipitation_range : tuple
        Кортеж (минимальное количество осадков, максимальное количество осадков), задающий диапазон осадков.

    Возвращает
    -------
    tuple
        Кортеж, содержащий случайно сгенерированные значения температуры, влажности и осадков.
    """
    temperature = random.uniform(*temp_range)
    humidity = random.uniform(*humidity_range)
    precipitation = random.uniform(*precipitation_range)
    return temperature, humidity, precipitation

def create_weather_data(start_date, end_date, cities, temp_range, humidity_range, precipitation_range):
    """
    Создает список словарей с данными о погоде для различных дат и городов.

    Параметры
    ----------
    start_date : str
        Начальная дата в формате ГГГГ-ММ-ДД.
    end_date : str
        Конечная дата в формате ГГГГ-ММ-ДД.
    cities : list
        Список названий городов.
    temp_range : tuple
        Кортеж (минимальная температура, максимальная температура), задающий диапазон температур.
    humidity_range : tuple
        Кортеж (минимальная влажность, максимальная влажность), задающий диапазон влажности.
    precipitation_range : tuple
        Кортеж (минимальное количество осадков, максимальное количество осадков), задающий диапазон осадков.

    Возвращает
    -------
    list
        Список словарей, каждый из которых представляет данные о погоде для конкретной даты и города.
    """
    weather_data = []
    for date in generate_dates(start_date, end_date):
        for city in cities:
            temperature, humidity, precipitation = generate_weather_data(temp_range, humidity_range, precipitation_range)
            weather_data.append({
                "date": date,
                "city": city,
                "temperature": round(temperature, 2),
                "humidity": round(humidity, 2),
                "precipitation": round(precipitation, 2)
            })
    return weather_data


def get_average_temperatures(data: list[dict]) -> dict[str, float]:
    '''Возвращает словарь город-средняя_температура.'''
    # Создаём словарь (город-список_температур) со стандартным значением [].
    city_temperatures: dict[str, list[float]] = defaultdict(list)

    # При помощи map создаём список кортежей (город-температура)
    # и итерируемся по нему.
    for city, temp in map(lambda x: (x['city'], x['temperature']), data):
        # Добавляем значение температуры города в список словаря по городу.
        city_temperatures[city].append(temp)

    # Создаём словарь (город-средняя_температура),
    # итерируясь по словарю (город-список_температур)
    # и вычисляя среднее значение температуры, и возвращаем его.
    return {city: sum(temps) / len(temps)
            for city, temps in city_temperatures.items()}


def get_total_precipitations(data: list[dict]) -> dict[str, float]:
    '''Возвращает словарь город-общее_количество_осадков.'''
    # Создаём словарь (город-список_осадков) со стандартным значением [].
    city_precipitations: dict[str, list[float]]  = defaultdict(list)

    # При помощи map создаём список кортежей (город-осадки)
    # и итерируемся по нему.
    for city, prec in map(lambda x: (x['city'], x['precipitation']), data):
        # Добавляем значение осадков города в список словаря по городу.
        city_precipitations[city].append(prec)

    # Создаём словарь (город-сумма_осадков), итерируясь по словарю
    # (город-список_осадков) и вычисляя сумму осадков, и возвращаем его.
    return {city: reduce(lambda a, b: a + b, precipitations)
            for city, precipitations in city_precipitations.items()}


def get_days_with_high_humidity(data: list[dict],
                                humidity_limit: float) -> list[dict]:
    '''Возвращает список словарей дней с превышением влажности.'''
    # При помощи filter выделяем в data словари,
    # в которых превышена влажность, в список и возвращаем его.
    return list(filter(lambda x: x['humidity'] > humidity_limit, data))


def get_city_min_humidity(data: list[dict], city: str) -> float:
    '''Возвращает минимальную влажность по городу.'''
    # При помощи filter выделяем в data словари, в которых нужный нам город,
    # в список. Затем при помощи map создаём список из значений влажности
    # и находим минимальное значение.
    return min(map(lambda x: x['humidity'],
                   filter(lambda x: x['city'] == city, data)))


def get_city_max_humidity(data: list[dict], city: str) -> float:
    '''Возвращает максимальную влажность по городу.'''
    # Аналогично get_city_min_humidity.
    return max(map(lambda x: x['humidity'],
                   filter(lambda x: x['city'] == city, data)))


def get_aggregated_data(data: list[dict]) -> dict:
    '''Возвращает словарь с агрегированными данными.'''
    # Создаём множество названий городов.
    cities: set[str] = set(map(lambda x: x['city'], data))
    # При помощи вышеуказанных функций получаем словари
    # со средними температурами и общими осадками.
    avg_temp: dict[str, float] = get_average_temperatures(data)
    total_prec: dict[str, float] = get_total_precipitations(data)

    # Создаём словарь, где ключи - это города.
    # Затем кладём в качестве значения словарь с данными.
    return {city: {'average_temperatures': avg_temp[city],
                   'total_precipitations': total_prec[city],
                   'max_humidity': get_city_max_humidity(data, city),
                   'min_humidity': get_city_min_humidity(data, city)}
            for city in cities}


def test() -> None:
    '''Тестирует функции.'''
    weather_data: list[dict] = create_weather_data(
        start_date='2023-11-01',
        end_date='2023-11-05',
        cities=['CityA', 'CityB', 'CityC'],
        temp_range=(10, 30),
        humidity_range=(50, 90),
        precipitation_range=(0, 10)
    )
    print('get_average_temperatures: ')
    print(get_average_temperatures(weather_data), '\n')

    print('get_total_precipitations: ')
    print(get_total_precipitations(weather_data), '\n')

    print('get_days_with_high_humidity(limit humidity = 85): ')
    print(get_days_with_high_humidity(weather_data, 85), '\n')

    print('CityA min max: ')
    print(get_city_min_humidity(weather_data, 'CityA'))
    print(get_city_max_humidity(weather_data, 'CityA'), '\n')

    print('get_aggregated_data: ')
    print(get_aggregated_data(weather_data), '\n')


if __name__ == '__main__':
    test()
