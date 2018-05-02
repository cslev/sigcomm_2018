---
layout: default
title: "ACM SIGCOMM 2018 Full-Day Tutorial on The Role of NFV and Kernel Bypass in High Performance Networking (HPNFV)"
group: Tutorials

dates:
    - info: Tutorial
      date: August 24, 2018
      
data:
  - type: day
    time: Monday, August 20, 2018
    room: TBA

organizers:
- name:        Timothy Wood
  affiliation: GWU, USA
  bio:         "<p>Timothy Wood is an associate professor in the Department of Computer Science at George Washington University. Before joining GW, he received a doctoral degree in computer science from the University of Massachusetts Amherst and a bachelor’s degree in electrical and computer engineering from Rutgers University. His research studies how new virtualization technologies can provide application agnostic tools that improve performance, efficiency, and reliability in cloud computing data centers and software-based networks. His PhD thesis received the UMass CS Outstanding Dissertation Award, his students have voted him CS Professor of the Year, and he has won three best paper awards, a Google Faculty Research Award, and an NSF Career award.</p>"

- name:        K. K. Ramakrishnan
  affiliation: UCR, USA
  bio:         "<p>K. K. Ramakrishnan is Professor of Computer Science and Engineering at the University of California, Riverside. Previously, he was a Distinguished Member of Technical Staff at AT&T Labs-Research. He joined AT&T Bell Labs in 1994 and was with AT&T Labs-Research since its inception in 1996. Prior to 1994, he was a Technical Director and Consulting Engineer in Networking at Digital Equipment Corporation. Between 2000 and 2002, he was at TeraOptic Networks, Inc., as Founder and Vice President.<br/>
  Dr. Ramakrishnan is an ACM Fellow, an IEEE Fellow and an AT&T Fellow, recognized for his fundamental contributions on communication networks, including his work on congestion control, traffic management and VPN services. His work on the \"DECbit\" congestion avoidance protocol received the ACM Sigcomm Test of Time Paper Award in 2006. He has published nearly 250 papers and has 167 patents issued in his name. K.K. has been on the editorial board of several journals and has served as the TPC Chair and General Chair for several networking conferences and has been a member of the National Research Council Panel on Information Technology for NIST.  K. K. received his MTech from the Indian Institute of Science (1978), MS (1981) and Ph.D. (1983) in Computer Science from the University of Maryland, College Park, USA.</p>"

---

# {{ page.title }}

## Call For Participation

This tutorial will offer an introduction to Network Function Virtualization (NFV) technologies and in-depth hands-on understanding of an NFV platform to demonstrate their use in building high performance middleboxes and endpoint services. We will cover kernel bypass networking using DPDK, managing chains of network functions using OpenNetVM, and deploying high performance endpoint services using the mTCP user-space stack.

## <i class="fa fa-calendar"></i> Important Dates

{% include dates2.html dates=page.dates %}

## Outline
- NFV Introduction 
- Motivation for NFV: Service Provider Perspective; Emergence of Edge-clouds 
- Hands-on: DPDK Basics 
- OpenNetVM Architecture 
- Hands-on: OpenNetVM service chaining 
- Overview of other NFV Platforms - netmap, BESS
- User-space TCP processing
- Hands-on: Combining OpenNetVM and mTCP
- NF Management Challenges 

## Audience Expectations and Prerequisites
Attendees will require no prior experience with NFV. In order to perform the hands-on portions of the tutorial, attendees will need a laptop with internet access and basic linux and C programming skills. We will provide servers using the NSF CloudLab platform for attendees to run high performance NF chains.


## Background
Network Function Virtualization (NFV) is an important area for networking at this time, as it brings much needed flexibility to accommodate innovation in an increasingly inflexible, large-scale, global network infrastructure. Recently, several high performance I/O libraries such as netmap, DPDK, and PF_RING have emerged to allow developers and researchers to build efficient NF prototypes.  These libraries typically enable packet processing rates of 10 Gbps or higher by avoiding the kernel’s networking stack. While this has been a boon for accelerating individual applications, these libraries do not assist with the composition of NFs nor their management. Thus, while the low-level tools to build network functions are becoming available, there is also a need for platforms that provide the higher level abstractions needed to compose them into service chains, facilitate protocol processing, and manage their resources. This tutorial seeks to elucidate the challenges and opportunities in software-based networks by providing hands-on experience with key NFV technologies.

OpenNetVM is an NFV platform that supports both high performance networked middleboxes and end-point applications. The OpenNetVM framework provides an abstraction layer to simplify deployment of network functions in containers. It can be used not only for simple layer 2/3 middleboxes, but also integrated with a user-space TCP stack to provide end-host services. OpenNetVM is publicly available as open source on Github [https://github.com/sdnfv/openNetVM](https://github.com/sdnfv/openNetVM).
 
This tutorial will provide valuable hands-on experience to researchers interested in learning about high performance network middleboxes. The tutorial will introduce attendees to an overview of NFV technology, motivation for NFV from the perspective of service providers, the DPDK I/O library, the mTCP user-space stack, and the OpenNetVM NF management platform. Attendees will get hands-on experience running a mixture of high performance middleboxes and end-host applications on an integrated platform managed by OpenNetVM.

## Organizers

{% include organizers.html presenters=page.organizers %}

<!--
## Tutorial Program

{% include program.html type="tutorial-p4" data=page.data %}
-->


