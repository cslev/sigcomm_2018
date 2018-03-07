---
layout: default
title: "ACM SIGCOMM 2018 Tutorial (Full-Day): P4→NetFPGA"
group: Tutorials

data:
  - type: day
    time: Friday, August 25, 2017
    room: "Faraday Room (Engineering IV)"

  - type: tutorial
    time: 9am - 10:30am
    title: Introduction to P4 and P4 Language Walkthrough, Joint Session with P4 Tutorial
    room: "Shannon Room (Engineering IV)"

  - type: break
    time: 10:30am - 10:45am
    room: Foyer
    title: Coffee Break

  - type: tutorial
    time: 10:45am - 11:15am
    title: NetFPGA Introduction and Architecture Overview

  - type: tutorial
    time: 11:15am - 12:30pm
    title: P4→NetFPGA design flow, start hands-on experience

  - type: break
    time: 12:30pm - 1:30pm
    room: Foyer
    title: Lunch Break

  - type: tutorial
    time: 1:30pm - 3:30pm
    title: Continue hands on experience, live demo

  - type: break
    time: 3:30pm - 4pm
    room: Foyer
    title: Coffee Break

  - type: tutorial
    time: 4pm - 5:30pm
    title: Expert panel, Conclusion

presenters:
  - name:        Gordon Brebner
    affiliation: Xilinx Labs, USA
    bio:         "<b>Gordon Brebner</b> is a Distinguished Engineer at Xilinx, Inc., the world’s leading provider of all-programmable FPGAs and SoCs.  He works in Xilinx Labs, leading an international group researching issues surrounding networked processing systems of the future.  His main personal research interests concern dynamically reconfigurable architectures, domain-specific languages with highly concurrent implementations, and high performance networking.  Most recently, his research has led to the Xilinx SDNet product for SDN and NFV at 100G+ rates.  He holds around 40 patents and has published around 60 papers in the general area of networking with FPGAs.  Prior to joining Xilinx in 2002, he was the Professor of Computer Systems and Head of the Department of Computer Science at the University of Edinburgh.  He is currently co-chair of the P4 Language Design working group in P4.org, and chair of the Protocol Independent Forwarding working group in the Open Networking Foundation."

  - name:        Noa Zilberman
    affiliation: University of Cambridge, UK
    bio:         "<b>Noa Zilberman</b> is a Leverhulme Early Career Fellow at the University of Cambridge
  ter Laboratory in England, where she is the Chief Architect of NetFPGA SUME. Her research interests include high-performance networking and computing architectures, converged interconnect, network measurements and open source hardware research. Zilberman has over 15 years of industrial experience. In her last role before joining the University of Cambridge, she was a Senior Principal Chip Architect at Broadcom's Network Switching group. She is a Senior Member of IEEE, a member of ACM, Usenix and BCS, and has a PhD in Electrical Engineering from Tel Aviv University."

  - name:        Nate Foster
    affiliation: Cornell University, USA
    bio:         "<b>Nate Foster</b> is an Associate Professor of Computer Science at Cornell University and a Visiting Researcher at Barefoot Networks. He serves as chair of the P4 Technical Steering Committee and as co-chair of the P4 Language Design Working Group. His research focuses on the design and implementation of languages for programming software-defined networks. In the past he has also worked on bidirectional languages (also known as 'lenses'), data provenance, type systems, mechanized proof, and formal semantics. He received a PhD in Computer and Information Science from the University of Pennsylvania, an MPhil in History and Philosophy of Science from Cambridge University, and a BA in Computer Science from Williams College. His awards include a Sloan Research Fellowship, an NSF CAREER Award, a Most Influential POPL Paper Award, a Tien '72 Teaching Award, a Cornell Engineering Research Excellence Award, and a Rubinoff Award."

  - name:        Stephen Ibanez
    affiliation: Stanford University, USA
    bio:         "<b>Stephen Ibanez</b> is a PhD Candidate at Stanford working with Professor Nick McKeown. His research interests involve finding new and exciting applications for programmable data-planes, running P4 programs on programmable hardware, network measurement and management, as well as network security. He is currently using P4 to design switches that implement proactive congestion control algorithms for next generation datacenter networks. Stephen is leading the effort to bring together a community of developers and users for the P4→NetFPGA platform."

---

## {{ page.title }}

### Call For Participation

Open source research has been playing a key role over the last decade in networking evolution. Today, [P4](http://p4.org/) is the leading high level programming language for expressing how packets are processed by the data plane of any programmable packet processing device. [NetFPGA](http://netfpga.org/site/#/) is an open platform enabling researchers and instructors to build high-speed, hardware-accelerated networking systems and the de-facto experimental platform for line-rate implementations of network research. This tutorial will provide an introduction to prototyping P4 programs on the NetFPGA platform, and provide a hands-on experience in implementing practical designs.

### Presenters

{% include presenters.html presenters=page.presenters %}

### Tutorial Program

{% include program.html type="tutorial-p4-netfpga" data=page.data %}

### Motivation

Since its initial proposal in 2014 [2], P4 has generated notable momentum within the networking community. It has captured the attention of high-profile network operators in industry as well as distinguished researchers in academia. P4 was developed as a high-level language to describe how packets should be processed by programmable network forwarding devices such as CPUs, NPUs, FPGAs, and programmable ASICs. The language was designed with three main goals in mind: protocol independence, target independence, and reconfigurability in the field. P4 has become the language of choice for developing novel data-plane algorithms, including in-band network telemetry, path-condition-aware adaptive routing, a better NetFlow, and Paxos.

While many of the modern P4 compilers target software switches or test software environments, only a few commercial hardware targets currently support running P4 programs [1], [3]. The NetFPGA platform is an open source platform for rapid prototyping of networking applications, designed for the research community. The latest NetFPGA Platform, NetFPGA-SUME [4] has I/O capabilities for 100Gbps operation, enabling researchers to prototype in hardware high performance applications.

This tutorial will introduce P4→NetFPGA: the development flow of P4-based applications on NetFPGA. The tutorial will provide a hands-on example, giving the participants an opportunity to experience prototyping on hardware a working networking application written in P4. It will also provide a live demonstration of an advanced P4 program running on NetFPGA SUME.

### Expected Audience and Prerequisites

The target audience is not restricted to P4 or hardware researchers: P4→NetFPGA provides the ideal platform for research across a wide range of networking topics from architecture to algorithms and from energy-efficient design to routing and forwarding.

No knowledge of P4 is required to attend the tutorial, although knowledge of the language is needed to program P4→NetFPGA. The tutorial will provide the all background required to successfully complete the hands-on example.

Participants will get remote access to the relevant hardware equipment using their laptops.

### References

- [1] White Paper: Programming NFP with P4 and C. Technical Report, Netronome Systems, 2016.

- [2] Pat Bosshart, Dan Daly, Glen Gibb, Martin Izzard, Nick McKeown, Jennifer Rexford, Cole Schlesinger, Dan Talayco, Amin Vahdat, George Varghese, et al. P4: Programming protocol independent packet processors. ACM SIGCOMM Computer Communication Review, 44(3):87-95, 2014.

- [3] Barefoot Networks. Tofino, 2017. https://www.barefootnetworks.com/technology/#tofino.

- [4] Noa Zilberman, Yury Audzevich, G.Adam Covington, and Andrew W. Moore. NetFPGA SUME: Toward 100 Gbps as Research Commodity. IEEE Micro, 34(5):32-41, September 2014.
