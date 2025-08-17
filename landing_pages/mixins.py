

class BootstrapFormMixin(object):

    fields=[]
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        print(self.fields)

        for field in self.fields:
            print(field)
            default_css_class= 'form-control'

            new_attrs={
                "class":default_css_class,
                "id":f"{field}",
                "placeholder":f"Your {field}"
            }

            if field == "email2":
                new_attrs["placeholder"]=f"Your confirm email"

            self.fields[field].widget.attrs.update(new_attrs)
