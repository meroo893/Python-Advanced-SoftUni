def even_odd(*args):
    type = args[-1]
    if type == "even":
        return [x for x in args[:-1] if int(x) % 2 == 0]
    else:
        return [x for x in args[:-1] if int(x) % 2 != 0]