
class CustomClassMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Iterate through all fields and set attributes for their widgets
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                # Add more attributes if needed
            })
            