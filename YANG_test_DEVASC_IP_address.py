from ncclient import manager
import xml.dom.minidom

# Courseware Cisco DevNet Sandbox
HOST = '131.226.217.135'
USER = 'developer'
PASS = 'SF!_Zx623_37'
PORT = 830

# filtering interface GigabitEthernet1 only
netconf_filter = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
       <name>GigabitEthernet1</name>
    </interface>
  </interfaces>
</filter>
"""

# device is Cisco CSR
m = manager.connect(host=HOST, port=PORT, username=USER, password=PASS,
                         hostkey_verify=False, device_params={'name': 'csr'})

reply = m.get_config(source='running', filter = netconf_filter)
# Pretty print the XML reply
print(xml.dom.minidom.parseString(reply.xml).toprettyxml())
m.close_session()

#Branch1_test

#Branch2_test
