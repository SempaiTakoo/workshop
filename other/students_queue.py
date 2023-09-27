def get_all_students_list() -> set:
    return {
        'Александр Ф', 'Алексей Г', 'Анастасия Н',
        'Андрей Д', 'Андрей И', 'Анна О',
        'Анна С', 'Далгат И', 'Даниил Г',
        'Даниил Ц', 'Данил З', 'Иван К',
        'Исмаил Х', 'Кирилл С', 'Кристина Б',
        'Леонид А', 'Леонид К', 'Михаил К',
        'Тариель К', 'Николай Ц', 'Роман Г',
        'Роман С', 'Рустам Р', 'Серафим Ш'
    }


def get_my_english_group() -> set:
    return {
        'Даниил Г', 'Исмаил Х', 'Роман С',
        'Анастасия Н', 'Николай Ц', 'Анна С',
        'Анна О', 'Данил З', 'Даниил Ц',
        'Серафим Ш', 'Александр Ф', 'Тариель К'
    }


def print_english_group():
    students = get_my_english_group()
    for i in range(len(students)):
        print(f'{i + 1:>2} | {students.pop()}')


if __name__ == '__main__':
    print_english_group()