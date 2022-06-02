from django.contrib import admin
from recipes.models import Recipe, Step

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    pass

class StepAdmin(admin.ModelAdmin):
    pass

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Step, StepAdmin)