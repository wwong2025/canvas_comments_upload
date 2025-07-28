from canvasapi import Canvas
import os
import csv
CANVAS_API_URL = "https://XXXXX"             # XXXXX: insert canvas url
CANVAS_API_KEY_PERSONAL = "XXXXX"   # XXXXX: insert between quotation marks api key from canvas settings generate key

course_id = XXXXX               # XXXXX: comp 1021 summer 2025 from canvas course page url
assignment_id = XXXXX         # XXXXX: Lab 2 Sketchbook from canvas grades download title cell
#test_user_id =  XXXXX           # XXXXX: user_id frm canvas grades download file, NOT canvas id or just ID

canvas = Canvas(CANVAS_API_URL,CANVAS_API_KEY_PERSONAL)
course = canvas.get_course(course_id)
#current_user = canvas.get_current_user()
#print (current_user.name,current_user.id, current_user.permissions)

comments_folder = "XXXXX"        # XXXXX: insert folder path
commments_csv = "XXXXX"         # XXXXX: insert file name or csv file. first column user_id (NOT sis id or just ID), second column: comments written for that user_id
comments_dict = {}
with open(comments_folder+"\\"+commments_csv,"r",newline='') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    #headers = next (csv_reader)    ## needed only if there is a title row
    for row in csv_reader:
        comments_dict[row[0]] = row[1]
#print (f"{list(comments_dict.items())[:2]}", comments_dict[str(test_user_id)])


assignment = course.get_assignment(assignment_id)
submissions = assignment.get_submissions()
for submission in submissions:
    print (submission.user_id,submission.grade,end=' ')
    if str(submission.user_id) in comments_dict.keys():
        comments = comments_dict[str(submission.user_id)]
        print(comments)
        #submission.edit(comment={"text_comment":"test"})
        if comments != None:
            submission.edit(comment={"text_comment":comments})



