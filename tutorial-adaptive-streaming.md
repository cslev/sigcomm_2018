---
layout: default
title: "ACM SIGCOMM 2018 Tutorial (Half-Day): Adaptive Streaming of Traditional and Omnidirectional Media"
group: Tutorials

data:
  - type: day
    time: Monday, August 21, 2017
    room: "Faraday Room (Engineering IV)"

  - title: Welcome and Intro
    time: 2:00pm - 2:15pm
    type: tutorial

  - title: "Part I: The HTML5 Standard and Adaptive Streaming"
    time: 2:15pm - 3:30pm
    type: tutorial

  - title: Coffee Break
    time: 3:30pm - 4:00pm
    type: break
    room: Foyer

  - title: "Part II: Omnidirectional (360°) Media"
    time: 4:00pm - 5:30pm
    type: tutorial

presenters:
  - name:        Ali C. Begen
    affiliation: Networked Media / Ozyegin University
    bio:         "<p>Ali C. Begen is the co-founder of Networked Media, a technology company that offers consulting services to industrial, legal and academic institutions in the IP video space. He has been a research and development engineer since 2001, and has broad experience in mathematical modeling, performance analysis, optimization, standards development, intellectual property and innovation. Between 2007 and 2015, he was with the Video and Content Platforms Research and Advanced Development Group at Cisco, where he has architected, designed and developed algorithms, protocols, products and solutions in the service provider and enterprise video domains. Currently, he is also affiliated with Ozyegin University, where he is an assistant professor in the computer science department.</p>
<br/>
<p>Ali holds a Ph.D. degree in electrical and computer engineering from Georgia Tech. He received a number of scholarly and industry awards, and he has editorial positions in prestigious magazines and journals in the field. He is a senior member of the IEEE and a senior member of the ACM. In January 2016, he was elected as a distinguished lecturer by the IEEE Communications Society. Information on his projects, publications, talks, and teaching, standards and professional activities can be found at http://ali.begen.net.</p>"

  - name: Christian Timmerer
    affiliation: Institute of Information Technology (ITEC) / Bitmovin
    bio: "Christian Timmerer received his M.Sc. (Dipl.-Ing.) in January 2003 and his Ph.D. (Dr.techn.) in June 2006 (for research on the adaptation of scalable multimedia content in streaming and constrained environments) both from the Alpen-Adria-Universität (AAU) Klagenfurt. He joined the AAU in 1999 (as a system administrator) and is currently an Associate Professor at the Institute of Information Technology (ITEC) within the Multimedia Communication Group. His research interests include immersive multimedia communication, streaming, adaptation, Quality of Experience, and Sensory Experience. He was the general chair of WIAMIS 2008, QoMEX 2013, and MMSys 2016 and has participated in several EC-funded projects, notably DANAE, ENTHRONE, P2P-Next, ALICANTE, SocialSensor, COST IC1003 QUALINET, and ICoSOLE. He also participated in ISO/MPEG work for several years, notably in the area of MPEG-21, MPEG-M, MPEG-V, and MPEG-DASH where he also served as a standard editor. In 2012, he cofounded Bitmovin (http://www.bitmovin.com/) to provide professional services around MPEG-DASH where he holds the position of the Chief Innovation Officer (CIO)."

---

## {{ page.title }}

### Call For Participation

Universal media access is now a reality. We can generate, distribute, share and consume any media content, anywhere, anytime and with/on any device. A major technical breakthrough was the adaptive streaming over HTTP resulting in the standardization of MPEG-DASH, which is now successfully deployed in HTML5 environments thanks to corresponding media source extensions (MSE). The next big thing in adaptive media streaming is virtual reality applications and, specifically, omnidirectional (360°) media streaming, which is currently built on top of the existing adaptive streaming ecosystems.

Unlike most of its counterparts that offer mostly theoretic content, this tutorial will focus on practical matters such as the existing products and solutions that are being used by millions of users around the globe and the new developing technologies that will be used by even more users in a few years.

### Presenters

{% include presenters.html presenters=page.presenters %}

### Tutorial Program

[Tutorial slides](files/tutorial-adaptive-streaming.pdf)

{% include program.html type="tutorial-adaptive-streaming" data=page.data %}

### Topics Covered

This tutorial consists of two main parts. In the first part, we provide a detailed overview of the HTML5 standard and show how it can be used for adaptive streaming deployments. In particular, we focus on the HTML5 video, media extensions, and multi-bitrate encoding, encapsulation and encryption workflows, and survey well-established streaming solutions. Furthermore, we present experiences from the existing deployments and the relevant de jure and de facto standards (DASH, HLS, CMAF) in this space.

In the second part, we focus on omnidirectional (360°) media from creation to consumption. We survey means for the acquisition, projection, coding and packaging of omnidirectional media as well as delivery, decoding and rendering methods. Emerging standards and industry practices are covered as well. Throughout the tutorial, we present some of the current research trends, open issues that need further exploration and investigation, and various efforts that are underway in the streaming industry.

Upon attending this tutorial, the participants will have an overview and understanding of the following topics:

- Principles of HTTP adaptive streaming for the Web/HTML5
- Principles of omnidirectional (360°) media delivery
- Content generation, distribution and consumption workflows for traditional and omnidirectional media
- Standards and emerging technologies in the adaptive streaming space
- Current and future research on traditional and omnidirectional media delivery

### Tutorial Type

The tutorial will be in the form of a lecture. However, live demonstrations are planned to show specific examples.

### Target Audience and Prerequisites

This tutorial includes both introductory and advanced level information. The audience is expected of understanding of basic video coding and IP networking principles. Researchers, developers, content and service providers are all welcome.
