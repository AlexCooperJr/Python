from bakery import assert_equal
from bakery_canvas import get_courses
from bakery_canvas import get_submissions, Submission
import matplotlib.pyplot as plt
from datetime import datetime
'''
This file uses canvas data and ONLY canvas data. To use you must first obtain a canvas user_token from the canvas settings
'''
def count_courses(user_token: str) -> int:
    '''
    Purpose:
        This function intakes a user_token and produces the the number of courses
        they are taking.
    Arguements:
        user_token: represents a unique ID for the user to access data
    Returns:
        sum: the total sum of the amount of courses
    '''
    sum=0
    course_list=get_courses(user_token)
    for course in course_list:
        sum=sum+1
    return sum

def find_cs1(user_token:str)->int:
    '''
    Purpose: 
        This function intakes a unique str representing a user token and returns the 
        id for the course which is an integer
    Arguement:
        user_token: a string that represents a unique person to access data on them
    Returns:
        course id as an integer or 0 if CISC1 cannot be found
    '''
    new_list=[]
    course_list=get_courses(user_token)
    if course_list==[]:
        return 0
    for course in course_list:
        if "CISC1" in course.code:
            new_list.append(course.id)
            return new_list[0]
    else: 
        return 0

def find_course(user_token:str,course_id:int)->str:
    '''
    Purpose:
        This funtion intakes a user_token as a string and an integer representing the 
        course id and looks for the full name of the course
    Arguements:
        user_token: a strng representing a unique user token used to access their data
        course_id: an integer represetning a unique code for each course
    Returns:
        Returns a string either the courses full name or "no courses found"
        if the course_id does not match any in the user token data
    '''
    course_list=get_courses(user_token)
    for course in course_list:
        if course_id==course.id:
            return course.name
    else:
        return "no course found"   

def render_courses(user_token:str)->str:
    '''
    Purpose:
        
    Arguements:
        
    Returns:
        
    '''
    final=""
    course_list=get_courses(user_token)
    if course_list==[]:
        return ""
    else:
        for course in course_list:
            id_string=str(course.id)
            final=final+id_string+":"+" "+course.code+"\n"
        return final

def total_points(user_token:str,course_id:int)->int:
    '''
    Purpose:
        This function will intake a user_token:a string and a course_id:an integer and return
        an integer representing the total points. This is done by using the get_submissions 
        funtion to retrieve the submissions and adding up all the points_possible values
    Arguements:
        user_token: a string representing a unique code for each individuals canvas 
        course_id: an integer representing the course id of a specific course   
    Returns:
        total_points: an integer representing the total amount of points available in the course
    '''
    
    total_points=0
    submissions=get_submissions(user_token,course_id)
    for submission in submissions:
        total_points=total_points+submission.assignment.points_possible
    return total_points

#assert_equal(total_points('annie', 679554), 420)
#assert_equal(total_points('annie', 386814), 700)
#assert_equal(total_points('annie', 100167), 1060)
#assert_equal(total_points('jeff', 679554), 420)
#assert_equal(total_points('jeff', 386814), 700)
#assert_equal(total_points('troy', 394382), 100)

def count_comments(user_token:str,course_id:int)->int:
    '''
     Purpose:
        This function will intake a user_token:a string and a course_id:an integer and return
        an integer representing the amount of comments left on submitted assignments. This is done by using the get_submissions 
        funtion to retrieve the submissions and adding up all instances of comments within the submissions
    Arguements:
        user_token: a string representing a unique code for each individuals canvas 
        course_id: an integer representing the course id of a specific course   
    Returns:
        count: an integer representing the total amount of comments across the submissions
    '''
    count=0
    submissions=get_submissions(user_token,course_id)
    for submission in submissions:
        for comment in submission.comments:
            count=count+1
    return count
            
#assert_equal(count_comments('annie', 679554), 14)
#assert_equal(count_comments('annie', 386814), 1)
#assert_equal(count_comments('jeff', 679554), 5)
#assert_equal(count_comments('jeff', 386814), 6)
#assert_equal(count_comments('troy', 394382), 0)

def ratio_graded(user_token:str,course_id:int)->str:
    '''
     Purpose:
        This function will intake a user_token:a string and a course_id:an integer and return
        a string representing ratio of graded assingments. This is done by using the get_submissions 
        funtion to retrieve the submissions and adding up all the assignments that have been graded
        and adding up all the assignments in the course. These integers are then converted into strings
        adn added together. 
    Arguements:
        user_token: a string representing a unique code for each individuals canvas 
        course_id: an integer representing the course id of a specific course   
    Returns:
        ratio: an string that represents the amount of graded assignments (an integer converted to a string) 
               with the "/" and then the total amount of assignments as a string (an integer converted to a string)
    '''
    graded_count=0
    total_count=0
    submissions=get_submissions(user_token,course_id)
    for submission in submissions:
        if submission.graded_at!="":
            graded_count=graded_count+1
        total_count=total_count+1
    graded_count=str(graded_count)
    total_count=str(total_count)
    ratio=graded_count+"/"+total_count
    return ratio

#assert_equal(ratio_graded('annie', 679554), "10/10")
#assert_equal(ratio_graded('annie', 134088),"6/11" )

def average_score(user_token:str,course_id:int)->float:
    '''
     Purpose:
        This function will intake a user_token:a string and a course_id:an integer and return
        a float representing the amount of points scored divided by the total points of graded assignments. 
        This is done by using the get_submissions funtion to retrieve the submissions 
        and adding up all the scores and adding up all the points_possible values from graded assignments then dividing
    Arguements:
        user_token: a string representing a unique code for each individuals canvas 
        course_id: an integer representing the course id of a specific course   
    Returns:
        averaged_score: an integer representing the the amount of earned points
                        divided by the total amount of points available for ONLY assignments that have been graded.
    '''
    graded_points=0
    total_points=0
    submissions=get_submissions(user_token,course_id)
    for submission in submissions:
        if submission.graded_at!="":
            graded_points=graded_points+((submission.score))
            total_points=total_points+submission.assignment.points_possible
            averaged_score= graded_points/total_points
    return averaged_score

#assert_equal(average_score('annie', 679554), 0.95)
#assert_equal(average_score('annie', 386814),0.97)
#assert_equal(average_score('jeff', 386814), 0.70)

def average_weighted(user_token:str,course_id:int)->float:
    '''
     Purpose:
        This function will intake a user_token:a string and a course_id:an integer and return
        a float representing average scores after being weighted of graded assignments in a course.
        This is done by using the get_submissions funtion to retrieve the submissions and adding up 
        all the scores after they have been multiplied by the weight. Then adding up all the 
        points_possible values after weighting of them. The integers are then divided. 
    Arguements:
        user_token: a string representing a unique code for each individuals canvas 
        course_id: an integer representing the course id of a specific course   
    Returns:
        average_weighted: a float representing the averaged score after being weighted for all graded
                          assignments
    '''
    graded_points=0
    total_points=0
    submissions=get_submissions(user_token,course_id)
    for submission in submissions:
        if submission.graded_at!="":
            graded_points=graded_points+((submission.score)*submission.assignment.group.weight)
            total_points=total_points+(submission.assignment.points_possible*submission.assignment.group.weight)
            average_weighted=graded_points/total_points
    return average_weighted

#assert_equal(average_weighted('annie', 679554), 0.9471153846153846)
#assert_equal(average_weighted('annie', 386814),0.97)
#assert_equal(average_weighted('jeff', 386814), 0.70)

def average_group(user_token:str,course_id:int,group_name:str)->float:
    '''
    Purpose:
        This function will intake a user_token:a string, a course_id:an integer and a group_name:a string
        and returns a float representing average scores within a specific category of graded assignments in a course.
        This is done by using the get_submissions funtion to retrieve the submissions and adding up 
        all the scores of assignments that are within the group determined by the group_name.
        Then adding up all the points_possible values among graded assignments in the group. 
        The integers are then divided. 
    Arguements:
        user_token: a string representing a unique code for each individuals canvas 
        course_id: an integer representing the course id of a specific course   
        group_name: a string representing a specific category within a course
    Returns:
        group_average: a float representing the averaged grade ratio between assignments within the same subset
                       of a course for example, homework.
        0.0: is returned in the case that no assignments can be found in the category or 
             no assignments in the category are graded.
    '''
    points_earned=0
    total_points=0
    submissions=get_submissions(user_token,course_id)
    group_name=group_name.lower()
    for submission in submissions:
        if submission.assignment.group.name.lower()==group_name:
            if submission.graded_at!="":
                points_earned=points_earned+submission.score
                total_points=total_points+submission.assignment.points_possible
    if total_points != 0:
        group_average= points_earned/total_points
        return group_average
    else:
        return 0.0

#assert_equal(average_group('abed', 134088,'homeWORK'),0.796)
#assert_equal(average_group('annie', 679554,"homework"), 0.9636363636363636)
#assert_equal(average_group('annie', 134088,'homeWORK'),0.9379999999999999)
#assert_equal(average_group('jeff', 386814,"homework"), 0.0)

def render_assignment(user_token:str,course_id:int,assignment_id:int)->str:
    '''
    Purpose:
        This function will intake a user_token:a string, a course_id:an integer and an assignment_id:an integer
        and return a string representing an assingment. This is done in smaller steps. using get_submissions the submissions
        are obtained, the submissions are then checked for a matching assignment_id. if they match the the info for the submission
        is recorded this includes the assignment name, group, module, and grade (unless a grade is unavailble). This information
        is converted to a string if not already a string value, then added together, using "\n" to seperate lines.
    Arguements:
        user_token: a string representing a unique code for each individuals canvas 
        course_id: an integer representing the course id of a specific course   
        assignment_id: an integer representing a unique id for each indivdual assignment
    Returns:
        lines: a columination of 4 seperate lines that are determined by the funtion
        "Assignment missing:...": this is the return when an assignment_id does not match 
                                  any within the submissions
    '''
    new_list=[]
    submissions=get_submissions(user_token,course_id)
    for submission in submissions:
        if submission.assignment.id==assignment_id:
            assignment_id=str(assignment_id)+": "
            assignment_name=submission.assignment.name
            line_1=assignment_id+assignment_name+"\n"
            group_name=submission.assignment.group.name
            line_2="Group: " + group_name + "\n"
            module_name=submission.assignment.module
            line_3="Module: " +module_name+"\n"
            if submission.graded_at!="":
                score=str(submission.score)
                points_possible=str(submission.assignment.points_possible)
                grade=submission.grade
                line_4="Grade: " + score + "/" + points_possible + " " + "("+grade+")"
            else:
                line_4="Grade: (missing)"
            new_list.append( line_1+line_2+line_3+line_4)
    if new_list==[]:
        return "Assignment missing: " + str(assignment_id)
    else:
        lines= line_1+line_2+line_3+line_4
        return lines
        
#assert_equal(render_assignment('annie', 679554, 7), 'Assignment missing: 7')
#assert_equal(render_assignment('annie', 679554, 299650), '299650: Introduction\nGroup: Homework\nModule: Module 1\nGrade: 10.0/10 (A)')
#assert_equal(render_assignment('annie', 679554, 553716), '553716: Basic Addition\nGroup: Homework\nModule: Module 2\nGrade: 14.0/15 (A)')
#assert_equal(render_assignment('annie', 679554, 805499), '805499: Basic Subtraction\nGroup: Homework\nModule: Module 2\nGrade: 19.0/20 (A)')
#assert_equal(render_assignment('annie', 134088, 937202), '937202: Technology in the outdoor classroom\nGroup: Homework\nModule: Module 2\nGrade: (missing)')
#assert_equal(render_assignment('jeff', 386814, 24048), '24048: HOMEWORK 3\nGroup: Assignments\nModule: MODULE 1\nGrade: 58.0/100 (F)')        

def render_all(user_token:str,course_id:int)->str:
    '''
     Purpose:
        This function will intake a user_token:a string, and a course_id:an integer and returns phrase which
        is a string representing the id, name, and graded status for each assignment in a course. This is done by 
        obtaining the submissions then finding the id and name for the assignment, then determining
        whether it is graded or not this is done for each assignment,the info for each assignment is converted to a string
        then the strings are added together
    Arguements:
        user_token: a string representing a unique code for each individuals canvas 
        course_id: an integer representing the course id of a specific course   
    Returns:
        phrase: a string representing the columination of assignment id, name, and whether or not its graded for
                for each assignment in a course
    '''
    data_list=[]
    phrase=""
    submissions=get_submissions(user_token,course_id)
    for submission in submissions:
        assignment_id=str(submission.assignment.id)+": "
        assignment_name=submission.assignment.name
        part_1=assignment_id+assignment_name
        if submission.graded_at!="":
            part_2="(graded)"+"\n" 
        else:
            part_2="(ungraded)"+"\n"
        render=part_1+" "+part_2
        data_list.append(render)
    for data in data_list:
        phrase=phrase+data
    return phrase
    
#assert_equal(render_all('annie', 679554),'299650: Introduction (graded)\n553716: Basic Addition (graded)\n805499: Basic Subtraction (graded)\n749969: Basic Multiplication (graded)\n763866: Basic Division (graded)\n979025: Midterm 1 (graded)\n870878: Logarithms (graded)\n126393: Antiderivatives (graded)\n122494: Actual Sorcery (graded)\n683132: Final Exam (graded)\n')
#assert_equal(render_all('annie', 134088),'674440: Welcome (graded)\n735575: History of Phys Ed Instruction (graded)\n11003: Fundamentals of Instructional Design (graded)\n633504: Academic Motivation and Football (graded)\n472737: Assessment Design (graded)\n419696: Self-regulation, Rules, and Regulations (graded)\n937202: Technology in the outdoor classroom (ungraded)\n796663: Advanced Advancing (ungraded)\n712831: Teacher Placements (ungraded)\n388186: Teacher Placements II (ungraded)\n378705: Final Exam (ungraded)\n')
#assert_equal(render_all('jeff', 386814),'806809: HOMEWORK 1 (graded)\n212220: HOMEWORK 2 (graded)\n24048: HOMEWORK 3 (graded)\n982248: HOMEWORK 4 (graded)\n269027: HOMEWORK 5 - COPY 1 (graded)\n476501: HOMEWORK 7 (graded)\n654144: HOMEWORK 8 FINAL (graded)\n')

def plot_scores(user_token:str,course_id:int):
    '''
     Purpose:
        This function will intake a user_token:a string, a course_id:an integer and uses this info to create a graph
        The graph represents the distribution of fractional scores of graded assignments that are worth more than 0 points
        fractional scores are determined by dividing the score by the points possible then multiplying by 100. This value is then
        passed into the plt.hist function.
    Arguements:
        user_token: a string representing a unique code for each individuals canvas 
        course_id: an integer representing the course id of a specific course   
    Returns:
        this function doesnt technically return anything, it prints a graph.
    '''
    data_list=[]
    submissions=get_submissions(user_token,course_id)
    for submission in submissions:
        if submission.graded_at!='':
            if submission.assignment.points_possible>0:
                fractional_score=submission.score/submission.assignment.points_possible
                fractional_score=fractional_score*100
                data_list.append(fractional_score)
    plt.title("Distribution of fractional scores")
    plt.xlabel("fractional score")
    plt.ylabel("Times scored")
    plt.hist(data_list)
    plt.show()

#plot_scores('annie', 100167)
#plot_scores('abed', 100167)
#plot_scores('jeff', 100167)

def days_apart(first_date: str, second_date: str) -> int:
    """
    Determines the days between `first` and `second` date.
    Do not modify this function!
    """
    first_date = datetime.strptime(first_date, "%Y-%m-%dT%H:%M:%S%z")
    second_date = datetime.strptime(second_date, "%Y-%m-%dT%H:%M:%S%z")
    difference = second_date - first_date
    return difference.days

def plot_earliness(user_token:str,course_id:int):
    '''
     Purpose:
        This function will intake a user_token:a string, a course_id:an integer and uses this info to create a graph
        The graph represents the distribution of how early assignments are being submitted. This is determined by 
        determining the submission date and due date then using the helper function to determine the difference
        This value is then passed into the plt.hist function.
    Arguements:
        user_token: a string representing a unique code for each individuals canvas 
        course_id: an integer representing the course id of a specific course   
    Returns:
        this function doesnt technically return anything, it prints a graph.
    '''
    data_list=[]
    submissions=get_submissions(user_token,course_id)
    for submission in submissions:
        if submission.submitted_at!="":
            if submission.assignment.due_at:
                first_date=submission.submitted_at
                second_date=submission.assignment.due_at
                difference=days_apart(first_date,second_date)
                data_list.append(difference)
    plt.title("Distribution of Early Submssions")
    plt.xlabel("Days Early")
    plt.ylabel("Times Submitted Early")
    plt.hist(data_list)
    plt.show()
        
#  ...

#plot_earliness('annie', 100167)
#plot_earliness('abed', 100167)
#plot_earliness('jeff', 100167)

def plot_points(user_token:str,course_id:int):
    '''
    Purpose:
        This function will intake a user_token:a string, a course_id:an integer and uses this info to create a graph
        The graph represents the comparison between the unweighted points possible to the weighted points possible. To determine 
        weighted points possible, the function adds the points possible time to the weight of the group this finds the total. This integer is then 
        divided by 100. From there the points possible is multiplied by its group weight then divided by the total. This integer deemed y_value 
        represents the y value. the x value is found by identifying submission.assignment.points_possible
    Arguements:
        user_token: a string representing a unique code for each individuals canvas 
        course_id: an integer representing the course id of a specific course   
    Returns:
        this function doesnt technically return anything, it prints a graph.
    '''
    x_list=[]
    y_list=[]
    submission_list=[]
    total_weighted_points=0
    submissions=get_submissions(user_token,course_id)
    for submission in submissions:
        submission_list.append(submission) 
        total_weighted_points=total_weighted_points+(submission.assignment.points_possible*submission.assignment.group.weight)
    total_weighted_points=total_weighted_points/100
    for submission in submissions:
        if total_weighted_points!=0:
            y_value=((submission.assignment.points_possible*submission.assignment.group.weight)/total_weighted_points)
            y_list.append(y_value)
            x_value=submission.assignment.points_possible
            x_list.append(x_value) 
    plt.xlabel("points possible")
    plt.ylabel("weighted points possible")
    plt.title("points possible compared to weighted points possible")
    plt.scatter(x_list,y_list)
    plt.show()

#plot_points('annie', 100167)
#plot_points('annie', 679554)
#plot_points('annie', 386814)

def predict_grades(user_token:str,course_id:int):
    '''
    Purpose:
        This function will intake a user_token:a string, a course_id:an integer and uses this info to create a graph
        The graph that represents the comparison of 3 seperate instances of grades possible. The first instance is the max
        amount of points a student could score. The second is the event that they receive perfect scores on all remaining
        ungraded assignments. The final instances would be if the student scored 0 on remaining ungraded assignments
    Arguements:
        user_token: a string representing a unique code for each individuals canvas 
        course_id: an integer representing the course id of a specific course   
    Returns:
        this function doesnt technically return anything, it prints a graph.
    '''
    x_list=[]
    max_points_list=[]
    max_score_list=[]
    max_score_list2=[]
    min_score_list=[]
    min_list=[]
    weighted_points_possible=0
    total_score=0
    max_points=0
    max_score=0
    min_score=0
    submissions=get_submissions(user_token,course_id)
    for submission in submissions:
        max_points=max_points+(submission.assignment.points_possible*submission.assignment.group.weight)
    max_points=max_points/100
    for submission in submissions:
        total_score=total_score+(submission.assignment.points_possible*submission.assignment.group.weight)
        x=total_score/max_points
        max_points_list.append(x)
    for submission in submissions:
        if submission.graded_at!="":
            max_score_list.append(submission.score*submission.assignment.group.weight)
        if submission.graded_at=="":
            max_score_list.append(submission.assignment.points_possible*submission.assignment.group.weight)
    for score in max_score_list:
        max_score=max_score+score
        maximum=max_score/max_points
        max_score_list2.append(maximum)       
    for submission in submissions:
        if submission.graded_at!="":
            min_score_list.append(submission.score*submission.assignment.group.weight)
        if submission.graded_at=="":
            min_score_list.append(0)
    for score in min_score_list:
        min_score=min_score+score
        minimum=min_score/max_points
        min_list.append(minimum)
    plt.title("Grade Predictions")
    plt.xlabel("Number of Assignments")
    plt.ylabel("Possible Grade")
    plt.plot(max_points_list)
    plt.plot(max_score_list2)
    plt.plot(min_list)
    plt.show()

#print("Introduction to Computer Science")
#predict_grades('annie', 100167)
#predict_grades('abed', 100167)
#predict_grades('jeff', 100167)
#print("Physical Education Education")
#predict_grades('annie', 134088)
#predict_grades('abed', 134088)
#predict_grades('jeff', 134088)
    
def execute(command:str,user_token:str,course_id:int)->int:
    '''
    Purpose: This function will intake a user command, a string a user token, another string and a course_id an integer
             The function will match the command to the appropriate request and produce the proper informations
    Arguements:
            command: a string that is input by the user (technically comes from the main function)
            user_token: a string representing a unique code for each individuals canvas 
            course_id: an integer representing the course id of a specific course   
    Returns:
           This function can return a range of outputs based upon the request(see the docstring for the specific functions for more info)    
    '''
    if command=="course":
        print(render_courses(user_token))
        new_id=input("Please input new ID")
        new_id=int(new_id)
        print(find_course(user_token,new_id))
        return new_id
    if command=="exit":
        return 0
    if command=="points":
        points=total_points(user_token,course_id)
        print(points)
        return course_id
    if command=="comments":
        comments=count_comments(user_token,course_id)
        print(comments)
        return course_id
    if command=="graded":
        graded=ratio_graded(user_token,course_id)
        print(graded)
        return course_id
    if command=="score_unweighted":
        unweighted_score=average_score(user_token,course_id)
        print(unweighted_score)
        return course_id
    if command=="score":
        score=average_weighted(user_token,course_id)
        print(score)
        return course_id
    if command=="group":
        print("input group name")
        group_name=input()
        group=average_group(user_token,course_id,group_name)
        print(group)
        return course_id
    if command=="assignment":
        print("input assignment id")
        assignment_id=input()
        assignment_id=int(assignment_id)
        assignment_render=render_assignment(user_token,course_id,assignment_id)
        print(assignment_render)
        return course_id
    if command=="list":
        list_render=render_all(user_token,course_id)
        print(list_render)
        return course_id
    if command=="scores":
        plot_scores(user_token,course_id)
        return course_id
    if command=="earliness":
        plot_earliness(user_token,course_id)
        return course_id
    if command=="compare":
        plot_points(user_token,course_id)
        return course_id
    if command=="predict":
        predict_grades(user_token,course_id)
        return course_id
    if command=="help":
        print("exit > Exit the application"+"\n"+"help > List all the commands"+"\n"+"course > Change current course"+"\n"+"points > Print total points in course"+"\n"+"comments > Print how many comments in course"+"\n"+"graded > Print ratio of ungraded/graded assignments"+"\n"+"score_unweighted > Print average unweighted score"+"\n"+"score > Print average weighted score"+"\n"+"group > Print average of assignment group, by name"+"\n"+"assignment > Print the details of a specific assignment, by ID"+"\n"+"list > List all the assignments in the course"+"\n"+"scores > Plot the distribution of grades in the course"+"\n"+"earliness > Plot the distribution of the days assignments were submitted early"+"\n"+"compare > Plot the relationship between assignments' points possible and their weighted points possible"+"\n"+"predict > Plot the trends in grades over assignments, showing max ever possible, max still possible, and minimum still possible")
        return course_id
    else: 
        return course_id
              
def main(user_token:str):
    '''
    Purpose: This function acts as a gateway between the user and the execute function
    Arguments: 
             user_token: a string representing a unique code for each individuals canvas 
    Returns: this function doesnt return anything (it can return "no courses available if the user has no courses)
             but it interacts to give a course_id to the execute function
    '''
    current_course_ID=0
    course_count=count_courses(user_token)
    if course_count==0:
        return print("No courses available")
    else:
        course_id=find_cs1(user_token)
        if course_id==0:
            courses_list=get_courses(user_token)
            course=courses_list[0]
            current_course_ID=course.id            
        if course_id!=0:
            current_course_ID=course_id
    while current_course_ID!=0:
        command=input("Please input your request , 'exit', or 'help'")
        executed=execute(command,user_token,current_course_ID)
        current_course_ID=executed
main(input("Please type your user token"))

#assert_equal(total_points('annie', 679554), 420)
#assert_equal(total_points('annie', 386814), 700)
#assert_equal(total_points('annie', 100167), 1060)
#assert_equal(total_points('jeff', 679554), 420)
#assert_equal(total_points('jeff', 386814), 700)
#assert_equal(total_points('troy', 394382), 100)
        
#assert_equal(count_comments('annie', 679554), 14)
#assert_equal(count_comments('annie', 386814), 1)
#assert_equal(count_comments('jeff', 679554), 5)
#assert_equal(count_comments('jeff', 386814), 6)
#assert_equal(count_comments('troy', 394382), 0)

#assert_equal(ratio_graded('annie', 679554), "10/10")
#assert_equal(ratio_graded('annie', 134088),"6/11" )

#assert_equal(average_score('annie', 679554), 0.95)
#assert_equal(average_score('annie', 386814),0.97)
#assert_equal(average_score('jeff', 386814), 0.70)

#assert_equal(average_weighted('annie', 679554), 0.9471153846153846)
#assert_equal(average_weighted('annie', 386814),0.97)
#assert_equal(average_weighted('jeff', 386814), 0.70)

#assert_equal(average_group('abed', 134088,'homeWORK'),0.796)
#assert_equal(average_group('annie', 679554,"homework"), 0.9636363636363636)
#assert_equal(average_group('annie', 134088,'homeWORK'),0.9379999999999999)
#assert_equal(average_group('jeff', 386814,"homework"), 0.0)

#assert_equal(render_assignment('annie', 679554, 7), 'Assignment missing: 7')
#assert_equal(render_assignment('annie', 679554, 299650), '299650: Introduction\nGroup: Homework\nModule: Module 1\nGrade: 10.0/10 (A)')
#assert_equal(render_assignment('annie', 679554, 553716), '553716: Basic Addition\nGroup: Homework\nModule: Module 2\nGrade: 14.0/15 (A)')
#assert_equal(render_assignment('annie', 679554, 805499), '805499: Basic Subtraction\nGroup: Homework\nModule: Module 2\nGrade: 19.0/20 (A)')
#assert_equal(render_assignment('annie', 134088, 937202), '937202: Technology in the outdoor classroom\nGroup: Homework\nModule: Module 2\nGrade: (missing)')
#assert_equal(render_assignment('jeff', 386814, 24048), '24048: HOMEWORK 3\nGroup: Assignments\nModule: MODULE 1\nGrade: 58.0/100 (F)')        

#plot_scores('annie', 100167)
#plot_scores('abed', 100167)
#plot_scores('jeff', 100167)

#plot_points('annie', 100167)
#plot_points('annie', 679554)
#plot_points('annie', 386814)

#print("Introduction to Computer Science")
#predict_grades('annie', 100167)
#predict_grades('abed', 100167)
#predict_grades('jeff', 100167)
#print("Physical Education Education")
#predict_grades('annie', 134088)
#predict_grades('abed', 134088)
#predict_grades('jeff', 134088)
