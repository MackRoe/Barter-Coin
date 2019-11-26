from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from bartercoin.models import Profile


# Create your views here.
# def post_list(request):
#     return render(request, 'post_list.html', {})

class PageList(ListView):
    """
     On GET, display a homepage that shows all Pages in your wiki.
    """
    model = Profile

    def get(self, request):
        """ Returns a list of wiki pages. """
        list_context = {
            "pages": Profile.objects.all()
        }
        return render(request, 'post_list.html', list_context)


class PageDetailView(DetailView):
    """
    On GET, render a template named `page.html`.
    """
    model = Profile

    def get(self, request, slug):
        """ Returns a specific page by slug. """
        page = Profile.objects.get(slug=slug)
        context = {
            "page" : page
        }
        return render(request, "detail_page.html", context)
        pass

    def post(self, request, slug):
        pass
