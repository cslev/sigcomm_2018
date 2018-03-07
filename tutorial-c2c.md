---
layout: default
title: "ACM SIGCOMM 2018 Tutorial (Half-Day): Towards the Tactile Internet: Low Latency Communication for Connected Cars"
group: Tutorials

data:
  - type: day
    time: Friday, August 25, 2017
    room: "Tesla Room (Engineering IV)"

  - title: Welcome and Intro
    type: tutorial
    time: 2:00pm - 2:15pm

  - title: Lecture, Part I
    type: tutorial
    time: 2:15pm - 3:30pm

  - title: Coffee Break
    type: break
    time: 3:30pm - 4:00pm
    room: Foyer

  - title: Lecture, Part II
    type: tutorial
    time: 4:00pm - 5:30pm

presenters:
- name:        Falko Dressler
  affiliation: Paderborn University, Germany
  bio:         "<p>Falko Dressler is Full Professor for Computer Science and Chair for Distributed Embedded Systems at the Heinz Nixdorf Institute and the Dept. of Computer Science, University of Paderborn, where he is also a member of the University Senate. Dr. Dressler received his M.Sc. and Ph.D. degrees from the Dept. of Computer Science, University of Erlangen in 1998 and 2003, respectively.</p>
<br/>
<p>He is associate editor-in-chief for Elsevier Computer Communications as well as an editor for journals such as IEEE Trans. on Mobile Computing, Elsevier Ad Hoc Networks, and Elsevier Nano Communication Networks. He has been guest editor of special issues in IEEE Journal on Selected Areas in Communications (JSAC), IEEE Communications Magazine, Elsevier Ad Hoc Networks, and many others. Dr. Dressler has been chairing conferences such as IEEE INFOCOM, ACM MobiSys, ACM MobiHoc, IEEE VNC, IEEE GLOBECOM, and many others. He authored the textbooks Self-Organization in Sensor and Actor Networks published by Wiley & Sons and Vehicular Networking published by Cambridge University Press. Dr. Dressler has been an IEEE Distinguished Lecturer as well as an ACM Distinguished Speaker.</p>
<br/>
<p>Dr. Dressler is an IEEE Fellow as well as a a Senior Member of the ACM, and member of GI. He also serves in the IEEE COMSOC Conference Council. His research objectives include adaptive wireless networking, self-organization techniques, and embedded system design with applications in ad hoc and sensor networks, vehicular networks, industrial wireless networks, and nano-networking.</p>"

---

## {{ page.title }}

### Call For Participation

In this tutorial lecture, we discuss the challenges and opportunities of the Tactile Internet and its fundamental concepts. Early 5G research was mainly about big data pipes and further increasing possible data rates in cellular as well as access networks. This situation changes. Current research towards 5G networks and the Tactile Internet focuses primarily on two core aspects: providing ultra-low latency as well as ultra-high reliability. Among many others, distributed control is considered a target application for such networking technologies. In the scope of this tutorial, we concentrate on connected cars as a prominent example – other include industry automation and smart city operations. In this scenario, short range radio broadcast as well as direct machine to machine communication will play a major role. The Tactile Internet activities are now coordinated by the IEEE Communications Society Tactile Internet Sub-Committee.

Looking back at the last decade, one can observe enormous progress in the domain of vehicular networking. In this growing community, many ongoing activities focus on the design of communication protocols to support safety applications, intelligent navigation, multi-player gaming and others. Very large projects have been initiated to validate the theoretic work in field tests and protocols are being standardized. With the increasing interest from industry, security and privacy have also become crucial aspects in the stage of protocol design in order to support a smooth and carefully planned roll-out. Researchers from academia and industry recently met at an international Dagstuhl seminar to discuss open research challenges as well as open issues related to market-oriented design. We are now entering an era that might change the game in road traffic management. This is supported by the U.S. federal government announcement in February 2014 that National Highway Traffic Safety Administration (NHTSA) plans to begin working on a regulatory proposal that would require V2V devices in new vehicles in a future year. This NHTSA announcement coincides with the final standardization of higher layer networking protocols in Europe by the ETSI.

We will primarily discuss the challenges and opportunities of the connected cars vision in relation to some of the most needed components in modern smart cities: improved road traffic safety combined with reduced travel times and emissions. Using selected application examples including the use of virtual traffic lights, intelligent intersection management, and platooning, we assess the needs on the underlying system components with a particular focus on inter-vehicle communication. We also shed light on the potentials of a vehicular cloud based on parked vehicles as a spatio-temporal network and storage infrastructure. Vehicular networking solutions have been investigated for more than a decade but recent standardization efforts just enable a broad use of this technology to build large scale Intelligent Transportation Systems (ITS). One of the key questions is whether some pre-deployed infrastructure is needed to enable and to boost vehicular networks. We see many benefits in such infrastructure to store information and to provide connectivity among the vehicles. Yet, instead of using Roadside Units (RSUs), we envision to rely on parked vehicles to provide such vehicular cloud services.

The tutorial is supported by a textbook on "Vehicular Networking" authored by Falko Dressler that will be published just ahead of the tutorial lecture by Cambridge Press.

### Presenters

{% include presenters.html presenters=page.presenters %}

### Tutorial Program

[Tutorial slides](files/tutorial-c2c.pdf)

{% include program.html type="tutorial-c2c" data=page.data %}

### Topics Covered

A tentative schedule of what we plan to cover in the tutorial is listed below. We will select a subset of topics for presentation closer to the tutorial date. The tutorial is planned as a lecture-style presentation.

- Tactile Internet: Vision and Fundamental Concepts
- Recapping the Past: Vehicular Networking Applications
- Requirements of applications ranging from safety to infotainment
- Protocol design options for connected cars
- Platooning as a strategic application example
- Simulation tools: Overview of (integrated) network and traffic simulators
- Open issues and areas that require further research

### Expected Audience and Prerequisites

The tutorial has no specific prerequisites and is geared to networking researchers and practitioners. 

### References

- [1] Christoph Sommer and Falko Dressler, Vehicular Networking, Cambridge University Press, 2014.

- [2] Falko Dressler, Hannes Hartenstein, Onur Altintas and Ozan K. Tonguz, "Inter-Vehicle Communication - Quo Vadis," IEEE Communications Magazine, vol. 52 (6), pp. 170-177, June 2014.

- [3] Stefan Joerer, Bastian Bloessl, Michele Segata, Christoph Sommer, Renato Lo Cigno, Abbas Jamalipour and Falko Dressler, "Enabling Situation Awareness at Intersections for IVC Congestion Control Mechanisms," IEEE Transactions on Mobile Computing, vol. 15 (7), pp. 1674-1685, June 2016.

- [4] Michele Segata, Bastian Bloessl, Stefan Joerer, Christoph Sommer, Mario Gerla, Renato Lo Cigno and Falko Dressler, "Towards Communication Strategies for Platooning: Simulative and Experimental Evaluation," IEEE Transactions on Vehicular Technology, vol. 64 (12), pp. 5411-5423, December 2015.

- [5] Christoph Sommer, Stefan Joerer, Michele Segata, Ozan K. Tonguz, Renato Lo Cigno and Falko Dressler, "How Shadowing Hurts Vehicular Communications and How Dynamic Beaconing Can Help," IEEE Transactions on Mobile Computing, vol. 14 (7), pp. 1411-1421, July 2015.

- [6] Christoph Sommer, Reinhard German and Falko Dressler, "Bidirectionally Coupled Network and Road Traffic Simulation for Improved IVC Analysis," IEEE Transactions on Mobile Computing, vol. 10 (1), pp. 3-15, January 2011.
