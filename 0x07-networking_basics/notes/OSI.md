# OSI model (Open Systems Interconnection model)

* Conceptual framework for how applications communicate over a network

* There are 7 layers, and the layers depiction help users identify what happens in a networking system:
    * 7 | [Application](#the-application-layer)
    * 6 | [Presentation](#the-presentation-layer)
    * 5 | [Session](#the-session-layer)
    * 4 | [Transport](#the-transport-layer)
    * 3 | [Network](#the-network-layer)
    * 2 | [Data Link](#the-data-link-layer)
    * 1 | [Physical](#the-physical-layer)

* These layers are provided by a mixture of network car drivers, operating systems, applications and networking hardware that facilitate the transmission over wifi, fibre optic or any other wireless [protocols](#00-network-protocol)

<br>

### The Application Layer

* The application layer is used by end-user software such as web browsers and email clients. It provides protocols that allow software to send and receive information and present meaningful data to users.

* One of these protocols may be [FTP](#02-ftp), [SMPT](#03-smtp) or [HTTP](#01-http) that work with various browsers, Chrome, Firefox, Brave etc

### The Presentation Layer

The presentation layer prepares data for the application layer. It defines how two devices should encode, encrypt, and compress data so it is received correctly on the other end. The presentation layer takes any data transmitted by the application layer and prepares it for transmission over the session layer. Example: jpg, jpeg, png image files are encrypted in presentation layer (`turned into a signal ex: 101010101010`) when sent over a network then decrypted so that the client can view it in the application layer.

### The Session Layer

The session layer creates communication channels, called sessions, between devices. It is responsible for opening sessions, ensuring they remain open and functional while data is being transferred, and closing them when communication ends

### The Transport Layer

The transport layer takes data transferred in the session layer and breaks it into “segments” on the transmitting end. It is responsible for reassembling the segments on the receiving end, turning it back into data that can be used by the session layer. The transport layer carries out flow control, sending data at a rate that matches the connection speed of the receiving device, and error control, checking if data was received incorrectly and if not, requesting it again ex: ([TCP UDP](UDP_TCP.md))

### The Network Layer

The network layer has two main functions. One is breaking up segments into network packets, and reassembling the packets on the receiving end. The other is routing packets by discovering the best path across a physical network. The network layer uses network addresses (typically Internet Protocol addresses) to route packets to a destination node. ex: ([IP](INTERNET.md), IPX, ICMP)

### The Data Link Layer

The data link layer establishes and terminates a connection between two physically-connected nodes on a network. It breaks up packets into frames and sends them from source to destination. This layer is composed of two parts—Logical Link Control (LLC), which identifies network protocols, performs error checking and synchronizes frames, and Media Access Control (MAC) which uses MAC addresses to connect devices and define permissions to transmit and receive data. ex: (ETHERNET, PPP)

### The Physical Layer

The physical layer is responsible for the physical cable or wireless connection between network nodes. It defines the connector, the electrical cable or wireless technology connecting the devices, and is responsible for transmission of the raw data, which is simply a series of 0s and 1s, while taking care of bit rate control. ex: (ETHERNET, USB)

<br><br>
<hr>

## Definitions

### 00# network protocol:

A network protocol is a set of rules for formatting data so that all connected devices can process it. Read about the different network layer protocols.

### 01# HTTP

HTTP(HyperText Transfer Protocol) is an application protocol for fetching resources such as HTML documents. It is the foundation of any data exchange on the Web and it is a client-server protocol, which means requests are initiated by the recipient, usually the Web browser.

### 02# FTP

FTP (File Transfer Protocol) is a network protocol for transmitting files between computers over Transmission Control Protocol/Internet Protocol (TCP/IP) connections. Within the TCP/IP suite, FTP is considered an application layer protocol.

### 03# SMTP

The Simple Mail Transfer Protocol (SMTP) is an application used by mail servers to send, receive, and relay outgoing email between senders and receivers. Common providers include: iCloud, Gmail, Outlook, AT&T, Comcast, AOL
