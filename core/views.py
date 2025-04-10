from django.template.response import TemplateResponse


def home_page(request):
    """Домашняя страница"""
    return TemplateResponse(request, 'pages/home.html', {})
