#! /usr/bin/env python2

"""

Title: Analyzing Student Grades From Google Classroom
Author: Holm Smidt
Version: 1.0
Date: 11-16-2017

Overview:
* read info from a google classroom grade sheet
* compute max
* compute students grades by activity, exctra credit, and total
* plot grades
* send emails to students and cc instructor

"""

import os
import ConfigParser
import argparse
import csv

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class grader:

    def __init__(self, filename):

        if filename == "": self.filename = '../../../../grades/ITM387K_Grades.csv'
        else: self.filename = filename

        self.assignments = []
        self.dates = []
        self.points = []

        self.students = []
        self.emails = []
        self.grades = []

        self.stats = []
        self.full = [0.0, 0.0, 0.0]


    def load_data(self):
        """
        Load the data, '../../../../grades/ITM387K_Grades.csv'

        line 1 - first, las, email, assignment1, assignment2, etc.
        line 2 - date, empty, empty, due date 1, due date 2, etc.
        line 3 - points, empty, empty, max point 1 , max point 2
        line 4 - empty
        line 5+ - student data
        """

        rdr= csv.reader(open(self.filename))

        self.assignments.append(rdr.next()[3::])
        self.dates.append(rdr.next()[3::])
        self.points.append([(float(x) if x else 0) for x in rdr.next()[3::]])
        self.full = self.calc_stats(self.points[0])
        blank = rdr.next()
        for line_num, row in enumerate(rdr):
            self.students.append(row[0])
            self.emails.append(row[2])
            scores = [(float(x) if x else 0) for x in row[3::]]
            self.grades.append(scores)
            self.stats.append(self.calc_stats(scores))


        #print self.assignments
        #print self.dates
        #print self.points
        #for student, email, scores, stats in zip(self.students, self.emails, self.grades, self.stats):

            #print student, email, scores, stats

    def calc_stats(self, grades):
        """
        calculate sum of all, lab, and ec
        """

        total = sum(grades)
        lab = sum([grades[i] for i, j in enumerate(self.assignments[0]) if 'Lab Act' in j])
        ec = sum([grades[i] for i, j in enumerate(self.assignments[0]) if 'Extra' in j])
        #li = [scores[i] for i, j in enumerate(self.assignments[0]) if 'Lab' in j]

        return [total, lab, ec]

    def plot_grades(self, tag, studentid):
        """
        Plots grades for a student, either by extra credit or lab activities.
        Returns the relative output filepath.

        Allowable tag inputs: 'Extra Cr' , 'Lab Act'
        """
        outputFile = "output/ITM387K_tracker_"+self.students[studentid]+".png"

        name = [self.assignments[0][i].split(" ", 2)[2][:2] for i, j in enumerate(self.assignments[0]) if tag in j]
        data = [self.grades[studentid][i] for i, j in enumerate(self.assignments[0]) if tag in j]
        full = [self.points[0][i] for i, j in enumerate(self.assignments[0]) if tag in j]

        df = pd.DataFrame({"Names": name, "Your Points": data, "Max Points": full})
        df["Names"].astype('category')
        #df.set_index(["Names"])#,inplace=True)

        plot = df.plot(kind='bar', lw=2, colormap='Spectral', title="Grade Tracker for "+self.students[studentid], alpha=0.75, rot=0)
        plot.set_xlabel("Lab Activity")
        plot.set_ylabel("Points")
        #handles, labels = plot.get_legend_handles_labels() # reversed(handles), reversed(labels)
        plt.legend(loc='center', bbox_to_anchor=(0.35, 0.9))
        fig = plot.get_figure()
        fig.savefig(outputFile)

        return outputFile


class mailer:

    def __init__(self, configfile, secure, debug):

        self.secure = secure
        self.debug = debug
        self.user, self.passwd = self.config_init(configfile)

    def config_init(self, configFile):
        """Loads configuratin data from config.ini
        """

        config = ConfigParser.ConfigParser()
        config.read(configFile)

        user = config.get('email_login', 'username')
        passwd = config.get('email_login', 'passwd')
        if self.secure and self.debug:
            print user, '\t', passwd
        return user, passwd

    """outdated from me322 grader times ... revise for possible utility """
    def parseArgs(self):
       parser = argparse.ArgumentParser(description='Grade report and email tool')
       parser.add_argument('-a', '--assign1', help='first assignment name (must be identical to whatever is in csv file)', required=True)
       parser.add_argument('-b', '--assign2', help='second assignment name (must be identical to whaterver is in csv file)', required=False)
       parser.add_argument('-c', '--assign3', help='third assignment name (must be identical to whatever is in csv file)', required=False)
       args = vars(parser.parse_args())
       return args


    def send_email(self, recipient, subject, body):
        gmail_user = self.user
        gmail_pwd = self.passwd
        FROM = self.user
        TO = recipient if type(recipient) is list else [recipient]
        SUBJECT = subject
        TEXT = body

        # Prepare actual message
        message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        try:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.ehlo()
            server.login(gmail_user, gmail_pwd)
            server.sendmail(FROM, TO, message)
            server.close()
            print 'successfully sent the mail'
        except:
            print "failed to send mail"


    def send_image(self, rec, subject, body, ImgFileName):
       gmail_user = self.user
       gmail_pwd = self.passwd
       img_data = open(ImgFileName, 'rb').read()
       msg = MIMEMultipart()
       msg['Subject'] = subject
       FROM = self.user
       recipient = [rec, 'hsmidt@hawaii.edu']
       TO = recipient if type(recipient) is list else [recipient]

       text = MIMEText(body)
       msg.attach(text)
       image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
       msg.attach(image)

       try:
          s = smtplib.SMTP_SSL("smtp.gmail.com", 465)
          s.ehlo()
          s.login(gmail_user, gmail_pwd)
          s.sendmail(FROM, TO, msg.as_string())
          s.close()
          print 'successfully sent mail and image to ' + str(recipient)
       except:
          print 'failed to sent mail and image'


"""
It'd be cleaner if this was run in separate file using classes from this file.

>> import analyzeGrades
>> grader = analyzeGrades.grader('')
>> emailer = analyzeGrades.mailer('config.ini', secure, debug)
"""
secure = 1
debug = 1
emailer = mailer('config.ini', debug, debug)
grader = grader('')
grader.load_data()

for id, student in enumerate(grader.students):
    print 'Email: ', grader.emails[id]
    text=("Aloha "+student+
             ",\n\nOne of the drawbacks of Google Classroom is that it doesn't give a nice summary of your grades. "+
             "So I've created a summary for you as an update on your total points, points in lab activities, and points through extra credit activities. "+
             "Note that these grades are not final and can change based on revisions as well as late submission deductions.\n\n"+
             "Please contact me if you have any questions regarding the information in this message.\n\n"+
             "As with any automated message, there may be problems/mistakes in this message. Please contact me if something is off and needs to be corrected." +
             "\n\nBest,\nHolm \n\n# BEGIN SUMMARY\n\n"+
             "Last Update: 11/16 @ noon "
             "\nYour Total Points: " +str(grader.stats[id][0]) + " out of " + str(grader.full[0]) + " possible points" +
             "\nYour Lab Activity Points: " +str(grader.stats[id][1])+ " out of " + str(grader.full[1]) + " possible points" +
             "\nYour Extra Credit Points: "  +str(grader.stats[id][2])+ " out of " + str(grader.full[2]) + " possible points" )
    print text

    img =  grader.plot_grades('Lab Act', id)
    emailer.send_image(grader.emails[id], 'ITM387K: Grade Report for '+student, text, img)
