import json

def list_dn_in_class(session, apic_ip, query_path, class_name):
# This function send GET request to the specified APIC and 
# list all objects DN in the specified class.
# Input:  session     - a session object from requests library 
#         apic_ip     - APIC's IP address
#         query_path  - class URL, typically /api/node/class/
#         class_name  - class name, for example fvTenant    
    url = apic_ip + query_path + class_name + ".json"
    response_body = session.get(url, verify=False)
    object_list = json.loads(response_body.text)["imdata"]
    dn_list = []
    for object in object_list:
        dn_list.append(object[class_name]["attributes"]["dn"])
    return dn_list

