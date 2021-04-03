from django.shortcuts import render
from codingsession.models import CodingSession
# Create your views here.

def codingsessionspage(request):
    coding_sessions = CodingSession.objects.all()
    return render(request, template_name="codingsession/all.html",
                  context={'coding_sessions' : coding_sessions }
                  )
