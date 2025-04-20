from .models import NavbarButtons

def base_template_variables(request):
    """
    Context processor to add a base template variable to the context.
    """
    navbar_buttons = NavbarButtons.objects.all()
    return {"navbar_buttons": navbar_buttons}
