from django.shortcuts import render_to_response
from models import Host_detail,Guest_detail,Alumni
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.template import Context, loader

from django.template import loader, RequestContext
from django.http import Http404, HttpResponse, HttpResponseForbidden
from django.core.xheaders import populate_xheaders
from django.core.paginator import Paginator, InvalidPage
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.loading import get_model


def host(request):
       host_list = Host_detail.objects.all()
       t = loader.get_template('congress/host.html')
       c = Context({'host_list':host_list,'user': request.user})
       return HttpResponse(t.render(c))
     
def alumni(request):
       alumni_list = Alumni.objects.all()
       t = loader.get_template('congress/alumni.html')
       c = Context({'alumni_list':alumni_list,'user': request.user})
       return HttpResponse(t.render(c))

def guest(request):
       guest_list = Guest_detail.objects.all()
       t = loader.get_template('congress/guest.html')
       c = Context({'guest_list':guest_list,'user': request.user})
       return HttpResponse(t.render(c))

def print_detail(request, app_label, model_name, pk, template_name=None, template_name_field=None,
        template_loader=loader, extra_context=None,
        context_processors=None, template_object_name='object',
        mimetype=None):
    """
    Put the following line in your urls.py BEFORE your admin include
    (r'^admin/(?P<app_label>[\d\w]+)/(?P<model_name>[\d\w]+)/(?P<pk>[\d]+)/print/', 'biola.utils.print_view.print_detail'),

    Generic detail of an object.

    Templates: ``<app_label>/<model_name>_print_detail.html``
    Context:
        object
            the object
    """
    if not request.user.is_staff:
        return HttpResponseForbidden()
    if extra_context is None: extra_context = {}
    try:
        model = get_model(app_label, model_name)	
        obj = model.objects.get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404, "No %s found matching the query" % (model._meta.verbose_name)
    if not template_name:
        template_name = "%s/%s_print_detail.html" % (model._meta.app_label, model._meta.object_name.lower())
    if template_name_field:
        template_name_list = [getattr(obj, template_name_field), template_name]
        t = template_loader.select_template(template_name_list)
    else:
        t = template_loader.get_template(template_name)
    c = RequestContext(request, {
        template_object_name: obj,
    }, context_processors)
    for key, value in extra_context.items():
        if callable(value):
            c[key] = value()
        else:
            c[key] = value
    response = HttpResponse(t.render(c), mimetype=mimetype)
    populate_xheaders(request, response, model, getattr(obj, obj._meta.pk.name))
    return response

def post_detail(request, id, showDetails=False):
      posts = Guest_detail.objects.get(pk=id)
      return render_to_response('congress/post_detail.html',{'posts':posts})

def host_detail(request, id, hostsDetails=False):
      hosts = Host_detail.objects.get(pk=id)
      return render_to_response('congress/host_detail.html',{'hosts':hosts})

def post_search(request, term):
	if request.GET.get('search_item','') != '':
		term = request.GET.get('search_item','')
	guest = Guest_detail.objects.filter(surname__icontains=term) | Guest_detail.objects.filter(other_name__icontains=term)
	return render_to_response('congress/post_search.html',{'guest':guest,'term':term,'user': request.user})

def host_search(request, term):
	if request.GET.get('search_item','') != '':
		term = request.GET.get('search_item','')
	host = Host_detail.objects.filter(surname__icontains=term) | Host_detail.objects.filter(other_name__icontains=term)
	return render_to_response('congress/host_search.html',{'host':host,'term':term,'user': request.user})



def home(request):
    return render_to_response('congress/base.html',{'user':request.user})
