from Roadmap import Roadmap
from wsgiref.simple_server import make_server


def simple_wsgi_application(environment, start_response_callback):
    '''
    :param environment: Контекст окружения
    :type environment: dict

    :param start_response_callback: Обработчик запроса
    :type start_response_callback: callable

    :return: Тело ответа
    :rtype: iterable
    '''
    response_headers = [
        ('Content-type', 'text/html; charset=utf-8'),
    ]
    start_response_callback('200 OK', response_headers)
    return [str(roadmap.get_critical()).encode('utf-8')]

if __name__ == '__main__':
    roadmap = Roadmap('./dataset.yml')
    http_server = make_server('127.0.0.1', 8080, simple_wsgi_application)
    http_server.serve_forever()