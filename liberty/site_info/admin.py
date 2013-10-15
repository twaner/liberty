from django.contrib import admin

from site_info.models import Site_Equipment, Site_Panel, Site_Camera,Service_Information, Installation_Information

admin.site.register(Site_Equipment)
admin.site.register(Site_Camera)
admin.site.register(Site_Panel)
admin.site.register(Service_Information)
admin.site.register(Installation_Information)