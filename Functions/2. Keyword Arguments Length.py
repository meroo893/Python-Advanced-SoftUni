def kwargs_length(**kwargs):
    return len(kwargs.keys())

print(kwargs_length(Peter = 5, George = "Bye"))
