def liczby(c, *cyfry):
    suma = c
    count = len(cyfry)
    print(c)
    print(cyfry)
    for i in cyfry:
        suma += i
    print(f"Suma {suma}, średnia {suma / count}")


liczby(5, 1)
liczby(5, 1, 4, 45, 67, 45, 67, 88, 1, 2, 3, 4, 5, 6, 67, 8, 9, 0)


def connect(**opcje):
    print(opcje)
    connect_param = {
        'host': '127.0.0.7',
        'port': '8080',
        'user': 'admin',
        'pass': '123456'
    }
    connect_param['pwd'] = opcje
    print(connect_param)


connect(user='/home')
connect(root='/')
connect(root='/', user='/home')


def allparams2(a, b, /, c=42, *args, d=256, e, **kwargs):
    print('a, b, c ', a, b, c)
    print('d, e', d, e)
    print('args', args)
    print('kwargs', kwargs)


allparams2(2, 4, 7, 8, 9, 11, 12, 33, 33, d=7, e=6, f=14)
allparams2(2, 4, 7, 8, 9, 11, 12, 33, 33, e=6, f=14)