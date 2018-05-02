---
layout: default
title: "ACM SIGCOMM 2018 Morning Tutorial on Service-oriented RAN: Challenges, Technologies, and Tools to enable RAN slicing (SO-RAN)"
group: Tutorials

dates:
    - info: Tutorial
      date: August 24, 2018
      
data:
  - type: day
    time: Monday, August 20, 2018
    room: TBA

organizers:
- name:        Navid Nikaein
  affiliation: EURECOM, France
  photo:       Navid-Nikaein.png
  bio:         "<p>Navid Nikaein is an Assistant Professor in Communication System Department at Eurecom. He  received his Ph.D. degree in communication systems from the Swiss Federal Institute of Technology EPFL in 2003.  He is leading a group on experimental 4G-5G system research related to radio access and core networks  with a blend of communication, computing, and data analysis in divers settings such as cellular, mesh, and cloud. He is very active in collaborative research projects related to 5G and beyond in the context of European FP6, FP7, H2020 framework programmes. He is also leading the development of the radio access layer of OpenAirInterface and its evolution towards 5G as well as coordinating the Mosaic-5G initiative whose goal is to provide software-based 4G/5G service delivery platforms.</p>"

---

# {{ page.title }}

## Call For Participation

This tutorial will provide participants with the challenges, solutions and technologies, and enabling available tools to realize service-oriented 5G vision through RAN and CN slicing, and open up discussions directions towards RAN data mining and analytics to optimize the network and support user quality-of-service (QoS). 

Attendee will learn about how dynamic virtualization and flexible customization of a BS can be achieved, as well as existing prototypes and opensource tools with alternative RAN and CN slicing approaches to realize the service-oriented 5G vision.


## <i class="fa fa-calendar"></i> Important Dates

{% include dates2.html dates=page.dates %}

## Outline
The tutorial is organized in 6 parts for a duration of 3 hours (half a day) as follows:  

- **Principles (30 minutes)**:  In this part, we start by highlighting target use-cases and their requirements in the context of 5G, followed by definitions, taxonomy, and design elements of RAN slicing. Then relevant standardization activities (3GPPP, NGMN, ETSI, ONF) and 5G-related activities (5G-PPP projects, 5G-Forum, opensource initiatives) will be presented.

- **Challenges (50 minutes)**: In this part, we present main challenges in realizing RAN slicing, and provide fundamental trade-offs and practical limits in realizing RAN softwarization and virtualization/cloudification in terms of  performance, scalability, computation/complexity, realtime. We present the realworld measurements in the context of 4G/4G+ obtained through the OpenAirInterface and Mosaic5G platforms. Implication and feasibility in slicing of heterogeneous RAN, and inter-networking with 5G core network (CN) slicing will be also discussed. Finally, we elaborate on the RAN data mining and analytics in order to optimize slice-specific QoS requirements. 

- **Technologies (50 minutes)**: In this part, we will analyze different techniques in RAN virtualization and softwarization and identify the role of cloud, SDN, and NFV to enable RAN slicing. In particular, we elaborate on RAN slicing properties such as isolation, resources sharing, customization and programmability, and present the 3GPPP vision of RAN slice orchestration in 5G. We also present technologies, techniques and methodology to mine and analyze the RAN data in both online and offline scenarios. Finally, we provide the lessons learnt from the realworld experimentation particularly through open-source solutions.

- **Prototyping and Validations (30 minutes)**: In this part, we detail the design methodology in RAN slicing, and the main past and on-going efforts in prototyping RAN slicing highlighting their main features and objectives. Finally, recent findings and performance results available on RAN slicing and analytics will be presented.

- **Conclusion (15 minutes)**: In this part we summarize the efforts in RAN slicing,  and present the main conclusions and future directions. 

- **References (5 minutes)**: In the last part, we provide an extensive list of publications and efforts in the area of  from the research communities as well as industries.
 
 
## Audience Expectations and Prerequisites
Attendees will be expected to have a quick look at the references [1-11] below, which can be downloaded with the provided link.

## Background
**Network slicing** is one of the key enablers to provide the required flexibility for the envisioned service-oriented 5G. It enables the composition and deployment of multiple logical networks over a shared physical infrastructure, and their delivery as a service or slice. A slice can either be completely isolated from other slices down to the different sets of spectrum and cell site (as in most of current 3G and 4G deployment), or be shared across all types of resources including radio spectrum and network functions (e.g., all network layers of protocol stack), or be customized for a subset of user-plane (UP) and control-plane (CP) processing with an access to a portion of radio resources in a virtualized form. In addition, a slice may span across **domain-specific resources** each with different levels of isolation and sharing with the objective of accommodating both slice service and underlying infrastructures. To this end, **softwarization**, **virtualization**, and **disaggregation** are the key slicing enablers to flexibly customize a slice, automate its life-cycle management, and ease the development of network functions and applications with the objective to accommodate the requirements of an end-to-end (E2E) service.  They constitute the foundation for a multi-service and multi-tenant 5G network architecture, and are realized by applying the principles of software-define networking (SDN), network function virtualization (NFV), and cloud computing to the mobile networks.

## Organizers

{% include organizers.html presenters=page.organizers %}

<!--
## Tutorial Program

{% include program.html type="tutorial-p4" data=page.data %}
-->



### References
<p>
[1] C-Y. Chang, N. Nikaein, et al., 2018, Slice Orchestration for Multi-Service Disaggregated Ultra Dense RANs, IEEE Communication Magazine. <a href="http://www.eurecom.fr/fr/publication/5494/download/comsys-publi-5494.pdf">[Download]</a><br/>
[2] Xenofon Foukas et al. 2017. Orion: RAN Slicing for a Flexible and Cost-Effective Multi-Service Mobile Network Architecture. In Proceedings of ACM MobiCom. <a href="http://homepages.inf.ed.ac.uk/mmarina/papers/orion-mobicom17.pdf">[Download]</a><br/>
[3] X. Foukas, N. Nikaein,  et al. 2016. FlexRAN: A Flexible and Programmable Platform for Soware-Dened Radio Access Networks. In Proceedings of ACM CoNEXT. <a href="http://www.eurecom.fr/fr/publication/5082/download/comsys-publi-5082.pdf">[Download]</a><br/>
[4] A. Ksentini and N. Nikaein, 2017, Toward enforcing network slicing on RAN: Flexibility and resources abstraction, IEEE Communications Magazine. <a href="http://www.eurecom.fr/fr/publication/5233/download/comsys-publi-5233.pdf">[Download]</a><br/>
[5] Akihiro Nakao et al. 2017. End-to-end Network Slicing for 5G Mobile Networks. Journal of Information Processing 25. <a href="https://www.jstage.jst.go.jp/article/ipsjjip/25/0/25_153/_pdf/-char/en">[Download]</a><br/>
[6] NGMN-Alliance. 2015. 5G White Paper. (Feb 2015). <a href="https://www.ngmn.org/fileadmin/ngmn/content/downloads/Technical/2015/NGMN_5G_White_Paper_V1_0.pdf">[Download]</a><br/>
[7] Peter Rost et al. 2017. Network Slicing to Enable Scalability and Flexibility in 5G Mobile Networks. IEEE Communications magazine. <a href="https://arxiv.org/ftp/arxiv/papers/1704/1704.02129.pdf">[Download]</a><br/>
[8] <a href="http://www.openaiinterface.org">[http://www.openaiinterface.org]</a><br/>
[9] <a href="https://gitlab.eurecom.fr/oai/">[https://gitlab.eurecom.fr/oai/]</a><br/>
[10] <a href="http://mosiac5g-io">[http://mosiac5g-io]</a><br/>
[11] <a href="https://gitlab.eurecom.fr/mosaic5g/">[https://gitlab.eurecom.fr/mosaic5g/]</a><br/>
</p>