#def my_function():
#print("This is my function")
#my_function()


#def my_function(fname):
#print(fname+"Guleria")
#my_function("Rahul")
#my_function("Rahul2")
#my_function("Rahul3")


#def my_function(fname, lname):
#print(fname + " " + lname)
#my_function("Rahul", "Guleria")


def my_function(students):
    print("topper of class is" +students[0])
    my_function("Riya", "Rahul", "vijay")


    def my_function(child3, child2, child1):
        print("The youngest child is " + child3)
        my_function
        (child1="Rahul,"
        child2="Rahul2"
        child3="Rahul3")


def my_function(**hello):
    print("The last name is" + hello["lname"])
    my_function
    (fname="Rahul",
     lname="Guleria")  


number=[23,5,42,12,37,1,30,16,48,55,8,19,51,26,34,44,0,29,53,39,10,31,17,57,3,25,46,22,14,49,6,41,58,20,36,9,52,7,28,45,15,43,2,24,38,11,33,50,4,59,13,35,18,21,47,27,32,40,54,56]
length=len(number)
print(f"This is the length of the list:{length}")
final_index=(length-1)
print(f"This is the final idex of the list:{final_index}")