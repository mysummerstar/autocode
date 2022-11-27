def demo(*args):
    print(args)
    print(type(args))


demo(10,20)


def demo2(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(kwargs)

demo2(a=1,b=2)
