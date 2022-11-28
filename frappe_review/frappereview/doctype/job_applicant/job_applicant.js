// Copyright (c) 2022, Sunil and contributors
// For license information, please see license.txt

frappe.ui.form.on('Job Applicant', {

	validate: function(frm){
		frm.set_value({
			'full_name' : frm.doc.fname + ' ' + frm.doc.middle_name + ' '+ frm.doc.last_name
		})
	}
});
