# MAC, IP, IPV4, IPV6

## What is a MAC Address?

A Media Access Control (MAC) address is a string of characters that identifies a device on a network. It’s tied to a key connection device in your computer called the network interface card, or NIC. The NIC is essentially a computer circuit card that makes it possible for your computer to connect to a network. A NIC turns data into an electrical signal that can be transmitted over the network.

Every NIC has a hardware address that’s known as a MAC address. Whereas IP addresses are associated with a networking software called TCP/IP, MAC addresses are linked to the hardware of network adapters

## What is an IP adress?

An IP address (Internet Protocol address) is a numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication. IP addresses serve two main purposes: identifying the host or network interface and providing the location of the device in the network

* ### IPv4

  IPv4 (Internet Protocol version 4) is the fourth version of the Internet Protocol and is the most widely used version to date. It uses a 32-bit address format, represented in four sets of numbers ranging from 0 to 255, separated by dots (e.g., 192.168.1.1). The total number of unique IPv4 addresses is approximately 4.3 billion.

* ### IPv6

  IPv6 (Internet Protocol version 6) is the successor to IPv4 and was introduced to address the issue of IPv4 address exhaustion. It uses a 128-bit address format, represented in eight groups of hexadecimal digits, separated by colons (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334). This significantly expands the number of available IP addresses to an astronomical amount, making it practically limitless.


## HOW is MAC different from IP

A MAC address (Media Access Control address) is a unique identifier assigned to each network interface card (NIC) or network adapter of a device. It is a hardware address and is used at the data link layer of the OSI (Open Systems Interconnection) model to identify devices within a local area network (LAN). Unlike an IP address, which is assigned to a device by the network and can change depending on the network it is connected to, a MAC address is hard-coded into the network interface's hardware by the manufacturer and remains constant throughout the device's lifetime.

MAC addresses are 48-bit or 64-bit binary values (usually displayed in hexadecimal format) and have a globally unique identifier called the Organizationally Unique Identifier (OUI). The first half of the MAC address represents the OUI, which is assigned to the manufacturer of the network interface, while the second half is a unique value assigned by the manufacturer.

Here's an example of a MAC address: 00:1A:2B:3C:4D:5E

Key differences between a MAC address and an IP address:

1. Location in the network stack: A MAC address operates at the data link layer (Layer 2) of the OSI model, providing a unique identifier for devices within the same local network. An IP address, on the other hand, operates at the network layer (Layer 3) and is used for communication across different networks.

2. Uniqueness: A MAC address is typically globally unique for each network interface card produced by different manufacturers. IP addresses, especially in IPv4, can be shared or reused within different networks, leading to the need for Network Address Translation (NAT) to manage the limited address space.

3. Assignment: A MAC address is assigned by the network adapter's manufacturer and cannot be changed easily. An IP address is assigned dynamically by a DHCP (Dynamic Host Configuration Protocol) server or statically configured by a network administrator, and it can be changed as devices move between networks.

4. Scope: A MAC address is relevant only within the local network segment (LAN), while an IP address enables communication between devices across different networks, including local and global networks (e.g., the internet).

In summary, MAC addresses are used to identify devices within a local network, while IP addresses are used to identify devices and enable communication across different networks on the internet. Each serves a distinct purpose in the process of data transmission and network communication.
