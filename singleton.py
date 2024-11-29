# para tener variables de clases "globales" ya que no se pueden usar variables globales en python.
# https://stackoverflow.com/questions/6760685/what-is-the-best-way-of-implementing-singleton-in-python

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance