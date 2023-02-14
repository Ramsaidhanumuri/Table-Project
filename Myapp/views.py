from django.shortcuts import render
from .models import Employees

# Create your views here.
# def index(request):
#     Templates = loader.get_template('index.html')
#     return HttpResponse(Templates.render())

def index(request):
    objects = Employees.objects.all()
    context = {'objects':objects}
    return render(request, 'index.html', context)

def forms(request):
    return render(request, 'form.html')

def forms_submission(request):
    print('Form is submitted')
    employee_id = request.POST['empid']
    last_name = request.POST['lname']
    email = request.POST['email']
    hire_date = request.POST['hdate']
    job = request.POST['job']

    Employees_data = Employees(employee_id=employee_id, last_name=last_name, email=email, hire_date=hire_date, job_id=job)
    Employees_data.save()

    return render(request, 'form.html')