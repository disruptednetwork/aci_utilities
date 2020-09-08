import requests
import json
import urllib3
from aci_operation import aci_operation as op

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

CLASS_PATH = "/api/node/class/"

# Add object name and the corresponding class name as needed
OBJECT_MAPPING = {
    "leaf_profile": {"class": "infraNodeP"},
    "intf_profile": {"class": "infraAccPortP"},
    "phys_domain": {"class": "physDomP"}
}

def main():
    # Open the settings.json and read apic's IP along with the credentials
    with open('settings.json') as f:
        settings = json.load(f)
        apic_ip = settings["apic_ip"]
        username = settings["username"]
        password = settings["password"]
    credentials = '{ "aaaUser": { "attributes": { "name":"' + username \
                  + '", "pwd":"' + password + '"}}}'
    # Login to the APIC
    session = requests.Session()
    res_body = session.post(apic_ip + '/api/aaaLogin.json' \
              , data=json.dumps(json.loads(credentials)), verify=False)
    # Example to get a list of leaf profiles
    # For a list of tenants, use
    # object_list = op.list_dn_in_class(session, apic_ip, CLASS_PATH, "fvTenant")
    object_list = op.list_dn_in_class(session, apic_ip, CLASS_PATH, OBJECT_MAPPING.get("leaf_profile").get("class"))
    print(json.dumps(object_list,indent=4))

if __name__ == "__main__":
    main()

