---
layout: default
title: "ACM SIGCOMM 2018 Tutorial (Half-Day): Named Data Networking (NDN) Tutorial"
group: Tutorials

data:
  - type: day
    time: Monday, August 21, 2017
    room: "Shannon Room (Engineering IV)"

  - title: Welcome and Introduction
    type: tutorial
    time: 9:00am - 9:05am

  - title: NDN Architecture (Van Jacobson)
    type: tutorial
    time: 9:05am - 10:30am

  - title: Coffee Break
    type: break
    time: 10:30am - 11:00am
    room: Foyer

  - title: "NDN Research (NDN project team)"
    type: tutorial
    time: 11am - 12:30am

presenters:
- name:        Alexander Afanasyev
  affiliation: Florida International University
  bio:         "<p>Alexander Afanasyev is Assistant Professor in Florida International University, Miami.  He received his Ph.D. degree in computer science from UCLA in 2013.  His research focus is on the next-generation Internet architecture as part of the Named Data Networking (NDN) project. His research interests include a variety of topics that are vital for the success of NDN, including scalability of name-based routing, auto-configuration, distributed data synchronization, application and network security.  Dr. Afanasyev is also leading the development effort of the overall NDN codebase.</p>"

- name:        Jeff Burke
  affiliation: UCLA School of Theater, Film and Television (TFT)
  bio:         "<p>Jeff Burke is Assistant Dean for Technology and Innovation at the UCLA School of Theater, Film and Television (TFT), where he has been a faculty member since 2001.  His research explores the intersections of the built environment, computer networks, and storytelling. He has produced, managed, programmed, and designed performances, short films, new genre art installations and new facility construction internationally for over fifteen years, incorporating emerging technologies as part of these projects and creative works.  Burke co-founded REMAP, a joint center of TFT and the Henry Samueli School of Engineering and Applied Science, which uses a mixture of research, artistic production, and community engagement to investigate the interrelationships among culture, community, and technology. From 2006-2012, Burke was the area lead for participatory sensing at the NSF Center for Embedded Networked Sensing (CENS). He is Co-PI and application team lead for the Named Data Networking research project. </p>"

- name:        Patrick Crowley
  affiliation: Washington University in St. Louis
  bio:         "<p>Patrick Crowley is Professor of Computer Science & Engineering at Washington University in St. Louis, where he directs the Applied Research Lab. He is also founder and CTO of Observable Networks, a cloud-native network security company. His research interests are in computer and network systems architecture, with a current focus on information-centric networking, programmable network systems design, and the invention of superior network monitoring and security techniques.</p>"

- name:        Van Jacobson
  affiliation: University of California, Los Angeles / Google
  bio:         "<p>Van Jacobson has been a long-term contributor to the Internet. His algorithms for the Transmission Control Protocol (TCP) saved Internet from congestion collapse in 1980's and are used by over 90% of Internet hosts today. He developed the blueprint of Named Data Networking (NDN) 10 years ago and continues to serve as the NDN architect.</p>"

- name:        Beichuan Zhang
  affiliation: University of Arizona
  bio:         "<p>Beichuan Zhang is Associate Professor at the Department of Computer Science, the University of Arizona. His research interest is in Internet routing architectures and protocols. He has been working on Named Data Networking, green networking, and inter-domain routing. He received the Applied Networking Research Prize in 2011 by ISOC and IRTF, and best paper awards at IEEE ICDCS in 2005 and IWQoS in 2014. Dr. Zhang received Ph.D. from UCLA and B.S. from Peking University.</p>"

- name:        Lixia Zhang
  affiliation: University of California, Los Angeles
  bio:         "<p>Lixia Zhang is Professor in the Computer Science Department of UCLA.  She received her Ph.D in computer science from MIT and was a member of the research staff at Xerox PARC before joining UCLA. She is a fellow of ACM and IEEE, the recipient of IEEE Internet Award, and the holder of UCLA Postel Chair in Computer Science.  Since 2010 she has been leading the effort on the design and development of the NDN architecture.</p>"

---

## {{ page.title }}

### Call For Participation

This half-day SIGCOMM tutorial provides an introduction to [Named Data Networking (NDN)](https://named-data.net/), a newly developed data-centric Internet architecture.
NDN makes a conceptually simple yet fundamental change to the narrow waist of the Internet's narrow waist architecture by replaces TCP/IP's narrow focus on "where" to send packet with "what" content to fetch. We believe that this shift to data-centric networking can greatly help enhance Internet security, enable mobility support, scale both data disseminations as well as data collection (e.g., from IoT devices), as well as facilitate new application developments.

The morning starts with an introduction of the NDN architecture by Van Jacobson, followed by research topics and recent results.
For more detailed information about the tutorial and additional activities, please check out [NDN Tutorial homepage](https://named-data.net/tutorials/sigcomm2017/)

### Presenters

{% include presenters.html presenters=page.presenters %}

### Tutorial Program

Tutorial slides and videos:

1. [NDN – Why Bother? (Van Jacobson)](https://youtu.be/uvnP-_R-RYA)

2. [NDN Research (Beichuan Zhang)](https://youtu.be/1BOU-Dky93I) ([Slides](https://named-data.net/tutorials/sigcomm2017/assets/slides/3-research.pdf))

3. [NDN Codebase and Development (Alex Afanasyev)](https://youtu.be/5fncxmCPsdw) ([Slides](https://named-data.net/tutorials/sigcomm2017/assets/slides/4-codebase-overview.pdf))

4. [NDN Demos I: ONL, Testbed (John DeHart)](https://youtu.be/KhPqFPg4oWo) ([Slides](https://named-data.net/tutorials/sigcomm2017/assets/slides/5-demo-1.pdf))

5. [NDN Demos II: Cloud-optional Home IoT (Jeff Burke, Yanbiao Li)](https://youtu.be/9e9cnQVZcJE) ([Slides](https://named-data.net/tutorials/sigcomm2017/assets/slides/6-demo-2.pdf))

6. [NDN Demos III: NDNHealth (Jeff Burke, Haitao Zhang)](https://youtu.be/k74e8w3JbBw)

7. [Wrap-up (Lixia Zhang)](https://youtu.be/Bs06zntYI9c)

{% include program.html type="tutorial-ndn" data=page.data %}

Note this tutorial has a companion afternoon program with the description of what have been accomplished so far using IoT and global-scale demonstrations.
See more on [NDN Tutorial homepage](https://named-data.net/tutorials/sigcomm2017/)

### Motivation

This half-day tutorial aims to provide a comprehensive overview of [Named Data Networking (NDN)](https://named-data.net/), a newly developed Internet architecture. NDN replaces TCP/IP architecture's focus on "where", i.e., the addresses and hosts, with "what", i.e., the content that users and applications care about. This fundamental shift brings profound impacts to enhancing Internet security, enabling mobility support, scaling both data disseminations as well as data collection (e.g., from IoT devices), and facilitating new application development.

Launched in 2010 under the NSF's Future Internet Architecture program, the NDN project has attracted researchers from both academia and industry around the world to explore all aspects of its design, implementation, and applications.  It is arguably the most prominent inspiration and realization of the Information-Centric Networking (ICN) vision, around which a growing research community has formed over the past several years.

Together with an increasing interests in NDN, there are also a number of questions as well as misconceptions regarding NDN.  This tutorial aims to bring NDN to the broader networking community by explaining NDN's basic architectural concepts, articulating research issues, demonstrating NDN operations and applications, and introducing its open-source code development. We expect the tutorial to benefit network researchers and students with different levels of background knowledge on NDN/ICN, from people who want to learn what NDN really is, to people who are looking for new topics to explore, or for ways to contribute to NDN design and development.

The tutorial will start with an introduction to the NDN architecture by Van Jacobson, followed by an overview of the NDN research topics and recent results by the NDN project team researchers.

### Topics Include

- Introduction of the basic concepts, fundamental principles, key mechanisms, and articulation on how to take NDN to the next stage.

- Survey on existing NDN research work, with emphasis on research challenges and recent results, including

    - Routing
    - Forwarding
    - Caching
    - Mobility
    - Security
    - Applications

### Expected Audience and Prerequisites

This tutorial targets the general networking research community with no specific prerequisite. We expect the tutorial to benefit network researchers and students with different levels of background knowledge on NDN/ICN, from people who want to learn what NDN really is, to people who are looking for new topics to explore, or for ways to contribute to NDN design and development.
