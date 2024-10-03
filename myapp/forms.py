from django import forms


class MovieForm(forms.Form):

    title = forms.CharField()

    options=(
        ('Action','Action'),
        ('Thriller','Thriller'),
        ('Comedy','Comedy'),
        ('Survival_Drama','Survival Drama'),
        ('Fiction','Fiction')
    )

    genre = forms.ChoiceField(choices=options)

    language = forms.CharField()

    year = forms.CharField()

    run_time = forms.IntegerField()

    director = forms.CharField()

    def clean(self):

        cleaned_data=super().clean()

        year=cleaned_data.get("year")

        run_time=cleaned_data.get("run_time")
        
        if int(year)<1990:

            error_message="the year must be above 1990"

            self.add_error("year",error_message)


        if run_time<60 or run_time>210:

            error_mes="the run time should not exeeds 210 mins and need a min of 60 mins"

            self.add_error("run_time",error_mes)