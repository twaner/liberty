# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Billing_Information.attention_first_name'
        db.add_column(u'common_billing_information', 'attention_first_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True),
                      keep_default=False)

        # Adding field 'Billing_Information.attention_last_name'
        db.add_column(u'common_billing_information', 'attention_last_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True),
                      keep_default=False)

        # Adding field 'Billing_Information.business_name'
        db.add_column(u'common_billing_information', 'business_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=35, blank=True),
                      keep_default=False)

        # Adding field 'Billing_Information.is_business'
        db.add_column(u'common_billing_information', 'is_business',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Renaming column for 'Address.state' to match new field type.
        db.rename_column(u'common_address', 'state_id', 'state')
        # Changing field 'Address.state'
        db.alter_column(u'common_address', 'state', self.gf('django.db.models.fields.CharField')(max_length=30))
        # Removing index on 'Address', fields ['state']
        db.delete_index(u'common_address', ['state_id'])


        # Changing field 'Address.zip_code'
        db.alter_column(u'common_address', 'zip_code', self.gf('django.db.models.fields.CharField')(max_length=10))

    def backwards(self, orm):
        # Adding index on 'Address', fields ['state']
        db.create_index(u'common_address', ['state_id'])

        # Deleting field 'Billing_Information.attention_first_name'
        db.delete_column(u'common_billing_information', 'attention_first_name')

        # Deleting field 'Billing_Information.attention_last_name'
        db.delete_column(u'common_billing_information', 'attention_last_name')

        # Deleting field 'Billing_Information.business_name'
        db.delete_column(u'common_billing_information', 'business_name')

        # Deleting field 'Billing_Information.is_business'
        db.delete_column(u'common_billing_information', 'is_business')


        # Renaming column for 'Address.state' to match new field type.
        db.rename_column(u'common_address', 'state', 'state_id')
        # Changing field 'Address.state'
        db.alter_column(u'common_address', 'state_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.State']))

        # Changing field 'Address.zip_code'
        db.alter_column(u'common_address', 'zip_code', self.gf('django.db.models.fields.IntegerField')(max_length=10))

    models = {
        u'common.address': {
            'Meta': {'object_name': 'Address'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.City']", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'NY'", 'max_length': '30'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'common.billing_information': {
            'Meta': {'object_name': 'Billing_Information'},
            'attention_first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'attention_last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'billing_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'business_name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'is_business': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'common.city': {
            'Meta': {'object_name': 'City'},
            'city_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'city_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'common.contact': {
            'Meta': {'object_name': 'Contact'},
            'cell': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'office_phone': ('django.db.models.fields.CharField', [], {'max_length': '13', 'blank': 'True'}),
            'office_phone_extension': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '13', 'blank': 'True'}),
            'phone_extension': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'common.equipment': {
            'Meta': {'object_name': 'Equipment'},
            'equipment_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'equipment_notes': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'equipment_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'common.state': {
            'Meta': {'object_name': 'State'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['common']