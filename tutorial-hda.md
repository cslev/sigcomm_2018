---
layout: default
title: "ACM SIGCOMM 2018 Morning Tutorial on Host Dataplane Acceleration (HDA)"
group: Tutorials

dates:
    - info: Tutorial
      date: August 20, 2018
      
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

## Tutorial Program

{% include program-online.html type="hda" %}

## Call For Participation
This tutorial will provide participants with a hands-on introduction to new technologies to accelerate network function processing on server networking hardware (​[www.open-nfp.org](https://www.open-nfp.org)​). Attendees will learn how to express new data-plane applications in eBPF and P4 and how to compile, execute, and evaluate these applications on production hardware.



## <i class="fa fa-calendar"></i> Important Dates
{% include dates2.html dates=page.dates %}


## Outline
Attendees will prototype network applications in the eBPF and P4 and compile them to
production networking hardware in a sequence of hands-on labs.

The tutorial will cover the following topics:

eBPF:
- Introduction to eBPF: The VM, Instruction set, Maps, Helper Functions, Verifiers, Development process
- Introduction to XDP eBPF: XDP hooks, actions and use cases 
- eBPF XDP offload: Open source implementations to offload XDP to a SmartNIC or another device.
- XDP Offload Lab (Load balancer): Hands on lab.

P4-16:
- P4-16 with Netronome SmartNIC.
- C-based externs with P4-16 - Development process for functions not supported in P4.
- P4-16 Lab (Telemetry) - Hands-on lab.

## Audience Expectations and Prerequisites
Attendees will be expected to bring their own laptops with remote desktop protocol installed. We
will provide access to a VM containing all the necessary packages and tools.


## Background
The Extended Berkeley Packet Filter (eBPF) has rapidly been adopted into a number of
systems since its introduction into the Linux kernel in 2014. Uses of eBPF have quickly grown to include network monitoring, network traffic manipulation, and system monitoring, etc. - all of which can be accelerated via Agilio CX SmartNIC programming and offload approaches. Netronome and the Open-NFP community have created several sources of information and samples on eBPF.

P4 is a high-level programming language for software-defined networks. It is intended to describe the behavior of the data plane of any system or appliance that forwards, modifies or inspects network traffic. Researchers are innovating using P4 in server-based networking systems with novel approaches to offloading servers using SmartNICs and realizing new functionality.

This tutorial will be based on recent technical papers on eBPF offload and P4 applications in server-based networking.


### References
<p>
[1] <a href="https://open-nfp.org/documents/1/eBPF_HW_OFFLOAD_HNiMne8.pdf">eBPF ​ Hardware ​ Offload ​ to SmartNICs: cls bpf and XDP</a>​, N. Viljoen and J. Kicinski, Netdev, 2016.<br/>
[2] <a href="https://open-nfp.org/dataplanes-ebpf/">https://open-nfp.org/dataplanes-ebpf/</a><br/>
[3] <a href="https://open-nfp.org/dataplanes-p4/">https://open-nfp.org/dataplanes-p4/</a><br/>
[4] <a href="https://conferences.sigcomm.org/sigcomm/2017/tutorial-P4-NetFPGA.html">https://conferences.sigcomm.org/sigcomm/2017/tutorial-P4-NetFPGA.html</a><br/>
</p>



