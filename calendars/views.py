from django.shortcuts import render

# Create your views here.
def view_calendar(request):
    return render(request, 'calendars/view_calendar.html')
