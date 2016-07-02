from flask import render_template,url_for
from ..config import report_base_template



def render_html(html):

    return render_template(report_base_template,report=html)