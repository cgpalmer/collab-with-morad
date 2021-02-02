from django.shortcuts import render


# Create your views here.
def view_profiles(request):
    return render(request, 'calendars/view_calendar.html')
