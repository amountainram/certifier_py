from certifier.arguments import get_parser
from certifier.setup import config
import yaml


def main():
    """Entrypoint of certifier"""

    parsed_arguments = get_parser().parse_args()
    command = parsed_arguments.command

    print(command)

    if(command == 'setup'):
        config()
        exit(0)

    try:
        conf = yaml.load(parsed_arguments.config,
                           Loader=yaml.FullLoader)
    except FileNotFoundError:
        print("Cannot find a configuration file, please setup your environment first")
        exit(1)

    # command = parsed_arguments.command
    # subcommand = parsed_arguments.subcommand

    # if(command == 'ca'):
    #     ca.setup(parsed_arguments, config)
    # if(subcommand == 'remove'):
    #     ca.remove()
    # if(subcommand == 'create'):
    #     ca.create_ca()
    # elif(subcommand == 'sign'):
    #     ca.sign_ca()

    # if parsed_arguments.remove:
    #     ca.remove()

    exit(0)


if __name__ == "__main__":
    main()
