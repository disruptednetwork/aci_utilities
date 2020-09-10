# This file stores constants

CLASS_PATH = "/api/node/class/"

NODE_PATH = "/api/node/mo/"

# Modify this to fit your needs
OBJECT_MAPPING = {
    "leaf_profile": { "class": "infraNodeP", "dn_prefix": "uni/infra/nprof-" },
    "interface_profile": { "class": "infraAccPortP", "dn_prefix": "uni/infra/accportprof-" },
    "phys_domain": { "class": "physDomP", "dn_prefix": "uni/phys-" },
    "l3_domain": { "class": "l3extDomP", "dn_prefix": "uni/l3dom-" },
    "vlan_pool": { "class": "fvnsVlanInstP", "dn_prefix": "uni/infra/vlanns-" },
    "aep": { "class": "infraAttEntityP", "dn_prefix": "attentp-" }
}

