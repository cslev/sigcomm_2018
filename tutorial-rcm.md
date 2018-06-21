---
layout: default
title: "ACM SIGCOMM 2018 Afternoon Tutorial on Repeatability and Comparability in Measurement (RCM)"
group: Tutorials

dates:
    - info: Tutorial
      date: August 20, 2018
      
data:
  - type: day
    time: Monday, August 20, 2018
    room: TBA

committees:
    - role: Organizers
      people:
      - name:        Brian Trammell
        affiliation: ETH, Switzerland
      - name:        Korian Edeline
        affiliation: ULiège, Belgium
      - name:        Iain R. Learmonth
        affiliation: Aberdeen, UK
         

---

# {{ page.title }}

## Tutorial Program

{% include program-online.html type="rcm" %}

## Call For Participation
Repeatability of experiments and comparability of results is a cornerstone of the scientific method. This tutorial dives into the subject of repeatability and comparability in active Internet measurements. We begin with a brief introduction to a set of well-known measurement tools and platforms and examine two active measurement tools focused on a specific problem in Internet measurement: detecting and localizing impairments to feature deployment at layer 4. We then show how frameworks for handling metadata can contribute to repeatability, and how the systemization of normalization and successive data analysis can lead to better repeatability and comparability. This will be done using the MAMI Path Transparency Observatory, which implements this process for impairment measurement in the Internet.


## <i class="fa fa-calendar"></i> Important Dates

{% include dates2.html dates=page.dates %}


## Outline
Part 1: Introduction to active measurements of network performance and path transparency

Part 2: Path tracing with tracebox

Part 3: Measuring endpoint support and path transparency with PATHspider

Part 4: Data collection, preservation, and analysis using the Path Transparency Observatory (PTO)

## Audience Expectations and Prerequisites
Attendees must bring their own laptop. A virtual image will be provided that can be installed on
any machine that conforms to current standards. More detailed hardware requirements will be
provided to the attendees a couple of weeks before the tutorial. We expect general base knowledge about active measurement and Linux. 
However, no specialized knowledge about specific measurements is expected, and an introduction to the tools used will be provided in the tutorial.

## Background
Network measurement is a common tool for network research, either to directly gather knowledge
about network or traffic behavior in the wild or as a way to determine realistic input parameters for the evaluation of new proposed network and protocol mechanisms.

However, before the actual measurement study can be started, there are usually a lot of questions
to answer first and addition work to do: What is the goal of the measurement? Are the targets
representative of the research questions? Which tools should be uses? When and how often
should measurements be run? Which information should be captured? Which metadata needs to
be kept? And so on.

In many cases, people even start writing their own tools, based on the usually-incorrect
assumption that this is faster than becoming familiar with existing tooling. Utilizing the wide set of
available tools might not only be faster, it can also often provide better and more reliable results,
as e.g. additional metadata are automatically collected that might have given further insight about
potential impacting factors, and makes data more comparable between different campaigns.

This tutorial provides an introduction to a set of well-known measurement tools including basic
tools such as ping and traceroute, as available on all desktop operating systems and as provided
by the RIPE Atlas measurement network. We will focus on practical exercises with tracebox, an
extension to traceroute which also provides information about manipulation of packets along a
path; and PATHspider, which probes for connectivity and negotiation of optional protocol features
on a given path.

Performing these basic measurements is the first step in an Internet measurement campaign. 
The selection of tools and configurations used, and the definition of metadata related to that selection, is key to repeatability. 
The next step is pulling these measurements together so they can be
compared with other measurements at scale. The tutorial will therefore cover aspects of data
collection, preservation, and accessibility. It will examine the Path Transparency Observatory
(PTO) as one example for a data collection and analysis system that is designed to provide easy
access to comparable data that has been derived from different sources/tools and campaigns.
For the tracebox experimentation, we will use a virtual testbed composed of several networks that
each introduce different middlebox impairments on the traffic passing through. In addition, we will
deploy PATHspider on the same testbed to measure endpoint as well network support of various
protocols or protocol features; as well as on the open Internet, to demonstrate the use in a largescale set-up. 
Finally, we will normalize and analyze the raw results with the help of the framework provided by the PTO, whereby results from different vantage points can be consolidated and higher-level conclusions can be drawn about the targets and features being measured.

## Organizers

{% include committees.html committees=page.committees %}
