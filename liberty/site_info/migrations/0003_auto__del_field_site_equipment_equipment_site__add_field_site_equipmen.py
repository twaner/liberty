# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Site_Equipment.equipment_site'
        db.delete_column(u'site_info_site_equipment', 'equipment_site_id')

        # Adding field 'Site_Equipment.equipment_site_id'
        db.add_column(u'site_info_site_equipment', 'equipment_site_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['site_info.Site_Information']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Site_Equipment.equipment_site'
        db.add_column(u'site_info_site_equipment', 'equipment_site',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['site_info.Site_Information']),
                      keep_default=False)

        # Deleting field 'Site_Equipment.equipment_site_id'
        db.delete_column(u'site_info_site_equipment', 'equipment_site_id_id')


    models = {
        u'client.client': {
            'Meta': {'object_name': 'Client'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Address']", 'null': 'True', 'blank': 'True'}),
            'billing': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Billing_Information']", 'null': 'True', 'blank': 'True'}),
            'business_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'client_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'client_number': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'contact_info': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Contact']", 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'is_business': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
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
            'pay_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'pay_type': ('django.db.models.fields.CharField', [], {'default': "'HR'", 'max_length': '3'}),
            'termination_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'termination_reason': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
        },
        u'employee.title': {
            'Meta': {'object_name': 'Title'},
            'title': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'title_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'site_info.call_list_details': {
            'Meta': {'object_name': 'Call_List_Details'},
            'call_list_contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Contact']", 'null': 'True', 'blank': 'True'}),
            'call_list_details_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'call_list_details_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'site_info.camera': {
            'DVR_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'Meta': {'object_name': 'Camera', '_ormbases': [u'common.Equipment']},
            'camera_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'camera_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'communication_type': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            u'equipment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['common.Equipment']", 'unique': 'True'})
        },
        u'site_info.installation_information': {
            'Meta': {'object_name': 'Installation_Information'},
            'additional_equipment': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['common.Equipment']", 'symmetrical': 'False'}),
            'cameras_installed': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'cameras'", 'symmetrical': 'False', 'to': u"orm['site_info.Camera']"}),
            'installation_end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'installation_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'installation_site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['site_info.Site_Information']"}),
            'installation_start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'installation_tech': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['employee.Employee']", 'symmetrical': 'False'}),
            'panels_installed': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'panels'", 'symmetrical': 'False', 'to': u"orm['site_info.Panel']"})
        },
        u'site_info.module': {
            'Meta': {'object_name': 'Module'},
            'install_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'install_tech': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employee.Employee']"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'module_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module_panel_alarm': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['site_info.Panel']"}),
            'module_site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['site_info.Site_Information']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'part_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['site_info.Service_Information']"})
        },
        u'site_info.panel': {
            'Meta': {'object_name': 'Panel', '_ormbases': [u'common.Equipment']},
            u'equipment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['common.Equipment']", 'unique': 'True'}),
            'panel_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'panel_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'site_info.service_information': {
            'Meta': {'object_name': 'Service_Information'},
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'service_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service_panel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['site_info.Panel']"}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'technician': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employee.Employee']"})
        },
        u'site_info.site_camera': {
            'Meta': {'object_name': 'Site_Camera'},
            'camera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['site_info.Camera']"}),
            'camera_site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['site_info.Site_Information']"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'site_camera_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'site_info.site_equipment': {
            'Meta': {'object_name': 'Site_Equipment', '_ormbases': [u'common.Equipment']},
            'equipment_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'equipment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['common.Equipment']", 'unique': 'True'}),
            'equipment_site_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['site_info.Site_Information']"})
        },
        u'site_info.site_information': {
            'Meta': {'object_name': 'Site_Information'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Address']"}),
            'site_call_list_details': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['site_info.Call_List_Details']", 'symmetrical': 'False'}),
            'site_client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['client.Client']"}),
            'site_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'site_info.site_panel': {
            'Meta': {'object_name': 'Site_Panel'},
            'communication_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'panel_site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['site_info.Site_Information']"}),
            'site_panel_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site_panel_panel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['site_info.Panel']"})
        },
        u'site_info.zone': {
            'Meta': {'object_name': 'Zone'},
            'install_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'install_tech': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employee.Employee']"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'part_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['site_info.Service_Information']"}),
            'zone_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'zone_site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['site_info.Site_Information']"}),
            'zones_panel_alarm': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['site_info.Panel']"})
        }
    }

    complete_apps = ['site_info']