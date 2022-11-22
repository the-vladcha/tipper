from django.db.models import Value, Sum, F
from django.http import HttpResponse
from django.views import generic

from calculator.forms import CoordinatesForm
from calculator.models import Tippers, Storages


class Calculator(generic.ListView):
    template_name = 'calculator/index.html'
    context_object_name = 'tippers'
    model = Tippers

    def get_queryset(self):
        return Tippers.objects.all().annotate(overcargo=
                                              (F('cargo') - F('max_load_capacity')) * 100 / F('max_load_capacity'))

    def get_context_data(self, **kwargs):
        context = super(Calculator, self).get_context_data(**kwargs)
        context.update({
            'storages': Storages.objects.all(),
        })
        context['coordinates'] = CoordinatesForm()
        return context


# class Result(generic.ListView):
#     template_name = 'calculator/index.html'
#     context_object_name = 'storages'
#     model = Storages
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
