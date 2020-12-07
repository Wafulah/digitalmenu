from django.contrib import admin

from .models import Price, Meal,Drinks


class PriceInline(admin.TabularInline):
    model = Price
    extra = 0




class DrinksAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['drinks_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    
    list_display = ('drinks_text', 'pub_date','was_published_recently')
    search_fields = ['drinks_text']


class MealAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['meal_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [PriceInline]
    list_display = ('meal_text', 'pub_date','was_published_recently')
    search_fields = ['meal_text']



admin.site.register(Meal, MealAdmin)
admin.site.register(Drinks, DrinksAdmin)