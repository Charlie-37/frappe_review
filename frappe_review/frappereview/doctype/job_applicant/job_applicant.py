# Copyright (c) 2022, Sunil and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class JobApplicant(Document):
	def validate(self):
		if len(self.mobile_number) == 10:
			frappe.msgprint('Perfect 10 digit')

		else:
			frappe.throw('Not 10 digit')
					
	def on_update(self):
		frappe.msgprint('It is on update')

	def before_insert(self):
		frappe.msgprint('It is on before Insert')
    		
    	
		
    	
    	 			  	
	def on_submit(self):
    		
		if self.workflow_state == 'Approved': 
			doc = frappe.new_doc('Employee')
			doc.fname = self.fname
			doc.last_name = self.last_name
			doc.middle_name = self.middle_name
			doc.full_name = self.full_name
			doc.designation = self.job_role
			doc.mobile_number = self.mobile_number

			for i in self.app_past_company:
				doc.append('emp_past_company',{
					'past_company_name' : i.past_company_name,
					'designation' : i.designation,
					'kra':i.kra,
					'technologies_used': 'i.technologies_used'
				})

			doc.save()
			doc.submit()

		


	
		




    		

