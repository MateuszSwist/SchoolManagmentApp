# SchoolManagmentApp

Welcome to the School Management App, a web application designed to streamline and manage various aspects of educational institutions. This project is built using a powerful stack of technologies, ensuring a robust and efficient solution.

[![AWS RDS](https://img.shields.io/badge/AWS%20RDS-Cloud-orange)](https://aws.amazon.com/rds/) [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-orange)](https://www.postgresql.org/) [![Django](https://img.shields.io/badge/Django-Backend-blue)](https://www.djangoproject.com/) [![Python](https://img.shields.io/badge/Python-Backend-blue)](https://www.python.org/) [![HTML5](https://img.shields.io/badge/HTML5-Frontend-yellow)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) [![CSS](https://img.shields.io/badge/CSS3-Frontend-yellow)](https://developer.mozilla.org/en-US/docs/Web/CSS) [![JavaScript](https://img.shields.io/badge/JavaScript-Frontend-yellow)](https://developer.mozilla.org/en-US/docs/Web/JavaScript) [![Bootstrap](https://img.shields.io/badge/Bootstrap-Frontend-yellow)](https://getbootstrap.com/) 

![Home page](https://github.com/Mrokus95/SchoolManagmentApp/assets/59625513/d3abdfbe-1bf6-4752-bf9a-1a2e36fb742b)

## Table of contents
* [Installation process](#installation-process)
* [Technologies](#technologies)
* [Tests](#tests)
* [Features](#features)
* [About authors](#authors)


## Installation process:

1. Clone the repository to your local computer:

    ```
    $ git clone 'https://github.com/Mrokus95/SchoolManagmentApp.git'
    ```

2. Navigate to the project directory:

    ```
    $ cd SchoolManagmentApp
    ```

3. (Optional) It is recommended to create and activate a Python virtual environment:

    ```
    $ python -m venv venv
    $ python venv/bin/activate
    ```

4. Install the required dependencies:

    ```
    $ pip install -r requirements.txt
    ```

5. Set the environment variables:

    **General Django settings:**
    - `SECRET_KEY`: Django secret key (automatically generated when creating a Django project)
    - `DEBUG`: True

    **AWS RDS settings:**
    - `NAME`: The database name.
    - `USER`: The username that you configured for your database.
    - `PASSWORD`: The password that you configured for your database.
    - `HOST`: The hostname of the DB instance.
    - `PORT`: The port where the DB instance accepts connections. The default value varies among DB engines.

    **Gmail account credentials:**
    - `EMAIL_HOST_USER`: The email address
    - `EMAIL_HOST_PASSWORD`: The key or password app

    **Gmail SMTP settings:**
    - `EMAIL_HOST`: 'smtp.gmail.com'
    - `EMAIL_USE_TLS`: True
    - `EMAIL_PORT`: 587

    You can set the environment variables on your operating system or place them in a .env file in the project's root directory.

6. Run the Django development server:

    ```
    $ python manage.py runserver
    ```

    The application will be available at http://localhost:8000/.

## Technologies

We have utilized a diverse range of technologies to develop the School Management App, ensuring its functionality, scalability, and efficiency.

### AWS RDS (Amazon Relational Database Service) <img src="https://github.com/Mrokus95/SchoolManagmentApp/assets/59625513/93a6776b-0dfb-4d21-8cb7-15af08644212" alt="aws rds" width="25px" height="25px">


We integrated AWS RDS to host our database in the Amazon cloud. This allowed us to work collaboratively on the same dataset while gaining experience in cloud-based services integration. The use of Amazon RDS enables efficient and reliable data storage.

### PostgreSQL Database <img src="https://github.com/Mrokus95/SchoolManagmentApp/assets/59625513/017d3d41-b9bd-4c05-b5c7-8cd1e32e5efc" alt="postgreSQL" width="30px" height="30px">

To surpass the limitations of SQLite and enhance our relational database capabilities, we migrated to PostgreSQL. This allowed us to work with larger datasets and practice handling more complex database interactions. 

### HTML5, CSS, JS, and Bootstrap <img src="https://github.com/Mrokus95/SchoolManagmentApp/assets/59625513/78447f01-ef70-44ce-b7d7-e10729e3c4a0" alt="html5-logo png" width="25px" height="25px"><img src="https://github.com/Mrokus95/SchoolManagmentApp/assets/59625513/be020416-3f50-4d2b-a3e0-85847c5e3312" alt="css3" width="25px" height="25px"><img src="https://github.com/Mrokus95/SchoolManagmentApp/assets/59625513/0c875413-b287-4950-8d9f-d4daeb87346f" alt="js" width="25px" height="25px"><img src="https://github.com/Mrokus95/SchoolManagmentApp/assets/59625513/16bd8ee7-c4b9-4125-a6c1-34aeeb83c5d0" alt="bootstrap" width="25px" height="25px">


For the frontend, we leveraged HTML5, CSS3, JavaScript, and Bootstrap5. These technologies collectively allowed us to design and develop a responsive, user-friendly, and visually appealing user interface.

### Python and Django <img src="https://github.com/Mrokus95/SchoolManagmentApp/assets/59625513/b82413c4-2b4c-4c82-a06d-b0ba5cdeebfe" alt="python" width="25px" height="25px"> <img src="https://github.com/Mrokus95/SchoolManagmentApp/assets/59625513/6cb9996c-5ab0-4797-a422-1c8894d2b7de" alt="django" width="30px" height="30px">



The backend of the project was developed using Python 3.12 and Django 4.2. Python's versatility and readability empowered us to create robust backend logic. Django's high-level framework facilitated rapid development, efficient database management, and seamless integration of various components.

Through the harmonious collaboration of these technologies, we've crafted a comprehensive School Management App that embodies modern best practices and offers a rich user experience.

## Tests

Ensuring the reliability and functionality of our application is of paramount importance. To achieve this, we extensively employed the built-in testing framework provided by Django, specifically the `TestCase` class.

### Unit Testing with TestCase

We conducted comprehensive unit testing to validate the functionality of our School Management App. Leveraging Django's `TestCase` class, we focused on the two most critical components of the app: `usersApp` and `eventApp` covered them with over 150 unit tests.

#### usersApp Testing

The `usersApp` module, responsible for user registration, authentication, and account creation, underwent rigorous testing. Our test suite covered over 90% of the codebase, ensuring the reliability of user-related functionalities.

#### eventApp Testing

Similarly, we meticulously tested the `eventApp` module, which handles the creation and management of school events. Our diligent testing practices resulted in over 90% code coverage, affirming the robustness of event-related operations.

### Visualizing Test Coverage

For transparency and accountability, we've provided a screenshot of the test coverage report. This report showcases the extent of code coverage achieved through our diligent testing efforts.

![coverage raport](https://github.com/Mrokus95/SchoolManagmentApp/assets/59625513/2440620f-60e1-4e28-b2f8-f9d203c0e470)

## Features

The project was developed with the purpose of refining skills in the Django framework. Its goals included encompassing a diverse array of functionalities while staying closely aligned with market demands and venturing beyond the conventional scope of such projects. Recognizing a potential need, we identified an opportunity for a school platform that facilitates information dissemination and communication among all entities within the school community. The result of our endeavor is precisely this project.

Functions and permissions vary depending on the account type. The website offers slightly different capabilities for teachers, students, and parents.

### UsersApp:

The School Management App has been meticulously designed to enhance school administration and communication, providing a suite of features tailored to meet the diverse needs of the school community.

- Home Page and Login: The app also serves as the homepage with a login panel that warmly greets users when they visit our website. It's here that users initiate their interaction with the application.

- User Account Creation: Administrators can effortlessly create new user accounts with relevant attributes. When setting up a student account, administrators not only provide standard details but also select a class and assign a parent, facilitating effective student-parent tracking. Similarly, while creating a teacher account, specifying the subject they will teach is crucial for clear role definition.

- Customizable Profiles: User profiles are highly customizable. Users can upload a photograph to personalize their profile, enhancing visual identification and community engagement.

- User Authentication and Management: This section is pivotal for user authentication. Administrators can log in with appropriate privileges to create, manage, and oversee user accounts. Each user, whether a teacher, student, or parent, has the autonomy to update crucial information like email addresses and passwords.

- Password Reset Convenience: The app offers an efficient solution for password recovery through email communication. Users can request a password reset, receiving an email with an authentication link to securely reset their password, ensuring account security and seamless access.

This comprehensive array of features not only streamlines user management but also reinforces the security and accessibility of the platform, fostering effective communication and collaboration within the school community.

#### Adding student by admin:
![register student](https://github.com/Mrokus95/SchoolManagmentApp/assets/59625513/58a798af-6852-4d1e-8bfa-53fd4fde166e)

#### Reset password email:
![email reset](https://github.com/Mrokus95/SchoolManagmentApp/assets/59625513/de8fa275-73e5-4084-8afd-e6ac4b380fe5)


### TeacherApp:

ATeacherApp is a crucial component of the project, enabling lesson management and facilitating associated formalities.

- Starting lesson:
At the outset, the user selects a class and subject, which serve as the foundation for report categorization.

- Attendance:
Subsequently, they are directed to the attendance tracking view, where a list of students for the chosen class is generated.
  
- Main raport:
Finally, they access the report view, allowing them to update attendance, add grades with brief descriptions, and assign events such as tests or homework. Before finalizing, they input the lesson's topic and provide a short description. Following lesson finalization, each student and their associated parent can review the lesson's occurrences and related events.

- Viewing raports:
Teachers have their dedicated dashboard for reviewing their reports, equipped with filtering capabilities based on date, class, or subject.

#### Adding grades:
![Adding_Grades](https://github.com/Mrokus95/SchoolManagmentApp/assets/123180025/e382df2d-7ce8-4b25-86c8-f2decc24f967)

#### Adding lesson report:
![Lesson_Conducting](https://github.com/Mrokus95/SchoolManagmentApp/assets/123180025/c147d16b-4cb4-483d-906d-b2f16257c93e)

Filtering reports:
![Lesson_Report_Filter](https://github.com/Mrokus95/SchoolManagmentApp/assets/123180025/defc983f-4c6f-42c0-ac89-330ff9a37f08)

### MessagesApp:

The MessagesApp is an integral part of our platform, designed to streamline communication between various entities. This feature-rich panel offers users the convenience of managing messages within three distinct sections: Inbox, Sent, and Important. The app goes beyond just sending and receiving messages, providing an array of functionalities to enhance the messaging experience.

- Inbox Management:
In the Inbox section, users have access to all incoming messages. Messages are intelligently sorted by the date they were received. Unread messages are highlighted, making it easy for users to identify new communication at a glance. The app employs a smart notification system, displaying an attention-grabbing icon until a new message is read.

- Sent Messages:
The Sent section enables users to view their outbound messages. This transparency ensures users have a comprehensive overview of their correspondence, aiding in tracking communication threads. Each sent message is timestamped and sorted chronologically for easy navigation.

- Marking Messages as Important:
The MessagesApp empowers users with the ability to designate messages as "Important." This feature ensures that essential communication doesn't get lost among the clutter. By marking a message as Important, users can easily prioritize and locate crucial information whenever needed.

- Message Deletion:
Our app takes a pragmatic approach to message deletion. Users are given the liberty to remove messages from their mailbox, but with certain considerations. While all messages can be deleted, those marked as "Important" remain immune from deletion. This safeguard ensures that critical information is preserved even during routine message clean-up.

- Whitespace Formatting:
The MessagesApp is engineered to handle whitespace formatting, recognizing that readability is paramount in effective communication. This attention to detail ensures that messages are presented exactly as intended, maintaining clarity and avoiding any confusion arising from formatting discrepancies.

- Read Status and Unread Message Count:
A standout feature of the MessagesApp is its ability to track message read status. Unread messages are readily identifiable, helping users to efficiently manage their incoming messages. The app provides a visual counter of unread messages, allowing users to gauge their inbox activity at a glance.

In summary, the MessagesApp transcends the conventional messaging experience by offering a comprehensive suite of features tailored for effective communication management. Users can seamlessly navigate their messages, mark them as important, and engage in responsive communication. With its robust capabilities and user-friendly interface, the MessagesApp transforms messaging into a streamlined and organized process, enhancing communication efficiency across the platform.

#### Create new message:
![Create new email](https://github.com/Mrokus95/SchoolManagmentApp/assets/59625513/9cbd4379-9bac-4dac-8745-29b96b8ab87c)

#### Inbox:
![inbox](https://github.com/Mrokus95/SchoolManagmentApp/assets/59625513/9adfcdeb-b54b-436e-9557-09496a82f5ea)

#### View of received email:
![received email](https://github.com/Mrokus95/SchoolManagmentApp/assets/59625513/61d3bd2b-05a0-4af6-ab8e-cc2d1d85d90c)

### GradesApp:

The GradesApp is an essential component of our platform designed to facilitate grade management. This feature-rich application enables users to meticulously monitor and analyze student performance across various subjects and semesters.

- Grades Overview:
The application allows users to review grades within three main sections: Inbox, Sent, and Important. Each section provides a unique way of organizing grades, making it easier to track students' progress.

- Student Grade Management:
For users with the student role, the app presents their individual grades, assigned to specific subjects and semesters. These grades are thoughtfully arranged chronologically and grouped in a manner that enables users to easily understand their learning progress.

- Reports for Parents:
For users with the parent role, the app delivers comprehensive grade reports for their children. Each child is represented separately, and parents can review grades in specific subjects and semesters. This view provides parents with a well-rounded understanding of their children's achievements in an educational context.

- Thoughtful Filters:
The app offers flexible filtering options by semester, class, subject, and student. This allows users to fully customize the grade view to their needs, gaining specific insights into performance.

- Intuitive Interface:
GradesApp features a simple and intuitive user interface that facilitates navigation and access to essential information. This allows users to comfortably review grades, analyze student progress, and make informed educational decisions.

- Security Considerations:
The app has been designed with data security and student privacy in mind. Access to grades is controlled based on account type, providing appropriate permissions to users.

In summary, GradesApp is a powerful tool for student grade management and monitoring. Through functionalities tailored for students, parents, and educational staff, the app enables a comprehensive understanding of student educational outcomes, supporting effective teaching and learning processes.

#### Viewing grades:
![Grades_By_Teacher_With_Details](https://github.com/Mrokus95/SchoolManagmentApp/assets/123180025/09b72b14-cdbe-4cf6-88d4-3478141ac465)

### EventsApp:

The StudentApp is a significant component of the application responsible for displaying events associated with a particular student or parent.

- Event viewing:
Students can view events related to them, while parents are directed to their child's events or can choose from among them if the school has multiple students. Teachers can see all events they have added.

- Details:
Each user has the ability to access event details by clicking on them and can navigate to the related lesson report view.

- Filtering:
Events can be filtered based on subject, event type, or by selecting a date range.

#### Viewing events for student:
![Events_Student](https://github.com/Mrokus95/SchoolManagmentApp/assets/123180025/58bb1c31-dbf1-432f-866e-ab23989d4f2a)

###  CalendarApp:

The CalendarApp is a fundamental application within our educational platform, designed to effectively manage schedules and class timetables. This comprehensive tool offers users the ability to organize and monitor classes, lessons, and teacher assignments across various subjects and days.

Key Features and Functionalities:

- Teachers and Subjects: The application allows users to view teachers' schedules and assignments for specific subjects. Through thoughtful filtering options, users can effortlessly access the schedules of teachers dedicated to particular subjects.

- Weekday Overview: Users are provided with an insightful weekday overview, showcasing classes, lessons, and teacher assignments for each day. This overview simplifies the process of tracking the daily schedule and optimizing time management.

- Lesson Modifications: For administrators, the app facilitates modifications to lesson schedules. This includes adjustments to lesson timings, teacher assignments, and classroom allocations. These modifications ensure seamless coordination of class activities. 

- Exceptions and Changes: The app accommodates exceptions and changes to the regular schedule. Administrators can make modifications to lesson dates, teacher assignments, and classroom reservations. This feature supports adaptability in the face of unforeseen events.

- Viewing Schedules: Users can easily view class schedules by specifying the class unit and the desired week offset. The app dynamically generates weekly schedules, allowing users to navigate through different weeks and monitor class activities.

- Intuitive Interface: The CalendarApp boasts an intuitive user interface that simplifies navigation and access to crucial information. This user-friendly design enables users to review schedules, analyze timetables, and make informed decisions regarding class management.

- Security Considerations: Data security and privacy are paramount in the development of the app. Access to schedules and class-related information is managed based on user roles, ensuring appropriate permissions and confidentiality.

- Notifications for Students: It's worth noting that each introduced modification in the lesson schedule automatically generates notifications for students of the respective class. These notifications appear in students' mailboxes, informing them about changes in the class schedule. This element is particularly important as it keeps students aware of any updates and alterations in their learning plans, contributing to maintaining an effective organization of classes.

In summary, the CalendarApp emerges as an indispensable tool for managing class schedules and timetables. By catering to the needs of teachers, administrators, and educational staff, the application provides an organized and accessible platform for coordinating class activities. Its functionalities, including weekday overviews, lesson modifications, and adaptive scheduling, contribute to efficient class management and support effective teaching and learning processes. With its user-friendly interface and robust security measures, the CalendarApp significantly enhances the efficiency and organization of educational institutions.

#### Auto message after changed lesson:
![Changed_Auto_Message](https://github.com/Mrokus95/SchoolManagmentApp/assets/123180025/90ddf414-6f4b-49cc-a349-9b532024e065)

#### Shedule:
![Sheludes_Student](https://github.com/Mrokus95/SchoolManagmentApp/assets/123180025/13740fa7-c73d-40a5-9a2f-3d95829c7946)

## Authors:

<table>
  <tr>
    <td>
      <img src="https://github.com/Mrokus95/SchoolManagmentApp/assets/59625513/3b26a154-ab53-4590-a756-3c9f88681a2d" alt="Łukasz Mroczkowski" width="150px" height="150px">
    </td>
    <td>
      <ul>
        <b>Łukasz Mroczkowski</b>
        <p>Junior Python Developer</p>
        <li><a href="https://www.codewars.com/users/Mrokus95">CodeWars</a> <img src="https://www.codewars.com/users/Mrokus95/badges/small" alt="CodeWars"></li>
        <li><a href="https://www.linkedin.com/in/mroczkowski-lukasz/">LinkedIn</a> <img src="https://img.shields.io/badge/LinkedIn-PROFIL-blue" alt="LinkedIn"></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/Mrokus95/SchoolManagmentApp/assets/59625513/a6ca45f3-4579-4201-bac3-0e770780e6dd" alt="Łukasz Mroczkowski" width="150px" height="150px">
    </td>
    <td>
      <ul>
        <b>Mateusz Świst</b>
        <p>Junior Python Developer</p>
        <li><a href="https://www.codewars.com/users/MatS1">CodeWars</a> <img src="https://www.codewars.com/users/MatS1/badges/small" alt="CodeWars"></li>
        <li><a href="https://www.linkedin.com/in/mateusz-%C5%9Bwist/">LinkedIn</a> <img src="https://img.shields.io/badge/LinkedIn-PROFIL-blue" alt="LinkedIn"></li>
      </ul>
    </td>
  </tr>
</table>
