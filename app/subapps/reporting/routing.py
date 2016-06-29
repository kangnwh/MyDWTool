 # -*- coding: utf-8 -*-
from flask import Blueprint
from flask import render_template
from BI.Reports import render_report

reportRoute = Blueprint('reportRoute', __name__,
                     template_folder='templates', static_folder='static')


@reportRoute.route('/', methods=['GET', 'POST'])
def index():

    return render_template('report/index.html')