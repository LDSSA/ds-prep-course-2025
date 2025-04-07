import random

def card_deck():
    return random.randrange(15)

def hints (exercise, hint_number):

    """
    hints (exercise, hint_number)
    exercise: string with exercise number/chapter for example "1.1"
    hint_number: int, number of hint,  for example 1  - there are up to 3 for each exercise
    """

    hint="If you need more help please reach out to your instructors on slack."

    if exercise == "1.1":
        if hint_number==1:
            hint="Check SLU04 - 3 Data Structure - Dictionary on how to create dictonaries."
    elif exercise == "1.2":
        if hint_number==1: 
            hint="Check Learning Notebook 1 of this SLU to remind yourself of the rules of precedence."
        elif hint_number==2:   
            hint="The table of precedence is here: https://docs.python.org/3/reference/expressions.html#operator-precedence."  
        elif hint_number==3:
            hint="If you do not remember lists check SLU04 - also don't forget the quotation marks for the strings."  
    elif exercise == "1.3":
        if hint_number==1: 
            hint= "Look at the code in the picture and try to think like python would."
        elif hint_number==2:
            hint= "All solutions should be lower case strings, just like in the picture above."
    elif exercise == "2.1":
        if hint_number==1: 
            hint="Check the unit of the height in your table."
        elif hint_number==2:
            hint="You can loop over entries in a dictonary, check Learning notebook 2: for loops with dictionaries."
        elif hint_number==3: 
            hint="Try using a for loop and loop over the values of the entries."
    elif exercise == "2.2":
        if hint_number==1: 
            hint="Try using a while loop."
        elif hint_number==2: 
            hint="Don't forget to update Wendus height each time the loop runs to avoid an infinity loop. Also dont forget to count the times the loop runs."
        elif hint_number==3:
            hint="Don't forget to calculate Wendus new BMI."
    elif exercise == "2.3":
        if hint_number==1:
            hint="To save all the BMIs in a list, remember the append() function."
        elif hint_number==2:
            hint="You can count the number of balls as executions of the loop."
        elif hint_number==3:
            hint="You can use two variables for the condition of the while loop, each of which can change during the execution of the loop."
    elif exercise == "2.4":
        if hint_number==1: 
            hint="You can use a for loop."
        elif hint_number==2:
            hint="Do you remember range()?"
        elif hint_number==3:
            hint="Use one variable for the prize pool and one for the nex value you want to add to it."
    elif exercise == "3.1":
        if hint_number==1:
            hint="You can use append() to add an eligible candidate to the list."
        elif hint_number==2:
            hint="If you do not remember all the ways to loop over the items of a dictionary check here: Learning notebook 2: for loops with dictionaries."
        elif hint_number==3:
            hint="Use sorted() to put the list in the right order."
    elif exercise == "3.2":
        if hint_number==1:
            hint="You can have one loop in another -check Nested while and for loops."
        elif hint_number==2:
            hint="Make sure to only calculate the height for players that participate."
        elif hint_number==3:
            hint="Remember the climbed height is in centimetres."
    elif exercise == "3.3":
        if hint_number==1:
            hint="Check out how to sort a dictionary with sorted() in the link provided."
        elif hint_number==2:
            hint="You can access values of a list by their index, check out SLU04 if you do not remember how."
    elif exercise == "3.4":
        if hint_number==1:
            hint= "Use a while loop and check if two conditions are simultaneously fullfilled."
        elif hint_number==2:
            hint= " % can be used to calculate the rest of a division, do not forget to count the number of fills."
        elif hint_number==3:
            hint= "Use if and elif conditions to determine the winning team and the laster player of each."
    elif exercise == "4.1":
        if hint_number==1:
            hint="Do not forget about range() ."
        elif hint_number==2:
            hint= "Get the rest of a division using % ."
        elif hint_number==3:
            hint= "You can combine for and if for list comprehension."
    elif exercise == "4.2":
        if hint_number==1:
            hint= "You can check if several conditions are true with any() ."
        elif hint_number==2:
            hint= "You can use another for loop within any"
        elif hint_number==3:
            hint= "Don't forget to check if the rest of the division is 0 with % ."
    elif exercise == "4.3":
        if hint_number==1:
            hint= "You can nest for loops for list comprehension to create lists in lists."
        elif hint_number==2:
            hint= "You can calculate each value of the matrix from its indices."
        elif hint_number==3:
            hint= "Just assigning the matrix as list of lists is kind of cheating."

    print(hint)
