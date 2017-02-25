from django.contrib import admin

<<<<<<< HEAD
# Register your models here.
=======
# Register your models here.
from .models import FoodItems,Restaurant

class FoodItemsAdmin(admin.ModelAdmin):
	model = Restaurant
	list_display = ['name','get_name']

	def get_name(self,obj):
		return obj.rest.name
	get_name.short_description = 'Restaurant'


admin.site.register(FoodItems, FoodItemsAdmin)
admin.site.register(Restaurant)
>>>>>>> 00ad753503eb95e9ea6dd3eb7d4c195a96707f0e
