#MenuTitle: Generate HTML Glyph List
'''Generate HTML unsorted list(ul) with all unicode and exporting glyphs in current font'''

thisFont = Glyphs.font # frontmost font

def htmlEscapedGlyphs( thisFont ):
	allUnicodes = ["&#x%s;" % g.unicode for g in thisFont.glyphs if g.unicode and g.export ]
	return allUnicodes
	
def makeHtmlList( arr ):
	htmlList = '<ul> \n'
	for g in arr:
		htmlList += '  <li>\n    <span>'
		htmlList += g
		htmlList += '</span>\n  </li>\n'
	htmlList += '</ul>\n'
	return htmlList
	
htmlGlyphStrings = htmlEscapedGlyphs( thisFont )
htmlList = makeHtmlList( htmlGlyphStrings )
print( htmlList )