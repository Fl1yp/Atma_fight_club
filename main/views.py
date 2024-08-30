import os

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.cache import never_cache

from main.models import Main, Contact, Photo, Question
from django.utils import timezone
from django.shortcuts import redirect
from django.core.management import call_command
from django.views.generic.edit import CreateView
from .models import Contact
from .forms import ContactForm

MESSAGE_COOLDOWN = 120  # Время ожидания в секундах


class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "front/modal_window.html"
    success_url = reverse_lazy('main:contact_create')
    MESSAGE_COOLDOWN = 120  # Время ожидания в секундах

    def form_valid(self, form):
        # Получаем текущее время
        current_time = timezone.now().timestamp()
        last_sent_time = self.request.session.get('last_message_time', 0)

        # Проверяем время ожидания
        if current_time - last_sent_time >= self.MESSAGE_COOLDOWN:
            contact = form.save(commit=False)  # Сохраняем форму, но не записываем в БД пока

            # Отправляем уведомление
            call_command('bot', contact.id)
            self.request.session['last_message_time'] = current_time  # Обновляем время последней отправки

            # Теперь сохраняем контакт в БД
            contact.save()

            return super().form_valid(form)
        else:
            # Сообщение о неудаче из-за слишком частых отправок
            self.request.session['form_submitted'] = False  # Отметка только в случае успеха

            # Перенаправляем на страницу main или возвращаем сообщение об ошибке
            return redirect('main:main')


def main(request):
    main = Main.objects.all()
    photo = Photo.objects.all()
    question = Question.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            current_time = timezone.now().timestamp()
            last_sent_time = request.session.get('last_message_time', 0)

            if current_time - last_sent_time >= ContactCreateView.MESSAGE_COOLDOWN:
                contact = form.save()  # Сохраняем контакт

                # Отправка уведомления
                call_command('bot', contact.id)
                request.session['last_message_time'] = current_time  # Обновляем время

                return redirect('main:main')
            else:
                # Сообщение о неудаче из-за слишком частых отправок
                request.session['form_submitted'] = False  # Отметка только в случае успеха

                return redirect('main:main')
    else:
        form = ContactForm()

    context = {
        'main': main,
        'form': form,
        "photo": photo,
        "question": question,
    }
    return render(request, 'main_list.html', context)


@never_cache
def some_view(request):
    return render(request, 'main_list.html')
