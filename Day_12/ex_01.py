class Student:
    sub_1 = int(input())
    sub_2 = int(input())
    sub_3 = int(input())
    total = sub_1+sub_2+sub_3
    avg = total/3
    def printing_std():
        print("Enter sub1 val :", Student.sub_1)
        print("Enter sub2 val :", Student.sub_2)
        print("Enter sub3 val :", Student.sub_3)
        print("Total Marks obtained by student is ", Student.total)
        print("Average Marks obtained by student is ", Student.avg)
print("Printing Maarks: ")
printing_std()