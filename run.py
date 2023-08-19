from dotenv import load_dotenv
 # load environment variables from .env file
load_dotenv()

from root import create_app



app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
