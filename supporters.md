---
layout: default
title: Supporters
---

# {{ page.title }}

<!--
<p>
<div class="ui-corner-all custom-corners">
<div class="ui-bar ui-bar-a" markdown="1">
### Host
</div>

<div class="ui-body ui-body-a" markdown="1">
<div style="text-align: center;">
{% for supporter in site.data.supporters
%}{% if supporter[7] == "host"
%}<a href="{{ supporter[2] }}"><img src="{{ site.baseurl }}/images/sponsors/{{ supporter[1] }}" alt="{{ supporter[3] }}" style="height: 150px; margin: 10px" /></a>
{% endif
%}{% endfor %}
</div>
</div>
</div>
-->

<p>
<div class="ui-corner-all custom-corners">
<div class="ui-bar ui-bar-a" markdown="1">
### Platinum
</div>

<div class="ui-body ui-body-a" markdown="1">
- Brief airtime at special event
- Designated special event support
- Designated lunch or coffee break
- Recruitment of exhibit table
- Small display space for brochures or flyers
- Three company-provided promotion items in each tote-bag.
- May supply giveaways or swags.
- 4 conference registrations included.

<!-- Current Sponsors: -->

<div style="text-align: center;">
{% for supporter in site.data.supporters
%}{% if supporter[7] == "platinum"
%}<a href="{{ supporter[2] }}"><img src="{{ site.baseurl }}/images/sponsors/{{ supporter[1] }}" alt="{{ supporter[3] }}" style="height: 100px; margin: 10px" /></a>
{% endif
%}{% endfor %}
</div>
</div>
</div>

</p>

<p>
<div class="ui-corner-all custom-corners">
<div class="ui-bar ui-bar-a" markdown="1">
### Gold
</div>

<div class="ui-body ui-body-a" markdown="1">
- Designated lunch or coffee break
- Recruitment of exhibit table
- Small display space for brochures or flyers
- Two company-provided promotion items in each tote bag.
- May supply giveaways or swags.
- 3 conference registrations included.

<div style="text-align: center;">
{% for supporter in site.data.supporters
%}{% if supporter[7] == "gold"
%}<a href="{{ supporter[2] }}"><img src="{{ site.baseurl }}/images/sponsors/{{ supporter[1] }}" alt="{{ supporter[3] }}" style="height: 90px; margin: 10px" /></a>
{% endif
%}{% endfor %}
</div>
</div>
</div>

</p>

<!-- Current Sponsors: -->

<p>
<div class="ui-corner-all custom-corners">
<div class="ui-bar ui-bar-a" markdown="1">
### Silver

</div>

<div class="ui-body ui-body-a" markdown="1">
- Designated lunch or coffee break
- Recruitment of exhibit table
- Small display space for brochures or flyers
- One company-provided promotion item in each tote bag
- May supply giveaways or swags
- 2 conference registration included

<div style="text-align: center;">
{% for supporter in site.data.supporters
%}{% if supporter[7] == "silver"
%}<a href="{{ supporter[2] }}"><img src="{{ site.baseurl }}/images/sponsors/{{ supporter[1] }}" alt="{{ supporter[3] }}" style="height: 90px; margin: 10px" /></a>
{% endif
%}{% endfor %}
</div>
</div>
</div>

</p>

<!-- Current Sponsors: -->

<p>
<div class="ui-corner-all custom-corners">
<div class="ui-bar ui-bar-a" markdown="1">
### Bronze

</div>

<div class="ui-body ui-body-a" markdown="1">
- Logo or name visibility (web, print, email, on-site)
- May supply giveaways or swags
- 1 conference registration included

<div style="text-align: center;">
{% for supporter in site.data.supporters
%}{% if supporter[7] == "bronze"
%}<a href="{{ supporter[2] }}"><img src="{{ site.baseurl }}/images/sponsors/{{ supporter[1] }}" alt="{{ supporter[3] }}" style="height: 90px; margin: 10px" /></a>
{% endif
%}{% endfor %}
</div>
</div>
</div>

</p>


