from filewatch.tail import Tail


def func(path, line):
    print("%s: %s" % (path, line))


t = Tail()
t.tail("/Users/congsl/*.log")
t.subscribe(func)