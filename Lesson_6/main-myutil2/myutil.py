def myutil_test():
    print('myutil_test() called')
    print('__name__ of myutil : ' + __name__)

# エントリポイントの場合の処理
if __name__ == '__main__':
    print('myutil.py is entry point')
    myutil_test()
