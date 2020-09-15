from time import localtime, strftime

class Pylog:
    def __init__(self, name, include_timestamp=True):
        self.name = name
        self.include_timestamp = include_timestamp
        if self.name is not None:
            f = open(self.name, "w")  
            f.close()      

    @property
    def include_timestamp(self):
        return self._timestamp

    @include_timestamp.setter
    def include_timestamp(self, value):
        if isinstance(value, bool):
            self._timestamp = value
        elif value is not None:
            raise TypeError("include_timestamp must be a valid boolean")
        else:
            self._timestamp = True

    def _get_timestamp(self):
        return strftime("%H:%M:%S", localtime())
    
    def log(self, values):
        if values is not None:
            f = open(self.name, "a")
            if self.include_timestamp:
                write = lambda x : f.write("{} || {}\n".format(self._get_timestamp(), x))
                
                if self._is_iter(values) and values:
                    for value in values:
                        write(value)
                else:
                    write(values)
            else:

                f.write("{}\n".format(values))
                
            f.close()
        else:
            raise ValueError("Please enter a valid value")
    @property
    def name(self):
        if self._name:
            return self._name+".txt"

    @name.setter
    def name(self, name):

        if isinstance(name, str) and name:
            self._name = name
        else:
            raise TypeError("Logger name must be a string")

    def _is_iter(self, value):
        try:
            iter(value)
        except Exception:
            return False
        else:
            return True
