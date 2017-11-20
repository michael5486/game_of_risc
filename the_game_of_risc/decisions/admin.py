from django.contrib import admin

# Register your models here.

from .models import Decision, Adjudication, UserProfile

#fix user and userprofiles here

# class DecisionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Related entities',            {'fields': ['adjudication_id', 'user_id']}),
#         ('Answer',                      {'fields': ['answer']}),
#         ('Timestamp',                   {'fields': ['timestamp']}),
#         # ('Decision_id'),                {'fields': ['id']},
#     ]

# admin.site.register(Decision, DecisionAdmin)

# class AdjudicationAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,                  {'fields': ['digest']}),
#         ('Adjudication Outcome',{'fields': ['outcome']}),
#     ]

# admin.site.register(Adjudication, AdjudicationAdmin)

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
