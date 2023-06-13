# note
# don't forget to change Cascade in this line :
# mainunit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True,blank=True,verbose_name = " الحالة الصادر لها")

from datetime import timedelta
from django.db import models
from django.utils import timezone
from dateutil.relativedelta import relativedelta
levelchoices=[
    ('soldier','جندى'),
    ('arrif','عريف'),
    ('raqib','رقيب'),
    ('raqiba','رقيب اول'),
    ('mosaid','مساعد'),
    ('mosaida','مساعد اول'),
    ('molazim','ملازم'),
    ('molazima','ملازم أول'),
    ('naqib','نقيب'),
    ('raid','رائد'),
    ('moqadim','مقدم'),
    ('aqid','عقيد'),
    ('amid','عميد'),
    ('lwaa','لواء'),
]

branchchoices=[
    ('secrtary','السكرتارية'),
    ('nozom','نظم'),
    ('intag','انتاج'),
    ('tasleeh','تسليح'),
    ('tafteesh',' تفتيش'),
    ('amn','امن'),
    ('maly',' مالى'),
    ('tanzimafrad','تنظيم وافراد'),
    ('shdobat',' شئون ضباط'),
    ('takhtit','تخطيط'),
    ('hamla','حملة'),
    ('ishara','اشارة'),
    ('kadaa','قضاء'),
    ('motabaa','متابعة'),
    ('tadreeb','تدريب'),
]

hliday_types=[
    ('leave','اجازة معتادة'),
    ('rest','راحة'),
    ('emerg','عارضة'),
    ('crest','بدل راحة'),
    ('yearly','سنوية'),
    ('mission',' مأمورية'),
    ('training','دورة'),
]


# verbose_name='عنوان الامتحان'
# class Meta:
#         verbose_name_plural = 'الامتحانات'
#         ordering = ['created_at']

class Unit(models.Model):
    mainunit = models.CharField(max_length=200 ,verbose_name='الوحدة الاساسية') # الوحدة الاساسية
    class Meta:
        verbose_name_plural = 'الوحدات الاساسية'
        verbose_name=' وحده اساسية'
    def __str__(self):
        return self.mainunit

class Person(models.Model):
    name = models.CharField(verbose_name = " الاسم",max_length=200,null=True,blank=True)
    national_id = models.CharField(verbose_name = " الرقم القومى",max_length=14 ,null=True,blank=True)
    military_number = models.CharField(verbose_name = " الرقم العسكرى",max_length=13 ,null=True,blank=True)
    level = models.CharField(verbose_name = " الرتبة او الدرجة",choices=levelchoices ,max_length=50,default='soldier') # الرتبة
    date_added = models.DateField(verbose_name = " تاريخ الانضمام",default=timezone.now(),null=True,blank=True)
    date_out = models.DateField(verbose_name = " تاريخ التسريح",null=True,blank=True)
    mainunit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True,blank=True,verbose_name = "   الوحدة الاساسية") 
    branch = models.CharField(verbose_name = "  الفرع",choices=branchchoices ,max_length=100,default='secrtary') 
    # redif_detection = models.CharField(max_length=5,null=True,blank=True) 
    class Meta:
        verbose_name_plural = ' الافراد'
        verbose_name='  فرد'

    def detect_redif_wich_dofaa(self):
        if self.date_out:
            redif_time = self.date_out - timedelta(days=3 * 30)
            # redif_time = self.date_out - relativedelta(months=3)
            months = redif_time.month
            years = redif_time.year
            redif_formatted = f"{years}-{months}"
        else:
            redif_formatted = 'غير معروف'
        return redif_formatted
    
    # def soldiers_number(self):
    #     return Person.objects.filter(level='soldier').count()
    # def saf_number(self):
    #     return Person.objects.filter(level='soldier').count() + User.objects.filter(level='arrif').count() + User.objects.filter(level='raqib').count() + User.objects.filter(level='raqiba').count() + User.objects.filter(level='mosaid').count() + User.objects.filter(level='mosaida').count()  
    
    detect_redif_wich_dofaa.short_description = 'رديف دفعة'
    # soldiers_number.short_description = 'عدد الجنود'
    # saf_number.short_description = 'عدد ضباط الصف'

    def __str__(self):
        return self.name

class Holiday(models.Model):
    # person = models.ManyToManyField(Person,verbose_name = "الفرد") 
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True,blank=True,verbose_name = "الفرد") 
    hliday_type = models.CharField(verbose_name = "نوع الاجازة",choices=hliday_types ,default= 'leave' ,max_length=100)
    date_from = models.DateField(verbose_name = "تاريخ الذهاب",default=timezone.now(),null=True,blank=True)
    date_to = models.DateField(verbose_name = "تاريخ العوده",default=timezone.now()+timedelta(days=7),null=True,blank=True)

    def __str__(self) :
        return self.person.name

    class Meta:
        verbose_name_plural = ' الاجازات'
        verbose_name='  اجازة'
