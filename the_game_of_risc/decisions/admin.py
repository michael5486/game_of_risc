from django.contrib import admin
from .models import Decision, Adjudication, UserProfile

# Register your models here.


class AdjudicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'digest', 'outcome')
    list_filter = ('outcome',)


class DecisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'adjudication_id', 'user_id', 'answer', 'timestamp')
    list_filter = ('answer',)


class UserProfileAdmin(admin.ModelAdmin):
    # list_display = ('user', 'email_address', 'first_name', 'last_name', 'num_guesses', 'num_correct_guesses')
    list_display = ('user', 'num_guesses', 'num_correct_guesses')

admin.site.register(Adjudication, AdjudicationAdmin)
admin.site.register(Decision, DecisionAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
