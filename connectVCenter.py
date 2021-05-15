import requests
import urllib3
from vmware.vapi.vsphere.client import create_vsphere_client
session = requests.session()

# Disable cert verification for demo purpose.
# This is not recommended in a production environment.
session.verify = False

# Disable the secure connection warning for demo purpose.
# This is not recommended in a production environment.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Connect to a vCenter Server using username and password
vsphere_client = create_vsphere_client(server='100.98.13.40', username='administrator@vsphere.local', password='Dell$1234', session=session)
if vsphere_client:
    print("Connection success ",vsphere_client)
# List all VMs inside the vCenter Server
my_list = vsphere_client.vcenter.VM.list()
print(my_list)
n = 1
a = [my_list[i:i + n] for i in range(0, len(my_list), n)]

for s in a:
    print(*s)
