from django.template import Context, loader
from apps.models import application
from django.http import HttpResponse
from django.http import Http404


def index(request):
    earliest_deadline_list = application.objects.all().order_by('-deadline_date')[:]
    t = loader.get_template('applications/index.html')
    c = Context({
        'earliest_deadline_list': earliest_deadline_list,
    })
    return HttpResponse(t.render(c))

def detail(request, application_id):
    try:
        p = application.objects.get(pk=application_id)
    except application.DoesNotExist:
        raise Http404
    return render_to_response('applications/detail.html', {'application': p})
