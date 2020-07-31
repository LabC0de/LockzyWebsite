from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string

from .models import ContentTable


def default_page_helper(request, site=1, subarticle="what"):
    subarticles = get_object_or_404(ContentTable, pk=site)
    sidebar = render_to_string('sidebar_cnt.html', {"subarticles": subarticles})
    article = render_to_string('articles/' + subarticle + '.html')
    return render(request, 'main_template.html', {"related_links": sidebar,
                                                  "subarticles": subarticles,
                                                  "article": article})


# Create your views here.
def empty(request):
    return redirect('/index')


def index(request, subarticle="what"):
    return default_page_helper(request, 1, subarticle)


def about(request, subarticle="team"):
    return default_page_helper(request, 2, subarticle)


def vision(request, subarticle="inspiration"):
    return default_page_helper(request, 3, subarticle)


def getlockzy(request, subarticle="buy"):
    return default_page_helper(request, 4, subarticle)
