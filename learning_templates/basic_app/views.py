from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text': 'Hello World', 'number': 100}
    return render(request, 'basic_app/index.html', context_dict)

def others(request):
    return render(request, 'basic_app/others.html')

def relative_url_templates(request):
    return render(request, 'basic_app/relative_url_templates.html')
