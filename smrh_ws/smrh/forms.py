from django.db import models
from django.forms import ModelForm
from models import Contact,EmployeeDetails,EmpPhoneDetails,EmpAddressDetails


class ContactForm(ModelForm):
	class Meta:
		model = Contact
	def is_valid(self):
		print ('the forn is %s' %(self))
		return True

class EmployeeForm(ModelForm):
	class Meta:
		model = EmployeeDetails 
	def is_valid(self):
		print ('the forn is %s' %(self))
		return True

class EmployeePhForm(ModelForm):
	class Meta:
		model = EmpPhoneDetails
	def is_valid(self):
		print ('the forn is %s' %(self))
		return True
class EmployeeAddrForm(ModelForm):
	class Meta:
		model = EmpAddressDetails
		exclude = ('employee',)
	def is_valid(self):
		print ('the form is %s' %(self))
		return True
'''class EmployeeDepedents(ModelForm):
	class Meta:
		model = EmployeeDepedents 
		exclude = ('employee',)
	def is_valid(self):
		print ('the form is %s' %(self))
		return True'''
