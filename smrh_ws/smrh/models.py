from django.db import models
import datetime
from google.appengine.ext import db


# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question
    
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    def __unicode__(self):
        return self.choice

class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
    	def __unicode__(self):
        	return self.choice

class CustomForm(db.Expando):
	formName = db.StringProperty(multiline=True)
	orgName = db.StringProperty(multiline=True)
	#customFields = db.ListProperty(FormFields)
	customFormFields = db.ListProperty(db.Key)

class FormFields(db.Model):
	fieldType = db.StringProperty(multiline=True)
	fieldName = db.StringProperty(multiline=True)
	fieldDataType = db.StringProperty(multiline=True)
	pointTable = db.StringProperty(multiline=True)
	pointColumn = db.StringProperty(multiline=True)

class Desc(object):
    
    def __get__(self, obj, cls=None):
        pass

    def __set__(self, obj, val):
        pass

    def __delete__(self, obj):
        pass

class EmployeeDetails(models.Model):
	firstName = models.CharField(max_length=200)
	lastName = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	nickName = models.CharField(max_length=200)
	dob = models.DateTimeField()
	bloodGroup = models.CharField(max_length=200)
	secondaryEmail = models.CharField(max_length=200)
	twitterId = models.CharField(max_length=200)
	facebook = models.CharField(max_length=200)
	website = models.CharField(max_length=200)
	currentCompanyId = models.IntegerField()
	currentDesignation = models.CharField(max_length=200)



class EmpPhoneDetails(models.Model):
	employee = models.BigIntegerField(editable=False)
	phone = models.CharField(max_length=100)
	phoneType= models.CharField(max_length=100)
'''class FormValues(db.Model):
	formName = db.StringProperty(multiline=True)
	value = db.StringProperty(multiline=True)'''
class EmpAddressDetails(models.Model):
	employee = models.ForeignKey(EmployeeDetails)
	addrLine1 = models.CharField(max_length=200)
	addrLine2 = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	country = models.CharField(max_length=200)

class EmpDependents(models.Model):
	employee = models.ForeignKey(EmployeeDetails)
	deptId = models.IntegerField()
	firstName = models.CharField(max_length=200)
	lastName = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=100)
	dob = models.DateTimeField()
	relatedBy = models.CharField(max_length=100)
class EmpRoles(models.Model):
	employee = models.ForeignKey(EmployeeDetails)

