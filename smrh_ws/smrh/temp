def contact(request):
    user = users.get_current_user()
    if user is None:
	    return HttpResponseRedirect('/accounts/login') # Redirect after POST

    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
	    fformFiedls = FormFields()
	    formFiedls.fieldType = "text"
	    formFiedls.fieldName = "Custom text1"
	    formFiedls.fieldDataType = "int"
	    formFiedls.pointTable = "Employee"
	    formFiedls.pointColumn = "name"
	    formFiedls.save()
	    
	    formFiedls1 = FormFields()
	    formFiedls1.fieldType = "text"
	    formFiedls1.fieldName = "Custom text1"
	    formFiedls1.fieldDataType = "int"
	    formFiedls1.pointTable = "Employee"
	    formFiedls1.pointColumn = "name"
	    formFiedls1.save()

	    customForm = CustomForm()
	    customForm.formName = "testForm"
	    customForm.orgName = "rensys"
	    customForm.formFields.append(customFormFields)
	    customForm.formFields.append(formFiedls1)
	    customForm.theCustomText1 = "the txt in field1"
	    customForm.theCustomText2 = "the txt in field1"
	    customForm['theCustomText3'] = "the txt in fied3"
	    print customForm.dynamic_properties()

            return HttpResponseRedirect('/contacts/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form
	formFiedls = FormFields()
	formFiedls.fieldType = "text"
	formFiedls.fieldName = "Custom text1"
	formFiedls.fieldDataType = "int"
	formFiedls.pointTable = "Employee"
	formFiedls.pointColumn = "name"
	formFiedls.save()
	formFiedls1 = FormFields()
	formFiedls1.fieldType = "text"
	formFiedls1.fieldName = "Custom text1"
	formFiedls1.fieldDataType = "int"
	formFiedls1.pointTable = "Employee"
	formFiedls1.pointColumn = "name"
	formFiedls1.save()
	
	customForm = CustomForm()
	customForm.formName = "testForm"
	customForm.orgName = "rensys"
	customForm.customFormFields.append(formFiedls.key())
	customForm.customFormFields.append(formFiedls1.key())
	customForm.theCustomText1 = "the txt in field1"
	customForm.theCustomText2 = "the txt in field1"
	setattr(customForm,'theCustomText3',85934589)
	#print "\n #################### the customForm %s  ################ \n" %(getattr(customForm,'theCustomText1'))
	#print "\n #################### the customForm 3 ---> %s  ################ \n" %(getattr(customForm,'theCustomText3'))
	#customForm['theCustomText3'] = "the txt in fied3"
	'''self.response.headers['Content-Type'] = 'text/plain'
	self.response.out.write("the views are %s"%(customForm.dynamic_properties()))'''
	


    return render_to_response('smrh/contact.html', {
	    'form': form,'customFormDyFields':customForm.dynamic_properties(),'theListFiedls':customForm.customFormFields,
    })


