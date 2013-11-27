# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Call_List_Details'
        db.create_table(u'site_info_call_list_details', (
            ('call_list_details_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('call_list_details_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('order', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'site_info', ['Call_List_Details'])

        # Adding model 'Call_List'
        db.create_table(u'site_info_call_list', (
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('call_list_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('call_list_detail', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site_info.Call_List_Details'], null=True, blank=True)),
            ('call_list_contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Contact'], null=True, blank=True)),
        ))
        db.send_create_signal(u'site_info', ['Call_List'])

        # Adding model 'Site_Information'
        db.create_table(u'site_info_site_information', (
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Address'])),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Contact'])),
            ('site_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site_client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['client.Client'])),
        ))
        db.send_create_signal(u'site_info', ['Site_Information'])

        # Adding M2M table for field site_call_list on 'Site_Information'
        m2m_table_name = db.shorten_name(u'site_info_site_information_site_call_list')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('site_information', models.ForeignKey(orm[u'site_info.site_information'], null=False)),
            ('call_list', models.ForeignKey(orm[u'site_info.call_list'], null=False))
        ))
        db.create_unique(m2m_table_name, ['site_information_id', 'call_list_id'])

        # Adding model 'Panel'
        db.create_table(u'site_info_panel', (
            (u'equipment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['common.Equipment'], unique=True)),
            ('panel_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('panel_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'site_info', ['Panel'])

        # Adding model 'Module'
        db.create_table(u'site_info_module', (
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('manufacturer', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('part_number', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('serial_number', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('install_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('install_tech', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employee.Employee'])),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site_info.Service_Information'])),
            ('module_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('module_panel_alarm', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site_info.Panel'])),
            ('module_site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site_info.Site_Information'])),
        ))
        db.send_create_signal(u'site_info', ['Module'])

        # Adding model 'Zone'
        db.create_table(u'site_info_zone', (
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('manufacturer', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('part_number', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('serial_number', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('install_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('install_tech', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employee.Employee'])),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site_info.Service_Information'])),
            ('zone_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zones_panel_alarm', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site_info.Panel'])),
            ('zone_site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site_info.Site_Information'])),
        ))
        db.send_create_signal(u'site_info', ['Zone'])

        # Adding model 'Site_Equipment'
        db.create_table(u'site_info_site_equipment', (
            (u'equipment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['common.Equipment'], unique=True)),
            ('equipment_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('equipment_site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site_info.Site_Information'])),
        ))
        db.send_create_signal(u'site_info', ['Site_Equipment'])

        # Adding model 'Camera'
        db.create_table(u'site_info_camera', (
            (u'equipment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['common.Equipment'], unique=True)),
            ('camera_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('camera_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('DVR_type', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('communication_type', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
        ))
        db.send_create_signal(u'site_info', ['Camera'])

        # Adding model 'Site_Panel'
        db.create_table(u'site_info_site_panel', (
            ('site_panel_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('panel_site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site_info.Site_Information'])),
            ('site_panel_panel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site_info.Panel'])),
            ('communication_id', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'site_info', ['Site_Panel'])

        # Adding model 'Site_Camera'
        db.create_table(u'site_info_site_camera', (
            ('site_camera_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('camera_site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site_info.Site_Information'])),
            ('camera', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site_info.Camera'])),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'site_info', ['Site_Camera'])

        # Adding model 'Service_Information'
        db.create_table(u'site_info_service_information', (
            ('service_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('service_panel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site_info.Panel'])),
            ('technician', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employee.Employee'])),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'site_info', ['Service_Information'])

        # Adding model 'Installation_Information'
        db.create_table(u'site_info_installation_information', (
            ('installation_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('installation_site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site_info.Site_Information'])),
            ('installation_start_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('installation_end_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'site_info', ['Installation_Information'])

        # Adding M2M table for field installation_tech on 'Installation_Information'
        m2m_table_name = db.shorten_name(u'site_info_installation_information_installation_tech')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('installation_information', models.ForeignKey(orm[u'site_info.installation_information'], null=False)),
            ('employee', models.ForeignKey(orm[u'employee.employee'], null=False))
        ))
        db.create_unique(m2m_table_name, ['installation_information_id', 'employee_id'])

        # Adding M2M table for field panels_installed on 'Installation_Information'
        m2m_table_name = db.shorten_name(u'site_info_installation_information_panels_installed')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('installation_information', models.ForeignKey(orm[u'site_info.installation_information'], null=False)),
            ('panel', models.ForeignKey(orm[u'site_info.panel'], null=False))
        ))
        db.create_unique(m2m_table_name, ['installation_information_id', 'panel_id'])

        # Adding M2M table for field cameras_installed on 'Installation_Information'
        m2m_table_name = db.shorten_name(u'site_info_installation_information_cameras_installed')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('installation_information', models.ForeignKey(orm[u'site_info.installation_information'], null=False)),
            ('camera', models.ForeignKey(orm[u'site_info.camera'], null=False))
        ))
        db.create_unique(m2m_table_name, ['installation_information_id', 'camera_id'])

        # Adding M2M table for field additional_equipment on 'Installation_Information'
        m2m_table_name = db.shorten_name(u'site_info_installation_information_additional_equipment')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('installation_information', models.ForeignKey(orm[u'site_info.installation_information'], null=False)),
            ('equipment', models.ForeignKey(orm[u'common.equipment'], null=False))
        ))
        db.create_unique(m2m_table_name, ['installation_information_id', 'equipment_id'])


    def backwards(self, orm):
        # Deleting model 'Call_List_Details'
        db.delete_table(u'site_info_call_list_details')

        # Deleting model 'Call_List'
        db.delete_table(u'site_info_call_list')

        # Deleting model 'Site_Information'
        db.delete_table(u'site_info_site_information')

        # Removing M2M table for field site_call_list on 'Site_Information'
        db.delete_table(db.shorten_name(u'site_info_site_information_site_call_list'))

        # Deleting model 'Panel'
        db.delete_table(u'site_info_panel')

        # Deleting model 'Module'
        db.delete_table(u'site_info_module')

        # Deleting model 'Zone'
        db.delete_table(u'site_info_zone')

        # Deleting model 'Site_Equipment'
        db.delete_table(u'site_info_site_equipment')

        # Deleting model 'Camera'
        db.delete_table(u'site_info_camera')

        # Deleting model 'Site_Panel'
        db.delete_table(u'site_info_site_panel')

        # Deleting model 'Site_Camera'
        db.delete_table(u'site_info_site_camera')

        # Deleting model 'Service_Information'
        db.delete_table(u'site_info_service_information')

        # Deleting model 'Installation_Information'
        db.delete_table(u'site_info_installation_information')

        # Removing M2M table for field installation_tech on 'Installation_Information'
        db.delete_table(db.shorten_name(u'site_info_installation_information_installation_tech'))

        # Removing M2M table for field panels_installed on 'Installation_Information'
        db.delete_table(db.shorten_name(u'site_info_installation_information_panels_installed'))

        # Removing M2M table for field cameras_installed on 'Installation_Information'
        db.delete_table(db.shorten_name(u'site_info_installation_information_cameras_installed'))

        # Removing M2M table for field additional_equipment on 'Installation_Information'
        db.delete_table(db.shorten_name(u'site_info_installation_information_additional_equipment'))


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
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.City']"}),
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
        u'site_info.call_list': {
            'Meta': {'object_name': 'Call_List'},
            'call_list_contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Contact']", 'null': 'True', 'blank': 'True'}),
            'call_list_detail': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['site_info.Call_List_Details']", 'null': 'True', 'blank': 'True'}),
            'call_list_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'site_info.call_list_details': {
            'Meta': {'object_name': 'Call_List_Details'},
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
            'equipment_site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['site_info.Site_Information']"})
        },
        u'site_info.site_information': {
            'Meta': {'object_name': 'Site_Information'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Address']"}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Contact']"}),
            'site_call_list': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['site_info.Call_List']", 'symmetrical': 'False'}),
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