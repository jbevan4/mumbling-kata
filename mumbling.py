def mumble(string_to_mumble):
    return '-'.join((value * index).capitalize() for index, value in enumerate(string_to_mumble, start=1))
