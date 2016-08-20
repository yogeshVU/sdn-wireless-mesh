#!/usr/bin/python
 
"""
This example shows how to work with different APs
"""
from mininet.net import Mininet
from mininet.node import  Controller, RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink
 
def topology():
    "Create a network."
    net = Mininet( controller=Controller, link=TCLink, switch=OVSKernelSwitch )
 
    print "*** Creating nodes"
    sta1 = net.addStation( 'sta1', wlans= 2)
    h1 = net.addHost( 'h1', ip="192.168.10.1/24" )
    h2 = net.addHost( 'h2', ip="192.168.20.1/24" )
    ap1 = net.addBaseStation( 'ap1', ssid="ssid_1", mode="g", channel="1" )
    ap2 = net.addBaseStation( 'ap2', ssid="ssid_2", mode="g", channel="6" )
    c0 = net.addController('c0', controller=Controller, ip='127.0.0.1', port=6633 )
 
    print "*** Adding Link"
    net.addLink(h1,ap1)
    net.addLink(h2,ap2)
    net.addLink(sta1, ap1)
    net.addLink(sta1, ap2)
 
    print "*** Starting network"
    net.build()
    c0.start()
    ap1.start( [c0] )
    ap2.start( [c0] )
    sta1.cmd('ifconfig sta1-wlan0 192.168.10.10 netmask 255.255.255.0')
    sta1.cmd('ifconfig sta1-wlan1 192.168.20.10 netmask 255.255.255.0')
    print "*** Running CLI"
    CLI( net )
    print "*** Stopping network"
    net.stop()
 
if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()
