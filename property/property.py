class Property(object):
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


class SomeClass(object):
    def __init__(self, value):
        self.value = value

    @Property
    def prop(self):
        return 'x = ' + str(self.value)

    @prop.setter
    def prop(self, value):
        self.value = value

    @prop.deleter
    def prop(self):
        del self.value


if '__main__' == __name__:
    obj = SomeClass(1)
    print obj.__class__.__dict__['prop']
    print obj.prop
    obj.prop = 2
    print obj.prop
    del obj.prop
    print '42'
