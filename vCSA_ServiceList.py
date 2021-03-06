
from vmware.vapi.vsphere.client import create_vsphere_client

from samples.vsphere.common import (sample_cli, sample_util)
from samples.vsphere.common.ssl_helper import get_unverified_session


"""
Description: Demonstrates services api workflow
1.List all services
"""

parser = sample_cli.build_arg_parser()
args = sample_util.process_cli_args(parser.parse_args())
session = get_unverified_session() if args.skipverification else None
client = create_vsphere_client(server=args.server,
                               username=args.username,
                               password=args.password,
                               session=session)

service_list = client.appliance.Services.list()

print("Example: List Appliance Services:")
print("-------------------\n")
for key, values in service_list.items():
    print("Service Name : {} ".format(key))
    print("value : {}".format(values.description))
    print("State: {} \n".format(values.state))