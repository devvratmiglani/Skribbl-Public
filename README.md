# Skribbl AutoJoin

## Overview

Skribbl AutoJoin is a Python package that connects to Skribbl.io, generates a game session, and automatically opens the game link in your browser while copying it to your clipboard.

## Installation

To install the package, use:
```
pip install git+https://github.com/devvratmiglani/Skribbl-Public.git 
```
or
```
git clone https://github.com/devvratmiglani/Skribbl-Public.git
cd Skribbl-Public
pip install .
```
### Requirements

- Python 3.7 or higher
- An active internet connection

## Usage

After installation, run the following command:
```
skribbl-public
```

or make a shortcut on desktop for instant launch:
```
skribbl-public --shortcut
```

to search public lobby with available capacity
```
skribbl-public --space_required 3
```
or 
```
skribbl-public -r 3
```

This will:
- Connect to Skribbl.io's public server
- Generate a unique public game session
- Copies the game link to your clipboard
- Open the game in your default browser
- Can search lobbies required capacity

If the browser does not open, you can manually paste the link from your clipboard.

## Troubleshooting

### WebSocket Connection Fails
- Ensure you have an active internet connection.
- Check if you are not already connected to skribbl.io

## Contributing

1. Fork the repository.
2. Create a new branch (`feature-xyz`).
3. Commit your changes.
4. Open a pull request.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE Version 3 License.

## Contact

For issues or feature requests, open a GitHub issue or reach out via:
  
GitHub: [devvratmiglani](https://github.com/devvratmiglani)
