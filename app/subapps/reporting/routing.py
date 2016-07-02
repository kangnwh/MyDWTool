 # -*- coding: utf-8 -*-
from flask import Blueprint
from .common import render_html
from BI.Reports import render_report

reportRoute = Blueprint('reportRoute', __name__,
                     template_folder='templates', static_folder='static')


@reportRoute.route('/', methods=['GET', 'POST'])
def index():
    report = render_report('F:\\business\\MyECharts\\app\\subapps\\reporting\\templates\\report\\demo.xml',stock_code="000001")
    return render_html(report)