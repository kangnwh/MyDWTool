from flask import Blueprint, request, redirect, url_for,flash
from flask import render_template
echartsRoute = Blueprint('echartsRoute', __name__,
                     template_folder='echarts_template', static_folder='echarts_static')


@echartsRoute.route('/', methods=['GET', 'POST'])
def index():
    return 'ECharts Page'