from django.shortcuts import render, render_to_response

from django.template import Template, Context
from django.http import HttpResponse, Http404

import datetime

# Create your views here.


def home_page(request):
    print(request)
    return HttpResponse("It Work!!!")


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