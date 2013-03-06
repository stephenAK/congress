from django.db import models
from django.db import models
from django.contrib import admin
from reg.thumbs import ImageWithThumbsField
from reg.thumbs import generate_thumb
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe

'''
class AdminImageFieldWithThumbWidget(AdminFileWidget):
     
     def render(self,name,value,attrs = None):
         thumb_html = ""
         if value and hasattr(value,"url"):
            thumb_html = '<img src ="%s" width ="60" />'%(value.url)
	    return mark_safe("%s%s" %(thunb_html,super (AdminImageFieldWithThumbWidget,self).render(name,value,attrs)))

class imageAdmin(admin.ModelAdmin):
      
      def formfield_for_dbfield(self, db_field,**kwargs):
          if db_field.name =='image':
              from django import forms
              return forms.CharField(widget = AdminImageFieldWithThumbWidget(**kwargs))
          else:
              return super(imageAdmin,self).formfield_for_dbfield(db_field,**kwargs)
'''
class Host_detail(models.Model):
 
     host_ID = models.AutoField(primary_key=True,editable = False,blank = True)
     surname = models.CharField(max_length = 30)
     other_name = models.CharField("Other name(s) ",blank = True,null = True,max_length = 30,help_text ="May enter initials/ Last name")
     sex = models.CharField('Gender', choices =(("Male","Male"),("Female","Female")),max_length = 7)
     phone_number = models.CharField(max_length = 15,blank = True, null = True)
     Email = models.EmailField(blank = True,null = True)
     hall = models.CharField('Halls', choices=(("COMMONWEALTH","COMMONWEALTH"),("VOLTA","VOLTA"),("LEGON","LEGON"),("AKUAFO","AKUAFO"),("SARBAH","SARBAH"),   ("JUBILEE","JUBILEE"),("JEAN-NELSON","JEAN-NELSON"),("ALEX-KWAPONG","ALEX-KWAPONG"),("SEY","SEY"),("PENTAGON","PENTAGON"),("LEMAN","LEMAN"),("OTHER","OTHER")),max_length = 20)
     room_number = models.CharField(max_length = 90,blank = True, null = True)
     is_hosting = models.BooleanField(('hosting status'),default = False,
        help_text=('Designates whether the person is hosting someone'))
     #is_hosting = models.CharField (max_length = 3, choices = (("YES","YES"),("NO","NO")))
     #number_of_guest = models.CharField(max_length = 10,null = True, blank = True,default = 'NONE')
     #photo = ImageWithThumbsField(upload_to='images', sizes=((125,125),(300,200)),blank =True, null = True)
     #pic = models.ImageField(upload_to='images', sizes=((125,125),(300,200)),blank =True, null = True)
     date_registered  = models.DateTimeField (auto_now_add=True, blank =True, null = True)
     date_updated     = models.DateTimeField (auto_now=True,blank =True, null = True)
    # guest_count = lambda(self:self.guest_detail_set.count())   

     def host_vital(self):
         return '%s | %s | %s' % (self.phone_number,self.hall,self.is_hosting) 

     def ID(self):
           if self.host_ID <10:
               return "#00%s" %(self.host_ID)
           elif self.host_ID> 9:
               return "#0%s" %(self.host_ID)
           else:
               return "#%s" %(self.host_ID)


     def __unicode__(self):
           return '%s %s || %s ' % (self.surname.upper(), self.other_name.upper(), self.phone_number)  
    
     def guests(self):
                return self.guest_detail_set.count()
             
     def is_hosting_(self):
          if self.guest_detail_set.count()  > 0:
             	self.is_hosting = True
                self.save()                 
                return "YES"
          elif self.guest_detail_set.count()== 0:
                self.is_hosting = False
                self.save()
                return "NO"

     def r00m_number(self):
	   return "%s" %(self.room_number.upper()) 
     

     class Meta:
		verbose_name 	    = "Host Details"
		verbose_name_plural = "Host Details"
		ordering 	    = ('surname', 'other_name','host_ID')
      
 
     def Full_name (self):
          return '%s %s' % (self.surname.upper(), self.other_name.upper())
'''    
     def admin_image(self):
         if self.photo:
              return  '<embed src="%s" </embed>' %(self.photo.url_125x125)
             #return u'<img src ="%s" />'%(self.photo.url_125x125)
         else:
             return 'no image'
     admin_image.short_description = 'Thumbnail'
     admin_image.allow_tags = True
       

     class AdminImageFieldWithThumbWidget(AdminFileWidget):
     
       def render(self,name,value,attrs = None):
          thumb_html = ""
          if value and hasattr(value,"url"):
             thumb_html = '<img src ="%s" width ="60" />'%(value.url)
	     return mark_safe("%s%s" %(thunb_html,super (AdminImageFieldWithThumbWidget,self).render(name,value,attrs)))

     class imageAdmin(admin.ModelAdmin):
      
       def formfield_for_dbfield(self, db_field,**kwargs):
           if db_field.name =='image':
               from django import forms
               return forms.CharField(widget = AdminImageFieldWithThumbWidget(**kwargs))
           else:
               return super(imageAdmin,self).formfield_for_dbfield(db_field,**kwargs)  
'''
class Guest_detail(models.Model):
 
     guest_ID = models.AutoField(primary_key=True,editable = False)
     surname = models.CharField(max_length = 30)
     other_name = models.CharField("Other name(s) ",max_length = 30,help_text ="Please Enter initials/ Last name")
     sex = models.CharField('Gender', choices =(("Male","Male"),("Female","Female")),max_length = 7)
     institution = models.CharField('Institution',choices =(("KNUST","KNUST"),("UCC","UCC"),("UPS","UPS"),("UDS","UDS"),("OTHER","OTHER")),max_length = 7)
     Nationality = models.CharField('Country', choices =(("Ghana","Ghana"),("Nigeria","Nigeria"),("Other","Other")),max_length = 10)
     phone_number = models.CharField(max_length = 15,null = True, blank = True)
     Email = models.EmailField(blank = True, null = True)
     date_registered  = models.DateTimeField (auto_now_add=True, blank =True, null = True)
     date_updated     = models.DateTimeField (auto_now=True,blank =True, null = True)
     host   = models.ForeignKey(Host_detail, null = True, blank = True)
   

     def __unicode__(self):
           return '%s %s' % (self.surname.upper(), self.other_name.upper())
   
     class Meta:
		verbose_name 	    = "Guest Details"
		verbose_name_plural = "Guest Details"
		ordering 	    = ('guest_ID', 'surname','other_name')
    
     def Full_name (self):
          return '%s %s' % (self.surname.upper(), self.other_name.upper())

     def guest_id (self):
         if self.guest_ID <10:
              return '00%s' % (self.guest_ID)
         else:
             return '0%s' % (self.guest_ID)
     def guest_hall(self):
	  if self.host:
            guest_Hall = self.host.hall
            return "%s" %(guest_Hall)

     def guest_institution(self):
         return '%s | %s | %s' % (self.institution,self.host.hall,self.phone_number) 
    # def host_status(self):
     #    if self.save():
      #       self.host.save()
       #  else:
        #    self.host.save()

     def host_gender(self):
          return "%s" %(self.host.sex)
     def host_room_number(self):
         return "%s" %(self.host.room_number.upper())
     def ID(self):
         if self.guest_ID <10:
               return "#00%s" %(self.guest_ID)
         elif self.guest_ID> 9:
               return "#0%s" %(self.guest_ID)
         else:
               return "#%s" %(self.guest_ID)

class Alumni(models.Model):
     ID = models.AutoField(primary_key=True,editable = False)
     surname = models.CharField(max_length = 30)
     other_name = models.CharField("Other name(s) ",max_length = 30,help_text ="Please Enter initials/ Last name")
     sex = models.CharField('Gender', choices =(("Male","Male"),("Female","Female")),max_length = 7)
     institution = models.CharField('Institution',choices =(("KNUST","KNUST"),("UCC","UCC"),("UPS","UPS"),("UDS","UDS"),("OTHER","OTHER")),max_length = 7)
     phone_number = models.CharField(max_length = 15,null = True, blank = True)
     email = models.EmailField('Email-address',blank = True, null = True)
     Banquet = models.BooleanField(default=False,
        help_text=('Designates whether the person was/would be available for the Banquet'))
     comment = models.TextField(blank = True,null =True)
     date_registered  = models.DateTimeField (auto_now_add=True, blank =True, null = True)
     date_updated     = models.DateTimeField (auto_now=True,blank =True, null = True)
    
     def Full_name (self):
          return '%s %s' % (self.surname.upper(), self.other_name.upper())

     class Meta:
		verbose_name 	    = "Alumni Details"
		verbose_name_plural = "Alumni Details"
		ordering 	    = ('ID', 'surname','other_name')


     def __unicode__(self):
           return '%s %s' % (self.surname.upper(), self.other_name.upper())
     
     def comment_first_10(self):
		return self.comment[:10]



class GuestInline(admin.TabularInline):
	model = Guest_detail     
  

class Host_Admin(admin.ModelAdmin):
      list_display = ('host_ID','Full_name','phone_number','hall','r00m_number','is_hosting_','guests')
      search_fields = ('host_ID','surname','other_name')
      list_filter = ('sex','is_hosting','hall','date_registered','date_updated')
      ordering = ('-date_registered',)
      date_hierarchy = 'date_registered'
      list_per_page = 20
      inlines = [GuestInline]

class Guest_Admin(admin.ModelAdmin):
      list_display = ('guest_ID','Full_name','phone_number','institution','sex','host','host_gender','guest_hall','host_room_number')
      search_fields = ('guest_ID','surname','other_name')
      list_filter = ('sex','date_registered','date_updated')
      ordering = ('-date_registered',)
      date_hierarchy = 'date_registered'
      raw_id_fields = ('host',)
      list_per_page = 20

class Alumni_Admin(admin.ModelAdmin):
      list_display = ('ID','Full_name','phone_number','institution','sex','email','Banquet','comment_first_10')
      search_fields = ('ID','surnname','other_name')
      list_filter = ('sex','date_registered','institution')
      ordering = ('-date_registered',)
      date_hierarchy = 'date_registered'
      list_per_page = 20


admin.site.register(Host_detail,Host_Admin)
admin.site.register(Guest_detail,Guest_Admin)
admin.site.register(Alumni,Alumni_Admin)


