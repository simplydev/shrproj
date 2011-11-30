# Create your views here.
from django.template import Context, loader
from django.shortcuts import get_object_or_404,render_to_response
from django.core.urlresolvers import reverse
from smrh.models import Choice, Poll
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from smrh.models import Contact
from smrh.models import CustomForm
from smrh.models import * 
from smrh.forms import * 
from google.appengine.api import users

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    #output = ', '.join([p.question for p in latest_poll_list])
    #return HttpResponse(output)
    #t = loader.get_template('index.html')
    #c = Context({
    #    'latest_poll_list': latest_poll_list,
    #})
    #return HttpResponse(t.render(c))
    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})
    

def detail(request, poll_id):
	try:
        	p = Poll.objects.get(pk=poll_id)
    	except Poll.DoesNotExist:
        	raise Http404
    	return render_to_response('polls/detail.html', {'poll': p},context_instance=RequestContext(request))
    

def results(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	return render_to_response('polls/results.html', {'poll': p})
    

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))
	return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))
	
    
def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
	    form.save()
            return HttpResponseRedirect('/contacts/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render_to_response('smrh/contact.html', {
        'form': form,'action':'newcontact',
    })    

def loginTest(request):
	user = users.get_current_user()
	if user:
		print 'the user is there %s' % (user.email())
	else:
		print ' the user is not signed in redirecting'

	return HttpResponseRedirect('/contacts/')



def employeeDetails(request):
    if request.method == 'POST': # If the form has been submitted...
        form = EmployeeForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
	    form.save()
            return HttpResponseRedirect('/employees/') # Redirect after POST
    else:
        form = EmployeeForm() # An unbound form

    return render_to_response('smrh/plainform.html', {
        'form': form,'action':'newemployee',
    })   



def employeePhDetails(request,empPk):
    if request.method == 'POST': # If the form has been submitted...
        form = EmployeePhForm(request.POST) # A form bound to the POST data
	#empPhoneDetails	= EmpPhoneDetails()
	#empPhoneDetails.employee = 
	#emp = EmployeeDetails.objects.get(pk=empPk)
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
	    #EmpPhoneDetails.objects.create(employee=long(empPk),phone=form['phone'],phoneType=form['phoneType'])
	    empPhModel = form.save(commit = False)
	    empPhModel.employee = long(empPk)
	    empPhModel.save()
            return HttpResponseRedirect('/employees/') # Redirect after POST
    else:
        form = EmployeePhForm(initial={'employee':long(empPk)}) # An unbound form

    return render_to_response('smrh/plainform.html', {
        'form': form,'action':'empphdetai/%s'%(empPk),
    },context_instance=RequestContext(request))    



def employeePhView(request,empPk):
	objects = EmpPhoneDetails.objects.filter(employee__exact=long(empPk))
	return render_to_response('smrh/employeePhTable.html', {
		'employeeph_list':objects,'action':'empphdetai/%s'%(empPk),
    })


def employeeAddrDetails(request,empPk):
	if request.method == 'POST': # If the form has been submitted...
		form = EmployeeAddrForm(request.POST) # A form bound to the POST data
		employee = EmployeeDetails.objects.get(pk=long(empPk))
		if form.is_valid(): # All validation rules pass
			empAddrModel = form.save(commit = False)
			empAddrModel.employee = employee 
			empAddrModel.save()
			return HttpResponseRedirect('/employees/') # Redirect after POST
	else:
		employee = EmployeeDetails.objects.get(pk=long(empPk))
		form = EmployeeAddrForm(initial={'employee':employee}) # An unbound form
	
	return render_to_response('smrh/plainform.html', {
        'form': form,'action':'empadrdetai/%s'%(empPk),
	},context_instance=RequestContext(request))
def employeeAddrView(request,empPk):
	employee = EmployeeDetails.objects.get(pk=long(empPk))
	objects = EmpAddressDetails.objects.filter(employee__exact=employee)
	return render_to_response('smrh/employeeAddrTable.html', {
		'employeeaddr_list':objects,'action':'empphdetai/%s'%(empPk),
    })
