from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand

from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
from cloudmesh.shell.command import map_parameters

class GlobusCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_globus(self, args, arguments):
        """
        ::

          Usage:
                globus login FROM_EP TO_EP
                globus transfer FROM_EP TO_EP DIR FROM TO [--mkdir=no]
                globus list

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """


        # arguments.FILE = arguments['--file'] or None

        map_parameters(arguments, "file")

        VERBOSE(arguments)

        from cloudmesh.globus.globus import Globus

        if arguments.login or arguments.transfer:

            from_ep = arguments.FROM_EP
            to_ep = arguments.TO_EP

            globus = Globus(source_endpoint=from_ep,
                            destination_endpoint=to_ep)
            globus.login(from_ep, to_ep)

        if arguments.transfer:
            "globus transfer FROM_EP TO_EP DIR FROM TO"

            base_directory = arguments.DIR
            from_dir = arguments.FROM
            to_dir = arguments.TO

            # SETUP LABEL
            source = f"{from_ep}:{base_directory}/{from_dir}"
            destination = f"{to_ep}:{to_dir}/{from_dir}"

            char = "-"
            label = f"{source}---{destination}"\
                .replace("/", char)\
                .replace(":", char)\
                .replace(" ", char)\
                .replace("_", char)\
                .replace(".", char)

            # SETUP ENDPOINTS
            from_ep = globus.bookmark(from_ep)
            to_ep = globus.bookmark(to_ep)

            source = f"{from_ep}:{base_directory}/{from_dir}"
            destination=f"{to_ep}:~{to_dir}/{from_dir}"



            if arguments["--mkdir"] not in ["no", "NO", "0"]:
                globus.mkdir(to_ep, f"/~{to_dir}")

            globus.transfer(source, destination, label=label)


        elif arguments.list:
            print("option b")

        return ""
