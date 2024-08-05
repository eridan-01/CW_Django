from django.urls import path

from newsletter.apps import NewsletterConfig
from newsletter.views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView, \
    MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView, MailingListView, \
    MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView, HomeView, AttemptListView

app_name = NewsletterConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('client_list/', ClientListView.as_view(), name='client-list'),
    path('clients/<int:pk>/', (ClientDetailView.as_view()), name='client-detail'),
    path('clients/create/', ClientCreateView.as_view(), name='client-create'),
    path('clients/<int:pk>/update/', ClientUpdateView.as_view(), name='client-update'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client-delete'),

    path('messages/', MessageListView.as_view(), name='message-list'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),
    path('messages/create/', MessageCreateView.as_view(), name='message-create'),
    path('messages/<int:pk>/update/', MessageUpdateView.as_view(), name='message-update'),
    path('messages/<int:pk>/delete/', MessageDeleteView.as_view(), name='message-delete'),

    path('mailings/', MailingListView.as_view(), name='mailing-list'),
    path('mailings/<int:pk>/', MailingDetailView.as_view(), name='mailing-detail'),
    path('mailings/create/', MailingCreateView.as_view(), name='mailing-create'),
    path('mailings/<int:pk>/update/', MailingUpdateView.as_view(), name='mailing-update'),
    path('mailings/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing-delete'),

    path('attempts/', AttemptListView.as_view(), name='attempt-list'),
]