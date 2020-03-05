#!/bin/python

"""
Build a calendar.

A meeting is stored as a tuple of integers (start_time, end_time). 
These integers represent the number of 30-minute blocks past 9:00am.

For example:

(2, 3)# Meeting from 10:00-10:30 am
(6, 9)# Meeting from 12:00-1:30 pm

Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges.

For example, given:

  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
 
your function would return:

  [(0, 1), (3, 8), (9, 12)]
 
Do not assume the meetings are in order. The meeting times are coming from multiple teams.

Write a solution that's efficient even when we can't put a nice upper bound on the numbers representing our time ranges. 
Here we've simplified our times down to the number of 30-minute slots past 9:00 am. 
But we want the function to work even for very large numbers, like Unix timestamps. 
In any case, the spirit of the challenge is to merge meetings where start_time and end_time don't have an upper bound.
"""

def merge_ranges(meetings):
    
    sorted_meetings = sorted(meetings)
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_ending in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_ending))
        else:
            merged_meetings.append((current_meeting_start, current_meeting_ending))

    return merged_meetings

if __name__ == '__main__':

    meetings =  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    print(merge_ranges(meetings))
    print("Should return {}".format([(0, 1), (3, 8), (9, 12)]))
