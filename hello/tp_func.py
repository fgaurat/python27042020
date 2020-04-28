def say_hello(prenom, *p, **d):
    """Proc say hello to parameter 'nom' """
    for posi in p:
        print(posi)

    for key in d:
        print(key, d[key])

    print("hello", prenom)


def get_hello(prenom, *p, **d):
    """Func say hello to parameter 'nom' """
    print(p)
    print(d)

    return "hello "+prenom


say_hello("fred", "un autre prenom", "encore un autre prenom",
          key1="un nom", key2="machine", key3="une autre machine")
