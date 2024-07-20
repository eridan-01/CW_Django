from django.contrib import admin
from .models import Client, Message, Mailing, Attempt


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'last_name', 'first_name', 'middle_name', 'comment')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'body')


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'periodicity', 'status', 'message')


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'attempt_time', 'status', 'server_response')

