---
layout: default
title: "ACM SIGCOMM 2018 Full-Day Tutorial on Programming the Network Data Plane (P4)"
group: Tutorials

dates:
    - info: Tutorial
      date: August 20, 2018
      
data:
  - type: day
    time: Monday, August 20, 2018
    room: TBA

organizers:
- name:        Nate Foster
  affiliation: Cornell, USA
  bio:         "<p>Nate Foster is an Associate Professor of Computer Science at Cornell University and a Principal Research Engineer at Barefoot Networks. He serves as chair of the P4 Technical Steering Committee and as co-chair of the P4 Language Design Working Group. His research focuses on the design and implementation of languages for programming software-defined networks. He received a PhD in Computer and Information Science from the University of Pennsylvania, an MPhil in History and Philosophy of Science from Cambridge University, and a BA in Computer Science from Williams College. His awards include a Sloan Research Fellowship and an NSF CAREER Award.</p>"

- name:        Robert Soulé 
  affiliation: USI, Switzerland
  bio:         "<p>Robert Soulé is an Assistant Professor at the Università della Svizzera italiana (USI) and a Research Scientist at Barefoot Networks. His research interests are in distributed systems, networking, and applied programming languages. Prior to joining USI, he was a postdoctoral associate at Cornell University. He received his PhD from New York University, and his BA from Brown University. For two years, he was a research co-op in the Data Intensive Systems and Analytics Group at IBM T. J. Watson Research Center.</p>"
  
- name:       Noa Zilberman
  affiliation: Cambridge, UK
  bio:        "<p>Noa Zilberman is a Leverhulme Early Career Fellow, also supported by the Isaac Newton Trust, in the Systems Research Group, University of Cambridge' Computer Laboratory. In her last roles before joining the System Research Group, she was a senior principal chip architect in Broadcom's Network Switching group, and a researcher in the DIMES project (Tel-Aviv University). Amongst others, she led the hardware development of the first 100Gbps traffic manager, and the architecture of Broadcom's StrataDNX BCM88670. Her research interests include open-source network & computing research, network performance, routing and switching architectures, converged interconnect, memories architecture and performance, Internet measurements and topology. Noa received her BSC, MSc (both Magna Cum Laude) and PhD in Electrical Engineering from Tel-Aviv University.</p>"

---

# {{ page.title }}

## Tutorial Program

{% include program-online.html type="p4" %}

## Call For Participation

This tutorial will provide participants with a hands-on introduction to the P4 language [(www.p4.org)](www.p4.org). Attendees will learn how to express conventional and novel data-plane applications in the P4 language, and how to compile, execute, and evaluate P4 programs using Mininet, a network emulation framework

## <i class="fa fa-calendar"></i> Important Dates

{% include dates2.html dates=page.dates %}

## Outline
Through a series of simple exercises, we will show how to prototype network applications in the P4 language and compile them to programmable devices. We also aim to encourage researchers and developers to contribute to the P4 language and develop new applications. 

Specifically, we plan to cover the following topics:
- Background on P4 (2 hours)
- Demonstration of implementing features in P4 (1 hour)
- Hands-on training of P4 development environment (2.5 hours)
- Compiler
- Debugger
- Behavioral model and hardware targets
- Lab Exercises
- Mini-Workshop (1.5 hours)
- Research problems
- Teaching resources
- Getting involved
- Panel discussion

## Audience Expectations and Prerequisites
Attendees will be expected to bring their own laptops. We will provide a VM image containing all the necessary packages and tools. The P4 specification is publicly available at the P4 website under an Apache license. Key development tools (front-end compiler and software switch capable of running P4 programs) are available as open-source tools [(http://github.com/p4lang)](http://github.com/p4lang).


## Background
P4 [(www.p4.org)](www.p4.org) is a programming language for describing how network packets should be processed on a variety of targets ranging from general-purpose CPUs to network processors, FPGAs, and custom ASICs [1]. P4 was designed with three goals in mind: (i) protocol independence: devices should not “bake in” specific protocols; (ii) field re-configurability: programmers should be able to modify the behavior of devices after they have been deployed; and (iii) portability: programs should not be tied to specific hardware targets. The P4 community has created – and continues to maintain and develop – specifications (for data planes, control plane APIs, standard architectures), a set of open-source tools (compilers, debuggers, code analyzers, libraries, software P4 switches, etc.), and sample P4 programs with the goal of making it easy for P4 users to quickly and correctly author new data-plane behaviors. New ideas are being developed in P4, prototyped as new forwarding behaviors, and published at some of the top conferences in networking including SIGCOMM. Existing data-plane features typically realized in a fixed-function logic are also being authored in P4.

Recently, P4 has evolved to embrace the functional and architectural heterogeneity of various targets while keeping the language core simple and clean. 
                                                                                                                           
- One manifestation of this change is the development of a Portable Switch Architecture (PSA). The PSA describes common capabilities of network switch devices which process and forward packets across multiple interface. This specification improves the portability and composability of a P4 program, allowing P4 consumers and target providers to reuse their code. 
 
- Second, in the past year, there have been significant new developments on the control-plane API for P4 pipelines. This tutorial will introduce P4 Runtime, the silicon-independent and protocol-independent API that can be auto-generated from an unambiguous definition of a packet processing pipeline in P4. 

- Third, P4 continues to be a transformative technology in networking, and an increasingly popular choice for developing novel data-plane designs. Examples include P4 programs that realize in-band network telemetry [4], L4 connection load-balancing, path-condition-aware adaptive routing [5], a better NetFlow [6], and even replicated storage systems [7]. We believe there are many opportunities for academic researchers to help evolve the design of the language, discover new implementation techniques, and develop use cases.


## Organizers

{% include organizers.html presenters=page.organizers %}

<!--
## Tutorial Program

{% include program.html type="tutorial-p4" data=page.data %}
-->



### References
<p>
[1] Pat Bosshart, et al. "P4: Programming protocol-independent packet processors," ACM SIGCOMM CCR, 2014, 44(3): 87-95.<br/>
[2] <a href="http://p4.org/p4/p4-and-open-vswitch/">http://p4.org/p4/p4-and-open-vswitch/</a><br/>
[3] <a href="https://github.com/blp/ovs-reviews/tree/p4">https://github.com/blp/ovs-reviews/tree/p4</a><br/>
[4] Changhoon Kim, et al. “In-band Network Telemetry via Programmable Dataplanes,” demo at SIGCOMM 2015 and SOSR 2015.<br/>
[5] Naga Katta, et al. "HULA: Scalable Load Balancing Using Programmable Data-Planes," Proceedings of the ACM SOSR, 2016.<br/>
[6] Yuliang Li, et al. “FlowRadar: A Better NetFlow for Data Centers,” Proceedings of the USENIX NSDI, 2016.<br/>
[7] Xin Jin, et al. “NetChain: Scale-Free Sub-RTT Coordination,” to appear in NSDI 2018.
</p>

### Virtual Machine
We have created a virtual machine that has all of the software needed to complete the developer day exercises already installed. You can either download a virtual machine image or build it from source. Note that both of these procedures can take around 45 minutes depending on the speed of your network connection.


#### To download the virtual machine image
1. Install VirtualBox

   [https://virtualbox.org](https://virtualbox.org)
2. Download virtual machine image

   [P4 Tutorial 2018-06-01.ova](https://drive.google.com/uc?id=1f22-DYlUV33DsR88_MeMb4s7-1NX_ams&export=download)
3. Import virtual machine into VirtualBox 

   Open VirtualBox, select "File > Import Appliance", and navigate to the downloaded file.
4. Boot virtual machine

   Select "P4 Tutorial 2018-06-01", and click "Start".
 

#### To build the virtual machine from source
1. Install VirtualBox

   [https://virtualbox.org](https://virtualbox.org)
2. Install Vagrant

   [https://vagrantup.com](https://vagrantup.com)
3. Clone the tutorial repository

   `$ git clone https://github.com/p4lang/tutorials`
    
    - Navigate to the vm directory
    
      `$ cd tutorials/vm/`
    - Build the virtual machine
    
      `$ vagrant up`
 
#### Final steps
After the machine boots, you should have a graphical desktop with  all required software pre-installed, logged in as username "p4"  (with password "p4").