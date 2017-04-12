from flask import Flask, render_template, request, flash
from wtforms import Form, FloatField, BooleanField, SelectField, TextField, RadioField, validators


app = Flask(__name__)
app.secret_key = 'some_secret'


class InputForm(Form):
    name_field = TextField([validators.InputRequired()])
    year_field = FloatField(validators=[validators.InputRequired()])
    select_field = SelectField(choices=[('Fall','Fall'),('Spring','Spring')], validators=[validators.InputRequired()])
    boolean_field = BooleanField()

@app.route('/', methods=['GET', 'POST'])
def index():
    result_str = None
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        float_val = form.year_field.data
        select_val = form.select_field.data
        text_val = form.name_field.data
        boolean_val = form.boolean_field.data
        result_str = display(float_val, select_val, boolean_val, text_val)

    return render_template("index.html", template_form=form, result=result_str)

def display(f,s,b,t):
    view_str = "Text:{}, Float:{:.0f}, Select:{}, Boolean:{},".format(t,f,s,b)
    return view_str

if __name__ == '__main__':
    app.run(port=3456)