# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe, json
from frappe.model.document import Document
from frappe import _
from frappe.desk.search import sanitize_searchfield
from frappe.utils import (flt, getdate, get_url, now,
nowtime, get_time, today, get_datetime, add_days)
from frappe.utils import add_to_date, now, nowdate

@frappe.whitelist()
def cancel_facility_transaction_on_je_cancel(doc, method=None):
	if doc.reference_doctype == "Facility Transaction":
		facility_transaction = frappe.get_doc('Facility Transaction', doc.reference_link)
		facility_transaction.cancel()

@frappe.whitelist()
def cancel_guarantee_transaction_on_je_cancel(doc, method=None):
	if doc.reference_doctype == "Guarantee Transaction":
		guarantee_transaction = frappe.get_doc('Guarantee Transaction', doc.reference_link)
		guarantee_transaction.cancel()
