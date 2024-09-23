from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.
def home(request):
    # data=Student.objects.all()                   #================show all the data
    # print(data)
    # data=Student.objects.all().first()                       # 2type of query ---> single object query,multiple object query
    # print(data)
    # data=Student.objects.all().filter(stu_city="bhopal")     #==============filter
    # print(data.values())

    # data=Student.objects.all().exclude(stu_name="neeraj")     #============which object is excluded
    # print(data.values())

    # data=Student.objects.all().order_by('stu_name')  # =========object arrange in ascending order=======
    # print(data.values())
    # data=Student.objects.values('stu_name')   #==============show values
    # print(data)

    # data=Student.objects.values('stu_name')[::2]   #==========slicing
    # print(data)
 

#=================================single object query=======================================,,,,.
    data0 = Student.objects.get(id=2)
    print(data0)

    # data0 = Student.objects.first()
    # print(data0)
    
#  ===============order the data in ascending and descending order============================
    # data0 = Student.objects.order_by("stu_name").first()
    # print(data0)

    # data0 = Student.objects.order_by("-stu_name").first()
    # print(data0)

    # ==================create the data in database=================
    '''
    data0=Student.objects.create(stu_name='sakshi',stu_city='mumbai')
    print(data0.stu_name,data0.stu_city)
    '''

    # =================get_or_create=======combine=============
    '''
    data,created=Student.objects.get_or_create(stu_name="raj",stu_city="jabalpur",stu_email="raj@gmail.com")
    print(data.id,data.stu_name,data.stu_city,data.stu_email)
    '''

   #=====================delete================
    # data=Student.objects.get(id=4).delete()
    # print(data) or
    # data=Student.objects.get(id=8)
    # data.delete()

    # data=Student.objects.filter(stu_name="himanshi").delete()
    # print(data)
    return HttpResponse('hello...................')