sub1 =int(input("give of marks1"))
sub2 =int(input("give of marks2"))
sub3 =int(input("give of marks3"))
if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail")
elif((sub1+sub2+sub3)/3 <40 ):
        print("you are fail due to total percentage less than 40")
else:
        print("you are pass")