import requests
import json
import urllib3
from aci_operation import aci_operation as op
import object_mapping as om

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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
    object_name = "leaf_profile"
    object_list = op.list_dn_in_class(session, apic_ip, om.CLASS_PATH, om.OBJECT_MAPPING.get(object_name).get("class"))

    print("A list of {}".format(object_name))
    print(json.dumps(object_list, indent=4))

    # Example to print all objects in OBJECT_MAPPING    
    for obj_type in om.OBJECT_MAPPING:
        dn_list = op.list_dn_in_class(session, apic_ip, om.CLASS_PATH, om.OBJECT_MAPPING.get(obj_type).get("class"))
        print("A list of {}".format(obj_type))
        print(json.dumps(dn_list, indent=4))
    ################################################################################# 
    # Below is an example to delete all tenants except the pre-defined ones
    #   in fvTenant class
    # CAUTION: THIS WILL DELETE ALL TENANTS. DO NOT TRY THIS IN PRODUCTION
    # Uncomment to try
    #################################################################################
    # predefined_tenants = ["common", "infra", "mgmt"]
    # tenant_class = "fvTenant"
    # tenant_dn_prefix = "uni/tn-"
    # tenant_list = op.list_dn_in_class(session, apic_ip, om.CLASS_PATH, tenant_class)
    # for tenant in tenant_list:
    #     if not tenant[len(tenant_dn_prefix):] in predefined_tenants:
    #         op.delete_object(session, apic_ip, om.NODE_PATH, tenant, tenant_class)
    #################################################################################
    # Below is an example to delete all objects in OBJECT_MAPPING
    # EXTREME CAUTION: THIS WILL DELETE EVERY OBJECT IN THE OBJECT_MAPPING CLASS"
    # object_mapping.py contains leaf profile, interface profile, physical domain, 
    #   l3 domain VLAN pool and AEP. 
    # All objects under the mentioned classes will be deleted!!!!
    # DO NOT TRY THIS IN PRODUCTION 
    #################################################################################
    # for obj_type in om.OBJECT_MAPPING:
    #     obj_class = om.OBJECT_MAPPING.get(obj_type).get("class")
    #     obj_list = op.list_dn_in_class(session, apic_ip, om.CLASS_PATH, obj_class)
    #     print ("Class: {}".format(obj_class))
    #     for obj in obj_list:
    #         op.delete_object(session, apic_ip, om.NODE_PATH, obj, obj_class)
    #################################################################################
 
    
if __name__ == "__main__":
    main()

