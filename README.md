<h1> GuideXP Landing Page (2019 S2) </h1>

<h2><a name = "content"> Contents </a></h2>
<a href = "#Title1"><b> 1. Project Description </b></a><br/>
<a href = "#Title2"><b> 2. Outputs </b></a><br/>
<a href = "#Title3"><b> 3. How to use </b></a><br/>
<a href = "#Title4"><b> 4. Stakeholders </b></a><br/>
<a href = "#Title5"><b> 5. Team Roles and Management </b></a><br/>
<a href = "#Title6"><b> 6. Prototypes </b></a><br/>
<a href = "#Title7"><b> 7. Schedule </b></a><br/>
<a href = "#Title9"><b> 8. Links Summary</b></a><br/>

<br />
<h2><a name = "Title1"> 1. Project Description </a></h2>

The [GuideXP](https://guidexp.wordpress.com) is a local startup in Canberra with the vision of creating immersive visitor experiences for galleries, museums and more. GuideXP is a unique, cloud-based approach to audio guides, which allows for access to content from multiple attractions in one place and aims to minimise effort required in uploading and updating content.
In 2019, GuideXP is partnering with the ANU TechLauncher program to kick start our development. The program will enable us to create a first stage of our product roadmap while engaging with students and providing them real world experience.
We are currently seeking a partner institution to create or share visitor experience content and provide us with feedback as we develop the minimum viable product and test our value propositions. The partner institution will benefit from free use of the service for the duration of 2019.
The GuideXP Team consists of four members plus the our ANU TechLauncher team (TBC), with a myriad of experience in tech delivery projects, startups, and visitor experience. We are motivated and excited by the prospect of working with a renowned institution such as the National Capital Exhibition.


<br />
<h2><a name = "Title2"> 2. Outputs </a></h2>

**The Systems We Developed last semester**

As our client required, our source code is not open to the public. You need to use the GitHub account we provided to view the source code. We have provided this account in our audit presentation. We also sent an email that includes this account to tutors, examiners and shadow team. If you didn't get the account, please [open an issue](https://github.com/DannyFirmin/GuideXP/issues) in this repository and leave your email address, we will send it to you as soon as possible. We do apologise to the inconvenience.

* Visitor System:  
  * Deployed Address: http://new.guidexp.me/
  * [Source Code](https://github.com/DannyFirmin/guidexp.me)
  * JavaScript
  * Html/CSS
  * Bootstrap
* Administrator System: 
  * Deployed Address: http://admin.guidexp.me/
  * [Source Code](https://github.com/LiangHong95/django)
  * Django
  * Django REST framework
  * MySQL
  * Bootstrap
* API:
  * Return all exhibitions as JSON: http://admin.guidexp.me/api/exhibition/
  * Return the art's collection as JSON: http://admin.guidexp.me/api/exhibition/ExhibitionTest/
* Servers:
  * Configured Amazon Web Services (AWS) - Elastic Compute Cloud (EC2)
  * Configured Crazy Domains AU for DNS and domains
  * Configured nginx/uWSGI/Ubuntu

**The output for this semester**

This semester we will customize our system to support National Capital Exhibition.


* Statement of work
* Meeting minutes
* Decision log
* team activities
* investigation in National Capital Exhibition
* relfection 
* design of website



<br />
<h2><a name = "Title3"> 3. How to use </a></h2>

**For visitors**
* Homepage:
![Homepage](/week10/Homepage.png)<br/>
Visitors can select what they want to know through the navigation.
* Arts in an exhibition (test):
![Arts](/week10/artsinaexhi.png)<br/>
* Audio and text (test):
![Audio](/week10/Audioandtext.png)<br/>
Visitors can listen the audio about the art.
* Artists:
![Artists](/week10/Artist.png)<br/>
Visitors can know about the artists.

**For creaters and administrators**
* How to login:
![Howtologin](/week10/howtologin.png)<br/>
If the administrator have not signed in, then he or she will enter in the login page when press the two buttons. However, if the adminsitrator have signed in, then he or she will enter in the manage system when press the upload button.
* Login page:
![Loginpage](/week10/loginpage.png)<br/>
The account can only be provided by administrators, in case that anyone can log in and upload non-related files.
* Create new art:
![Createart](/week10/createnewart.png)<br/>
The creaters can create and upload new art and descriptions.
* Create new account:
![Createnewaccount](/week10/createnewaccount.png)<br/>
* Different type of account:
![Worker](/week10/worker.png)<br/>
![Cantcreate](/week10/cantcreateaccount.png)<br/>
If your account type is worker, then you cannot create other accounts.
<h2><a name = "Title4"> 4. Stakeholders </a></h2>

Visitors, Content creaters, galleries and museums

<br />


<h2><a name = "Title5"> 5. Team Roles and Management </a></h2>

**Roles**

| Team Member                      | Role                                     | 
|----------------------------------|------------------------------------------| 
| Kelin Zhu                        | Project manager                          | 
| Rutai Sun                        | Back-end(logic,algorithm)                | 
| Liang Hong                       | Back-end(database,test)                  |
| Yu Qiu                           | Back-end, API                            | 
| Yuanze Niu                       | Front-end (HTML,CSS), Documentation      | 
| Danny Feng                       | Front-end (HTML,CSS), Documentation      | 
| Yu Qiu                           | Back-end, API                            | 
| Tianai Qiu                       | Front-end (HTML,CSS), Documentation      |             

**Agile Tasks Assignment and User Stories**

[Trello](https://trello.com/b/ggidOa5S/guidexp-user-stories) <br />
![Trello](https://github.com/LiangHong95/GuideXP-S2/blob/master/trello.png)<br/>


**Team Communication**

Team meetings <br />
Team activities <br />
Slack <br />
Meeting Minutes <br />
<br />

<h2><a name = "Title6"> 6. Prototypes </a></h2>

[GUI Interaction](https://marvelapp.com/317d466/screen/33853357) <br />
[Wordpress](http://www.guidexp.me/) <br />

<h2><a name = "Title7"> 7. Schedule </a></h2>

**Schedule:**

|Period            |    Milestones                                                                                | 
|------------------|----------------------------------------------------------------------------------------------| 
|Week2 - Week3     |Discovery report                                                                              |
|Week4 - Week5     |Optimize existing system to support new requirements                                          |
|Week6 - Week7     |Build a prototype guide with several example exhibitions from the National Capital Exhibition |
|Week8 - Week9     |IImprove the website pattern & add all the data                                               |
|Week10 - Week11   |Add multi-language supporting function                                                        |  
|Week12            |Test, debug and gather feedback from clients and pass onto our clients                        |

<br />

**Milestones:**

| Phase          |    Milestones                                                                               | 
|----------------|---------------------------------------------------------------------------------------------| 
| Phase 1        |Discovery report                                                                             |
| Phase 2        |Database construction and webpage functions.                                                 |
| Phase 3        |Useable prototype guide of several example exhibitions from the National Capital Exhibition  |
| Phase 4        |Improved guide for the National Capital Exhibition with provided exhibition data             |
| Phase 5        |Website supports multi-language                                                              |  
| Phase 6        |Test the website and pass to clients                                                         |

<br />


<h2><a name = "Title9"> 8. Links Summary </a></h2>

* [GuideXP Previous Landing Page](https://github.com/DannyFirmin/GuideXP)
* [GuideXP Vistor System](http://new.guidexp.me/)
* [GuideXP Admin System](http://admin.guidexp.me/)
* [GuideXP API](http://admin.guidexp.me/api/exhibition/)

We will offer shadow team members, tutors and examiners premission to access the following contents in the first audit

* [GuideXP Agile Board (Trello)](https://trello.com/b/ggidOa5S/guidexp-user-stories) (NEED PERMISSION)
* [GuideXP Visitor System Git-repo](https://github.com/DannyFirmin/guidexp.me) (NEED PERMISSION)
* [GuideXP Admin System Git-repo](https://github.com/LiangHong95/django) (NEED PERMISSION)

