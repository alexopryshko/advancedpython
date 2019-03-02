class Base:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__()
        attrs = tuple(cls.__annotations__.keys())

        def __init__(self, *args, **kwargs):
            # Skimping on the argument-checking because I'm lazy.
            if len(args) > len(attrs):
                raise TypeError("too many positional arguments")
            for attr, val in zip(attrs, args):
                setattr(self, attr, val)
            for attr, val in kwargs.items():
                if attr not in attrs:
                    raise TypeError("got an unexpected keyword argument {!r}")
                setattr(self, attr, val)

        cls.__init__ = __init__
        print(kwargs)
        if kwargs.get("repr", True):
            repr_format = \
                f'<{", ".join(f"{attr}={{{attr}!r}}" for attr in attrs)}>'

            def __repr__(self):
                all_attrs = self.__class__.__dict__.copy()
                all_attrs.update(self.__dict__)
                return repr_format.format_map(all_attrs)

            cls.__repr__ = __repr__


class Simple(Base):
    question: str
    answer: int = 42


class OtherSimple(Base, repr=False):
    question: str = 'q'
    answer: int = '1'


a = Simple(question="Ultimate Question of Life, The Universe, and Everything")
print(repr(a))

b = OtherSimple()
print(repr(b))
