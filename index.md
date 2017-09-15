# Introduction

On this page you will find instructions and references for some of your lab assignments. Please remember to check our [Google Classroom](https://goo.gl/pcP2JU) as usual for lab assignment announcements, deadlines, submissions, feedback, etc..

The different aspects of BI/BA covered in our labs are:
* **What? Why?**
Visual Analytics (mainly applied in terms of Descriptive & Diagnostic Analytics)
* **What will happen?**
Predictive Analytics
* **What, why, and what will?**
Web & Social Analytics
* **How can we make it happen** Prescriptive Analytics

Through our labs, we will learn
* How to ask right **BI/BA questions**
* How to learn BI/BA related **tools and techniques**
* Create and use **business dashboards**
* Analyze & model different business cases for **problem-solving**
* Formulate and implement **BI/BA strategies**
* Document, Interpret and Report **BI/BA Results**


These instructions are to be taken as **guidelines** and **not as a solution manual**. Feel free to always contact me directly if you have any questions and/or problems.



## Lab 3a: Power BI - Part 1

### Status

In-Works, due after class 9/15

### Intro

Now that we have learned the fundamental aspects of building dashboards, it's time to use our acquired knowledge from Tableau to learn visual data exploration with Power BI Desktop. You will notice that many procedures and tools are very similar, the only differences lie in the execution of commands.

### Objective

Building executive dashboards with Power BI Desktop and publishing them to Power BI Online.

### BI Concept of the Week

**Agile BI**

As said very well in the first reference below from George Washington University, "agile BI involves applying an agile mindset to business intelligence".

Part of the agile methodology is typically to develop small story points (e.g. business reports) in so-called sprints (~2 weeks). The agile methodology not only applies to BI and software development, but also to workshops, college courses (such as this one), design/research projects, etc..

As future project managers, BI analysts, and scrum masters, this a great methodology to be aware of.

This concept
* [Agile BI Development Methodology - overview ](https://goo.gl/eSkWzh)
* [Agile BI - Whitepaper](https://goo.gl/ZVwQTf)



### Task

[Google Classrom Lab Activities](https://goo.gl/RC1oGZ).

Please load the Coffee-Chain dataset attached in Power BI Desktop and select three tables of location, product, and sales. We will learn about Power BI Desktop using this dataset. For your assignment, you only need to clean up the dataset, create a data model, develop a business dashboard with at least four KPIs, upload the dashboard to Power BI Online and submit the URL on Google Classroom.  

Note: By sharing your dashboard with me (hsmidt@hawaii.edu) on Power BI Online, you can create a required link and give me permission to view.

### Dataset

We will use the [Coffee-Chain dataset](https://goo.gl/HQbUXr).

### Guidelines

To complete this lab, you will essentially have to work through the following steps. You do not need to follow these steps point-by-point, they merely provide some guidelines.

#### What's your ultimate goal ?
Before starting your visual explorations process, you should ask yourself:
* What kind of dataset am I going to work with? What is is about, how large is the dataset, how detailed is it, is it properly formatted?
* Who am I exploring the data for and what is important to that person?
  - think of this question in terms of "KPI's of interest"
  - an answer would probably include types of measures, dimensions, geographic regions, and time scales

#### Power BI Interface

* Power BI Desktop is structure like most Microsoft Office applications and should thus look familiar. You have your tools on the top and your pages on the bottom.
* Power BI Desktop has three distinct views that can be selected on the left-most view pane:
  - Report (symbolize by a column chart)
  - Data (symbolized by a table)
  - Relationships (symbolized by a relations graph)
* Functionalities of these three views are intuitive:
  - The report view lets you create dashboards
  - The data pane lets you see the data and modify them
  - The relationship pane allows you to build a model
* You will typically use all three views and their tools for your visual data exploration process


#### Getting the data

* **Select** the `Get Data` tab and connect to your `Excel` file.
* Once selected, you can select each `sheet` from your `Excel` file individually, and then either `load` or `edit` the data.
  - `load`: this will load your data without any modifications to it
  - `edit`: this allows you to modify your query and do an initial "cleanup", e.g. removing unnecessary columns, changing column names, creating new columns, etc.
  - *note*: your queries (data) can be modified even after loading them. You can simply click on `Edit Queries`
* **Clean** your data by doing at least the following:
  - making sure that data types are assigned correctly
  - naming columns with the same information the same across multiple sheets
  - deleting obsolete data columns
  - create a profit ratio measure by:
    - Adding new column
    - Giving it a title (e.g. Profit ratio by sale)
    - Dividing profit by sales (this will give you profit ratio for each sales transaction)


#### Modeling Your Data

#### Modeling the data

#### Exploring / Visualizing the data



## Lab 2: Tableua - Part II

### Objective

Building stories with Tableau

### Status

PAU

### Task

See [Google Classroom, Lab 2](https://goo.gl/uJkycL)

## Lab 1: Executive dashboards with Tableau

### Objective

Building dashboards with Tableau and publishing them to Tableau Public.

### Status

PAU

### Task

See [Google Classroom, Lab 1](https://goo.gl/CinVWz)
