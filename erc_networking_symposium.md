---
layout: default
title: "ACM SIGCOMM 2018 Symposium on European Research in Computer        Networking (ERC Networking 2018)"
group: Workshops

dates:
    - info: ERC Networking 2018
      date: August 24, 2018
    
committees:
    - role: Symposium Chairs
      people:
       - name:        Telma Carvalho  
         affiliation: ERC Executive Agency, Belgium
       - name:        Xiaoming Fu 
         affiliation: GAU, Germany
       - name:        Sergey Gorinsky
         affiliation: IMDEA, Spain
       - name:        Andrzej Jajszczyk 
         affiliation: ERC Scientific Council and AGH, Poland
       - name:        Michael Schapira 
         affiliation: HUJI, Israel
       - name:        János Tapolcai
         affiliation: BME, Hungary
    

presenters:
    - name:        Anat Bremler-Barr 
      affiliation: IDC, Israel
      title:       "Advances in Deep Packet Inspection for Next Generation Network Devices"
      abstract:    "Deep Packet Inspection (DPI) aims to identify packets that contain a pattern from a large set of known patterns (e.g., codes of viruses etc.). In this talk I will present advanced DPI techniques that overcome and address the following issues related to DPI:<br/>
      
  1.   Faster and scalable solutions in terms of speed (throughput) memory requirements and power consumption.<br/>
  2.  DPI algorithms for compressed and other non-clear traffic.<br/> 
  3.  DPI techniques that are more immune and can stand DDoS DPI complexity attacks.<br/>
  4.  a holistic design of a DPI service as part of a software-defined framework for virtual network functions (VNF). The DPI service supports multi-tenant and presents a significant improvement both in scalability, security and functionality."
      bio:         "Anat Bremler-Barr is an Associate Professor with the School of Computer Science, Interdisciplinary Center, Herzliya, Israel. She received the Ph.D. degree (with distinction) in computer science from Tel Aviv University, Tel Aviv, Israel. In 2001, she co-founded and was the Chief Scientist of Riverhead Networks, Inc., which provided systems to protect from denial-of-service attacks. The company was acquired by Cisco Systems in 2004. She then joined the Interdisciplinary Center, Herzliya, in 2004. In 2011, she co-founded with Prof. David Hay the DEEPNESS lab (funded by an ERC starting grant,  [http://www.deepness-lab.org/](http://www.deepness-lab.org/)) that focuses on designing deep packet inspection for next-generation network devices. Her research interests are in computer networks and network security."
      
    - name:        Srdjan Capkun 
      affiliation: ETH, Switzerland
      title:       How to Build a Secure Positioning System
      bio:         "Srdjan Capkun (Srđan Čapkun) is a Full Professor in the Department of Computer Science, ETH Zurich and Director of the Zurich Information Security and Privacy Center (ZISC). He was born in Split, Croatia. He received his Dipl.Ing. Degree in Electrical Engineering / Computer Science from the University of Split in 1998, and his Ph.D. degree in Communication Systems from EPFL in 2004. Prior to joining ETH Zurich in 2006 he was a postdoctoral researcher in the Networked & Embedded Systems Laboratory (NESL), University of California Los Angeles and an Assistant Professor in the Informatics and Mathematical Modelling Department, Technical University of Denmark (DTU). His research interests are in system and network security. One of his main focus areas is wireless security. He is a co-founder of 3db Access, a company focusing on secure distance measuement and proximity-based access control, and of Sound-Proof a spin-off focusing on usable on-line authentication. In 2016 he received an ERC Consolidator Grant for a project on securing positioning in wireless networks."
      abstract:    "In this talk I will review security issues in today's navigation and close-range positioning systems. I will discuss why GNSS systems like GPS are hard to fully secure. I will then show how a different design of a positioning system can enable secure positioning, but also that this requires solving a set of relevant physical- and logical- layer challenges. Finally I will present a design and implementation of an IR UWB secure distance measurement (distance bounding) system that solves these challenges and enables secure distance measurement and secure positioning in IoT applications. Finally, I will review possible uses of positioning in security applications such as authentication and access control."

    - name:        Xenofontas Dimitropoulos 
      affiliation: UoC and FORTH, Greece
      title:       "ARTEMIS: Neutralizing BGP Hijacking within a Minute"
      bio:         "Xenofontas Dimitropoulos is an Assistant Professor at the University of Crete and Affiliated Researcher to the Foundation for Research and Technology Hellas (FORTH). He received a Ph.D. degree from the Georgia Institute of Technology. He presently leads the Internet Security, Privacy, and Intelligence Research (INSPIRE) Group. He has received grants from the European Research Council, the Marie Skłodowska-Curie Action, and the Fulbright Institute. His research focuses on Internet routing and Internet measurements and has won two best paper awards. He has served on the Program Committees of well-known conferences such as ACM SIGCOMM."
      abstract:    "BGP prefix hijacking is a critical threat to Internet organizations and users. Despite the availability of several defense approaches (ranging from RPKI to popular third-party services), none of them solves the problem adequately in practice. They suffer from: (i) lack of detection comprehensiveness, allowing sophisticated attackers to evade detection, (ii) limited accuracy, especially in the case of third-party detection, (iii) delayed verification and mitigation of incidents, reaching up to days, and (iv) lack of privacy and of flexibility in post-hijack counteractions, from the side of network operators. In this work, we propose ARTEMIS, a defense approach (a) based on accurate and fast detection operated by the AS itself, leveraging the pervasiveness of publicly available BGP monitoring services and their recent shift towards real-time streaming, thus (b) enabling flexible and fast mitigation of hijacking events. Compared to previous work, our approach combines characteristics desirable to network operators such as comprehensiveness, accuracy, speed, privacy, and flexibility. Finally, we show through real-world experiments that, with the ARTEMIS approach, prefix hijacking can be neutralized within a minute."


    - name:        Wolfgang Kellerer  
      affiliation: TUM, Germany
      title:       "How Flexible is Your Network? A Proposal to Quantify Flexibility in
                   Softwarized Networks"
      bio:         "Wolfgang Kellerer is a Full Professor with the Technical University of Munich (TUM), Germany, heading the Chair of Communication Networks at the Department of Electrical and Computer Engineering. Before, he was for over ten years with NTT DOCOMO's European Research Laboratories. His last position was head of the research department for wireless communication and mobile networking. His current research focuses on flexible networking based on SDN/NFV and wireless M2M networking towards 5G. He received his Dr.-Ing. degree (Ph.D.) and his Dipl.-Ing. degree (Master) from TUM, in 1995 and 2002, respectively. His research resulted in over 200 publications and 35 granted patents. In 2015, he has been awarded with a Consolidator Grant from the European Commission for his project FlexNets: \"Quantifying Flexibility in Communication Networks\". He is a member of ACM, VDE ITG and a Senior Member of IEEE."
      abstract:    "Empowering flexibility is a common objective of softwarized networks based on concepts such as Network Virtualization, Software Defined Networking and Network Function Virtualization. Up to now, flexibility is mainly used as a qualitative advantage for a certain design choice. Moreover, the meaning of flexibility in such qualitative argument is highly varying in the literature since a common understanding of flexibility is missing. In this talk, an approach towards defining flexibility and a proposal for a quantifying measure are presented. Based on this measure, different network designs can be analyzed and compared quantitatively. In our proposal, we refer to flexibility as the timely ability to support new requests that can be, e.g., changes in the requirements or new traffic distributions. Use case studies illustrate how an application of such measure could lead to a better understanding of flexibility. With our proposed flexibility measure, we would like to stimulate the discussion towards a more quantitative analysis of softwarized networks and beyond."



    - name:        Dejan Kostic
      affiliation: KTH, Sweden
      title:       "Metron: NFV Service Chains at the True Speed of the Underlying Hardware"
      bio:         "Dejan Kostic obtained his Ph.D. In Computer Science at the Duke University. He spent the last two years of his studies and a brief stay as a postdoctoral scholar at the University of California, San Diego. He received his Master of Science degree in Computer Science from the University of Texas at Dallas, and his Bachelor of Science degree in Computer Engineering and Information Technology from the University of Belgrade (ETF), Serbia. From 2006 until 2012 he worked as a tenure-track Assistant Professor at the School of Computer and Communications Sciences at EPFL (Ecole Polytechnique Federale de Lausanne), Switzerland. In 2010, he received a European Research Council (ERC) Starting Investigator Award. From 2012 until June 2014, he worked at the IMDEA Networks Institute (Madrid, Spain) as a Research Associate Professor with tenure. He is a Professor of Internetworking at KTH since April 2014. In 2017, he received a European Research Council (ERC) Consolidator Award."
      abstract:    "We present Metron, a Network Functions Virtualization (NFV) platform that achieves high resource utilization by jointly exploiting the underlying network and commodity servers¹ resources. This synergy allows Metron to: (i) offload part of the packet processing logic to the network, (ii) use smart tagging to setup and exploit the affinity of traffic classes, and (iii) use tag-based hardware dispatching to carry out the remaining packet processing at the speed of the servers¹ fastest cache(s), with zero intercore communication. Metron also introduces a novel resource allocation scheme that minimizes the resource allocation overhead for large-scale NFV deployments. With commodity hardware assistance, Metron deeply inspects traffic at 40 Gbps and realizes stateful network functions at the speed of a 100 GbE network card on a single server. Metron has 2.75-6.5x better efficiency than OpenBox, a state of the art NFV system, while ensuring key requirements such as elasticity, fine-grained load balancing, and flexible traffic steering."
       
 
      
    - name:        Angel Lozano 
      affiliation: UPF, Spain
      title:       "Post-Cellular Wireless Networks"
      bio:         "Angel Lozano is a Professor of Information & Communication Technologies at UPF (Universitat Pompeu Fabra). He received the Ph.D. in Electrical Engineering from Stanford University in 1999, worked for Bell Labs (Lucent Technologies, now Nokia) between 1999 and 2008, and served as Adj. Associate Professor of Electrical Engineering at Columbia University between 2005 and 2008. Prof. Lozano is a Fellow of the IEEE and a Highly Cited Author. He has held multiple editorial positions and is actively involved in committees and conference organization tasks for the IEEE. His papers have received several awards, including the 2009 Stephen O. Rice prize to the best paper published in the IEEE Transactions on Communications, the 2016 Fred W. Ellersick prize to the best paper published in the IEEE Communications Magazine, and the 2016 Communications Society & Information Theory Society joint paper award. He holds 15 patens and is also the recipient of an ERC Advanced Grant for the period 2016-2021."
      abstract:    "Wireless traffic grows relentlessly, poised to increase to truly staggering levels. There is a fledging awareness that this challenge can only be fended off by a process of network massification, with two views about it. In a first view, densification is the only strategy through which dramatic improvements can be attained hereafter; this leads to a vision where base stations become tiny and exceedingly abundant. A second view is built on the idea of dramatically scaling the number of colocated antennas per base station, from the current handful to possibly hundreds. Since neither form of massification can by itself resolve the challenge facing wireless systems, the two forms will have to end up coexisting. Reconciling these two forms of massification and enabling a truly phenomenal scaling calls for an entirely new architecture where cells and physical base stations become things of the past, replaced by dynamically defined virtual base stations. The signal processing needs to shift away from base stations, which become deconstructed, so as to gather at new places. In this talk, we discuss the implications of this leap in the evolution of wireless networks, and the research challenges that it poses."
      
    - name:        Adrian Perrig 
      affiliation: ETH, Switzerland 
      title:       "A Next-generation Secure Internet for the 21st Century"
      bio:        "Adrian Perrig is a Professor at the Department of Computer Science at ETH Zürich, Switzerland, where he leads the network security group. He is also a Distinguished Fellow at CyLab, and an Adjunct Professor of Electrical and Computer Engineering, and Engineering and Public Policy at Carnegie Mellon University. From 2002 to 2012, he was a Professor of Electrical and Computer Engineering, Engineering and Public Policy, and Computer Science (courtesy) at Carnegie Mellon University, becoming Full Professor in 2009. From 2007 to 2012, he served as the technical director for Carnegie Mellon's Cybersecurity Laboratory (CyLab). He earned his MS and PhD degrees in Computer Science from Carnegie Mellon University, and spent three years during his PhD at the University of California at Berkeley. He received his BSc degree in Computer Engineering from EPFL. Adrian's research revolves around building secure systems -- in particular his group is working on the SCION secure Internet architecture.<br/>He is a recipient of the NSF CAREER award in 2004, IBM faculty fellowships in 2004 and 2005, the Sloan research fellowship in 2006, the Security 7 award in the category of education by the Information Security Magazine in 2009, the Benjamin Richard Teare teaching award in 2011, the ACM SIGSAC Outstanding Innovation Award in 2013. He is an IEEE senior member and became an ACM Fellow in 2017."
      abstract:   "The Internet has been successful beyond even the most optimistic expectations. It permeates and intertwines with almost all aspects of our society and economy. The success of the Internet has created a dependency on communication as many of the processes underpinning the foundations of modern society would grind to a halt should communication become unavailable. However, much to our dismay, the current state of safety and availability of the Internet is far from commensurate given its importance.<br/>Although we cannot conclusively determine what the impact of a 1-day, or 1-week outage of Internet connectivity on our society would be, anecdotal evidence indicates that even short outages have a profound negative impact on society, businesses, and government. Unfortunately, the Internet has not been designed for high availability in the face of malicious actions by adversaries. Recent patches to improve Internet security and availability  have been constrained by the current Internet architecture, business models, and legal aspects. Moreover, there are fundamental design decisions of the current Internet that inherently complicate secure operation.<br/>Given the diverse nature of constituents in today's Internet, another important challenge is how to scale authentication of entities (e.g., AS  ownership for routing, name servers for DNS, or domains for TLS) to a global environment. Currently prevalent PKI models (monopoly and oligarchy) do not scale globally because mutually distrusting entities cannot agree on a single trust root, and because everyday users cannot evaluate the trustworthiness of each of the many root CAs in their browsers.<br/> To address these issues, we propose SCION, a next-generation Internet architecture that is secure, available, and offers privacy by design; that provides incentives for a transition to the new architecture; and that considers economic and policy issues at the design stage. We have implemented SCION and deployed it in the production networks of 2 ISPs."

    - name:        Costin Raiciu
      affiliation: UPB, Romania
      title:       Network Verification without Policy Specification
      bio:         "Costin Raiciu is Associate Professor at University Politehnica of Bucharest where he leads the Netsys group. Costin finished his PhD at UCL in 2011. His current research focus is on network verification. In his past work, Costin was one of the main people behind the development, implementation and standardization of Multipath TCP, a protocol that is now deployed by Apple and Samsung on their mobile devices. Recently, Costin worked on NDP, which is a radical redesign of the datacenter networking stack (Sigcomm 2017)."
      abstract:    "Networks are critical components of our society; when they fail, they cause massive disruption. Network verification analyzes snapshots of network data planes to decide if the network as a whole behaves according to some predefined policy. Despite massive advances in network verification recently, specifying the policy a network should obbey is far from easy, and this is one of the resons why network verificaiton has not been adopted widely. <br/>In this work we will discuss how one can verify certain forms of network correctness without requiring explicit policies. In both approaches, our aim is to find behaviours that are obviously wrong, and flag them to the user:<br/>1. Verifying P4 programs: we show how we can use exhaustive symbolic execution to find memory bugs, encapsulation and decapsulation bugs, implicit processing, parser problems in all the P4 programs that are available publicly, with modest runtimes.<br/>2. Equivalence: in many cases, two dataplane programs are meant to behave similarly. For instance, an abstract network configuration is specified by tenants in datacenters (e.g. in Openstack) and the cloud software translates this to a dataplane configuration that is deployed (e.g. via Openflow and iptables rules). We show how we can automatically check the equivalence of two network data planes, and how we have used this approach to find several bugs in Neutron, Openstack¹s networking driver."

    - name:        Georgios Smaragdakis
      affiliation: TU Berlin, Germany and MIT, USA
      title:       Deep Dive into BGP Communities
      bio:         "Georgios Smaragdakis is a Professor with Technical University (TU) Berlin, a research affiliate with the Massachusetts Institute of Technology (MIT) Computer Science and Artificial Intelligent Laboratory (CSAIL) and the MIT Internet Policy Research Initiative (IPRI), and a research collaborator with Akamai Technologies. From 2014-2017 he was a Marie Curie fellow at the MIT CSAIL. From 2008-2014 he acted as Senior Researcher at Deutsche Telekom Laboratories and the Technical University of Berlin. In 2008 he was a research intern at Telefonica Research. He earned the Ph.D. degree in Computer Science from Boston University in 2009 and the Diploma in Electronic and Computer Engineering from the Technical University of Crete. His research interests include the measurement, performance analysis, and optimization of content distribution systems on the Internet, as well as economic, peering, resilience, collaboration, and policy aspects of content delivery, and Internet, Web, and content delivery analytics. George's research was awarded a European Research Council Starting Grant Award (2015), a Marie Curie International Outgoing Fellowship (2013), and best paper awards at IEEE INFOCOM (2017), ACM IMC (2016 and 2011) and ACM CoNEXT (2015)."
      abstract:    "Today, our economy as well as our social life, rely on the smooth and uninterrupted operation of the Internet. To cope with the increasing complexity of inter-networking, network operators rely on advanced traffic engineering techniques, such as BGP communities, i.e., meta-information regarding prefix announcements. In this talk, I show that, indeed, the use of BGP communities is on the rise, but more importantly, it provides an excellent, yet unexplored, source of information to assess the state and health of the Internet. In particular, I show how we utilized BGP communities as a crowd-sourcing mechanism to: (i) detect outages at critical peering infrastructures and pinpoint the epicenter of the outage at the level of a building, (ii) detect mitigation of distributed denial of service, and (iii) infer network policies and assess the level of collaboration among networks. I conclude my talk by presenting shortcomings of the use of BGP communities and suggest ways to overcome them via better coordination of all the involved stakeholders."


      
    - name:        Klaus Wehrle
      affiliation: RWTH, Germany
      title:       Symbolic Analysis of Software-based Communication Systems
      bio:         "Klaus Wehrle is professor of Computer Science and head of the Chair of Communication and Distributed Systems at RWTH Aachen University, Germany. He received his Diploma and PhD degrees from University of Karlsruhe (now KIT). From 2002 till 2003, Klaus was postdoctoral researcher at the International Computer Science Institute at University of California at Berkeley. In 2004 he was awarded a DFG Emmy Noether (starting) grant and established a junior research group on Protocol Engineering and Distributed Systems at University of Tübingen. In 2006, he joined RWTH Aachen University as associate professor, since 2010 as full professor. His research activities are focused on (but not limited to) engineering of networking protocols, (formal) methods for protocol engineering and network analysis, network simulation, reliable communication software as well as all operating system issues of networking."
      abstract:    "The softwarization of networks provides a new degree of flexibility in network operation. But its software components can result in unexpected runtime performance and erratic network behavior. This challenges the deployment of flexible software functions, so-called Network Functions (NF), in performance critical (core) networks.<br/>To address this challenge, we propose Symbolic Execution as a rigorous and effective methodology enabling a qualitative and quantitative analysis of Network Functions, before deployment.<br/>The talk shows how symbolic analysis methods can be applied in various aspects of networked systems, how the computational challenges can be tackled and that very insidious bugs can be discovered in widely used software."

    - name:        Joerg Widmer 
      affiliation: IMDEA, Spain 
      title:       Efficient Networking in Millimeter Wave Bands
      bio:         "Joerg Widmer is Research Professor as well as Research Director of IMDEA Networks in Madrid, Spain. His research focuses on wireless networks, ranging from extremely high frequency millimeter-wave communication and MAC layer design to mobile network architectures. From 2005 to 2010, he was manager of the Ubiquitous Networking Research Group at DOCOMO Euro-Labs in Munich, Germany, leading several projects in the area of mobile and cellular networks. Before, he worked as post-doctoral researcher at EPFL, Switzerland on ultra-wide band communication and network coding. He was a visiting researcher at the International Computer Science Institute in Berkeley, USA, University College London, UK, and TU Darmstadt, Germany. Joerg Widmer authored more than 150 conference and journal papers and three IETF RFCs, and holds 13 patents. He serves or served on the editorial board of IEEE Transactions on Mobile Computing, IEEE Transactions on Communications, Elsevier Computer Networks and the program committees of several major conferences. He was awarded an ERC consolidator grant, the Friedrich Wilhelm Bessel Research Award of the Alexander von Humboldt Foundation, Mercator Fellowship of the German Research Foundation, a Spanish Ramon y Cajal grant, as well as seven best paper awards. He is senior member of IEEE and ACM."
      abstract:    "State-of-the-art wireless communication already operates close to Shannon capacity and one of the most promising options to further increase data rates is to increase the communication bandwidth. Very high bandwidth channels are only available in the extremely high frequency part of the radio spectrum, the millimeter wave band (mm-wave). Upcoming communication technologies, such as IEEE 802.11ad, are already starting to exploit this part of the radio spectrum to achieve data rates of several GBit/s. However, communication at such high frequencies also suffers from high attenuation and signal absorption, often restricting communication to line-of-sight (LOS) scenarios and requiring the use of highly directional antennas. This in turn requires a radical rethinking of wireless network design. On the one hand side, such channels experience little interference, allowing for a high degree of spatial reuse and potentially simpler MAC and interference management mechanisms. On the other hand, such an environment is extremely dynamic and channels may appear and disappear over very short time intervals, in particular for mobile devices. It is essential to take these characteristics into account to turn a collection of such very high speed but brittle links into an efficient, low latency, and reliable network. This talk will highlight some of the challenges of and possible approaches for mm-wave networking."

      


---

# {{ page.title }}

### Overview
ERC Networking 2018 meets in Budapest on Friday, August 24, during the ACM
SIGCOMM 2018 conference. The symposium brings together researchers and
educators for the purpose of presenting and discussing research results and
ideas pertaining to projects funded by the European Research Council (ERC).
The ERC Networking program consists exclusively of invited talks by ERC
grant holders, with two types of presentation being envisaged:

(1) Exciting new ideas. Similar in style to ACM HotNets workshop talks,
these presentations are intended to generate lively discussions on research
topics of high interest. 

(2) ERC research results. Presentations of this kind report on results
obtained as part of ERC-funded projects.

The European Research Council (ERC) has a mission to encourage the
highest-quality research in Europe through competitive funding and to
support excellent science driven by individual investigators. Being
investigator-driven bottom-up in nature, the ERC approach encourages
researchers to identify promising directions and exciting opportunities. The
ERC Networking 2018 symposium pursues the following two goals: (i) promoting
excellent European research within, or closely related to, the area of
computer networking by exposing ERC-funded results and ideas and (ii)
inspiring talent in computer networking from all over the world and
encouraging applications for ERC grants.

### Registration
Attendance of the symposium is by open registration and subject to the same
registration fees and rules as a regular SIGCOMM 2018 workshop. The
attendees who register for another SIGCOMM 2018 workshop on August 24 may
freely attend the ERC Networking symposium. Similarly, the registrants of
ERC Networking 2018 may freely attend the other workshops on August 24.

### Speakers
<span style="font-size:10pt">(click on the speaker’s name to see the talk title, abstract, and bio)</span>
{% include presenters.html presenters=page.presenters %}

### Important Dates

{% include dates2.html dates=page.dates %}


### Committees

{% include committees.html committees=page.committees %}

[Contact the Symposium Chairs](mailto:telma.CARVALHO@ec.europa.eu,sergey.gorinsky@imdea.org,fu@cs.uni-goettingen.de,jajszcz@agh.edu.pl,tapolcai@tmit.bme.hu,schapiram@cs.huji.ac.il?subject=[ERC Networking 2018]){: data-role="button" class="button" }