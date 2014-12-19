from django.views.generic import DetailView, ListView
from django.db.models import Count
from taggit.models import Tag, TaggedItem

from .models import Entry

class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.annotate(num_times=Count('taggit_taggeditem_items'))
        return context


class EntryDetail(DetailView):
    model = Entry

class EntryIndex(TagMixin, ListView):
    template_name = 'index.html'
    queryset = Entry.objects.order_by('-created_at')

class TagIndexView(TagMixin, ListView):
    template_name = 'index.html'
    model = Entry
    
    def get_queryset(self):
        return Entry.objects.filter(tags__slug=self.kwargs.get('slug'))
