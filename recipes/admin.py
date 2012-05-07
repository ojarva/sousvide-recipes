from recipes.models import *
from django.contrib import admin
import reversion

class IngredientAdmin(reversion.VersionAdmin):
    pass

class RecipeGroupAdmin(reversion.VersionAdmin):
    pass

class MakingAdmin(reversion.VersionAdmin):
    pass

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeGroup, RecipeGroupAdmin)
admin.site.register(Making, MakingAdmin)
