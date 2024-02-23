from django.contrib import admin
from .models import Unit , Person , Holiday,Branch,Level,HolidayType
from django.utils import timezone
from datetime import timedelta
# Register your models here.

from django.utils.translation import gettext_lazy as _

current_year = timezone.now().year

class RedifTimeFilter(admin.SimpleListFilter):
    title = _('رديف اى دفعة')
    parameter_name = 'redif_time'

    def lookups(self, request, model_admin):
        return (
            ('3-' + str(current_year), _('3-' + str(current_year))),
            ('6-' + str(current_year), _('6-' + str(current_year))),
            ('9-' + str(current_year), _('9-' + str(current_year))),
            ('12-' + str(current_year), _('12-' + str(current_year))),
        )

    def queryset(self, request, queryset):
        
        if self.value() == '3-' + str(current_year):
            return queryset.filter(date_out__month=3, date_out__year=current_year)
        elif self.value() == '6-' + str(current_year):
            return queryset.filter(date_out__month=6, date_out__year=current_year)
        elif self.value() == '9-' + str(current_year):
            return queryset.filter(date_out__month=9, date_out__year=current_year)
        elif self.value() == '12-' + str(current_year):
            return queryset.filter(date_out__month=12, date_out__year=current_year)
        else:
            return queryset


# مأمورية ام قوة هيئة
class MissionORMainUnitFilter(admin.SimpleListFilter):
    title = _('مأمورية ام قوة هيئة')
    parameter_name = 'missionORmainunit'

    def lookups(self, request, model_admin):
        return (
            ('mainunit', _('قوة هيئة')),
            ('mission', _('مأمورية')),

        )

    def queryset(self, request, queryset):

        if self.value() == 'mainunit':
            return queryset.filter(mainunit__mainunit = 'قوة هيئة')
        elif self.value() == 'mission':
            return queryset.exclude(mainunit__mainunit = 'قوة هيئة')
        else:
            return queryset

# كشف الانهاءات    
class FinishedORNotFilter(admin.SimpleListFilter):
    title = _('كشف الانهاءات ')
    parameter_name = 'FinishedORNot'

    def lookups(self, request, model_admin):
        return (
            ('finished', _('انهى الخدمة')),
            ('working', _('ما زال بالخدمة')),

        )

    def queryset(self, request, queryset):

        if self.value() == 'finished':
            return queryset.filter(date_out__lt= timezone.now())
        elif self.value() == 'working':
            return queryset.filter(date_out__gt= timezone.now())
        else:
            return queryset
        
# كشف الحضور 
class presentORabsentFilter(admin.SimpleListFilter):
    title = _('كشف الحضور ')
    parameter_name = 'presentORabsent'

    def lookups(self, request, model_admin):
        return (
            ('present', _('حاضر')),
            ('absent', _('اجازة')),
            ('comming', _('عودة اليوم')),
            ('commingtom', _('عودة غدا')),

        )

    def queryset(self, request, queryset):

        if self.value() == 'absent':
            return queryset.filter(date_from__lte= timezone.now(),date_to__gte= timezone.now())
        elif self.value() == 'present':
            return queryset.filter(date_from__lt= timezone.now())
        elif self.value() == 'comming':
            return queryset.filter(date_to= timezone.now())
        elif self.value() == 'commingtom':
            return queryset.filter(date_to= timezone.now() + timedelta(days=1))
        else:
            return queryset



class UnitAdmin(admin.ModelAdmin):
    list_display = ('mainunit',)
    list_filter = ('mainunit',)
    search_fields = ('mainunit',)
    ordering = ('mainunit',)
    list_per_page = 10
    change_list_template = 'admin/maindata/person/change_list.html'
admin.site.register(Unit, UnitAdmin)
from django.contrib import messages
from django.contrib.auth.admin import User
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','national_id','military_number','level','mainunit','date_added','date_out','branch','detect_redif_wich_dofaa')
    list_filter = ('level__level','date_added','date_out','branch__name','mainunit__mainunit',RedifTimeFilter,MissionORMainUnitFilter,FinishedORNotFilter)
    search_fields = ('name','national_id','military_number','date_added','date_out')
    ordering = ('name','level','mainunit','date_added','date_out','branch')
    list_per_page = 10
    list_editable = ()
    change_list_template = 'admin/maindata/person/change_list.html'
    def recordAbsence(self, request, queryset):
        try:
            holidaydays = int(request.POST.get('holidaydays'))
        except:
            holidaydays = 0
        if holidaydays == 0 :
            messages.error(request, 'لم يتم التنفيذ , برجاء اختيار عدد ايام الاجازة') 
        else:
            for person in queryset:
                Holiday.objects.create(person=person,date_from=timezone.now() ,date_to=timezone.now() + timedelta(days=holidaydays))
                
    def DisableEditFields(self, request, queryset):
        self.list_editable = ()
    def EnableEditFields(self, request, queryset):
        self.list_editable = ('national_id','military_number','level','mainunit','date_added','date_out','branch')

    recordAbsence.short_description = "تسجيل اجازة"  # Set the display name for the custom action
    EnableEditFields.short_description = " تعديل"  
    DisableEditFields.short_description = "الغاء التعديل"  
    actions = ['recordAbsence','EnableEditFields','DisableEditFields']
admin.site.register(Person, PersonAdmin) 


admin.site.register(Branch)         
admin.site.register(Level)         
admin.site.register(HolidayType)         
    
    


class HolidayAdmin(admin.ModelAdmin):
    # autocomplete_fields = ['person']
    raw_id_fields = ('person',)
    list_display = ('person', 'holidaytype', 'date_from', 'date_to')
    list_filter = ('holidaytype__holidaytype', 'date_from', 'date_to',presentORabsentFilter)
    search_fields = ('person__name',)
    change_list_template = 'admin/maindata/holiday/change_list.html'
    list_per_page = 10
    list_editable = ()
    def DisableEditFields(self, request, queryset):
        self.list_editable = ()
    def EnableEditFields(self, request, queryset):
        self.list_editable = ('holidaytype', 'date_from', 'date_to')
    EnableEditFields.short_description = " تعديل"  
    DisableEditFields.short_description = "الغاء التعديل"  
    actions = ['EnableEditFields','DisableEditFields']

admin.site.register(Holiday, HolidayAdmin)

