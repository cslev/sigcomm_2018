---
layout: default
title: Accommodations
group: Local Information

hotels:
- id: luskin
  name: TBA
  deadline: TBA
  rates: 
  amenities: 
  address: 
  url: 
  phone: 
  distance:
  reservation-info: 
---

# {{ page.title }}

<!-- The main conference venue is [UCLA Meyer and Renee Luskin Conference Center](http://luskinconferencecenter.ucla.edu/).
However, there are many other options for accommodation, including the Hotel Angeleno and AirBnB, available within walking distance, via hotel shuttle, or using public transportation.

<h2><b>Several rooms in Hotel Angeleno are still available. The conference cut off date is July 13, 2017!</b></h2>
-->
Below is a list of conference hotels:

{% for hotel in page.hotels %}
{% include hotel.html expanded=forloop.last %}
{% endfor %}

Note that the conference will provide breakfast and lunch.
