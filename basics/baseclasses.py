#!/usr/bin/env python

import abc

class RomaBase(object):
    # classmethod is same as static method
    # Find out all the classes that inhert from this class.
    @classmethod
    def subclasses(cls):
        work = [cls]
        classes = set()

        while len(work) > 0:
            item = work.pop()
            work.extend(item.__subclasses__())
            classes.add(item)

        classes.remove(cls)

        output = {}
        for item in classes:
            output[item.__name__] = item

        return output

    @property
    def class_name(self):
        return self.__class__.__name__


class BaseMatai(RomaBase):
    def __init__(self):
        self.myname = "BaseMatai"

    def to_dict(self):
        return  {'class': self.class_name, 'type': 'lastname'}

class RMatai(BaseMatai):
    def __init__(self):
        self.matai = "ajaymatai"

    def to_dict(self):
        return {'class': self.class_name, 'type': 'Inital+LastName'}


class Abstract(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def details(self):
        """something"""

class Concrete(Abstract):
    details = {'prop': 'value'}


if __name__ == "__main__":
    print "Classes RomaBase <- BaseMatai <- RMatai"
    print "BaseMatai.subclasses: %s" % BaseMatai.subclasses()

    print "RomaBase.subclasses: %s" % RomaBase.subclasses()

    roma = RMatai()
    print 'roma dict %s' % roma.to_dict()

    bm = BaseMatai()
    print 'bm dict %s' % bm.to_dict()

    conc = Concrete()
    print 'conc.details %s' % conc.details
