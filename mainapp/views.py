from django.shortcuts import render
from mainapp.models import Product, Partner
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from mainapp.tasks import send_user_email


def main_page_view(request):
    partners = Partner.objects.all()
    products = Product.objects.all()
    return render(request, 'mainapp/index.html', locals())


@require_POST
def send_email(request):
    data = request.POST.copy()
    number = data.get('recipient-phone')
    name = data.get('recipient-name')
    button = data.get('button')
    print(button)
    message = u'Добрый день! На сайт поступила заявка от пользователя {name}. Перезвоните на номер: {number}. Была задействована кнопка: {button}'.format(number=number, name=name, button=button)
    send_user_email.delay(u'Заявка на звонок', message, email=None)
    return JsonResponse({'response': u'Ваши данные отправлены отправлены на сервер'})
