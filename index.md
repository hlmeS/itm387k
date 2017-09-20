### URL: hlmes.github.io/itm387k

### Table of Contents

- General announcements
  - [Introduction](#introduction)
- Lab Assignments
  - [Lab3b: Power BI - Part II](#lab-3b-power-bi---part-2)
  - [Lab3a: Power BI - Part I](#lab-3a-power-bi---part-1) --- Updates available
  - [Lab 2: Tableau - Part II](#lab-2-tableau---part-2)
  - [Lab 1: Tableau - Part I](#lab-1-tableau---part-1)
- BI Concepts
  - [BI Concept (9/20)](#bi-concept-of-the-week-920)
  - [BI Concept (9/13)](#bi-concept-of-the-week-913)



# BI Concept of the week (9/20)

## Exploration and Exploitation

- [Exploration vs. Exploitation: What’s the Right Balance for a Business?](https://www.linkedin.com/pulse/exploration-vs-exploitation-whats-right-balance-business-don-peppers/)



# Lab 3b: Power BI - Part 2

## Status

In-Works, due 9/25

## Intro

One of the motivations for developing easy-to-comprehend executive dashboards is to enable data-driven decision making. But what does **_data-driven_** really mean?

Let's imagine the following scenario for the Coffee-Chain dataset: The sales department claims marketing efforts have not been successful; the marketing department claims otherwise.

Can we definitively determine who is right in this scenario using a visual analysis report (e.g. one or many dashboards)?

## Objective

Design a visual analytics report that supports the claims of the marketing department **or** the claims of the sales department.

## Task

Pick your side, sales or marketing, and defend your department's claim by developing some visuals.

For your assignment, you only need to develop a Power BI visual report supporting your claim, publish it online and submit the URL. Please remember to share the report with hsmidt@hawaii.edu

## Dataset
Same as in Lab3a: [Coffee-Chain dataset](https://goo.gl/HQbUXr).

## Guidelines

Similar strategies as those in Lab3a should be applied here. However, to advance your analysis process, here are more details on data modeling, relationships and DAX. If any of it is unclear, don't hesitate to ask about it.

I'm using [The Definitive Guide to DAX](https://books.google.com/books/about/The_Definitive_Guide_to_DAX.html?id=sJm9CgAAQBAJ&hl=en) as a reference here.

### Data Models and relationships

#### Data models

#### Cardinality constraints
#### Direction of a relations


# BI Concept of the Week (9/13)

## Agile BI

"Agile BI involves applying an agile mindset to business intelligence" -- [George Washington University](https://goo.gl/eSkWzh)

One component of the agile methodology is to typically develop small story points (e.g. business reports) in so-called sprints (~2 weeks). The agile methodology not only applies to BI and software development, but also skill development, college courses (such as this one), design/research projects, etc..

As future project managers, BI analysts, and scrum masters, this a great methodology for you to be aware of.

This concept
* [Agile BI Development Methodology](https://goo.gl/eSkWzh)
* [Agile BI - Whitepaper](https://goo.gl/ZVwQTf)


# Lab 3a: Power BI - Part 1

## Updates

If you've been having problems last class with date filtering/hierarchies, measure calculations, failed measure aggregation, and similar, please check the following modeling aspects:


  * Are you relating the appropriate columns?
  * Are you using the correct cardinality constraint?
  * Are you using the right cross filter direction? General advice is to always use **BOTH**!
  * Are you using the *date* datatype for the *date* column of your calendar table?


## Status

In-Works, due 9/20

## Intro

Now that we have learned the fundamental aspects of building dashboards, it's time to use our acquired knowledge from Tableau and learn about other visualization tools, in this case, Power BI Desktop. You will notice that many aspects and workflow operations are very similar, the only differences lie in the execution of these workflow operators.

## Objective

Building executive dashboards with Power BI Desktop and publishing them to Power BI Online.

## Task

[Google Classrom Lab Activities](https://goo.gl/RC1oGZ).

Please load the Coffee-Chain dataset attached in Power BI Desktop. For your assignment, you only need to clean up the dataset, create a data model, develop a business dashboard with at least four KPIs, upload the dashboard to Power BI Online and submit the URL on Google Classroom.  

Note: By sharing your dashboard with me (hsmidt@hawaii.edu) on Power BI Online, you can create a required link and give me permission to view.

## Dataset

We will use the [Coffee-Chain dataset](https://goo.gl/HQbUXr).

## Guidelines

To complete this lab, you will essentially have to work through the following steps. You do not need to follow these steps point-by-point; these instructions merely provide some guidance and seed of ideation.

### What's occurs ultimate goal ?
Before starting your visual explorations process, you should ask yourself:
* What kind of dataset am I going to work with? What is is about? How large is the dataset, how detailed is it, is it properly formatted?
* Who am I exploring the data for and what is important to that person?
  - why am doing this analysis
  - what are my KPI's of interest (types of measures, dimensions, geographic regions, and time scales)

### Power BI Interface

* Power BI Desktop is structured like most Microsoft Office applications and should thus look familiar. You have your tools in your toolbar on the top and then your pages (sheets) on the bottom.
* Power BI Desktop has three distinct views that can be selected on the left-most view pane:
  - Report (symbolized by a column chart)
  - Data (symbolized by a table)
  - Relationships (symbolized by a relations graph)
* Functionalities of these three views are rather intuitive:
  - The report view lets you create dashboards
  - The data pane lets you see the data and modify them
  - The relationship pane allows you to build a model
* You will typically use all three views and their tools for your visual data exploration process
* The right-most view pane in your report view show your data fields, and visualization tools.

### Getting the data

* **Select** the `Get Data` tab and connect to your `Excel` file.
  ![Getting data from Excel files](https://raw.github.com/hlmeS/itm387k/master/images/BI_data_1.png)
* Once selected, you can select each `sheet` from your `Excel` file individually, and then either `load` or `edit` the data.
  - `load`: this will load your data without any modifications to it
  - `edit`: this allows you to modify your query and do an initial "cleanup", e.g. removing/hiding unnecessary columns, changing column names, creating new columns, etc.
  - *note*: you can modify your queries (data) at every step of your analysis by simply clicking on `Edit Queries` in your toolbar

  ![Selecting tables and editing data. ](https://raw.github.com/hlmeS/itm387k/master/images/BI_data_2.png)

* **Clean** your data by doing at least the following:
  - making sure that data types are assigned correctly
  - naming columns with the same information the same across multiple sheets
  - renaming columns to make them more user friendly
  - deleting/hiding (currently) obsolete data columns

  ![Changing metadata of columns.](https://raw.github.com/hlmeS/itm387k/master/images/BI_data_3.png)
* After having cleaned the data, make sure to click `close & apply` (top left corner) when you want to load the data into the reports view.


### Modeling Your Data

Constructing your data model will allow you to leverage the relationships between a multitude of data resources, i.e. cross-database links. Although we only have three tables, we can still use them to model our data from the `Relationship View`. The concept of data modeling will probably remind you of the *relational DB modeling* from your DB course.

* The goal is to create relationships between fields (= attributes = columns ) of multiple relations (= tables). To do so, relations need to have a common field.
* You have two options to `create relationships`:
  - `drag and drop`: simply select a field and drop it onto another field in another relation. Then double click the relation and edit the details.
  - click `manage relationship` from the toolbar and then select the various relations/fields that you want to connect
  ![Relationship View in BI](https://raw.github.com/hlmeS/itm387k/master/images/BI_model_1.png)

* When `creating relationships`, add the (maximum) cardinality constraints as well. BI can infer it for you, but make sure to double-check as there may be multiple possible options based on the current data.
* As a reminder, `cardinality constraints` show how many instances of one relation can occur with respect to the other and vice versa.
* For example, `many students can register for a course and a course can have many students registered in it`, would be an example of a **M:M** relationship. The example, `Each person can hold many email addresses, but each email address can only be held by on person` would be a **1:M** relationship.
  ![Editing relationships.](https://raw.github.com/hlmeS/itm387k/master/images/BI_model_2.png)
* Another useful tool in the modeling process is the ability to hide fields from relations so that they don't show in the report, and thus helps to build more user-friendly reports. Simply `right-click on fields`, and select the `Hide in Report View` option.

  ![Changing columns names.](https://raw.github.com/hlmeS/itm387k/master/images/BI_model_3.png)

  ![Hiding columns from the report view.](https://raw.github.com/hlmeS/itm387k/master/images/BI_model_4.png)

### Exploring / visualizing the data

The visualization process should look familiar to you from your experience with Tableau. You have a variety of visualization options and can select multiple dimensions and measures to build your views. Depending on the type of view, you have different options for adding multiple dimensions and attributes to the viz. The paint brush gives you options for formatting the various aspects of your visualizations.

Please start exploring with respect to:
* the dataset
  - why are you analyzing the data and what's your goal
  - w.r.t to the **why**, **what** does the data show
  - how can you present your finding **most effectively**
* Power BI's toolset
  - what kind of visualizations does it allow for
  - how to drill in/out (e.g. the date field has a neat hierarchy feature)
  - how to make it interactive (e.g. use filters, action filter should work by default)
  - what kind of analysis tools can be used from the report view, which ones need to be done in the data view (e.g. creating new measures, calculating %-differences, etc.)

### Using M-Queries to create a Calendar table

The following describes a few steps for creating a calendar table that tabulates *day, month, dayoftheweek, monthoftheweek, quarter, year* for every day in some date range. You don't always need this, but it's a good exercise to learn about queries.

- From your `Get Data` dropdown menu, select the `Blank Query` option.
- Click on `View` and select `Advanced Editor`
  ![Selecting the advanced M-Query Editor](https://raw.github.com/hlmeS/itm387k/master/images/BI_date_2.png)
- Copy/Paste (or type!) the following code from this [blog post](https://www.agilebi.com.au/blog/power-bi-date-dimension) in your editor:
  ``` js
  //Create Date Dimension
  (StartDate as date, EndDate as date)=>
  let
  //Capture the date range from the parameters
  StartDate = #date(Date.Year(StartDate), Date.Month(StartDate),
  Date.Day(StartDate)),
  EndDate = #date(Date.Year(EndDate), Date.Month(EndDate),
  Date.Day(EndDate)),
  //Get the number of dates that will be required for the table
  GetDateCount = Duration.Days(EndDate - StartDate),
  //Take the count of dates and turn it into a list of dates
  GetDateList = List.Dates(StartDate, GetDateCount,
  #duration(1,0,0,0)),
  //Convert the list into a table
  DateListToTable = Table.FromList(GetDateList,
  Splitter.SplitByNothing(), {"Date"}, null, ExtraValues.Error),
  //Create various date attributes from the date column
  //Add Year Column
  YearNumber = Table.AddColumn(DateListToTable, "Year",
  each Date.Year([Date])),
  //Add Quarter Column
  QuarterNumber = Table.AddColumn(YearNumber , "Quarter",
  each "Q" & Number.ToText(Date.QuarterOfYear([Date]))),
  //Add Week Number Column
  WeekNumber= Table.AddColumn(QuarterNumber , "Week Number",
  each Date.WeekOfYear([Date])),
  //Add Month Number Column
  MonthNumber = Table.AddColumn(WeekNumber, "Month Number",
  each Date.Month([Date])),
  //Add Month Name Column
  MonthName = Table.AddColumn(MonthNumber , "Month",
  each Date.ToText([Date],"MMMM")),
  //Add Day of Week Column
  DayOfWeek = Table.AddColumn(MonthName , "Day of Week",
  each Date.ToText([Date],"dddd"))
  in
  DayOfWeek

  ```

- Once executed, you can rename your table as `Calendar` and enter your start and end date --> `1/1/2014 - 12/31/2015`
  ![Inserting start and end date](https://raw.github.com/hlmeS/itm387k/master/images/BI_date_3.png)
- Make sure that your first column (`Date`) is of type **Date**
- Now that you have your calendar relation, it's time `model its relationship`
  - you have a `Date` field in your **Sales** relation and your **Calendar** relation, so create a relationship between them
  - what kind of cardinality should this be ? (Hint: _Each day only occurs once in a calendar_)

  ![Creating the relationship between calendar and sales relations.](https://raw.github.com/hlmeS/itm387k/master/images/BI_date_4.png)

Now that you have your calendar relation set up, you can use it in your visualizations (e.g. as filter, table columns, etc. ).

### DAX calculations

A very specific aspect of Power BI is its DAX calculations, which you may know from Excel. There are so many powerful functions that come with it that it's impossible to remember them. You can refer to this [30 minute reference](https://goo.gl/N1a5Me), this [very long manual](https://goo.gl/SoGyDH), or simply to [Google Search](https://google.com).

Here is one of the many powerful functions available to you.

Imagine you want to calculate the Year-to-Date sales revenue and then compare it between two years. To do this, we need to create a new measure which requires some DAX syntax. The following can be done in the various views, but try it from the report view for now.

- select the `New Measure` tool
  - from the toolbar **OR**
  - right-click the sales tables and select `New measure`
- Enter this calculation
``` js
YTD Sales = TOTALYTD( SUM('Sales'[Sales]), 'Calendar'[Date])
```
- Now you can use the measure just like any other measure, such as in the graph shown below:

![YTD Sales by Quarter and Year](https://raw.github.com/hlmeS/itm387k/master/images/BI_ytd_1.png)

### Creating your dashboard

Creating the dashboard is its own separate step in the visual exploration process. An executive dashboard **is not** the first four visualizations that come to your mind. It's the product of your findings with respect to the initial goal, i.e. **who** is going to look at this dashboard, and with **what intention**?

In other words, to have a successful dashboard please ask yourself **whom** you are trying **to 'impress' and 'help'**, make the data **relevant** to them. Your KPI dashboard should be easy to **read in 10-30 sec.**, easy to **understand in 30 -60 sec.**, and then provide **interactive components for exploration**.

Remember, people 'love' beauty and beauty lies in simplicity, and as da Vinci noted **_"simplicity is the ultimate sophistication"_**.

Try to have fun with this open-ended assignment and DO NOT hesitate to ask your instructor and peers for help. It is **strongly encourage** to work in small teams.

[Sample dashboard](https://goo.gl/1AeCL7) --- lots to improve here, what do you think should be better?

<iframe width="800" height="600" src="https://goo.gl/1AeCL7" frameborder="0" allowFullScreen="true"></iframe>

Make sure to publish it online and then share it also with me.
![Publishing to online. ](https://raw.github.com/hlmeS/itm387k/master/images/BI_ytd_1.png)




# Lab 2: Tableau - Part II

## Objective

Building stories with Tableau

## Status

PAU

## Task

See [Google Classroom, Lab 2](https://goo.gl/uJkycL)

# Lab 1: Tableau - Part I

## Objective

Building dashboards with Tableau and publishing them to Tableau Public.

## Status

PAU

## Task

See [Google Classroom, Lab 1](https://goo.gl/CinVWz)


# Introduction

On this page you will find instructions and references for some of our lab projects. Please remember to check our [Google Classroom](https://goo.gl/pcP2JU) as usual for announcements, deadlines, submissions, feedback, etc..

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


These instructions are to be taken as **guidelines** and **not as solution manuals**. Feel free to always contact me directly if you have any questions and/or problems.
