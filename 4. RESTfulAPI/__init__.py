# Entry point for the application.
from .app import create_app
from .models import db

# Create the app
app = create_app()
