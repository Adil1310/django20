from django.shortcuts import render, redirect
from django.urls import reverse
from .models import MyModel
from .models import Event

# Create your views here.

def my_view(request):
    if request.method == 'POST':
        user_data = request.POST.get('input_field')
        if user_data:
            return redirect(reverse('myapp:success_page'))
    return render(request, 'my_template.html')

def get_single_record(request, record_id):
    record = MyModel.objects.get(pk=record_id)
    return render(request, 'single_record.html', {'record': record})

def get_records_list(request):
    records = MyModel.objects.all()
    return render(request, 'record_list.html', {'records': records})

def chronological_list(request):
    events = Event.objects.order_by('-event_date')
    return render(request, 'chronological_list.html', {'events': events})