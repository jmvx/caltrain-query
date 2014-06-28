#!/usr/bin/env python

import datetime
import time
import csv

# Opens schedule and outputs train departure times after current time
def get_upcoming_trains(s,d,w):
    upcoming_trains = []
    filename = "schedule.csv"
    with open(filename,'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == s and row[1] == d and row[2] == w:
                for i in xrange(3,len(row)):
                    arrival_time = datetime.datetime.strptime(row[i],"%H:%M").time()
                    if arrival_time > current_time:
                        upcoming_trains.append(arrival_time.strftime("%I:%M"))
    return upcoming_trains

# Opens schedule and outputs last train departure time for current day
def get_last_train(s,d,w):
    filename = "schedule.csv"
    with open(filename,'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == s and row[1] == d and row[2] == w:
                last_train = datetime.datetime.strptime(row[len(row)-1],"%H:%M").time()
                return last_train.strftime("%I:%M")

# Query
direction = "north"
station = "san jose"
now = datetime.datetime.now()
current_time = datetime.time(now.hour,now.minute)
if  0 <= now.weekday() <= 4:
    day = "weekday"
if now.weekday() == 5:
    day = "saturday"
if now.weekday() == 6:
    day = "sunday"

# Call functions
t = get_upcoming_trains(station,direction,day)
print("Next " + direction.title() + "bound " + station.title() + " Train: " + t[1])
print("Upcoming " + direction.title() + "bound " + station.title() + " Trains: " + t[2] + ", " + t[3] + ", and " + t[4])
print("Last Train Today: " + get_last_train(station,direction,day))

