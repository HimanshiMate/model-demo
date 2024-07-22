from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.
def home(request):
    data=Student.objects.all()                   #================show all the data
    print(data)
    data=Student.objects.all().first()                       # 2type of query ---> single object query,multiple object query
    print(data)
    data=Student.objects.all().filter(stu_city="bhopal")     #==============filter
    print(data.values())

    data=Student.objects.all().exclude(stu_name="neeraj")     #============which object is excluded
    print(data.values())

    data=Student.objects.all().order_by('stu_name')  # =========object arrange in ascending order=======
    print(data.values())
    data=Student.objects.values('stu_name')   #==============show values
    print(data)

    data=Student.objects.values('stu_name')[::2]   #==========slicing
    print(data)
    



    return HttpResponse("hello..............................")