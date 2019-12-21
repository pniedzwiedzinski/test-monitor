# test-monitor

Managing the display - display the site from `current_page`

## Usage

On the display open browser in kiosk mode and open https://pniedzwiedzinski.github.io/test-monitor

To change displayed site modify the `current_page` file and after ~1 minute new site will show.

#### Why is it 1 minute?

- 30s - that's the process of generating and uploading new site to GitHub pages.
- every 30 seconds the frontend checks if it should update.
