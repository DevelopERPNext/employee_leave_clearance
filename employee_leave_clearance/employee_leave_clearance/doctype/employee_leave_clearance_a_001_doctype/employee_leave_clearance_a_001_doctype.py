# Copyright (c) 2024, khattab.info and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


import time
import datetime
import calendar

import json
from frappe import _
from frappe.utils import (
    add_days,
    cint,
    cstr,
    date_diff,
    flt,
    formatdate,
    get_fullname,
    get_link_to_form,
    getdate,
    nowdate,
)

from frappe.utils import (money_in_words,)





class EmployeeLeaveClearancea001DocType(Document):
    pass



@frappe.whitelist()
def create_print_msg(doc, method=None):
    frappe.msgprint("Test ******* -----  ********* All")


# ======================================================================
# ======================================================================

@frappe.whitelist()
def get_latest_salary_slip(doc, method=None):
    # employee_name = frappe.get_value("Employee", {"employee": employee}, "employee_name")
    # employee = "HR-EMP-00001"
    employee = doc.employee

    # if not employee_name:
    #     frappe.msgprint(f"Employee with ID {employee} not found.")
    #     return None

    salary_slips = frappe.get_all(
        "Salary Slip",
        filters={"docstatus": 1, "employee": employee},
        order_by="creation desc",
        limit=1
    )

    if salary_slips:
        # return frappe.get_doc("Salary Slip", salary_slips[0].name)

        # frappe.msgprint(str(employee))
        # frappe.msgprint(str("****************"))
        # frappe.msgprint(str(salary_slips))
        # frappe.msgprint(str("==============="))
        # frappe.msgprint(str(frappe.get_doc("Salary Slip", salary_slips[0].name)))
        # frappe.msgprint(str('======= End  \' get_latest_salary_slip \' ========'))

        return salary_slips

def calculate_per_day_salary_components(doc, method=None):
    employee = doc.employee

    salary_slip_name = ""

    salary_slips = frappe.get_all(
        "Salary Slip",
        filters={"docstatus": 1, "employee": employee},
        order_by="creation desc",
        limit=1
    )

    if salary_slips:
        salary_slip_name = salary_slips[0].name

    salary_detail_list = frappe.get_all(
        "Salary Detail",
        filters={"parent": salary_slip_name},
        fields=["name", "abbr", "default_amount", "parent"],
    )

    per_component_per_day = {}
    #
    for salary_detail in salary_detail_list:
        salary_component_abbr = salary_detail.get("abbr")
        default_amount = salary_detail.get("default_amount")

        salary_component = frappe.get_all(
            "Salary Component",
            filters={"salary_component_abbr": salary_component_abbr, "include_in_annual_leave": 1},
            fields=["name", "salary_component_abbr"],
        )

        if salary_component:
            # # per_day_amount = default_amount / 30
            # # per_component_per_day[salary_component_abbr] = per_day_amount
            # frappe.msgprint("********** test *********")
            # frappe.msgprint(str(salary_component))
            # frappe.msgprint("********** test *********")
            per_day_amount = default_amount / 30
            per_component_per_day[salary_component_abbr] = per_day_amount
            # frappe.msgprint("********** ======== *********")
            # frappe.msgprint(str(per_component_per_day[salary_component_abbr]))
            # frappe.msgprint("********** ======== *********")
            # # per_component_per_day[salary_component_abbr] = per_day_amount * 10
            # # per_component_per_day[salary_component_abbr] = per_day_amount * doc.total_working_days
            per_component_per_day[salary_component_abbr] = per_day_amount * doc.leave_days
            # frappe.msgprint(str(per_component_per_day[salary_component_abbr]))


    # # # # return per_component_per_day
    # frappe.msgprint(str("==========  **** ============"))
    # frappe.msgprint(str(salary_slip_name))
    # frappe.msgprint(str("==========  --------- ============"))
    # frappe.msgprint(str(salary_detail_list))
    # # frappe.msgprint(str("==============="))
    # # frappe.msgprint(str(per_component_per_day))
    # # frappe.msgprint(str(per_day_amount))
    # frappe.msgprint(str('======= End  \' calculate_per_day_salary_components \' ========'))



# =============== {Leave Calculation} adding in table Earnings Two =================================


def adding_per_salary_components(doc, method=None):
    employee = doc.employee
    salary_slip_name = ""
    salary_components = []
    total_amount = 0

    total_gross_pay = doc.gross_pay

    salary_slips = frappe.get_all(
        "Salary Slip",
        filters={"docstatus": 1, "employee": employee},
        order_by="creation desc",
        limit=1
    )

    if doc.data_check_leave_application == 1 :
        if salary_slips:
            salary_slip_name = salary_slips[0].name

        salary_detail_list = frappe.get_all(
            "Salary Detail",
            filters={"parent": salary_slip_name},
            fields=["name", "abbr", "default_amount", "parent"],
        )

        per_component_per_day = {}
        for salary_detail in salary_detail_list:
            salary_component_name = salary_detail.get("name")
            salary_component_abbr = salary_detail.get("abbr")
            default_amount = salary_detail.get("default_amount")

            salary_component = frappe.get_all(
                "Salary Component",
                filters={"salary_component_abbr": salary_component_abbr, "include_in_annual_leave": 1},
                fields=["name", "salary_component_abbr"],
            )


            if salary_component:
                per_day_amount = default_amount / 30
                per_component_per_day[salary_component_abbr] = per_day_amount
                # per_component_per_day[salary_component_abbr] = per_day_amount * doc.leave_days

                per_component_per_day[salary_component_abbr] = int(per_day_amount * int(doc.leave_days))


                for component_data in salary_component:
                    component_abbr = component_data.get('salary_component_abbr')

                    existing_components_abbr = [comp.get('abbr') for comp in doc.earnings_two]
                    if component_abbr in existing_components_abbr:
                        continue

                    doc.append('earnings_two', {
                        'salary_component': component_data.get('name'),
                        'abbr': component_abbr,
                        'amount': float(per_component_per_day.get(component_abbr, 0))
                    })


        for earning in doc.earnings_two:
            if isinstance(earning.amount, float) or isinstance(earning.amount, int):
                total_amount += earning.amount

        # frappe.msgprint(str(total_amount), alert=True)
        # frappe.msgprint(str(total_gross_pay), alert=True)

        total_gross_pay += total_amount
        doc.gross_pay = total_gross_pay
        doc.net_pay = (doc.gross_pay - doc.total_deduction)
        doc.rounded_total = (doc.gross_pay - doc.total_deduction)

        doc.total_in_words = money_in_words(doc.net_pay)

        return salary_components


# ==================================================================
# ==================================================================




#  =================== Leave Application Calc Working Days - 1 =====================================
# ==================================================================================================
# ================================  validate_leave_application =====================================





@frappe.whitelist()
def working_days_leave_application(doc, method=None):
    # # doc_all = frappe.parse_json(doc)
    # frappe.msgprint(f"{doc.get('from_date')}", alert=True)

    if isinstance(doc.get('from_date'), str):
        from_date = datetime.datetime.strptime(doc.get('from_date'), "%Y-%m-%d").date()
    else:
        from_date = doc.get('from_date')

    working_days_calc = get_days_of_attendance_this_month(from_date)
    # frappe.msgprint(f"{working_days_calc}", alert=True)
    #
    # # frappe.db.set_value('Leave Application', doc_all.get('name'), 'working_days', working_days_calc)
    # # frappe.db.set_value('Leave Application', doc.name, 'working_days', working_days_calc)
    # # frappe.db.commit()

    doc.working_days = working_days_calc
    frappe.msgprint("Save successful!", alert=True)




@frappe.whitelist()
def set_nationality(doc, method=None):
    nationality = frappe.get_value("Employee", {"employee": doc.employee}, "nationality")
    doc.nationality_leave = nationality



@frappe.whitelist()
def validate_leave_application(doc, method=None):
    doc = frappe.parse_json(doc)

    if 'from_date' not in doc:
        frappe.throw("Attribute 'from_date' is missing in the input data.")

    from_date_str = doc.get('from_date')

    try:
        from_date = datetime.datetime.strptime(from_date_str, "%Y-%m-%d").date()
    except ValueError:
        frappe.throw("Invalid date format for 'from_date'. Use format 'YYYY-MM-DD'.")

    working_days = get_days_of_attendance_this_month(from_date)

    # frappe.throw(str(working_days))

    doc['working_days'] = working_days

    # frappe.msgprint(f"Updated working_days: {working_days}", alert=True)
    # frappe.msgprint("====================", alert=True)

    doc_obj = frappe.get_doc("Leave Application", doc.get('name'))

    doc_obj.working_days = working_days
    doc_obj.save(ignore_permissions=True)

    # frappe.msgprint(str(from_date), alert=True)
    # frappe.msgprint("====================", alert=True)
    # frappe.msgprint(str(working_days), alert=True)

    doc.working_days = working_days





    doc_data_attendance = {
        'employee': doc.get('employee'),
        'status': "Present",
        'from_date': frappe.utils.get_first_day(frappe.utils.getdate(doc.get('from_date'))),
        'working_days': doc.get('working_days')
    }

    create_attendance(doc_data_attendance)


    doc_data = {
        'employee': doc.get('employee'),
        'from_date': frappe.utils.get_first_day(frappe.utils.getdate(doc.get('from_date'))),
        'working_days': doc.get('working_days'),
        'total_leave_days': doc.get('total_leave_days')
    }

    create_salary_slip(doc_data)

    frappe.msgprint(str("Salary Slip has been created."), alert=True)



# # ===================================================================


@frappe.whitelist()
def create_salary_slip(doc, method=None):
    salary_slip = frappe.new_doc('Salary Slip')
    salary_slip.employee = doc.get('employee')
    salary_slip.start_date = frappe.utils.get_first_day(frappe.utils.getdate(doc.get('from_date')))

    salary_slip.total_working_days = doc.get('working_days')

    # frappe.db.set_value('Salary Slip', {'name': salary_slip.name, }, 'payment_days', doc.get('working_days'))
    salary_slip.payment_days = doc.get('working_days')

    salary_slip.leave_days = doc.get('total_leave_days')
    salary_slip.total_payment_days = doc.get('total_leave_days') + doc.get('working_days')

    salary_slip.data_check_leave_application = True

    salary_slip.save(ignore_permissions=True)




@frappe.whitelist()
def create_attendance(doc, method=None):
    total_working_days = doc.get('working_days')
    updated_working_days = 0
    from_date = frappe.utils.getdate(doc.get('from_date'))
    attendance_date = from_date.replace(day=1)

    for _ in range(total_working_days):
        if not frappe.db.exists('Attendance', {'employee': doc.get('employee'), 'attendance_date': attendance_date}):
            attendance = frappe.new_doc('Attendance')
            attendance.employee = doc.get('employee')
            attendance.status = "Present"
            attendance.attendance_date = attendance_date

            attendance.save(ignore_permissions=True)
            attendance.submit()
        else:
            frappe.msgprint(
                f"Attendance for employee {doc.get('employee')} is already marked for the date {attendance_date}",
                alert=True)

        attendance_date += datetime.timedelta(days=1)
        updated_working_days += 1



# # ==========================================
#     # Move to the next month
#     next_month = attendance_date.month % 12 + 1
#     next_year = attendance_date.year + attendance_date.month // 12
#     attendance_date = attendance_date.replace(year=next_year, month=next_month)
# # ==========================================


# # ====================================
# # ====================================
# # :::::::::::::::::::::::::::
# # ---------------------------
# # :::::::::::::::::::::::::::



def get_days_of_attendance_this_month(from_date):
    first_day_of_month = datetime.date(from_date.year, from_date.month, 1)
    days_of_attendance_this_month = get_number_of_days_in_period(
        first_day_of_month.strftime("%Y-%m-%d"), from_date.strftime("%Y-%m-%d"))
    return days_of_attendance_this_month - 1

def get_number_of_days_in_period(from_date, to_date):
    from_date = datetime.datetime.strptime(from_date, "%Y-%m-%d").date()
    to_date = datetime.datetime.strptime(to_date, "%Y-%m-%d").date()
    num_days = (to_date - from_date).days + 1
    if from_date.day == 1:
        return num_days
    else:
        days_in_month = get_number_of_days_in_month(from_date)
        days_in_first_month = days_in_month - from_date.day + 1
        days_in_last_month = to_date.day
        days_in_between_months = 0
        for year_month in range(from_date.year * 12 + from_date.month + 1, to_date.year * 12 + to_date.month):
            year, month = divmod(year_month, 12)
            if month == 0:
                month = 12
                year -= 1
            days_in_between_months += get_number_of_days_in_month(datetime.date(year, month, 1))
        return days_in_first_month + days_in_between_months + days_in_last_month

def get_number_of_days_in_month(date):
    return calendar.monthrange(date.year, date.month)[1]

# # :::::::::::::::::::::::::::
# # ---------------------------
# # :::::::::::::::::::::::::::
# # ====================================
# # ====================================










