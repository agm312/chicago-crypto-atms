from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import json
from urllib.parse import urlparse, unquote, parse_qs
import pandas as pd
from jinja2 import Environment, FileSystemLoader

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

class DirectoryServer(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Don't set directory in __init__ to allow dynamic path selection
        super().__init__(*args, **kwargs)
    
    def translate_path(self, path):
        # Parse the URL path
        parsed_url = urlparse(path)
        clean_path = unquote(parsed_url.path)
        print(f"Translating path: {clean_path}")  # Debug log
        
        # Handle search queries
        if clean_path == '/search':
            query_params = parse_qs(parsed_url.query)
            search_query = query_params.get('q', [''])[0].lower()
            print(f"Search query: {search_query}")
            
            # Generate search results page
            return self.generate_search_results(search_query)
            
        # Check if this is a static file request
        if clean_path.startswith('/static/'):
            static_path = os.path.join(os.getcwd(), clean_path.lstrip('/'))
            print(f"Looking for static file at: {static_path}")  # Debug log
            if os.path.exists(static_path):
                return static_path
        
        # Check if this is an ATM detail page
        if clean_path.startswith('/atm/'):
            atm_id = clean_path.split('/')[2]
            atm_path = os.path.join(os.getcwd(), "output", "atm", f"{atm_id}.html")
            print(f"Looking for ATM page at: {atm_path}")
            return atm_path
        
        # Check if this is a neighborhood detail page
        if clean_path.startswith('/neighborhood/'):
            neighborhood_id = clean_path.split('/')[2]
            neighborhood_path = os.path.join(os.getcwd(), "output", "neighborhood", f"{neighborhood_id}.html")
            print(f"Looking for neighborhood page at: {neighborhood_path}")
            if os.path.exists(neighborhood_path):
                print(f"Found neighborhood page: {neighborhood_path}")
                return neighborhood_path
            else:
                print(f"Neighborhood page not found: {neighborhood_path}")
                print(f"Available neighborhood files: {os.listdir(os.path.join(os.getcwd(), 'output', 'neighborhood'))}")
                # Try to find a close match
                available_files = os.listdir(os.path.join(os.getcwd(), 'output', 'neighborhood'))
                for file in available_files:
                    if file.startswith(neighborhood_id) or neighborhood_id in file:
                        print(f"Found potential match: {file}")
                        return os.path.join(os.getcwd(), "output", "neighborhood", file)
            return neighborhood_path
            
        # Check if this is a cryptocurrency detail page
        if clean_path.startswith('/cryptocurrency/'):
            crypto_id = clean_path.split('/')[2]
            crypto_path = os.path.join(os.getcwd(), "output", "cryptocurrency", f"{crypto_id}.html")
            print(f"Looking for cryptocurrency page at: {crypto_path}")
            return crypto_path
        
        # Check if this is the neighborhoods page
        if clean_path == '/neighborhoods':
            neighborhoods_path = os.path.join(os.getcwd(), "output", "neighborhoods.html")
            print(f"Looking for neighborhoods page at: {neighborhoods_path}")
            return neighborhoods_path
        
        # Check if this is the cryptocurrencies page
        if clean_path == '/cryptocurrencies':
            cryptocurrencies_path = os.path.join(os.getcwd(), "output", "cryptocurrencies.html")
            print(f"Looking for cryptocurrencies page at: {cryptocurrencies_path}")
            return cryptocurrencies_path
        
        # For root path, serve index.html
        if clean_path == '/' or clean_path == '':
            index_path = os.path.join(os.getcwd(), "output", "index.html")
            print(f"Looking for index page at: {index_path}")
            return index_path
        
        # For all other paths, try output directory first
        output_path = os.path.join(os.getcwd(), "output", clean_path.lstrip('/'))
        if os.path.exists(output_path):
            print(f"Found in output directory: {output_path}")
            return output_path
        
        # If not found in output, try static directory
        static_path = os.path.join(os.getcwd(), "static", clean_path.lstrip('/'))
        if os.path.exists(static_path):
            print(f"Found in static directory: {static_path}")
            return static_path
        
        # If neither exists, let parent class handle it
        print(f"Path not found, letting parent class handle: {clean_path}")
        return super().translate_path(path)

    def do_GET(self):
        # Print request info for debugging
        print(f"\nRequested path: {self.path}")
        
        try:
            # Try to serve the file
            f = self.send_head()
            if f:
                try:
                    self.copyfile(f, self.wfile)
                finally:
                    f.close()
        except Exception as e:
            print(f"Error serving {self.path}: {e}")
            self.send_error(500, f"Internal server error: {e}")

    def generate_search_results(self, query):
        """Generate a search results page for the given query"""
        print(f"Generating search results page for query: {query}")
        
        # Check if the search query matches a cryptocurrency
        crypto_symbols = {
            'btc': 'btc', 'bitcoin': 'btc',
            'eth': 'eth', 'ethereum': 'eth',
            'usdt': 'usdt', 'tether': 'usdt',
            'usdc': 'usdc', 'usd coin': 'usdc',
            'xrp': 'xrp', 'ripple': 'xrp',
            'doge': 'doge', 'dogecoin': 'doge',
            'ltc': 'ltc', 'litecoin': 'ltc',
            'bch': 'bch', 'bitcoin cash': 'bch',
            'dai': 'dai',
            'shib': 'shib', 'shiba inu': 'shib'
        }
        
        # First check for exact matches
        if query in crypto_symbols:
            symbol = crypto_symbols[query]
            crypto_path = os.path.join(os.getcwd(), "output", "cryptocurrency", f"{symbol}.html")
            print(f"Search exact match cryptocurrency: {symbol}, redirecting to {crypto_path}")
            if os.path.exists(crypto_path):
                print(f"Found cryptocurrency page: {crypto_path}")
                return crypto_path
        
        # Then check for partial matches
        for key, symbol in crypto_symbols.items():
            if key in query:
                # Redirect to the cryptocurrency page
                crypto_path = os.path.join(os.getcwd(), "output", "cryptocurrency", f"{symbol}.html")
                print(f"Search matched cryptocurrency: {symbol}, redirecting to {crypto_path}")
                if os.path.exists(crypto_path):
                    print(f"Found cryptocurrency page: {crypto_path}")
                    return crypto_path
        
        # If no cryptocurrency match, check for neighborhood matches
        neighborhoods = {
            'loop': 'loop', 'the loop': 'loop',
            'river north': 'river-north', 'river-north': 'river-north',
            'lincoln park': 'lincoln-park', 'lincoln-park': 'lincoln-park',
            'wicker park': 'wicker-park', 'wicker-park': 'wicker-park',
            'logan square': 'logan-square', 'logan-square': 'logan-square',
            'west loop': 'west-loop', 'west-loop': 'west-loop',
            'south loop': 'south-loop', 'south-loop': 'south-loop',
            'gold coast': 'gold-coast', 'gold-coast': 'gold-coast',
            'lakeview': 'lakeview',
            'uptown': 'uptown'
        }
        
        for key, neighborhood_id in neighborhoods.items():
            if key in query:
                # Redirect to the neighborhood page
                neighborhood_path = os.path.join(os.getcwd(), "output", "neighborhood", f"{neighborhood_id}.html")
                print(f"Search matched neighborhood: {neighborhood_id}, redirecting to {neighborhood_path}")
                if os.path.exists(neighborhood_path):
                    print(f"Found neighborhood page: {neighborhood_path}")
                    return neighborhood_path
        
        # If no direct matches, generate a search results page
        print(f"No direct matches found for query: {query}, generating search results page")
        
        # Create a temporary file for the search results
        search_results_dir = os.path.join(os.getcwd(), "output", "search")
        os.makedirs(search_results_dir, exist_ok=True)
        
        search_results_path = os.path.join(search_results_dir, "results.html")
        
        # Load the search results template
        template = env.get_template('search_results.html')
        
        # Render the template with the search query
        html = template.render(query=query, results=[])
        
        # Write the rendered HTML to the file
        with open(search_results_path, 'w') as f:
            f.write(html)
        
        print(f"Generated search results page at: {search_results_path}")
        return search_results_path

def run_server(port=None):
    if port is None:
        # Use environment variable PORT if available (for cloud platforms like Heroku)
        port = int(os.environ.get('PORT', 8084))
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, DirectoryServer)
    print(f"Server running at http://localhost:{port}/")
    print(f"Static files served from: {os.path.join(os.getcwd(), 'static')}")
    print(f"Output files served from: {os.path.join(os.getcwd(), 'output')}")
    httpd.serve_forever()

if __name__ == "__main__":
    # First generate the site
    import process_data
    process_data.main()
    
    # Then start the server
    try:
        run_server()
    except OSError as e:
        print(f"Error: {e}")
        print("Try using a different port by modifying the port number in server.py") 