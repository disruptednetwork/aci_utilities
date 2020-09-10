import json
import object_mapping as om

def list_dn_in_class(session, apic_ip, query_path, class_name):
# This function send a GET request to the specified APIC and 
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

def delete_object(session, apic_ip, mo_path, distinguish_name, class_name):
# This function send a POST request to the specified APIC and 
# delete the specified object DN from the specified class.
# Input:  session           - a session object from requests library 
#         apic_ip           - APIC's IP address
#         mo_path           - Managed Object path, typically /api/node/mo/
#         distinguish_name  - dn of the object. For example, uni/tn-Tenant1
#         class_name        - class name, for example fvTenant    
    dn = {}
    dn["dn"] = distinguish_name
    dn["status"] = "deleted"
    body = {}
    body[class_name] = { "attributes": dn, "children": [] }
    print ("Deleting {}".format(distinguish_name))
    response_body = session.post(apic_ip + url_path + ".json", data=json.dumps(body), verify=False)
    if (response_body.ok):
        print ("{} deleted successfully".format(distinguish_name))
    else:
        print ("{} not deleted with {} error".format(distinguish_name, response_body.status_code))

