---
layout: default
title: "ACM SIGCOMM 2018 Workshop on Security in Softwarized Networks: Prospects and Challenges (SecSoN 2018)"
group: Workshops

dates:
    - info: Workshop
      date: August 24, 2018
    - info: Camera-ready deadline
      date: June 10, 2018
    - info: Author notification (extended)
      date: <del>May 02, 2018</del>
    - info: Submission deadline
      date: <del>March 28, 2018</del>
    - info: Abstract submission deadline
      date: <del>March 28, 2018</del> 

committees:
    - role: Workshop Chairs
      people:
       - name:        Theophilus Benson
         affiliation: Brown, USA
       - name:        Pascal Bisson
         affiliation: Thales, France
       - name:        Rastin Pries
         affiliation: Nokia, Germany
       - name:        Thomas Zinner
         affiliation: JMU, Germany

    - role: Program Committee Members
      people:
       - name:        Joo Cho
         affiliation: ADVA, Germany         
       - name:        Luciana Costa
         affiliation: TIM, Italy  
       - name:        Oliver Hohlfeld
         affiliation: RWTH, Germany           
       - name:        Thorsten Holz
         affiliation: RUB, Germany         
       - name:        Wolfgang Hommel
         affiliation: UniBw, Germany         
       - name:        Hongxin Hu
         affiliation: Clemson, USA          
       - name:        Eric Keller
         affiliation: CU, USA         
       - name:        Felix Klaedtke
         affiliation: NEC, Germany 
       - name:        Piers O'Hanlon
         affiliation: Oxford, UK         
       - name:        Aurojit Panda
         affiliation: NYU, USA         
       - name:        Gregorio Martinez Perez
         affiliation: UM, Spain           
       - name:        Stefan Schmid
         affiliation: Univie, Austria       
       - name:        Corinna Schmitt
         affiliation: UZH, Switzerland
       - name:        Peter Schneider
         affiliation: Nokia, Germany         
       - name:        Sandra Scott-Hayward
         affiliation: Queen's, UK                          
       - name:        Seungwon Shin
         affiliation: KAIST, South Korea
       - name:        Paul Smith
         affiliation: AIT, Austria           
       - name:        John Sonchack
         affiliation: UPenn, USA            
       - name:        Jani Suomalainen
         affiliation: VTT, Finland 
       - name:        Steve Uhlig
         affiliation: QMUL, UK         
       - name:        Alexander von Gernler
         affiliation: genua, Germany         
       - name:        Jean-Philippe Wary
         affiliation: Orange, France                                  
       - name:        Vinod Yegneswaran
         affiliation: SRI, USA
---

# {{ page.title }}

### Workshop Program

{% include program-online.html type="secson" %}

### Call for Papers
The First Workshop on Security in Softwarized Networks: Prospects and Challenges (SecSoN) will be held in conjunction with ACM SIGCOMM 2018 in Budapest, Hungary, on August 20-24, 2018.

Operators and enterprises in general are increasingly moving towards a softwarization of their networks. Former dedicated network elements are virtualized and placed on commercial-off-the-shelf hardware. Technologies for softwarization are Software Defined Networking (SDN) and Network Function Virtualization (NFV). They allow for a more efficient management of the network. Whereas NFV replaces the tightly integrated middlebox appliances by flexible Virtualized Network Functions (VNFs) running as software instances on standard servers, SDN enables a fine-granular and programmable selection and redirection of flows in the network.
On one hand, this softwarization reduces the costs for network equipment. On the other hand, it broadens the attack surface as novel networking devices and protocols are deployed, which needs to be considered during the risk assessment. Especially due to their critical role within the softwarized management of the network, these devices and protocols are high ranked targets for potential attackers and thus, require extensive testing and hardening.
In addition, the adaptation of these technologies in enterprise networks remains limited. This is due to the fact, that the integration of new technologies into an existing network infrastructure is a highly complex task, as the compatibility with systems such as network management and cloud management must be assured for production environments.

SecSoN 2018 will focus on the prospects and challenges of softwarized networking with particular attention to the following topics.

### List of Topics
- Securing softwarized network architectures and virtualized environments
- Security for 5G, particularly secure network slicing and isolation
- Integration of hardware security components in a softwarized world
- Cognitive and automated network security management
- Integration of programmable data planes and stateful data path solutions  of security functions, e.g., firewalls, intrusion detection systems
- SDN/NFV interface hardening
- Pentesting and test automation in softwarized networks
- Security considerations for placement and orchestration
- Security monitoring of and with softwarized networks and threat analysis
- Trust relationships between softwarized entities
- Forensics, attack analysis and risk evaluation methods tailored to softwarized networks
- Security events processing and configuration verification and validation

### Submission Instructions
Submissions must be original, unpublished work, and not under consideration at another conference or journal. Submitted papers must be at most six (6) pages long, including all figures, tables, references, and appendices in two-column 10pt ACM format. Papers must include authors names and affiliations for single-blind peer reviewing by the PC. Authors of accepted papers are expected to present their papers at the workshop.

Please submit your paper via <a href="https://sigcomm18secson.hotcrp.com/">https://sigcomm18secson.hotcrp.com/</a>.

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

[Contact the SecSon chairs](mailto:secsonchairs2018@sigcomm.org?subject=[SecSon 2018]){: data-role="button" class="button" }
