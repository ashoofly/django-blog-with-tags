from django.views.generic import DetailView, ListView
from .models import Entry

class EntryDetail(DetailView):
    model = Entry

class EntryIndex(ListView):
    template_name = 'index.html'
    queryset = Entry.objects.order_by('-created_at')

class TagIndexView(ListView):
    template_name = 'index.html'
    model = Entry
    
    def get_queryset(self):
        return Entry.objects.filter(tags__slug=self.kwargs.get('slug'))
