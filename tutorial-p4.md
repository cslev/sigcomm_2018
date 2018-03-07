---
layout: default
title: "ACM SIGCOMM 2018 Tutorial (Full-Day): P4: Programming the Network Data Plane"
group: Tutorials

data:
  - type: day
    time: Friday, August 25, 2017
    room: "Shannon Room (Engineering IV)"

  - title: Introduction to P4 and P4 Language Walkthrough, Joint Session with P4→NetFPGA Tutorial
    time: 9am - 10:30am
    type: tutorial

  - title: Coffee Break
    time: 10:30am - 10:45am
    room: Foyer
    type: break

  - title: Hands-on training using P4 development tools
    time: 10:45am - 12:30pm
    type: tutorial

  - title: Lunch Break
    time: 12:30pm - 1:30pm
    room: Foyer
    type: break

  - title: Lab Exercises
    time: 1:30pm - 3:30pm
    type: tutorial

  - title: Coffee Break
    time: 3:30pm - 4pm
    room: Foyer
    type: break

  - title: Mini Research Workshop, Conclusion
    time: 4pm - 5:30pm
    type: tutorial

presenters:
- name:        Nate Foster
  affiliation: Cornell University
  bio:         "<p>Nate Foster is an Associate Professor of Computer Science at Cornell University and a Visiting Researcher at Barefoot Networks.  He serves as chair of the P4 Technical Steering Committee and as co-chair of the P4 Language Design Working Group. His research focuses on the design and implementation of languages for programming software-defined networks. In the past he has also worked on bidirectional languages (also known as \"lenses\"), data provenance, type systems, mechanized proof, and formal semantics. He received a PhD in Computer and Information Science from the University of Pennsylvania, an MPhil in History and Philosophy of Science from Cambridge University, and a BA in Computer Science from Williams College. His awards include a Sloan Research Fellowship, an NSF CAREER Award, a Most Influential POPL Paper Award, a Tien '72 Teaching Award, a Cornell Engineering Research Excellence Award, and a Rubinoff Award.</p>"

- name:        Changhoon Kim 
  affiliation: Barefoot Networks
  bio:         "<p>Changhoon Kim is Director of System Architecture at Barefoot Networks. Before joining Barefoot, he worked at Windows Azure, Microsoft's cloud-service division, and led engineering and research projects on the architecture, performance, management, and operation of datacenter and enterprise networks. Changhoon is interested in programmable network data plane, network monitoring and diagnostics, network verification, self-programming/configuring networks, and debugging and diagnosis of large-scale distributed systems. Changhoon received Ph.D. from Princeton University. Many of his R&D contributions — including VL2, Seawall, EyeQ, Ananta, and SEATTLE — are adopted in large production networks.</p>"

---

## {{ page.title }}

### Call For Participation

This hands-on tutorial will provide a comprehensive introduction to the P4 language. Attendees will learn how to express novel data-plane applications in the P4 language, and how to compile, execute, and evaluate P4 programs using Mininet, a network emulation framework.

### Presenters

{% include presenters.html presenters=page.presenters %}

### Tutorial Program

{% include program.html type="tutorial-p4" data=page.data %}

### Motivation

[P4](http://www.p4.org) is a new programming language for describing how network packets should be processed on a variety of targets ranging from general-purpose CPUs to network processors, FPGAs, and custom ASICs. P4 was designed with three goals in mind: (i) protocol independence: devices should not “bake in” specific protocols; (ii) field reconfigurability: programmers should be able to modify the behavior of devices after they have been deployed; and (iii) portability: programs should not be tied to specific hardware targets.

The P4 community has created—and continues to maintain and develop—a language specification, a set of open-source tools (compilers, debuggers, code analyzers, libraries, software P4 switches, etc.), and sample P4 programs with the goal of making it easy for P4 users to quickly and correctly author new data-plane behaviors. New ideas are being developed in P4, prototyped as new forwarding behaviors, and published at some of the top conferences in networking. Existing data-plane features typically realized in a fixed-function logic are also being authored in P4.

The most recent update to the P4 language specification incorporates features designed to embrace functional and architectural heterogeneity of various targets while keeping the language core simple and clean. The new specification also offers features to improve portability and composability of a P4 program, allowing P4 consumers and target providers to reuse their code. Second, the P4 development environment has also been evolving. The P4 community now has a more powerful compiler, along with an architecture-independent software P4 switch. There are now several P4-programmable targets, including programmable NICs, high-end switching chips, and even software switches such as OVS  and eBPF. Finally, P4 has become an increasingly popular choice for developing novel data-plane designs. Examples include P4 programs that realize in-band network telemetry, L4 connection load-balancing, path-condition-aware adaptive routing, a better NetFlow, and even Paxos. We believe there are many opportunities for academic researchers to help evolve the design of the language, discover new implementation techniques, and develop use cases.

### Topics Covered

- Background on P4 language (joint with P4→FPGA workshop)

- Demonstration of implementing features in P4

- Hands-on training with P4 development environment

    - Compiler

    - Debugger

    - Behavioral model and hardware targets

    - Lab Exercises

- Mini-Workshop

    - Research problems

    - Teaching resources

    - Getting involved

    - Panel discussion

### Audience Expectations and Prerequisites

The tutorial will be useful to researchers, students, and practitioners alike (engineers, network admins, network architects, and developers). Attendees will be expected to bring their own laptops. We will provide a VM image containing all necessary packages and tools. The P4 language specifications is publicly available on the P4 website under an Apache license. Key development tools (front-end compiler and software switch capable of running P4 programs) are available as [open-source tools](https://github.com/p4lang). We have given version of this tutorial at various venues, including previous SIGCOMMs, the P4 workshop, P4 Bootcamp, ONS Webniars, etc.
