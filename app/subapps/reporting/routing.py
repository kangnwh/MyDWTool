 # -*- coding: utf-8 -*-
from flask import Blueprint
from .common import render_html
from BI.Reports import render_report
import os

reportRoute = Blueprint('reportRoute', __name__,
                     template_folder='templates', static_folder='static')

REPORT_TEMPLATE_FOLDER = os.path.split(os.path.realpath(__file__))[0] + os.sep + "templates" +os.sep + "report"

@reportRoute.route('/', methods=['GET', 'POST'])
def index():
    report = render_report(REPORT_TEMPLATE_FOLDER+os.sep+'demo.xml',stock_code="000001")
    return render_html(report)