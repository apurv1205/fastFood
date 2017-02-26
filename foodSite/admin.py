from django.contrib import admin

# Register your models here.
from .models import FoodItems,Restaurant

class FoodItemsAdmin(admin.ModelAdmin):
	model = FoodItems
	list_display = ['name','get_name']

	def get_name(self,obj):
		return obj.rest.name
	get_name.short_description = 'Restaurant'


admin.site.register(FoodItems, FoodItemsAdmin)
admin.site.register(Restaurant)
