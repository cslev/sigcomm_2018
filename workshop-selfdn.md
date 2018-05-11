---
layout: default
title: "ACM SIGCOMM 2018 Afternoon Workshop on Self-Driving Networks (SelfDN 2018)"
group: Workshops

dates:
    - info: Workshop
      date: August 24, 2018
    - info: List of organization details
      date: Mid-June, 2018   
    - info: Program available online
      date: Mid-June, 2018   
    - info: Camera-ready deadline
      date: May 31, 2018
    - info: Acceptance notification
      date: April 30, 2018
    - info: Paper submission deadline
      date: <del>April 01, 2018</del>
    - info: Abstract submission deadline
      date: <del>March 25, 2018</del>
   

committees:
    - role: Workshop Chairs
      people:       
       - name:        Nick Feamster
         affiliation: Princeton, USA
       
       - name:        Jennifer Rexford
         affiliation: Princeton, USA
         
       - name:        Walter Willinger
         affiliation: NIKSUN, USA
    
    - role: Program Committee Members
      people:
       - name:        Manos Antonakakis
         affiliation: Georgia Tech, USA


       - name:        Marco Canini
         affiliation: KAUST, KSA
        
       - name:        Chen-Nee Chuah
         affiliation: Davis, USA

       - name:        Arpit Gupta
         affiliation: Princeton, USA
         
       - name:        Changhoon Kim
         affiliation: Barefoot, USA
      
       - name:        Priya Mahadevan
         affiliation: Google, USA
         
       - name:        Ratul Mahajan
         affiliation: Intentionet, USA

       - name:        Nikolai Matni
         affiliation: Berkeley, USA
         
       - name:        Srinivas Narayana
         affiliation: MIT, USA
        
       - name:        Matthew Roughan
         affiliation: Adelaide, Australia
                           
       - name:        Michael Schapira
         affiliation: HUJI, Israel
 
       - name:        Vyas Sekar
         affiliation: CMU, USA

       - name:        Anirudh Sivaraman
         affiliation: NYU, USA

       - name:        Alex C. Snoeren
         affiliation: UCSD, USA

       - name:        Renata Teixeira
         affiliation: Inria, France

       - name:        Ming Zhang
         affiliation: Alibaba, China

       - name:        Ying Zhang
         affiliation: Facebook, USA
         
         
---
# {{ page.title }}

### Call for Papers
For at least a decade, networking researchers, equipment vendors, and Internet service providers alike have argued for “autonomous” or “self-managing” networks, where network management and control decisions are made in real time and in an automated fashion. Yet, building such “self-driving” networks that are practically deployable has largely remained unrealized. Recent technological advances and scientific innovations, however, provide exciting new opportunities for finally realizing self-driving networks. These advances and innovations include (1) fully programmable, protocol-independent data planes and languages for programming them; and (2) the emergence of scalable platforms for processing distributed streaming data while leveraging the latest (big) data analysis and machine learning (ML) tools and software. 

On the one hand, the feasibility of self-driving networks derives from the control-theoretic principle that relies on closed-loop feedback to mitigate the effects of dynamic uncertainty on a system. At the same time, the coupling of the programmable control of software-defined networking (SDN) with the inference capabilities of ML promises unprecedented opportunities for querying high-volume and high-velocity, distributed streaming data at scale; this new technical capability can provide the necessary information to the many different network management and control tasks that self-driving networks should perform automatically and autonomously. 

The design and implementation of self-driving networks is one of the “grand challenges” of networking research today. Realizing this vision will require incorporating the collective expertise and input from the networking research community. 

This workshop will provide a forum for networking researchers to present and share their latest research on new technologies that can help realize practical, deployable self-driving networks. This workshop seeks contributions from experts in areas such as network programming, formal methods, control theory, distributed systems, machine learning, data science, data structures and algorithms, and optimization who share in the excitement of realizing the vision of self-driving networks. Of particular interest are original research papers that are informed by control-theoretic findings (e.g., hard limits, unavoidable tradeoffs) or describe use cases of specific network management or control tasks (e.g., as applied to network security or performance) that (1) demonstrate the successful implementation of the different feedback control components so that, together, they can perform the tasks at hand in an automated way and (2) identify bottlenecks in existing technologies or methods that prevent the practical deployment of full-fledged self-driving networks. 

Submissions related to all aspects of designing and building self-driving networks are welcome, but innovative work that incorporates all aspects of the control loop is preferred over piecemeal approaches that focus on individual aspects in isolation.



### Topics of Interest
- Predictive machine learning approaches to closed-loop traffic-engineering systems (e.g, traffic prioritization, routing, machine-learned TCP or hypervisor rate controllers)
- Applications of machine learning to network attack prediction and remediation
- New machine learning problems and questions that arise from network operations tasks that are related to performance or security
- Network measurement techniques that adapt collection or measurement based on changing network conditions
- Query languages that support queries for data-in-motion (i.e., streaming data) and data-at-rest (i.e., offline analysis)
- Efficient data structures and algorithms for querying (distributed) streaming data
- New algorithms for performing approximate queries (with accuracy guarantees) and dynamic queries
- New architectures for fine-grained and programmable network monitoring
- New optimizations for building smart run-time systems or scalable query engines
- Design and implementation of closed-loop feedback controls for the combined detection and mitigation of specific cyber attacks, or the detection and resolution of performance impairments
- Examples of design choices informed by control-theoretic findings (e.g., hard limits, unavoidable tradeoffs)
- Closed-loop systems that use measurement and inference to drive SDN-based control
- Provable correctness properties of concurrently running control actions and protocols
- Closed-loop network management systems that can incorporate human feedback (e.g., from users or operators) to achieve better efficiency, accuracy, or effectiveness.



### Submission Instructions
Submissions must be original, unpublished work, and not under consideration at another conference or journal. Submitted papers must be at most six (6) pages long, including all figures, tables, and appendices (but not counting references) in two-column 10pt ACM format. Papers must include authors names and affiliations for single-blind peer reviewing by the PC. Authors of accepted papers are expected to present their papers at the workshop.
Please submit your paper at [https://sigcomm-sdn18.hotcrp.com/](https://sigcomm-sdn18.hotcrp.com/).


### Authors Take Note
{% include workshop_authorstakenote.html %}

### Registration
{% include workshop_registration.html %}

### Camera-ready instructions
{% include camera-ready_ws_inst.html %}


### <i class="fa fa-calendar"></i> Important Dates

{% include dates2.html dates=page.dates %}

### Committees

{% include committees.html committees=page.committees %}


[Contact the SelfDN chairs](mailto:feamster@cs.princeton.edu,jrex@cs.princeton.edu,wwillinger@niksun.com?subject=[SelfDN 2018]){: data-role="button" class="button" }