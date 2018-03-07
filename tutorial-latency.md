---
layout: default
title: "ACM SIGCOMM 2018 Tutorial (Half-Day): Understanding Latency - A Root Cost and Mitigation Approach"
group: Tutorials

data:
  - type: day
    time: Friday, August 25, 2017
    room: "Tesla Room (Engineering IV)"

  - title: Introduction
    time: 9:00am - 9:15am
    type: tutorial

  - title: The latency budget
    type: tutorial
    time: 9:15am - 9:35am

  - title: Root causes - spending the budget
    type: tutorial
    time: 9:35am - 10:00am

  - title: Mitigations - refunds
    type: tutorial
    time: 10:00am - 10:30am

  - title: Coffee Break
    type: break
    time: 10:30am - 11:00am
    room: Foyer

  - title: Exploring case studies
    time: 11:00am - 11:30am
    type: tutorial

  - title: Some new opportunities
    time: 11:30am - 11:55am
    type: tutorial

  - title: Application in current and emerging networks
    time: 11:55am - 12:20pm
    type: tutorial

  - title: Conclusions and review (with Q&A)
    time: 12:20pm - 12:30pm
    type: tutorial

presenters:
- name:        Joe Touch
  affiliation: "University of Southern California / Information Sciences Institute"
  bio:         "<p>Joe Touch is the Postel Center Director at the University of Southern California's Information Sciences Institute and a Research Associate Professor of CS and EE/Systems. He received a B.S. in biophysics and CS from the Univ. of Scranton in 1985, an M.S. in CS from Cornell Univ. in 1987, and a Ph.D. in CS from the Univ. of Pennsylvania in 1992. He joined ISI in 1992 and his current projects involve recursive virtual networks, optical Internets, and high-performance network security. His interests include Internet protocols, network architecture, and network device design. He also served as an \"IPA\" as USAF SMC TSAT Space Segment Senior Network Engineer and ACG Network Chief from 2006-2010. He holds 5 US patents and published over 150 papers in conferences and journals. Joe is in Sigma Xi, an ACM Distinguished Scientist, an IEEE Senior Member and Communications Society Distinguished Lecturer, and an OSA Senior Member, Traveling Lecturer, and Nonlinear Optics TG co-chair. He is active in the IETF in the Transport, Internet, and Security Areas, serves on numerous conference committees. His \"first principles approach to computer networking\" course, based on his Recursive Network Architecture, is under development as a textbook. Joe has nearly three decadess of experience analyzing latency and his latency-focused publications include his Ph.D. dissertation.</p>"

---

## {{ page.title }}

### Call For Participation

"Time is fleeting," it has been said. Time delay, or latency, is the one metric that drives most others. It defines what it means to be **fast**, and limits us to what is **fast enough**.

Latency has always been a key part of network performance, but recently it has been elevated to a primary focus for electronic traders, search engines, name servers, data centers, and home and network routers. Increases in network bandwidth, router forwarding speed, and end system computational resources have helped bring latency to the forefront as a primary concern. New protocols are emerging to address latency as a primary issue, including Delay Tolerant Networking (DTN) and bufferbloat mitigations.

This tutorial presents a comprehensive exploration of the impact of latency on communication. It explores time as a budget to be spent, over-spent, rebated, and conserved. We explore the root causes of latency: generating data, transmitting it, processing it, and the impact of resource sharing through multiplexing and aggregation, as well as corresponding ways to mitigate each of these causes. We also explore ways to mask latency that cannot be reduced and to avoid incurring its cost in the first place. This tutorial provides examples of real system design and implementations, as well as exploring several key case studies to provide practical experience that attendees can immediately apply to their own systems.

### Presenters

{% include presenters.html presenters=page.presenters %}

### Tutorial Program

{% include program.html type="tutorial-latency" data=page.data %}

### Motivation

The evolution of technology has increased computer performance by many orders of magnitude, but whatever we improve, latency remains the last and most critical limit. Everything else has become so fast we now notice – and care – more about delay. Papers addressing latency issues have always been prevalent at Sigcomm and many other conferences in the IEEE, ACM, and IFIP, including the Internet Society Workshop on Reducing Internet Latency and the recent flurry of activity around bufferbloat. Computing resources have shifted from constraints to opportunities, where we now have enough surplus processing, memory, storage, and bandwidth that we can spend to reduce latency. Interaction has increased, where isolated computers are rare, collaborating groups of resources are larger and more ubiquitous, and the way resources relate is more complex. Some of this complexity and resource surplus has even made latency worse, as web page sizes, photos, and software become larger and buffer capacity has begun to hurt, rather than help. This is a useful time to consider the impact of system and protocol design on latency and find ways it can be reduced, masked, or avoided.

### Topics Covered

This tutorial presents a comprehensive discussion of communication latency, focusing on the fundamental properties and behaviors that cause latency to increase and corresponding ways to mitigate each of these causes. The following concepts are covered:

- The latency budget and how its bounds are determined

- The root causes of latency, i.e., how the latency budget is spent

- The corresponding mitigations of each root latency cause, i.e., how to receive refunds

- A variety of case studies, including bufferbloat, stock trading, data centers, and search engines

- New opportunities to reduce latency, including “fission” and “information advance”

- Use cases for tolerating latency in different environments

- Emerging applications, including TCP TFO, integrated forwarding, and future curiosities

### Tutorial type
Lecture

### Audience expectations and prerequisites

Audiences are expected to have basic knowledge of packet networking, including layering, TCP basics, and commonly used protocols such as DNS and the Web.

### References

A structured set of cited papers and presentations with corresponding links is available at [http://www.latency.org/](http://www.latency.org/).
