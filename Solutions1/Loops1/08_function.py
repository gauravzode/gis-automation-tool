def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
print_kwargs(name="Shaktiman", power="Lasor")
print_kwargs(name="Shaktiman")
print_kwargs(name="Shaktiman", power="Lasor", enemy="Jackal")