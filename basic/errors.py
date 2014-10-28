try:
    # raise AssertionError("test")
    a = 1/0
except AssertionError:
    print "error"
except ZeroDivisionError:
    print "integer division "
finally:
    print "exit"
