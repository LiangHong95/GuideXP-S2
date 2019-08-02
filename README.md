<h1> GuideXP-S2 </h1>

<h2><a name = "content"> Contents </a></h2>
<a href = "#Title1"><b> 1. Project Description </b></a><br/>
<a href = "#Title2"><b> 2. Outputs </b></a><br/>
<a href = "#Title3"><b> 3. How to use </b></a><br/>
<a href = "#Title4"><b> 4. Stakeholders </b></a><br/>
<a href = "#Title5"><b> 5. Team Roles and Management </b></a><br/>
<a href = "#Title6"><b> 6. Prototypes </b></a><br/>
<a href = "#Title7"><b> 7. Schedule </b></a><br/>
<a href = "#Title8"><b> 8. GuideXP Poster</b></a><br/>

<br />
<h2><a name = "Title1"> 1. Project Overview </a></h2>

The [GuideXP](https://guidexp.wordpress.com) is a local startup in Canberra with the vision of creating immersive visitor experiences for galleries, museums and more. GuideXP is a unique, cloud-based approach to audio guides, which allows for access to content from multiple attractions in one place and aims to minimise effort required in uploading and updating content.
In 2019, GuideXP is partnering with the ANU TechLauncher program to kick start our development. The program will enable us to create a first stage of our product roadmap while engaging with students and providing them real world experience.
We are currently seeking a partner institution to create or share visitor experience content and provide us with feedback as we develop the minimum viable product and test our value propositions. The partner institution will benefit from free use of the service for the duration of 2019.
The GuideXP Team consists of four members plus the our ANU TechLauncher team (TBC), with a myriad of experience in tech delivery projects, startups, and visitor experience. We are motivated and excited by the prospect of working with a renowned institution such as the Australian Parliament House.


<br />
<h2><a name = "Title2"> 2. Outputs </a></h2>

**The Systems We Developed**

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
| Rutai Sun                        | Product manager,back-end(logic,algorithm)| 
| Liang Hong                       | Back-end(database,test)                  | 
| Yuanze Niu                       | Front-end (HTML,CSS), Documentation      | 
| Danny Feng                       | Front-end (HTML,CSS), Documentation      | 
| Yu Qiu                           | Back-end, API                            | 

**Agile Tasks Assignment and User Stories**

[Trello](https://trello.com/b/ggidOa5S/guidexp-user-stories) <br />
![Trello](https://raw.githubusercontent.com/DannyFirmin/GuideXP/master/week10/Trello.png)<br/>


**Team Communication**

Slack <br />
Meeting Minutes are in each week's folder <br />
<br />

<h2><a name = "Title6"> 6. Prototypes </a></h2>

[GUI Interaction](https://marvelapp.com/317d466/screen/33853357) <br />
[Wordpress](http://www.guidexp.me/) <br />

<h2><a name = "Title7"> 7. Schedule </a></h2>

**Milestones:**

| Phase          |Period            |    Milestones                                                               | 
|----------------|------------------|-----------------------------------------------------------------------------| 
| Phase 1        |Week2 - Week3     |Discovery report                                                             |
| Phase 2        |Week4 - Week5     |Database construction                                                        |
| Phase 3        |Week6 - Week7     |Design the User Interface and logical function of the website                |
| Phase 4        |Week8 - Week9     |Implement the User Interface (UI)                                            |
| Phase 5        |Week10 - Week11   |Establish an Application Program Interface (API) which links UI and database |  
| Phase 6        |Week12            |Testing                                                                      |

<br />

<h2><a name = "Title8"> 8. GuideXP Poster </a></h2>
https://github.com/DannyFirmin/GuideXP/blob/master/GuideXP%20Poster.pdf<br/>
<br />


