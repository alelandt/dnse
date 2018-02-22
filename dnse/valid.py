def check_url(name):
    check = name.split('.')
    if len(check) == 2 and len(check[1]) > 0:
        return True
    else:
        return False
