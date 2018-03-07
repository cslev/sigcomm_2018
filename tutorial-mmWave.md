---
layout: default
title: "ACM SIGCOMM 2018 Tutorial (Half-Day): Millimeter-Wave Wireless Networking and Sensing"
group: Tutorials

data:
  - type: day
    time: Monday, August 21, 2017
    room: "Faraday Room (Engineering IV)"

  - title: Welcome and Intro
    time: 9:00am - 9:15am
    type: tutorial

  - title: TBD
    time: 9:15am - 10:30am
    type: tutorial

  - title: Coffee Break
    time: 10:30am - 11:00am
    type: break
    room: Foyer

  - title: TBD
    type: tutorial
    time: 11am - 12:30am

presenters:
- name:        Xinyu Zhang
  affiliation: University of Wisconsin-Madison
  bio:         "<p>Xinyu Zhang is an Assistant Professor in the Department of Electrical and Computer Engineering at the University of Wisconsin-Madison. He received his Ph.D. degree in Computer Science and Engineering from the University of Michigan in 2012. His research interest lies in wireless systems and ubiquitous computing, and more specifically in (i) designing next-generation wireless architectures based on millimeter-wave, large-scale distributed antennas, and physical-layer informed protocols; (ii) designing ubiquitous computing systems that leverage wireless signals to sense micro-locations and micro-activities at near-vision precision.  His research work has been regularly published in top conferences in these areas, especially ACM MobiCom, MobiSys, USENIX NSDI, and IEEE INFOCOM. He is the recipient of ACM MobiCom Best Paper Award in 2011, NSF CAREER Award in 2014, and Google Faculty Research Award in 2017.</p>"

- name:        Upamanyu Madhow
  affiliation: University of California, Santa Barbara
  bio:         "<p>Upamanyu Madhow is Professor of Electrical and Computer Engineering at the University of California, Santa Barbara. His research interests broadly span communications, signal processing and networking, with current emphasis on millimeter wave communication, and on distributed and bio-inspired approaches to networking and inference. He received his bachelor's degree in electrical engineering from the Indian Institute of Technology, Kanpur, in 1985, and his Ph. D. degree in electrical engineering from the University of Illinois, Urbana-Champaign in 1990. He has worked as a research scientist at Bell Communications Research, Morristown, NJ, and as a faculty at the University of Illinois, Urbana-Champaign.  Dr. Madhow is a recipient of the 1996 NSF CAREER award, and co-recipient of the 2012 IEEE Marconi prize paper award in wireless communications. He has served as Associate Editor for the IEEE Transactions on Communications, the IEEE Transactions on Information Theory, and the IEEE Transactions on Information Forensics and Security. He is the author of two textbooks published by Cambridge University Press, Fundamentals of Digital Communication (2008) and Introduction to Communication Systems (2014).</p>"

---

## {{ page.title }}

### Call For Participation

The past a few decades have witnessed tremendous penetration of wireless technologies on the microwave spectrum, especially through the WiFi and cellular networks. However, the capacity of such technologies is reaching a limit due to the limited amount of spectrum resource. In contrast, abundant spectrum exists at the millimeter-wave (mmWave) band. For example, around the 60 GHz mmWave band, 14 GHz of unlicensed spectrum is available, spanning 57 GHz to 71 GHz, about an order of magnitude wider than the microwave spectrum in use. This presents an opportunity for profound technological innovations via multi-Gbps indoor and outdoor networks, thus alleviating the capacity crisis facing mobile operators today.

Commercial interest in mmWave networking has been steadily increasing recently, with a main focus on commercializing short-range high-bandwidth mmWave radios based on recent IEEE standards (e.g., 802.11ad and 802.15.3c). However, the transformative potential of mmWave goes well beyond the current standards. The industry alliance has been exploring mmWave as an enabling technology for multi-Gbps cellular connectivity in 5G and beyond. The wide penetration of mobile mmWave radios is also bringing mmWave sensing to everyday life.

The objective of this tutorial is to present to networking researchers an overview of the unique characteristics of mmWave wireless communications, introduce the challenges and latest development in mmWave networking and sensing applications, and outline the future research problems in this domain. The tutorial will be provided by two speakers with complementary expertise in mmWave signal processing, network protocol design, and mmWave sensing applications. The tutorial content draws on insights from state-of-the-art in mmWave networking, as well as the speakers' years of research experience in modeling/measuring mmWave communication systems, and in designing mmWave testbeds, protocols and applications.

### Presenters

{% include presenters.html presenters=page.presenters %}

### Tutorial Program

Tutorial slides

- [Part 1. Intro and Channel models](files/tutorial-mmWave/1-intro.pptx)

- [Part 2. Protocol Standards](files/tutorial-mmWave/2-standards.pptx)

- [Part 3. Compressive Beamforming](files/tutorial-mmWave/3-beamforming.pptx)

- [Part 4. Higher layers](files/tutorial-mmWave/4-higher-layers.pptx)

- [Part 5. mmWave sensing](files/tutorial-mmWave/5-sensing.pptx)

- [Part 6. LOS mmWave MIMO](files/tutorial-mmWave/6-LOS.pptx)

- [Part 7. Conclusion](files/tutorial-mmWave/7-conclusion.pptx)

{% include program.html type="tutorial-mmWave" data=page.data %}

### Motivation

Despite the huge potential in increasing network capacity, mmWave networks face a number of challenges unseen in conventional low-frequency cellular and WiFi systems. mmWave radios commonly adopt many-element phased-array antennas to form highly directional steerable beams, which can leverage reflections to steer around obstacles. These unique characteristics of mmWave technologies require completely rethinking wireless network design from physical-layer signal processing all the way up to mobile applications. On the other hand, the commercialization of mmWave mobile devices is also triggering low-cost mmWave sensing applications, which used to be available only in dedicated environment for medical/security inspection. Together, short wavelength and high directionality translates into high sensitivity, enabling subtle object localization/tracking, vital-sign detection and mobile mmWave imaging. Given the critical role that mmWave will play in next-generation wireless networks and mobile devices, we expect the content to be timely and interesting for the SIGCOMM audience.

### Topics Covered

1. mmWave channel characteristics: models and measurements

    - Models of mmWave wireless channel: Emphasis will be put on channel sparsity, directionality, as well as differences from the low-frequency communication channels.

    - mmWave channel measurement and estimation: Major insights learned from recent measurements of mmWave network measurements, as well as algorithms to reduce the channel estimation overhead in mmWave systems.

2. mmWave communication technologies

    - Communication algorithms in mmWave standards: Overview of the modulation, power control, spectrum allocation, along with a contrast to the conventional WiFi systems.

    - mmWave beamforming: Structures of phased-arrays and beam patterns, and empirical models of the phased-array capabilities.  (iii) mmWave MIMO: High-level model of the mmWave MIMO and hybrid MIMO, under investigation in next-generation mmWave standards (e.g., 802.11ay).

3. mmWave MAC protocols

    - Medium access control in mmWave network standards.  Overview of unique challenges in mmWave MAC, e.g., imperfect directionality, sensitivity to blockage; and standard primitives to address these issues.

    - Beam searching protocol: Standard and state-of-the-art solutions to enable efficient beam searching on large phased-array antennas with hundreds
    of beam patterns.

    - Mesh networking through directional mmWave links: Unique aspects of mmWave mesh, with a focus on its unique interference mapping aspects.

4. Robust mmWave networking under blockage and mobility

    - Overcoming blockage: State-of-the-art solutions that leverage relays, reflectors, or out-of-band channels to sustain the link under human body blockage.

    - Making mmWave networks robust using multi-AP cooperation: Leveraging mmWave sensing to help optimizing mmWave access point deployment.

5. mmWave sensing systems

    - Using mmWave communication devices for object tracking: Millimeter-scale object tracking using 60 GHz directional beams.

    - Mobile mmWave imaging: Harnessing mobile mmWave radio devices to estimate the geometries of everyday objects.

### Tutorial Type

This tutorial will be lecture based, spanning half a day, and delivered by the two speakers in an interleaved manner.

### Expected Audience and Prerequisites

The tutorial will target networking researchers in general. Although certain content involves knowledge in wireless communications, it will be delivered from a high level to facilitate intuitive understanding of the mmWave characteristics.  The end goal of the tutorial is to help networking researchers to understand the disruptive aspects of mmWave as the foundation for wireless technologies at 5G and beyond. These aspects are anticipated to trigger the design of new network protocols and applications.
