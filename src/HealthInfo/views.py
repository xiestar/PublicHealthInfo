from django.template import loader,Context
from django.http import HttpResponse
from django.shortcuts import render_to_response

# function for list a table of all health informaiton.
def listHealthInfos(request):
	t = loader.get_template('all-health-table.html')
    c = Context({'healths': 'healths'})
    return HttpResponse(t.render(c))
# function for comparing health indicator.
def CompareIndicatorInfos(request):
    t = loader.get_template('compare-health-indicator.html')
    c = Context({'healths': 'healths'})
    return HttpResponse(t.render(c))
# function for making map of health information.
def MapHealthInfos(request):
    #jsonUrl = "'{% static 'data/beijing.json' %}' "
    #return render_to_response('beijing-map01.html',locals())
    t = loader.get_template('beijing-map01.html')
    return HttpResponse(t.render())
    