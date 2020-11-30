from urls_finder.logic import SearchEngine, OutputMethods, recursive_search



def get_search_params():
    search_query = str(input(
        'Введите поисковый запрос? '))
    urls_counter = int(input(
        'Какое количество ссылок хотите получить? Укажите цифрой. '))
    seo_engine = int(input(
        'В каком поисковике? '
        'Для поиска в Google введите - 2. '))
    is_recursive_search = int(input(
        'Ищем рекурсивно? Выберите: НЕТ - 1, ДА - 2. '))
    if is_recursive_search == 2:
        keyword = str(input(''
                            'Вы выбрали рекурсивный поиск? '
                            'Введите слово по смыслу которого будем искать: '))
    else:
        keyword = None
    output_format = int(input(
        'Куда вывести результаты? '
        'Выберите: Консоль - 1, JSON - 2, CSV - 3. '))
    search_params = {
        'search_query': search_query,
        'urls_counter': urls_counter,
        'seo_engine': seo_engine,
        'is_recursive_search': is_recursive_search,
        'output_format': output_format,
        'keyword': keyword
    }
    return search_params


if __name__ == '__main__':
    params = get_search_params()
    if params['seo_engine'] == 2:
        if params['is_recursive_search'] == 2:
            result = recursive_search(
                params['urls_counter'],
                params['keyword'],
                SearchEngine.google_search(
                    params['urls_counter'], params['search_query']))
        else:
            result = SearchEngine.google_search(
                params['urls_counter'], params['search_query'])

    om = OutputMethods()

    if params['output_format'] == 1:
        print(result)
    elif params['output_format'] == 2:
        om.json_output('results.json', result)
    else:
        om.csv_output('results.csv', result)