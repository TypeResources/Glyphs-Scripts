#MenuTitle: Launch Glyph Gazer
''' Open text content of currently open tab with Glyph Gazer web tool'''
import urllib	
import webbrowser

# Variables
baseUrl = "https://typeresources.github.io/glyph-gazer/?q="


# Get text content of currently open tab in Glyphs
currentText = Glyphs.font.currentText

# Convert encoding to UTF-8
currentTextUTF8 = currentText.encode('UTF-8','strict')

# URL escape string
encodedTextQuery = urllib.quote(currentTextUTF8)

# Create full URL
url = baseUrl+encodedTextQuery

# Open URL in browser
webbrowser.open(url)
