---
layout: default
title: Paper Submission Requirements
group: Main conference
---

# {{ page.title }}
The ACM SIGCOMM 2018 conference seeks papers describing significant research contributions to the field of data communication networks and networked systems. SIGCOMM’18 takes a broad view of networking research. This includes new ideas relating to (but not limited to) mobile, wide-area, data-center, home, and enterprise networks using a variety of link technologies (wired, wireless, visual, and acoustic), as well as social networks and network architecture. It encompasses all aspects of networks and networked systems, including packet-processing hardware and software, virtualization, mobility, sensors, provisioning and resource management, performance, energy consumption, topology, robustness and security, measurement, diagnosis, verification, privacy, economics and evolution, interactions with applications, internet-of-things, novel applications of machine learning to networking, and usability of underlying networking technologies.


Paper submissions typically report novel results firmly substantiated by experimentation, simulation, or analysis. As an aid to the community, the SIGCOMM web site provides [useful advice](https://www.sigcomm.org/publish/hints-tips-and-guides/) to authors planning to submit to SIGCOMM conferences. 

To submit papers to the SIGCOMM 2018 conference, please carefully read the rest of this document which provides information regarding paper formatting, registration, anonymity, and other important issues relevant to your submission. 

Then use [the paper submission site](https://sigcomm18.hotcrp.com) to: 

- Register your paper by <span style="color:red">{{ site.data.dates.main-registration.date }} 11:59pm ET</span>.
- Submit your paper by <span style="color:red">{{ site.data.dates.main-submission.date }} 11:59pm ET</span>.

These are <span style="color:red">hard deadlines</span> and no extensions will be given.

## Paper Formatting
All submissions must obey the following formatting requirements. 

- Submit papers of no more than **<span style="color:red">twelve (12) single--spaced pages</span>**, including figures, tables, any appendices, etc., followed by as many pages as necessary for references. Papers whose non-reference content is longer than 12 pages will not be reviewed.
- Submit papers formatted for printing on Letter-sized (8.5” by 11”) paper. Paper text blocks must follow ACM guidelines: double-column, with each column 9.25” by 3.33”, 0.33” space between columns. Each column must use 10-point font or larger, and contain no more than 55 lines of text. 
- It is your responsibility to ensure that your submission satisfies the above requirements. If you are using LaTeX, you can make use of [this template for ACM conference proceedings](https://github.com/scyue/ccp-sigcomm18). Unlike the official template, it only includes example for conference proceedings.

Your goal as an author is to produce a clearly readable submission within the above constraints. Authors are strongly discouraged from violating the formatting requirements with the aim of including additional material: <span style="color:red">**submissions that violate the formatting requirements may not be reviewed**</span>. You can visually inspect a page-by-page report of your paper format using the same tool as the submission system via a separate [online form](https://www.sysnet.ucsd.edu/sigops/banal/index.php).

After the submission deadline, we will use the same tool to check the conformance of papers. The format checking tool uses heuristics and can make mistakes. The PC chairs will manually inspect and possibly reject those papers with evident format violations. 

Please make sure that your submitted paper satisfies the following:
- List the submission number and the number of pages in your paper in the author block, e.g., “Paper #N, 14 pages”, beneath your title. Registering your title, abstract, etc., will provide a paper submission number. Per the anonymity guidelines, remember to remove any author names.
- Provide an abstract of no more than 200 words.
- Number the pages.
- Submit papers in PDF (Portable Document Format) and ensure that they are compatible with Adobe Acrobat (English version). Other formats, including Postscript, will not be accepted. Avoid using non-standard fonts. The PC must be able to display and print your submission exactly as we receive it using only standard tools and printers, so we strongly suggest that you use only standard fonts that are embedded in the PDF file.
- Ensure that the paper prints well on black-and-white printers, not color printers. Pay particular attention to figures and graphs in the paper to ensure that they are legible without color. Explicitly using grayscale colors will provide best control over how graphs and figures will print on black-and-white printers.
- Ensure that labels and symbols used in graphs and figures are legible, including the font sizes of tick marks, axis labels, legends, etc.
- Limit the file size to less than 15 MB. Contact the PC chairs if you have a file larger than 15 MB.


## Paper Registration
[Registration](https://sigcomm18.hotcrp.com/) only requires submission of paper metadata: paper title and abstract, author names, affiliations, contact email addresses, topics matching the subject matter of the paper, track (experience or main), and conflicts with PC members. The paper itself does not need to be submitted at the registration deadline. However, the paper title and abstract submitted during registration must be complete - not placeholders - and correctly characterize the paper that will be submitted. Authors can change the wording of their titles and abstracts for submission, but their essence should not fundamentally change. The PC will use the information provided during registration as a basis for making review assignments.

Both authors and PC members provide PC conflict information. The PC will review paper conflicts to ensure the integrity of the reviewing process, adding conflicts where necessary. Broadly, we define conflict of interest with a PC member using the following principles:

1. You are currently employed at the same institution, have been previously employed at the same institution within the last 12 months, or are going to begin employment at the same institution.
2. You have a professional partnership as follows:
   * Past or present association as thesis advisor or advisee.
   * Collaboration on a project, publication, or grant proposal within the past 2 years (i.e., 2016 or later).

If there is no basis for PC conflicts provided by authors, those conflicts will be removed. Improperly identifying PC members as a conflict to avoid having an individual review your paper may lead to your paper being rejected. If you have concerns, please contact the PC chairs.


## Paper Anonymity
All submitted papers will be judged based on their quality and relevance through double-blind reviewing, where the identities of the authors are withheld from the reviewers. As an author, you are required to make a good-faith effort to preserve the anonymity of your submission, while at the same time allowing the reader to fully grasp the context of related past work, including your own. Common sense and careful writing will go a long way towards preserving anonymity. Minimally, please take the following steps when preparing your submission:

- Remove the names and affiliations of authors from the title page.
- Remove acknowledgment of identifying names and funding sources.
- Use care in naming your files. Source file names (e.g., “Alice-n-Bob.dvi”) are often embedded in the final output as readily accessible comments.
- Use care in referring to related work, particularly your own. Do not omit references to provide anonymity, as this leaves the reviewer unable to grasp the context. Instead, reference your past work in the third person, just as you would any other piece of related work by another author.

## Experience Papers
Unlike recent years, SIGCOMM 2018 does not have a separate experience track.  SIGCOMM 2018 incorporates experience papers in the main track, and welcomes experience papers that bring novel insights about the design, analysis, and evaluation of commercial or otherwise widely used deployment. At registration time, there will be a category for experience papers to allow authors to declare their paper as such. 

## Ethics Considerations
Authors must as part of the submission process attest that their work complies with all applicable ethical standards of their home institution(s), including, but not limited to privacy policies and policies on experiments involving humans. The PC takes a broad view of what constitutes an ethical concern, and authors agree to be available at any time during the review process to rapidly respond to queries from the PC chairs regarding ethical standards.

## Paper Novelty
Under no circumstances should authors submit previously published work, submit the same work simultaneously to multiple venues, or submit papers that plagiarize the work of other authors. Like other conferences and journals, SIGCOMM prohibits these practices and may take action against authors who have engaged in them. In some cases, the program committee may share information about submitted papers with other conference chairs and journal editors to ensure the integrity of papers under consideration. If the PC discovers a violation of these principles, sanctions may include, but are not limited to, contacting the institutions of the authors and publicizing the details of the case.

SIGCOMM will review extended versions of previously-published short preliminary papers (such as workshop papers) in accordance with published [SIGCOMM policy](https://www.sigcomm.org/about/policies/frequently-asked-questions-faq/) and the [ACM Plagiarism Policy](https://www.acm.org/publications/policies/plagiarism_policy).

## Paper Acceptance
The SIGCOMM 2018 PC will notify authors of acceptance/rejection decisions by May 11, 2018. All accepted papers may be shepherded by members of the PC. Authors of accepted papers should plan to interact with their shepherds immediately after notification, and to budget sufficient time between acceptance notification and the camera-ready deadline to coordinate with their shepherd. It is a requirement that the paper be considered acceptable to the assigned shepherd so that the updates to the paper reflect the issues raised by the PC (conflicts will be mediated by the PC chairs) before the paper is considered “accepted” to appear in the conference proceedings. In addition, the publisher of the SIGCOMM proceedings will review all accepted papers submitted for the camera-ready deadline. Authors should also budget sufficient time immediately after the camera-ready deadline to be available and responsive to any editing changes requested by the publisher.

After acceptance, substantive changes to paper titles require approval by the PC chairs. Only in exceptional circumstances should authors change their author list, and only with the approval of the PC chairs.

Authors of accepted papers will also need to sign an ACM copyright release form. All rejected papers will be treated as permanently confidential.

[Contact the PC chairs](mailto:dina@csail.mit.edu,m.handley@cs.ucl.ac.uk?subject=[SIGCOMM 2018]){: data-role="button" class="button" }