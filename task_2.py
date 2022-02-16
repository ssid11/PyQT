# 2.Написать функцию host_range_ping() для перебора ip-адресов из заданного
# диапазона. Меняться должен только последний октет каждого адреса.
# По результатам проверки должно выводиться соответствующее сообщение.


from ipaddress import ip_address
from task_1 import host_ping



def host_range_ping():
    while True:
        start_ip = input("Введите стартовый адрес IP v.4:")
        try:
            last_oct = int(start_ip.split('.')[3])
            if last_oct > 254 or last_oct < 1:
                print('Недопустимое значение последнего октета')
            else:
                break
        except:
            print('Что-то это не похоже на IP адрес.\nДавайте еще.\n')
    while True:
        count =  input("Сколько адресов проверить?")
        if not count.isnumeric():
            print('Введите число проверяемых алресов.\n')
            continue
        count = int(count)
        if last_oct + count > 254:
            print('Последний октет проверяемого адреса не может быть больше 254.\n Повторите ввод\n')
            continue
        break

    return host_ping(list([str(ip_address(start_ip)+i) for i in range(count)]))



if __name__ == '__main__':
    print(host_range_ping())
