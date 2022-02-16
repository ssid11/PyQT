# 1.Написать функцию host_ping(), в которой с помощью утилиты ping будет
# проверяться доступность сетевых узлов. Аргументом функции является список,
# в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
# В функции необходимо перебирать ip-адреса и проверять их доступность с выводом
# соответствующего сообщения («Узел доступен», «Узел недоступен»).
# При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().

from ipaddress import ip_address
from pprint import pprint
from socket import gethostbyname
from subprocess import Popen, PIPE


def host_ping(hosts):
    # Словарь для записи результатов
    result = {'reachable_host': [], 'not_reachable_host': []}

    for host in hosts:
        try:
            host_ip = ip_address(host)
        except ValueError:
            host_ip = ip_address(gethostbyname(host))

        process = Popen(f'ping {host_ip} -w 500 -n 2', stdout=PIPE,
                        encoding='utf-8')
        process.wait()
        if process.returncode == 0:
            # Хост пингуется, добавляем в список доступных
            result['reachable_host'].append(str(host_ip))
        else:
            # Хост неоступен, добавляем его в список  недоступных
            result['not_reachable_host'].append(str(host_ip))
    return result


if __name__ == '__main__':
    hosts = ['192.168.0.200', '127.0.0.1', '2.2.2.2', 'ya.ru']
    #Красиво печатаем с отступами
    pprint(host_ping(hosts))
