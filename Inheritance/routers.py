class Router:
    def __init__(self, externalIPAddress, internalIPAddress, network):
        self.externalIPAddress = externalIPAddress
        self.internalIPAddress = internalIPAddress
        self.network = network

    def ifconfig(self):
        print("Uplink IP: ", self.externalIPAddress)
        print("Router IP: ", self.internalIPAddress)
        print("Network  : ", self.network)



class WirelessRouter(Router):
    def __init__(self, ssid, externalIPAddress, internalIPAddress, network):
        self.ssid = ssid
        #Router.__init__(self,externalIPAddress, internalIPAddress, network)
        super().__init__(externalIPAddress, internalIPAddress, network)
    def ifconfig(self):
        print("SSID = ", self.ssid)
        #Router.ifconfig(self)
        super().ifconfig()

class Layer3Switch(Router):
    def __init__(self, vlans, externalIPAddress, internalIPAddress, network):
        self.vlans = vlans
        #Router.__init__(self,externalIPAddress, internalIPAddress, network)
        super().__init__(externalIPAddress, internalIPAddress, network)
    def ifconfig(self):
        print("VLAN = ", self.vlans)
        #Router.ifconfig(self)
        super().ifconfig()


def main():
    e220Mikrotik = WirelessRouter("E220_2.4", "192.168.210.220","192.168.220.250","192.168.220.0")
    e208Mikrotik = WirelessRouter("E208_2.4", "192.168.208.220","192.168.208.250","192.168.208.0")
    e208Router = Layer3Switch("192.168.208.0","192.168.208.1","192.168.210.1","192.168.210.0")

    e220Mikrotik.ifconfig()
    e208Mikrotik.ifconfig()
    e208Router.ifconfig()

if __name__ == "__main__":
    main()
