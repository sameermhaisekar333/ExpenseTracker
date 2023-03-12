from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, DecimalField
from wtforms.validators import DataRequired, Length, NumberRange
from flask_wtf.file import FileField, FileRequired, FileAllowed


class EntryForm(FlaskForm):
    account = StringField("ACCOUNT",
                                validators=[
                                DataRequired(), 
                                Length(min=1, max=20, message='lfhl')]) 
    category = StringField("CATEGORY", 
                                validators=[
                                DataRequired(),
                                Length(min=1, max=20)])
    
    subcategory = StringField("SUBCATEGORY", 
                                 validators=[Length(max=20)])
    date = DateField("DATE", validators=[DataRequired()])
    amount = DecimalField("AMOUNT", 
                            validators=[
                            DataRequired(), 
                            NumberRange(min=0.1)])  
    submit = SubmitField("SUBMIT")  

class UploadFile(FlaskForm):
    file = FileField(
        "file",
        validators=[
            FileRequired(),
            FileAllowed(
                [
                    "csv",
                ],
                "only csv format!",
            ),
        ],
    )
    submit = SubmitField("UPLOAD") 