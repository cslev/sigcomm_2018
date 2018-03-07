---
layout: default
title: "ACM SIGCOMM 2018 Tutorial (Full-Day): The Netmap framework for NFV applications"
group: Tutorials

data:
  - type: day
    time: Friday, August 25, 2017
    room: "BH4760 (Boelter Hall)"

  - type: tutorial
    time: 9:00am - 9:15am
    title: Welcome and Intro

  - type: tutorial
    time: 9:15am - 10:30am
    title: "<ul>
    <li>Background and motivation.</li>
    <li>Introduction to the Netmap API with examples.</li>
    <li>The VALE switch and Netmap pipes.</li>
    </ul>"

  - type: break
    time: 10:30am - 11:00am
    room: Foyer
    title: Coffee Break

  - type: tutorial
    time: 11:00am - 12:30pm
    title: "<ul>
    <li>Netmap as a backend for VMs.</li>
    <li>Pass-through of host Netmap ports.</li>
    </ul>"

  - type: break
    time: 12:30pm - 2:00pm
    room: Foyer
    title: Lunch Break

  - type: tutorial
    time: 2:00pm - 3:30pm
    title: "<ul>
    <li>Hands-on experience: writing an NFV application using the Netmap API.</li>
    <li>Exploiting the different kinds of Netmap ports and passthrough.</li>
    </ul>"

  - type: break
    time: 3:30pm - 4:00pm
    room: Foyer
    title: Coffee Break

  - type: tutorial
    time: 4:00pm - 5:30pm
    title: "<ul><li>Continue hands-on experience:<ul><li>writing and loading an in-kernel VALE switch module.</li></ul></li>
    <li>Conclusion.</li>
    </ul>"

presenters:
  - name:        Giuseppe Lettieri
    affiliation: Universita' di Pisa
    bio:         "<p>Giuseppe Lettieri is researcher and lecturer at the Dipartiment di Ingegneria dell'Informazione. In the past few years he has contributed to the development and maintenance of the netmap framework for fast packet I/O, including the introduction of netmap pipes, a very fast IPC mechanism based on the netmap API, and the design of ptnetmap, a very fast virtual passthrough for virtual machines. For the Openlab EU project he has designed and implemented the Open vSwitch port for the PlanetLab EU testbed.</p>"

  - name:        Vincenzo Maffione
    affiliation: Universita' di Pisa
    bio:         "<p>Vincenzo Maffione is a second-year PhD student the Dipartimento di Ingegneria dell'Informazione of the Università di Pisa, Italy. In the past four years he has worked as a netmap maintainer and developed some of its subsystems, including the emulated netmap mode (to run netmap applications over any network interface), ptnetmap host support and guest drivers. He has also integrated the netmap datapath within various hypervisors, including QEMU, bhyve and Xen. His main research interests include high speed user-space networking and Virtual Machine networking.</p>"

  - name:        Luigi Rizzo
    affiliation: Universita' di Pisa
    bio:         "<p>Luigi Rizzo is associate professor at the Dipartimento di Ingegneria dell'Informazione, University of Pisa. His most popular achievements include the netmap framework for fast packet I/O, the dummynet traffic shaper, and a popular erasure code used for reliable multicast and software RAID. Moreover, he is a longtime FreeBSD committer. Prof. Rizzo has been a frequent visiting researcher at international research institutions and companies. He visited ICSI/Univ. Of California at Berkeley in autumn 2000, 2001, 2002 and 2013; Intel Research Cambridge in autumn 2003 and 2004; Intel Research Berkeley in autumn 2010; Google Mountain View in autumn 2012. He has received funding from several companies including Cisco, Microsoft Research, Intel Research, NetApp. He has been a Programme Committee Member for many conferences including ACM Sigcomm, Infocom, NGC, ICNP, Co-Next, NSDI, EuroSys, Usenix ATC; reviewer for the main journals in networking edited by IEEE, ACM and Elsevier; General Chair for the NGC'99 and ACM Sigcomm 2006 conferences, and Technical Program Co-Chair for the ACM Sigcomm 2009 and CoNEXT 2014 conferences.</p>"

  - name:        Michio Honda
    affiliation: NEC Laboratories Europe
    bio:         "<p>Michio Honda is a senior researcher at NEC Laboratories Europe in Germany. He has joined the netmap project since 2012. He has worked on transport protocols, middleboxes, user- and kernel-space network stacks, software switch and most recently, network stack design for non-volatile main memory. He received IRTF/ISOC Applied Networking Research Prize in 2011 for middlebox measurement work determining extensibility of TCP, and best paper award at ACM SOSR'15 for work on a scalable, modular software switch with other netmap developers.</p>"

---

## {{ page.title }}

### Call For Participation

The first part of this tutorial provides an overview and an analysis of the challenges for fast user-space network I/O frameworks such as netmap, DPDK, PF_RING. These frameworks support packet processing applications (e.g., routers, middleboxes) that need to deal with millions of packets per seconds (e.g., 10 Gbps or higher), which are often needed in the context of Network Function Virtualization (NFV). For performance reasons, the frameworks typically bypass the kernel or its network stack, and provide user-space applications with a device-independent API for direct access to the physical or virtual Network Interface Card (NIC) hardware.

The tutorial then focuses on Netmap [1, 2, 3] because of its flexibility, multi-faceted capabilities and unique advantages to other frameworks, in particular for NFV use cases.  We introduce Netmap along with its API and example programs. The different features are then presented one by one along with their corresponding use cases and performance numbers.

We aim at attendees becoming able to write a simple packet processing application using the netmap API and run it on several netmap ports on bare metal or inside containers and virtual machines.

### Presenters

{% include presenters.html presenters=page.presenters %}

### Tutorial Program

Tutorial slides:

- [An introduction to Netamp](files/tutorial-netmap/01-intro.pdf)

- [Netmap as a backend for VMs](files/tutorial-netmap/02-virtualization.pdf)

- [VALE (mSwitch)](files/tutorial-netmap/03-vale.pdf)

Tutorial codebase:

- [https://github.com/vmaffione/netmap-tutorial](https://github.com/vmaffione/netmap-tutorial)

{% include program.html type="tutorial-netmap-nfv" data=page.data %}

### Motivation

The need for an alternative mechanism and API for network I/O has been recognized by several O.S. bypass projects (DPDK, PF RING), and comes from the performance limitations of the traditional socket API (and the associated O.S. implementation) in terms of maximum packet rate.  Using a traditional socket API a single processor core is not able to send or receive more than 1-2 million packets per second (Mpps) at minimum packet size (60 bytes), despite of much faster modern NICs which support 10-100 Mpps.  These limitations are largely due to per-packet size-independent costs: system call, packet copy across user/kernel boundary, VFS layer overheads, dynamic (de)allocation of packet metadata (e.g. sk_buff on Linux), NIC register access and interrupts.  Moreover, moving networking to userspace facilitates experimentation and improves portability. The bypass solutions overcome these limitations by pre-allocating packet buffers, mapping those buffers in the application address space and allowing applications to send and receive multiple packets using a single operation (e.g. a system call or a NIC register access). They also use simple packet representation structures optimized for raw packet I/O rather than for full-fledged protocol stack.  When combined together, these techniques allow user-space applications to send/receive tens of millions of packets per second, saturating the NIC capacity even with short packets.  The study of Netmap is a good introduction to these topics, common to all frameworks. However, Netmap brings some additional benefits that are not found elsewhere: it does not force applications to resort to busy-polling, it is available on several platforms (FreeBSD, Linux, Windows), it supports more devices and it introduces a common API which can also be used for VM networking and Inter-Process Communication.

The Netmap framework has evolved significantly from its inception as a user-space packet I/O interface to NIC hardware in 2011.  It is now a flexible network I/O tool that supports many backends (in addition to NICs) and virtualized environments, accessible with the same API. The VALE [4,7] programmable switch (part of Netmap) acts as a virtual switch for Virtual Machines (VMs) and physical NICs, supporting hundreds of virtual ports and over 20 Mpps per-core between its ports.  Netmap pipes [8] are point-to-point virtual links that connect processes or VMs at over 40 Mpps, useful for service function chaining.  Netmap as a fast network backend has been integrated into hypervisors like QEMU, Bhyve and VirtualBox. Accelerated network I/O is also possible for lightweight virtualization (containers) by means of native support for Linux veth devices (over 40 Mpps).  Finally, a virtual pass-through device [5, 6] allows any Netmap interface (e.g. a VALE port, NIC or pipe endpoint) to be safely exposed inside a VM, enabling unprecedented packet-rates (20-40 Mpps) between VMs.

These Netmap features constitute the datapath building blocks for Network Function Virtualization (NFV) deployments. We are not aware of other technologies that allow applications running in two VMs or containers to exchange up to 20-40 Mpps at minimum packet size. With such powerful I/O capabilities, we believe Netmap is the preferred candidate to implement NFV applications such as load balancers, Intrusion Detection Systems, firewalls, etc.

### Tutorial type

This tutorial will be given as lectures mixed with hands-on training supervised by the speakers.  During the training sessions the participants will be given live images containing all the required software (Netmap, hypervisors, example applications, etc.).  The images will also be available for download on the [Netmap page](http://info.iet.unipi.it/luigi/netmap/).

### Expected Audience and Prerequisites

The tutorial targets network engineers and system developers that want to learn what Netmap is and how it can help improving throughput, latency and energy efficiency of their packet processing pipelines, both on bare-metal and Virtual Machines.

Attendees must bring their own laptop, with a Linux distribution or FreeBSD installed directly on the laptop or in a Virtual Machine. Attendees are also expected to have familiarity with networking and programming in C or C++.

### References

- [1] [The Netmap page](http://info.iet.unipi.it/~luigi/netmap/)
- [2] The official [Netmap code repository](https://github.com/luigirizzo/netmap)
- [3] L. Rizzo - netmap: a novel framework for fast packet I/O, USENIX ATC'12, June 2012, Boston, MA
- [4] L. Rizzo, G. Lettieri - VALE: a switched ethernet for virtual machines, ACM CoNEXT, December 2012, Nice, France
- [5] S. Garzarella, G. Lettieri, L. Rizzo - Virtual device passthrough for high speed VM networking, IEEE/ACM ANCS, May 2015, Oakland, CA
- [6] V. Maffione, L. Rizzo, G. Lettieri - Flexible Virtual Networking using netmap passthrough, IEEE LANMAN, June 2016, Rome, Italy
- [7] M. Honda, F. Huici, G. Lettieri, L. Rizzo - mSwitch: A Highly-Scalable, Modular Software Switch, ACM SOSR, June 2015, Santa Clara, CA
- [8] L. Rizzo, G. Lettieri, M. Honda - Netmap as a core networking technology, AsiaBSDCon, March 2014, Tokyo
