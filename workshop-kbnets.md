---
layout: default
title: "ACM SIGCOMM 2018 Workshop on Kernel Bypassing Networks (KBNets 2018)"
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
       - name:        Dongsu Han
         affiliation: KAIST, South Korea
       
       - name:        Hongqiang Liu
         affiliation: Alibaba, China
    
    - role: Program Committee Members
      people:
       - name:        Nandita Dukkipati
         affiliation: Google, USA

       - name:        Felipe Huici
         affiliation: NEC, Germany
        
       - name:        Xin Jin
         affiliation: JHU, USA

       - name:        Richard Mortier
         affiliation: Cambridge, UK
         
       - name:        Aurojit Panda
         affiliation: NYU, USA
      
       - name:        D. K. Panda
         affiliation: OSU, USA
         
       - name:        Kyoungsoo Park
         affiliation: KAIST, South Korea

       - name:        Simon Peter
         affiliation: UT, USA
         
       - name:        Jitu Padhye
         affiliation: Microsoft, USA
        
       - name:        Costin Raiciu
         affiliation: UPB, Romania
                           
       - name:        Timothy Wood
         affiliation: GWU, USA
 
       - name:        Eitan Zahavi
         affiliation: Mellanox, Israel

       - name:        Yibo Zhu
         affiliation: Microsoft, USA
---
# {{ page.title }}

### Call for Papers
Kernel Bypassing Networks (including, but not limited to RDMA, DPDK and SmartNIC) have
recently drawn much attention from both the research community and the industry. Emerging
applications such as AI training, distributed storage systems, virtual networking, and software
middle­boxes/NFV demand low latency, high bandwidth and low CPU overhead from the
network, and have been shown to benefit significantly from technologies that bypass the
conventional OS network stack. At the same time, recent switch and NIC developments (e.g.,
RoCE) have paved the way to the large­scale deployment of KBNets.

KBNets are thus starting to be deployed in practice. But plenty of research remains to be done.
For example, the research community is still debating whether the kernel should be bypassed in
different use­cases, what sort of control plane and network management systems are needed for
such networks, and how to design congestion control protocols for KBNets and deal with
inherent problems such as deadlocks, and how to design programming languages for KBNets.
Perhaps more importantly, there is much more work needed to understand how KBNets will
impact the design of distributed systems and applications that run over these networks.

We believe that networking community must expedite the research on the design of kernel
bypassing networks, understand both their strengths and their weaknesses, and rethink how we
design distributed systems to take advantage of these networks.

The ACM SIGCOMM Workshop on Kernel Bypassing Networks (KBNets 2018) is organized with
the goal of bringing together researchers from the networking, operating systems, and distributed
systems communities to promote the development and evolution of kernel bypassing networks.
All submissions related to KBNets and KBNets­based systems, including network/system
architecture, design, implementation, programing language, simulation, modeling, analysis, and
measurement will be welcome. We highly encourage novel and innovative early stage work that
will encourage discussion and future research on KBNets.



### Topics of Interest
Topics include but are not limited to:

- Network transport for kernel bypassing networks
- Control plane for kernel bypassing networks
- Security issues regarding kernel bypassing networks
- Distributed systems that are based on kernel bypassing networks, e.g., AI training, distributed storage, database and in­memory caches
- Data center network architectures for kernel bypassing networks
- Virtualization for kernel bypassing networks
- Programming languages for kernel bypassing networks
- NIC/switch hardware design for kernel bypassing networks
- Middle­boxes/NFV optimization with kernel bypassing networks
- Diagnosing and troubleshooting kernel bypassing networks
- Experiences and best­practices in deploying kernel bypassing networks
- Measurements of kernel bypassing and kernel optimizing networks
- Performance studies of kernel bypassing networks and applications
- Transition and backward compatibility with traditional network stacks
- Other approaches such as high performance OS data­plane architectures

### Submission Instructions
Submissions must describe original, previously unpublished, complete research, not currently
under review by another conference or journal. Papers must be submitted electronically via the
submission site. The length of papers must be no more than **6 pages**, including tables and
figures but excluding references. The cover page must contain the name and affiliation of author(s) for **single--blind** peer
reviewing by the program committee. Each submission will receive **at least three independent
blind reviews** from the TPC. At least one of the authors of every accepted paper must register
and present their work at the workshop.

### Authors Take Note
{% include workshop_authorstakenote.html %}

### Registration
{% include workshop_registration.html %}


### Important Dates

{% include dates2.html dates=page.dates %}

### Committees

{% include committees.html committees=page.committees %}


[Contact the KBNets chairs](mailto:dongsu.han@gmail.com,lampson0505@gmail.com?subject=[KBNets 2018]){: data-role="button" class="button" }