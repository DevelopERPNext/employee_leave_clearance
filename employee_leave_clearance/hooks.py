app_name = "employee_leave_clearance"
app_title = "Employee Leave Clearance"
app_publisher = "khattab.info"
app_description = "employee leave clearance"
app_email = "info@khattab.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/employee_leave_clearance/css/employee_leave_clearance.css"
# app_include_js = "/assets/employee_leave_clearance/js/employee_leave_clearance.js"

# include js, css files in header of web template
# web_include_css = "/assets/employee_leave_clearance/css/employee_leave_clearance.css"
# web_include_js = "/assets/employee_leave_clearance/js/employee_leave_clearance.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "employee_leave_clearance/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "employee_leave_clearance/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "employee_leave_clearance.utils.jinja_methods",
# 	"filters": "employee_leave_clearance.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "employee_leave_clearance.install.before_install"
# after_install = "employee_leave_clearance.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "employee_leave_clearance.uninstall.before_uninstall"
# after_uninstall = "employee_leave_clearance.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "employee_leave_clearance.utils.before_app_install"
# after_app_install = "employee_leave_clearance.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "employee_leave_clearance.utils.before_app_uninstall"
# after_app_uninstall = "employee_leave_clearance.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "employee_leave_clearance.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"employee_leave_clearance.tasks.all"
# 	],
# 	"daily": [
# 		"employee_leave_clearance.tasks.daily"
# 	],
# 	"hourly": [
# 		"employee_leave_clearance.tasks.hourly"
# 	],
# 	"weekly": [
# 		"employee_leave_clearance.tasks.weekly"
# 	],
# 	"monthly": [
# 		"employee_leave_clearance.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "employee_leave_clearance.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "employee_leave_clearance.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "employee_leave_clearance.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["employee_leave_clearance.utils.before_request"]
# after_request = ["employee_leave_clearance.utils.after_request"]

# Job Events
# ----------
# before_job = ["employee_leave_clearance.utils.before_job"]
# after_job = ["employee_leave_clearance.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"employee_leave_clearance.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }









doc_events = {
    "Leave Application": {
        "validate": [
            "employee_leave_clearance.employee_leave_clearance.doctype.employee_leave_clearance_a_001_doctype.employee_leave_clearance_a_001_doctype.set_nationality",
            "employee_leave_clearance.employee_leave_clearance.doctype.employee_leave_clearance_a_001_doctype.employee_leave_clearance_a_001_doctype.working_days_leave_application",
        ]
    },
    "Salary Slip": {
        # "on_submit":
        "validate": [
            # "employee_leave_clearance.employee_leave_clearance.doctype.employee_leave_clearance_a_001_doctype.employee_leave_clearance_a_001_doctype.get_latest_salary_slip",
            # "employee_leave_clearance.employee_leave_clearance.doctype.employee_leave_clearance_a_001_doctype.employee_leave_clearance_a_001_doctype.calculate_per_day_salary_components",
            "employee_leave_clearance.employee_leave_clearance.doctype.employee_leave_clearance_a_001_doctype.employee_leave_clearance_a_001_doctype.adding_per_salary_components",
        ]
    }
}


doctype_js = {
	"Salary Slip": "public/js/annual_leave_hrms_a_01.js",
	"Leave Application": "public/js/annual_leave_hrms_a_01.js"
}


fixtures = [ {"dt": "Custom Field","filters": [["module", "=", "Employee Leave Clearance"]] }]

