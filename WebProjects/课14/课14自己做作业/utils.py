import time


def log(*args, **kwargs):
    format = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    #中文windows默认打开文件编码是gbk，所以指定utf-8
    with open('log.txt', 'a', encoding='utf-8') as f:
        # 把日志写入文件f中
        print(dt, *args, file=f, **kwargs)