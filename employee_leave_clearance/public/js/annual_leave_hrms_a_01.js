frappe.ui.form.on("Salary Slip", {
    setup: function(frm) {
        $.each(["earnings_two"], function(i, table_fieldname) {
            frm.get_field(table_fieldname).grid.editable_fields = [
//                {fieldname: 'salary_component', columns: 3},
//                {fieldname: 'abbr', columns: 4},
//                {fieldname: 'amount', columns: 3}
                {fieldname: 'salary_component', columns: 6},
                {fieldname: 'amount', columns: 4}
            ];
        });
        $.each(["deductions_two"], function(i, table_fieldname) {
            frm.get_field(table_fieldname).grid.editable_fields = [
                {fieldname: 'salary_component', columns: 6},
                {fieldname: 'amount', columns: 4}
            ];
        });
    }
});

frappe.ui.form.on("Salary Slip", {
    onload: function(frm) {
        $.each(["earnings_two"], function(i, table_fieldname) {
            frm.get_field(table_fieldname).grid.editable_fields = [
//                {fieldname: 'salary_component', columns: 3},
//                {fieldname: 'abbr', columns: 4},
//                {fieldname: 'amount', columns: 3}
                {fieldname: 'salary_component', columns: 6},
                {fieldname: 'amount', columns: 4}
            ];
        });
        $.each(["deductions_two"], function(i, table_fieldname) {
            frm.get_field(table_fieldname).grid.editable_fields = [
                {fieldname: 'salary_component', columns: 6},
                {fieldname: 'amount', columns: 4}
            ];
        });
    },

});



// ================= Leave Application ========================

frappe.ui.form.on("Leave Application", {
    refresh: function(frm) {
//    onload: function(frm) {
//        if (frm.doc.salary_for_the_vacation_month && frm.doc.docstatus===0 && frm.doc.total_leave_days >= 21) {
//        if (frm.doc.docstatus === 0 && frm.doc.total_leave_days >= 21) {
        if (frm.doc.docstatus === 0 && frm.doc.total_leave_days >= 21 && frm.doc.nationality_leave === "Non-Saudi" ) {
            frm.add_custom_button(__('Create Salary Slip'), function() {
                frappe.call({
//                    method: "employee_leave_clearance.employee_leave_clearance.doctype.employee_leave_clearance_a_001_doctype.employee_leave_clearance_a_001_doctype.validate_leave_application",
                    method: "employee_leave_clearance.employee_leave_clearance.doctype.employee_leave_clearance_a_001_doctype.employee_leave_clearance_a_001_doctype.validate_leave_application",
                    args: {
                        "doc": frm.doc
                    },
                    callback: function(response) {
                        if (response.message) {
                            frappe.show_alert({
                                message: __(response.message),
                                indicator: 'green'
                            });
                            frm.reload_doc();
                        }
                    }
                });
            }).addClass('btn-warning').css({
                'color': 'white',
                'font-weight': 'bold',
                'background-color': '#274472'
            });
        }
    }
});


//// =========================================================
//// =========================================================
//// =========================================================