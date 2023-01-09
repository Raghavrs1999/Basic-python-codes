fair=float(input("\t\tRailway Ticket\n\nEnter the fair : "))
age=int(input("Enter the age: "))
if age<=5:
    print("You don't have to pay anything child under 5 year is absolutely free")
elif age>5 and age<60:
    c=int(input("Enter your catagory:\n1:General\n2:Other backward class(OBC)\n3:Scheduled Cast(SC)\n4:Scheduled Tribe(ST)\nEnter the option : "))
    if c==1:
        print("There is no consesion for general cast you have to pay Rs.{} only".format(fair))
    elif c==2:
        d=fair*.1;fair=fair-d
        print("You got 10% consesion on your fair noe you have to pay Rs.{} only".format(fair))
    elif c==3:
        d=fair*.12;fair=fair-d
        print("You got 12% consesion on your fair noe you have to pay Rs.{} only".format(fair))
    elif c==4:
        d=fair*.15;fair=fair-d
        print("You got 15% consesion on your fair noe you have to pay Rs.{} only".format(fair))
    elif c>=5:
        print("Please enter the valid input")
elif age>=60:
    dis=fair*.4
    c=int(input("Enter your catagory:\n1:General\n2:Other backward class(OBC)\n3:Scheduled Cast(SC)\n4:Scheduled Tribe\nEnter the option : "))
    if c==1:
        print("There is no consesion for general cast you have to pay Rs.{} only".format(fair))
    elif c==2:
        d=fair*.1;con=dis+d;fair=fair-con
        print("You got 10% consesion on your fair noe you have to pay Rs.{} only".format(fair))
    elif c==3:
        d=fair*.12;con=dis+d;fair=fair-con
        print("You got 12% consesion on your fair noe you have to pay Rs.{} only".format(fair))
    elif c==4:
        d=fair*.15;con=dis+d;fair=fair-con
        print("You got 15% consesion on your fair noe you have to pay Rs.{} only".format(fair))
    elif c>=5:
        print("Please enter the valid input")