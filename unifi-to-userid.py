from panos.firewall import Firewall
from panos.userid import UserId
from unificontrol import UnifiClient
import ssl

# Define UniFi API Creds

UNIFI_USER = '{username}'
UNIFI_PASSWORD = '{password}'
UNIFI_SITE = '{site}'

# Define Palo Alto FW Device
FW_IP = '{palo_fw_ip}'
FW_UN = '{palo_username}'
FW_PW = '{palo_password}'

# Get self-signed cert, and connect to UniFi
cert = ssl.get_server_certificate(("{unifi.localhost}", 8443))

client = UnifiClient(host="{unifi.localhost}",
    username=UNIFI_USER, password=UNIFI_PASSWORD, site=UNIFI_SITE,
    cert=cert)

# Get all connected UniFi Clients
all_devices = client.list_clients()

# Connect to PAN Firewall
fw = Firewall(FW_IP, FW_UN, FW_PW)
fwuid = UserId(fw)

for n in all_devices:
    try:
        user=n['hostname']
        ipadd=n['ip']
        UserId.login(fwuid, user=user, ip=ipadd, timeout=5)
    except:
        pass