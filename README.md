# panpy-scripts
### unifi-to-userid ###
This script pulls the client hostname value out from a UniFi controller along with associated IP address and maps it to UserId on a Palo Alto firewall. Valuable for small deployments where AD isn't in use, and allows for consistent reporting and information between Palo Alto and UniFi.

Requirements:
pip install pan-os-python
pip install unificontrol

For UniFi creditials, the account used to connect to your controller (for some reason) needs to be a cloud-enabled/remote account. For the account connecting to the PAN Firewall, the only permissions needed are XML-API/User-ID Agent.
