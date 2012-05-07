# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'IngredientForRecipe'
        db.delete_table('recipes_ingredientforrecipe')

        # Removing M2M table for field ingredients on 'Making'
        db.delete_table('recipes_making_ingredients')

        # Adding field 'RecipeGroup._order'
        db.add_column('recipes_recipegroup', '_order', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'IngredientForRecipe'
        db.create_table('recipes_ingredientforrecipe', (
            ('amount', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ingredient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Ingredient'])),
        ))
        db.send_create_signal('recipes', ['IngredientForRecipe'])

        # Adding M2M table for field ingredients on 'Making'
        db.create_table('recipes_making_ingredients', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('making', models.ForeignKey(orm['recipes.making'], null=False)),
            ('ingredientforrecipe', models.ForeignKey(orm['recipes.ingredientforrecipe'], null=False))
        ))
        db.create_unique('recipes_making_ingredients', ['making_id', 'ingredientforrecipe_id'])

        # Deleting field 'RecipeGroup._order'
        db.delete_column('recipes_recipegroup', '_order')


    models = {
        'recipes.imagefile': {
            'Meta': {'object_name': 'ImageFile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Making']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'recipes.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'recipes.making': {
            'Meta': {'object_name': 'Making'},
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.RecipeGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'temperature': ('django.db.models.fields.IntegerField', [], {}),
            'time': ('django.db.models.fields.TimeField', [], {})
        },
        'recipes.recipegroup': {
            'Meta': {'object_name': 'RecipeGroup'},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Ingredient']"})
        }
    }

    complete_apps = ['recipes']
