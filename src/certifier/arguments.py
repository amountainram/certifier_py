import argparse


def get_parser():
    parser = argparse.ArgumentParser(
        prog='certifier', description='launches certificate authority cli', epilog='use it with care')

    # setup
    subparsers = parser.add_subparsers(dest='command', help='sub-command help')

    subparsers.add_parser(
        'setup', help='setup of the local certification environment')

    # # setup ca
    # parser.add_argument('-c', '--config', type=argparse.FileType(
    #     'r', encoding='UTF-8'), default='./.certifierc.yaml')

    # parser_ca = subparsers.add_parser(
    #     'ca', help='setup of the certificate authority')
    # parser_ca.add_argument('--remove', action='store_true',
    #                        help='remove the certificate authority after setup is done')
    # subparsers_ca = parser_ca.add_subparsers(
    #     dest='subcommand', help='ca sub-command help')

    # # setup ca remove
    # parser_ca_remove = subparsers_ca.add_parser(
    #     'remove', help='remove certificate authority folder')

    # # setup ca create [--keep] [-y/--yes]
    # parser_ca_create = subparsers_ca.add_parser(
    #     'create', help='create a new certificate authority')
    # parser_ca_create.add_argument(
    #     '-o', '--overwrite', action='store_true', help='overwrite an existing ca')
    # # setup ca sign [-a/--all] [-y/--yes] [...]
    # parser_ca_sign = subparsers_ca.add_parser(
    #     'sign', help='signs certificates to selected services')
    # parser_ca_sign.add_argument(
    #     '--new', action='store_true', help='overwrite existing ca if exists with a new one')
    # parser_ca_sign.add_argument('-w', '--overwrite', action='store_true',
    #                             help='overwrite existing certificates if any is found')
    # group_sign = parser_ca_sign.add_mutually_exclusive_group(required=True)
    # group_sign.add_argument('-a', '--all', action='store_true')
    # group_sign.add_argument('-s', '--services', nargs='+', type=str)

    return parser
