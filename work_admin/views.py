from django.shortcuts import render

# Create your views here.
def view_work_admin(request):
    return render(request, 'work_admin/work_admin.html')
