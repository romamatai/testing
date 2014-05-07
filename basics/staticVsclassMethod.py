#!/usr/bin/env python

class MyBase():
    @classmethod
    def foo(cls):
        print "What class am I? %s" % cls


class MySub(MyBase):
    def somethod():
        print "some method"

    @classmethod
    def foo(cls):
        print "classmethod overriden as instance method %s" % cls


if __name__ == "__main__":
    print "MyBase.foo"
    MyBase.foo()
    print "MySub.foo"
    try:
        MySub.foo()
    except TypeError:
        pass
    finally:
        pass

    sub = MySub()
    sub.foo()
    
