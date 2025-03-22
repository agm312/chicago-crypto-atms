# Deploying as a Static Website

Since this project generates static HTML files, you can deploy it to any static hosting service for a simpler and often cheaper solution.

## Steps to Deploy as a Static Site

1. Generate the static files locally:
   ```
   python process_data.py
   ```

2. The generated files will be in the `output` directory.

3. Choose a static hosting provider:

   ### GitHub Pages
   
   1. Create a GitHub repository
   2. Push your code to the repository
   3. Configure GitHub Pages to serve from the `output` directory
   4. Your site will be available at `https://yourusername.github.io/repository-name`

   ### Netlify
   
   1. Create a Netlify account
   2. Drag and drop the `output` directory to Netlify's upload area
   3. Your site will be deployed instantly with a Netlify subdomain
   4. You can configure a custom domain later

   ### Vercel
   
   1. Create a Vercel account
   2. Install Vercel CLI: `npm i -g vercel`
   3. Navigate to your project directory
   4. Run `vercel` and follow the prompts
   5. Configure the output directory as `output`

   ### AWS S3 + CloudFront
   
   1. Create an S3 bucket
   2. Upload the contents of the `output` directory to the bucket
   3. Configure the bucket for static website hosting
   4. (Optional) Set up CloudFront for CDN and HTTPS

## Handling Search Functionality

Since the search functionality requires server-side processing, you have a few options:

1. **Convert to client-side search**: Modify the search to use JavaScript to filter results on the client side.

2. **Use a serverless function**: Create a small API using AWS Lambda, Netlify Functions, or Vercel Serverless Functions to handle search requests.

3. **Use a search service**: Integrate a service like Algolia to provide search functionality.

## Example: Client-Side Search Implementation

To implement client-side search, you would need to:

1. Generate a JSON file with all ATM data during the build process
2. Load this JSON file with JavaScript
3. Implement search logic in JavaScript to filter results
4. Display the filtered results on the page

This approach would allow your site to remain fully static while still providing search functionality. 