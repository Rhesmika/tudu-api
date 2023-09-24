<img width="475" alt="image" src="https://github.com/Rhesmika/tudu-api/assets/100621349/37f7550e-9d59-4a3e-8ac7-e72f830d0e65"># Tudu - Back End - API

Tudu is a task management website where users can catagorise, track and update their tasks.Tudu hopes to help users to bring digital organisation to their lives. 

The goal is to ensure users can:
- Signup/Login and view data that only they can see
- View all their boards
- View all their tasks
- Create Boards
- Create Tasks (and have them assigned to the board)
- Edit their Board name
- Edit and update their Task details
- Delete Boards
- Delete Tasks

The API provides the website (and user) to manager all the above. The front end website required the API to manage sorting and storing the users data correctly and as intended. It also gives access to filtering and ordering to users data. 

### Deployed Tudu 
+  Front End: https://tudu-fe.herokuapp.com/
+  Back End: https://tudu.herokuapp.com/

### User Stories for Development 
The development of the website was managed by user stories to track the progress. Here are the user stories used for the back end development. The user stories were tracked in a project on Github.
+ Create profiles Model
+ Profiles - List View (with filters available)
+ Profiles - Detail View
+ Profiles - Edit Profile
+ Create Task Model
+ Task - List View (with filters available)
+ Task - Detail View
+ Task - Delete Task
+ Task - Edit Task
+ Create Team Model
+ Teams - List View (with filters available)
+ Teams - Detail View
+ Teams - Delete Team
+ Teams - Edit Team
+ Create Board Model
+ Board - List View (with filters available)
+ Board - Detail View
+ Board - Delete Team
+ Board - Edit Board

To simplify the project, the teams were removed from the project and are considered to be a development oppertunity in the future. 

### Models
In planning for the api, the models were mapped externally. 
[Datafields.pdf](https://github.com/Rhesmika/tudu-api/files/12709630/Datafields.pdf)

The Task and Board are link via a foreign key. The development process of the models caused issues in the API. Testing occured throughout development,  and adding / removing Foreign keys meant the API database required to be reset. 
The Task model was constructed so that many tasks can be assigned to one board. This model collects all the information about a task including the title, desctiption, due date,, priority, status. The user can also include an attachment to their task which is stored in cloudinary.
The Board model was constructued so that many boards can be owned by a user. Tasks are assigned to a board which can be individually named for a better user experience. 
Profiles are automatically created upon user creation and have the ability to update the profile image automatically assigned. 
Teams was withdrawn from the project but has developmental oppertunities in the future. This model would allow for board and task collaboration and even task assignment 

### CRUD 
In planning for the API, the CRUD methods were mapped externally.  (Teams were removed from the pdf)
[crud tables.pdf](https://github.com/Rhesmika/tudu-api/files/12709647/crud.tables.pdf)
The CRUD abilities of the API means that the user will be able to view, edit and delete all their boards, all their tasks and edit their profiles. 

#### List Views
The API displays lists of all the models inputs and offers filtering. 

The Profile list view is accessed via "/profiles"
<img width="840" alt="Screenshot 2023-09-24 at 21 56 26" src="https://github.com/Rhesmika/tudu-api/assets/100621349/0accc7c1-2d28-41a7-af1d-c00ace5bc6b5">

Filtering available:
+ Ordering by owner
+ Search for username
<img width="895" alt="Screenshot 2023-09-24 at 22 01 20" src="https://github.com/Rhesmika/tudu-api/assets/100621349/d1e5324c-247a-4f1d-8b1c-a5aaa7e6d4b8">


The Board list view is accessed via "/boards"
<img width="496" alt="Screenshot 2023-09-24 at 21 56 53" src="https://github.com/Rhesmika/tudu-api/assets/100621349/226059bc-7cd5-46de-8851-f3d703beec9a">

Filtering available:
+ Ordering by Task count (how many tasks are assigned to the board) and title
+ Search for title 
<img width="896" alt="Screenshot 2023-09-24 at 22 01 57" src="https://github.com/Rhesmika/tudu-api/assets/100621349/f0286212-e359-4d02-b592-ad8472c6121b">


The Task list view is accessed via "/tasks"
<img width="922" alt="Screenshot 2023-09-24 at 21 58 17" src="https://github.com/Rhesmika/tudu-api/assets/100621349/f4ee3fee-eff7-48d9-acc7-297ec2f90664">

Filtering available:
+ Ordering by Priority, Status, duedate and title
+ Search for titles
+ +Field Filters for Board, Priority and Status
<img width="475" alt="image" src="https://github.com/Rhesmika/tudu-api/assets/100621349/63aebcf4-69bf-45c2-86eb-5a991ccb5136">


#### Detail Views
Each item submission for a profile, task and board can be accessed by adding the 'id' to the link.. ie
"/boards/1"  - this was set in the model's view.  The detail views allow the data to be accessed directly from the front end using 'get'.  
![Screenshot 2023-09-24 at 22 18 22](https://github.com/Rhesmika/tudu-api/assets/100621349/6f72b63e-e9e9-4584-8f7c-d7275ffd923f)
![Screenshot 2023-09-24 at 22 20 26](https://github.com/Rhesmika/tudu-api/assets/100621349/81e52c20-5e7a-49e5-99ef-c0d5badfbd85)
![Screenshot 2023-09-24 at 22 21 17](https://github.com/Rhesmika/tudu-api/assets/100621349/38302dd0-c421-43cf-bc9d-6ffa050e7677)
![Screenshot 2023-09-24 at 22 21 37](https://github.com/Rhesmika/tudu-api/assets/100621349/c0f47fee-210a-45cc-9800-33ba2181a7aa)
![Screenshot 2023-09-24 at 22 21 47](https://github.com/Rhesmika/tudu-api/assets/100621349/1d35081f-4d2c-4829-802f-42fe83ec1cc6)
![Screenshot 2023-09-24 at 22 21 25](https://github.com/Rhesmika/tudu-api/assets/100621349/75c1cd77-f71a-40e1-b73d-69de0afba76a)


