import argparse

def pars_dec():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', default=1)
    args = parser.parse_args

    return print(f'В скрипт передано: {args}')