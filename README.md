# DemoLogger

A demo project for [this post](https://shiina18.github.io/tech/2021/08/26/python-misc-2/#logging).

```
# info.log
2021-09-25 12:06:42,736 | utils.random_util | INFO | Simple format
2021-09-25 12:06:42.736|INFO|MainProcess-10960|7|module_dir.random_module:{"message": "Json format"}
2021-09-25 12:06:42.737|INFO|MainProcess-10960|15|__main__:{"message": "info"}
2021-09-25 12:06:42.737|WARNING|MainProcess-10960|16|__main__:{"message": "warning"}
2021-09-25 12:06:42.737|ERROR|MainProcess-10960|21|__main__:
{"message": "233", "exc_info": "Traceback (most recent call last):\n  File \"D:\\PycharmProjects\\DemoLogger\\main.py\", line 19, in <module>\n    1 / 0\nZeroDivisionError: division by zero"}
```

```
# error.log
2021-09-25 12:06:42,737 | __main__ | ERROR | 233
Traceback (most recent call last):
  File "D:\PycharmProjects\DemoLogger\main.py", line 19, in <module>
    1 / 0
ZeroDivisionError: division by zero
```
