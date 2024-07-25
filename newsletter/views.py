from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Client, Message, Mailing
from .forms import ClientForm, MessageForm, MailingForm


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('newsletter:client-list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('newsletter:client-list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('newsletter:client-list')


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('newsletter:message-list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('newsletter:message-list')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('newsletter:message-list')


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('newsletter:mailing-list')


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('newsletter:mailing-list')


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('newsletter:mailing-list')
