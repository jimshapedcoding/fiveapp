from django.shortcuts import render
from codingsession.models import CodingSession
from django.utils.timezone import utc
import datetime
# Create your views here.

def codingsessionspage(request):
    current_time = datetime.datetime.utcnow().replace(tzinfo=utc)
    coding_sessions = CodingSession.objects.filter(starting_time__gte=current_time)
    return render(request, template_name="codingsession/all.html",
                  context={'coding_sessions' : coding_sessions }
                  )
