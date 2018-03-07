---
layout: default
title: ACM SIGCOMM 2018 Workshop on In-Network Computing (NetCompute 2018)
group: Workshops


dates:
    - info: Abstract submission deadline
      date: March 18, 2018
    - info: Paper submission deadline
      date: March 25, 2018
    - info: Acceptance notification
      date: April 30, 2018
    - info: Camera-ready deadline
      date: May 31, 2018
    - info: Program available online
      date: Mid-June, 2018   
    - info: List of organization details
      date: Mid-June, 2018   
    - info: Workshop
      date: August 20 or 24, 2018

committees:
    - role: Workshop Chairs
      people:
       - name:        Xin Jin
         affiliation: JHU, USA
       - name:        Changhoon Kim
         affiliation: Barefoot, USA
    
    - role: Program Committee Members
      people:
       - name:        Aditya Akella 
         affiliation: Wisconsin, USA
       - name:        Theophilus Benson
         affiliation: Brown, USA
       - name:        Jun Bi
         affiliation: Tsinghua, China
       - name:        Gordon Brebner
         affiliation: Xilinx, USA
       - name:        Kai Chen
         affiliation: HKUST, China
       - name:        Marco Canini
         affiliation: KAUST, KSA
       - name:        Dan Daly
         affiliation: Intel, USA
       - name:        Nate Foster
         affiliation: Cornell, USA
       - name:        Chi-Yao Hong
         affiliation: Google, USA
       - name:        Arvind Krishnamurthy
         affiliation: UW, USA
       - name:        Xiaozhou Li
         affiliation: Barefoot, USA
       - name:        Hongqiang Liu
         affiliation: Alibaba, China
       - name:        Ben Pfaff
         affiliation: VMware, USA
       - name:        Dan Ports
         affiliation: UW, USA
       - name:        Jennifer Rexford
         affiliation: Princeton, USA
       - name:        Kun Tan
         affiliation: Huawei, China
       - name:        Laurent Vanbever
         affiliation: ETH, Switzerland
       - name:        Hongyi Zeng
         affiliation: Facebook, USA      
---

# {{ page.title }}

### Call for Papers
In-network computing is an emerging topic that draws a lot of attention from both academia and industry. In-network computing exploits the capabilities of new programmable network devices such as programmable switch ASICs, network processors, FPGAs, and programmable NICs to offload computing from CPUs to the network. While in-network computing can be dated back to early efforts such as active networking two decades ago, many believe that the time has finally come due to a combination of hardware and software innovations. On the hardware side, many hardware vendors have released products that provide programmability without sacrificing performance, such as Barefoot Tofino, Intel FlexPipe, Cavium XPliant, and Netronome Agilio. On the software side, besides new network functionalities such as in-network telemetry and layer-4 load balancing, many new application-level functionalities beyond traditional packet processing have been proposed, such as key-value caching, consensus, and even machine learning.

We believe that our community must expedite the research on in-network computing to make a profound influence on the theory and practice of future computer systems. There are significant open challenges: what are the killer apps of in-network computing; what are other application-level functionalities that can be offloaded to the network; fundamentally, what should be offloaded to the network and what should be kept on hosts; how to design better hardware primitives and software development platforms (e.g., domain-specific programming languages and compilers) to support the development of new applications; how to manage, monitor and debug heterogeneous systems that span servers and switches; how to incrementally deploy new applications; and many others.

The ACM SIGCOMM Workshop on In-Network Computing (NetCompute 2018) is organized with the goal of bringing researchers and engineers working on in-network computing together to present and discuss their latest ideas, research results and system experiences, thereby promoting the development and evolution of this area. All submissions on in-network computing related to architecture, design, implementation, simulation, modeling, analysis, and measurement are welcomed. We highly encourage novel and innovative early stage work that will encourage discussion and future research on in-network computing.

### Topics of Interest
- Applications of programmable network devices, e.g., machine learning, deep learning and key-value storage
- Architectures for in-network computing
- Control plane for in-network computing
- Switch and NIC hardware design for in-network computing
- Virtualization for in-network computing systems
- Programming languages and compilers for in-network computing
- Measurements and performance studies of programmable network devices
- Diagnosing and troubleshooting in-network computing systems
- In-network computing in clouds and edge clouds
- Security and privacy of in-network computing
- Deployment strategies and backward compatibility with traditional network functionalities
- Experiences and best-practices of in-network computing systems in production

### Submission Instructions
Submissions must describe original, previously unpublished research, not currently under review by another conference or journal. Papers must be submitted electronically via the submission site. The length of papers must be no more than **6 pages**, including tables, figures and references, using the same template as SIGCOMM submission (SIGCOMM submission instructions). The cover page must contain the name and affiliation of author(s) for single--blind peer reviewing by the program committee. Each submission will receive at least three independent blind reviews from the TPC. At least one of the authors of every accepted paper must register and present their work at the workshop. Paper registration and submission can be done via HotCRP at [https://sigcomm18netcompute.hotcrp.com](https://sigcomm18netcompute.hotcrp.com)




### Important Dates

{% include dates2.html dates=page.dates %}

### Committees

{% include committees.html committees=page.committees %}

[Contact the NetCompute chairs](mailto:xinjin@cs.jhu.edu,chang@barefootnetworks.com?subject=[NetCompute 2018]){: data-role="button" class="button" }