from django.shortcuts import render, render_to_response

from django.template import Template, Context
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from blog.models import Book, Author, Publisher
from django.core.mail import send_mail
from blog.forms import ContactForm

from django.template import RequestContext

import datetime

# Create your views here.


def home_page(request):
    print(request.META)
    data = ""
    for k, v in request.META.items():
        data += "%s:%s<br>" % (k, v)
    return HttpResponse("It Work!!!<br>" + data)


def hello(request):
    print(request)
    return HttpResponse("Hello World!")


def current_time(request):
    print(request)
    # now = datetime.datetime.now()
    # html = "<html><head><title>当前时间</title></head><body>当前时间:%s</body></html>" % (now,)
    # return HttpResponse(html)

    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {"current_date": now})


def hours_ahead(request, offset):
    print(request)
    try:
        hours = int(offset)
    except ValueError:
        raise Http404()
    
    curtime = datetime.datetime.now()
    dt = curtime + datetime.timedelta(hours=hours)
    # html = "<html><body><p>现在是:%s</p>%s 小时之后, 是: %s.</body></html>" % (curtime, hours, dt)
    # return HttpResponse(html)
    print(dt)
    return render_to_response('hours_ahead.html', {"next_time": dt})


def customtemplate(request):
    print(request)
    raw_template = """<p>Dear {{person_name}},</p>
    <p>Thanks for placing an order from {{company }}.
    ship on {{ ship_date|date:"F j,Y"}}.</p>
    <p>Here are the items you've ordered:</p>
    <ul>
    {% for item in item_list %}
    <li>{{item}}</li>
    {% endfor %}
    </ul>
    {% if ordered_warranty %}
    <p>Your warranty information will be included in the packing.</p>
    {% else %}
    <p>You didn't order a warranty , so you're on your own when
    the  products inevitably stop working.</p>
    {% endif %}
    <p>Sincerely, <br/>{{company}}</p>"""
    t = Template(raw_template)
    c = Context({"person_name": "John Smith", "company": 'Outdoor Equipment', "hip_date": datetime.date(2017, 9, 6), "order_warranty": True})
    return HttpResponse(t.render(c))


def display_meta(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append("<tr><td>%s</td><td>%s</td></tr>" % (k, v))
    return HttpResponse('<table>%s</table>' % (html, ))


def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append("Enter a search term.")
        elif len(q) > 20:
            errors.append("Please enter at most characters.")
        else:
            print("error:", errors)
            books = Book.objects.filter(title__icontains = q)
            return render_to_response('search_results.html', {"books": books, "query": q})

    print("error:", errors)
    return render_to_response('search_form.html', {'errors': errors})


def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.GET('subject', ''):
            errors.append("Enter a subject.")
        if not request.POST.GET('message', ''):
            errors.append("Enter a message.")
        if request.POST.GET('email') and '@' not in request.POST['email']:
            errors.append("Enter a valid e-mail address.")
        if not errors:
            send_mail(request.POST['subject'],
                      request.POST['message'],
                      request.POST.get('email', 'noreply@example.com'),
                      ['siteowner@example.com'],)
            return HttpResponseRedirect('/contact/thanks/')
    return render_to_response('contact_form.html', {"errors": errors,
                                                    'subject': request.POST.get('subject', ''),
                                                    'message': request.POST.get('message', ''),
                                                    'email': request.POST.get('email', ''), })


# 使用django.forms 框架
def contact2(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valiad():
            cd = form.cleaned_data
            send_mail(cd['subject'], cd['message'], cd.get('email', "noreply@example.com"), ['siteowner@example.com'])
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial = {"subject": "I Love your site!"})
    # return render_to_response('contact_form2.html', {"form": form}, context_instance = RequestContext(request))
    return render_to_response('contact_form2.html', {"form": form})
