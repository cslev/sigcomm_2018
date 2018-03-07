---
layout: default
title: Social Events
group: Conference

events:
- id: welcome
  name: Welcome Reception
  <!-- date: Monday, August 21 -->
  <!-- time: 7:00pm - 9pm -->
  <!-- address: Centennial Terrace, Luskin Center -->
  <!-- image: images/hotels/ucla-luskin-conference.jpg -->

- id: n2women-dinner
  name: N2Women Dinner
  <!-- date: Monday, August 21 -->
  <!-- time: 8:00pm - 10:30pm -->
  <!-- address: Centennial Hall (Salon C/Salon D), Luskin Center -->
  <!-- image: images/hotels/ucla-luskin-conference.jpg -->
  <!-- note: N2Women dinner will be held on Monday, the night before the conference, in Centennial Hall (Salon C/Salon D) in Luskin Center. N2Women Dinner aims to foster the minority community within SIGCOMM, and make it easier for the under-represented attendees to fully participate in the conference. Attendees will have the opportunity to meet multiple senior members of the community from universities, research labs and industry. The dinner is open to everyone who identifies with any minority, not just women. Everyone who has received a confirmed seat at the dinner will find the N2Women dinner ticket issued along with their name tags at the SIGCOMM registration desk. -->

- id: conference-banquet
  name: Conference Banquet
  <!-- date: Tuesday, August 22 -->
  <!-- time: 6:30pm - 9:00pm -->
  <!-- address: Dickson Plaza North, UCLA Campus -->
  <!-- image: images/map_UCLA/banquet.jpg -->
  <!-- image_url: images/map_UCLA/banquet.jpg -->
  map: 
  
- id: student-dinner
  name: Student Dinner
  <!-- date: Wednesday, August 23 -->
  <!-- time: 6:30pm - 9:00pm -->
  <!-- address: Sunset Recreation Center, UCLA Campus -->
  <!-- image: images/map_UCLA/student_dinner.jpg -->
  <!-- image_url: images/map_UCLA/student_dinner.jpg -->
  map: 
---

# {{ page.title }}

In addition to the technical activities, SIGCOMM 2018 will organize the following social events:

{% for event in page.events %}
{% include event.html %}
{% endfor %}
