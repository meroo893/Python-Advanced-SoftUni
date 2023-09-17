def grocery_store(**kwargs):
    return "\n".join([f"{name}: {q}" for name, q in sorted(kwargs.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))])

print(grocery_store(

bread=2,

pasta=2,

eggs=20,

carrot=1,

))