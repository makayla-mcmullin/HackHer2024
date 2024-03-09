from flask import redirect, render_template, request, session

from SageLink import app
from SageLink.models import *


@app.route('/')
# @authenticate
def home(ElderUser):

    
    return render_template('index.html', ElderUser=ElderUser,)


