# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Client.billing'
        db.alter_column(u'client_client', 'billing_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Billing_Information'], null=True))

        # Changing field 'Client.contact_info'
        db.alter_column(u'client_client', 'contact_info_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Contact'], null=True))

        # Changing field 'Client.address'
        db.alter_column(u'client_client', 'address_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Address'], null=True))

        # Changing field 'Sales_Prospect.contact_info'
        db.alter_column(u'client_sales_prospect', 'contact_info_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Contact'], null=True))

        # Changing field 'Sales_Prospect.address'
        db.alter_column(u'client_sales_prospect', 'address_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Address'], null=True))

        # Changing field 'Sales_Prospect.liberty_contact'
        db.alter_column(u'client_sales_prospect', 'liberty_contact_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employee.Employee'], null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Client.billing'
        raise RuntimeError("Cannot reverse this migration. 'Client.billing' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Client.billing'
        db.alter_column(u'client_client', 'billing_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Billing_Information']))

        # User chose to not deal with backwards NULL issues for 'Client.contact_info'
        raise RuntimeError("Cannot reverse this migration. 'Client.contact_info' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Client.contact_info'
        db.alter_column(u'client_client', 'contact_info_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Contact']))

        # User chose to not deal with backwards NULL issues for 'Client.address'
        raise RuntimeError("Cannot reverse this migration. 'Client.address' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Client.address'
        db.alter_column(u'client_client', 'address_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Address']))

        # User chose to not deal with backwards NULL issues for 'Sales_Prospect.contact_info'
        raise RuntimeError("Cannot reverse this migration. 'Sales_Prospect.contact_info' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Sales_Prospect.contact_info'
        db.alter_column(u'client_sales_prospect', 'contact_info_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Contact']))

        # User chose to not deal with backwards NULL issues for 'Sales_Prospect.address'
        raise RuntimeError("Cannot reverse this migration. 'Sales_Prospect.address' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Sales_Prospect.address'
        db.alter_column(u'client_sales_prospect', 'address_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Address']))

        # User chose to not deal with backwards NULL issues for 'Sales_Prospect.liberty_contact'
        raise RuntimeError("Cannot reverse this migration. 'Sales_Prospect.liberty_contact' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Sales_Prospect.liberty_contact'
        db.alter_column(u'client_sales_prospect', 'liberty_contact_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employee.Employee']))

    models = {
        u'client.client': {
            'Meta': {'object_name': 'Client'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Address']", 'null': 'True', 'blank': 'True'}),
            'billing': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Billing_Information']", 'null': 'True', 'blank': 'True'}),
            'business_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'client_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'client_number': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'contact_info': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Contact']", 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'is_business': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'client.sales_prospect': {
            'Meta': {'object_name': 'Sales_Prospect'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Address']", 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'contact_info': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Contact']", 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'if_client': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'initial_contact_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'liberty_contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employee.Employee']", 'null': 'True', 'blank': 'True'}),
            'probability': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'sale_type': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'sales_prospect_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'common.address': {
            'Meta': {'object_name': 'Address'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.City']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.State']"}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {'max_length': '10'})
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
            'cell': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'office_phone': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'office_phone_extension': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'phone_extension': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'common.state': {
            'Meta': {'object_name': 'State'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'employee.employee': {
            'Meta': {'object_name': 'Employee'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Address']"}),
            'contact_info': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Contact']"}),
            'e_title': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['employee.Title']", 'symmetrical': 'False'}),
            'employee_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'employee_number': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'hire_date': ('django.db.models.fields.DateField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'pay_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'pay_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'termination_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'termination_reason': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
        },
        u'employee.title': {
            'Meta': {'object_name': 'Title'},
            'title': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'title_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['client']