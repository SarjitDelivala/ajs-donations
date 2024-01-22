from app import create_app
from dotenv import load_dotenv
import os

load_dotenv()

# Create the Flask app using the factory function
app = create_app(os.getenv('CONFIG'))  # Change to 'development' for local development

if __name__ == '__main__':
    app.run()