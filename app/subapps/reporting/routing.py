 # -*- coding: utf-8 -*-
from flask import Blueprint,request
from .common import render_html
from BI.Reports import render_report
import os
from flask_login import login_required

reportRoute = Blueprint('reportRoute', __name__,
                     template_folder='templates', static_folder='static')

REPORT_TEMPLATE_FOLDER = os.path.split(os.path.realpath(__file__))[0] + os.sep + "templates" +os.sep + "report"

@reportRoute.route('/<template>', methods=['GET', 'POST'])
@login_required
def index(template):
    if request.method == 'GET':
        template = template # request.args.get('template',"demo.xml")
    print(request.args)
    kwargs = (request.args)
    report = render_report(REPORT_TEMPLATE_FOLDER+os.sep+template,kwargs=kwargs)
    return render_html(report)