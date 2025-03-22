# Chicago Crypto ATMs

A web application that helps users find cryptocurrency ATMs in Chicago neighborhoods.

## Features

- Browse ATMs by neighborhood
- Browse ATMs by cryptocurrency
- Search for ATMs by location or cryptocurrency
- View detailed information about each ATM

## Local Development

### Prerequisites

- Python 3.9+
- Required Python packages (install using `pip install -r requirements.txt`)

### Running Locally

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Generate the website:
   ```
   python process_data.py
   ```
4. Start the server:
   ```
   python server.py
   ```
5. Visit `http://localhost:8084` in your browser

## Deployment

### Deploying to Heroku

1. Create a Heroku account and install the Heroku CLI
2. Login to Heroku:
   ```
   heroku login
   ```
3. Create a new Heroku app:
   ```
   heroku create your-app-name
   ```
4. Push your code to Heroku:
   ```
   git push heroku main
   ```
5. Open your app:
   ```
   heroku open
   ```

### Deploying to Render

1. Create a Render account
2. Create a new Web Service
3. Connect your GitHub repository
4. Set the build command: `pip install -r requirements.txt`
5. Set the start command: `python process_data.py && python server.py`
6. Deploy

### Deploying to PythonAnywhere

1. Create a PythonAnywhere account
2. Upload your code or clone from GitHub
3. Set up a web app with manual configuration (Python)
4. Configure the WSGI file to run your application
5. Set up a virtual environment and install dependencies

## Project Structure

- `server.py`: Web server for serving the static site
- `process_data.py`: Script for generating HTML pages from data
- `templates/`: HTML templates for the website
- `static/`: Static assets (CSS, images, etc.)
- `output/`: Generated HTML files
- `data/`: Source data for ATMs

## License

MIT 