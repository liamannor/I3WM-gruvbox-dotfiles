#config.source('nord-qutebrowser.py')
nord = {
'nord0': '#282828',
  'nord1': '#2d2b2a',
    'nord2': '#32302f',
    'nord3': '#464443',
      # Snow Storm
    'nord4': '#d4be98',
    'nord5': '#dccbac',
    'nord6': '#e9debc',
    # Frost
    'nord7': '#8fbcbb',
    'nord8': '#88c0d0',
    'nord9': '#81a1c1',
    'nord10': '#5e81ac',
    # Aurora
    'nord11': '#ea6962',
    'nord12': '#e78a4e',
    'nord13': '#a9b665',
    'nord14': '#89b428',
    'nord15': '#d3869b',
   
}
config.load_autoconfig(False)
#darkmode
#config.set("colors.webpage.darkmode.enabled", True)
## When to show the statusbar.
## Type: String
## Valid values:
##   - always: Always show the statusbar.
##   - never: Always hide the statusbar.
##   - in-mode: Show the statusbar when in modes other than normal mode.
# the '#' character is a comment in python, as you may know
c.statusbar.show = 'never'
#c.url.default_page '/home/liam/Documents/qtpage/startpage.html'
c.url.default_page = 'file:///home/liam/sp/index.html'
c.url.start_pages ='file:///home/liam/sp/index.html'
## Background color of the completion widget category headers.
## Type: QssColor
c.colors.completion.category.bg = nord['nord0']

## Bottom border color of the completion widget category headers.
## Type: QssColor
c.colors.completion.category.border.bottom = nord['nord0']

## Top border color of the completion widget category headers.
## Type: QssColor
c.colors.completion.category.border.top = nord['nord0']

## Foreground color of completion widget category headers.
## Type: QtColor
c.colors.completion.category.fg = nord['nord5']

## Background color of the completion widget for even rows.
## Type: QssColor
c.colors.completion.even.bg = nord['nord1']

## Background color of the completion widget for odd rows.
## Type: QssColor
c.colors.completion.odd.bg = nord['nord1']

## Text color of the completion widget.
## Type: QtColor
c.colors.completion.fg = nord['nord4']

## Background color of the selected completion item.
## Type: QssColor
c.colors.completion.item.selected.bg = nord['nord3']

## Bottom border color of the selected completion item.
## Type: QssColor
c.colors.completion.item.selected.border.bottom = nord['nord3']

## Top border color of the completion widget category headers.
## Type: QssColor
c.colors.completion.item.selected.border.top = nord['nord3']

## Foreground color of the selected completion item.
## Type: QtColor
c.colors.completion.item.selected.fg = nord['nord6']

## Foreground color of the matched text in the completion.
## Type: QssColor
c.colors.completion.match.fg = nord['nord13']

## Color of the scrollbar in completion view
## Type: QssColor
c.colors.completion.scrollbar.bg = nord['nord1']

## Color of the scrollbar handle in completion view.
## Type: QssColor
c.colors.completion.scrollbar.fg = nord['nord5']

## Background color for the download bar.
## Type: QssColor
c.colors.downloads.bar.bg = nord['nord0']

## Background color for downloads with errors.
## Type: QtColor
c.colors.downloads.error.bg = nord['nord11']

## Foreground color for downloads with errors.
## Type: QtColor
c.colors.downloads.error.fg = nord['nord5']

## Color gradient stop for download backgrounds.
## Type: QtColor
c.colors.downloads.stop.bg = nord['nord15']

## Color gradient interpolation system for download backgrounds.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
c.colors.downloads.system.bg = 'none'

## Background color for hints. Note that you can use a `rgba(...)` value
## for transparency.
## Type: QssColor
c.colors.hints.bg = nord['nord13']

## Font color for hints.
## Type: QssColor
c.colors.hints.fg = nord['nord0']

## Font color for the matched part of hints.
## Type: QssColor
c.colors.hints.match.fg = nord['nord10']

## Background color of the keyhint widget.
## Type: QssColor
c.colors.keyhint.bg = nord['nord1']

## Text color for the keyhint widget.
## Type: QssColor
c.colors.keyhint.fg = nord['nord5']

## Highlight color for keys to complete the current keychain.
## Type: QssColor
c.colors.keyhint.suffix.fg = nord['nord13']

## Background color of an error message.
## Type: QssColor
c.colors.messages.error.bg = nord['nord11']

## Border color of an error message.
## Type: QssColor
c.colors.messages.error.border = nord['nord11']

## Foreground color of an error message.
## Type: QssColor
c.colors.messages.error.fg = nord['nord5']

## Background color of an info message.
## Type: QssColor
c.colors.messages.info.bg = nord['nord8']

## Border color of an info message.
## Type: QssColor
c.colors.messages.info.border = nord['nord8']

## Foreground color an info message.
## Type: QssColor
c.colors.messages.info.fg = nord['nord5']

## Background color of a warning message.
## Type: QssColor
c.colors.messages.warning.bg = nord['nord12']

## Border color of a warning message.
## Type: QssColor
c.colors.messages.warning.border = nord['nord12']

## Foreground color a warning message.
## Type: QssColor
c.colors.messages.warning.fg = nord['nord5']

## Background color for prompts.
## Type: QssColor
c.colors.prompts.bg = nord['nord2']

# ## Border used around UI elements in prompts.
# ## Type: String
c.colors.prompts.border = '1px solid ' + nord['nord0']

## Foreground color for prompts.
## Type: QssColor
c.colors.prompts.fg = nord['nord5']

## Background color for the selected item in filename prompts.
## Type: QssColor
c.colors.prompts.selected.bg = nord['nord3']

## Background color of the statusbar in caret mode.
## Type: QssColor
c.colors.statusbar.caret.bg = nord['nord15']

## Foreground color of the statusbar in caret mode.
## Type: QssColor
c.colors.statusbar.caret.fg = nord['nord5']

## Background color of the statusbar in caret mode with a selection.
## Type: QssColor
c.colors.statusbar.caret.selection.bg = nord['nord15']

## Foreground color of the statusbar in caret mode with a selection.
## Type: QssColor
c.colors.statusbar.caret.selection.fg = nord['nord5']

## Background color of the statusbar in command mode.
## Type: QssColor
c.colors.statusbar.command.bg = nord['nord2']

## Foreground color of the statusbar in command mode.
## Type: QssColor
c.colors.statusbar.command.fg = nord['nord5']

## Background color of the statusbar in private browsing + command mode.
## Type: QssColor
c.colors.statusbar.command.private.bg = nord['nord2']

## Foreground color of the statusbar in private browsing + command mode.
## Type: QssColor
c.colors.statusbar.command.private.fg = nord['nord5']

## Background color of the statusbar in insert mode.
## Type: QssColor
c.colors.statusbar.insert.bg = nord['nord14']

## Foreground color of the statusbar in insert mode.
## Type: QssColor
c.colors.statusbar.insert.fg = nord['nord1']

## Background color of the statusbar.
## Type: QssColor
c.colors.statusbar.normal.bg = nord['nord0']

## Foreground color of the statusbar.
## Type: QssColor
c.colors.statusbar.normal.fg = nord['nord5']

## Background color of the statusbar in passthrough mode.
## Type: QssColor
c.colors.statusbar.passthrough.bg = nord['nord10']

## Foreground color of the statusbar in passthrough mode.
## Type: QssColor
c.colors.statusbar.passthrough.fg = nord['nord5']

## Background color of the statusbar in private browsing mode.
## Type: QssColor
c.colors.statusbar.private.bg = nord['nord3']

## Foreground color of the statusbar in private browsing mode.
## Type: QssColor
c.colors.statusbar.private.fg = nord['nord5']

## Background color of the progress bar.
## Type: QssColor
c.colors.statusbar.progress.bg = nord['nord5']

## Foreground color of the URL in the statusbar on error.
## Type: QssColor
c.colors.statusbar.url.error.fg = nord['nord11']

## Default foreground color of the URL in the statusbar.
## Type: QssColor
c.colors.statusbar.url.fg = nord['nord5']

## Foreground color of the URL in the statusbar for hovered links.
## Type: QssColor
c.colors.statusbar.url.hover.fg = nord['nord8']

## Foreground color of the URL in the statusbar on successful load
## (http).
## Type: QssColor
c.colors.statusbar.url.success.http.fg = nord['nord5']

## Foreground color of the URL in the statusbar on successful load
## (https).
## Type: QssColor
c.colors.statusbar.url.success.https.fg = nord['nord14']

## Foreground color of the URL in the statusbar when there's a warning.
## Type: QssColor
c.colors.statusbar.url.warn.fg = nord['nord12']

## Background color of the tab bar.
## Type: QtColor
c.colors.tabs.bar.bg = nord['nord3']

## Background color of unselected even tabs.
## Type: QtColor
c.colors.tabs.even.bg = nord['nord3']

## Foreground color of unselected even tabs.
## Type: QtColor
c.colors.tabs.even.fg = nord['nord5']

## Color for the tab indicator on errors.
## Type: QtColor
c.colors.tabs.indicator.error = nord['nord11']

## Color gradient start for the tab indicator.
## Type: QtColor
# c.colors.tabs.indicator.start = nord['violet']

## Color gradient end for the tab indicator.
## Type: QtColor
# c.colors.tabs.indicator.stop = nord['orange']

## Color gradient interpolation system for the tab indicator.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
c.colors.tabs.indicator.system = 'none'

## Background color of unselected odd tabs.
## Type: QtColor
c.colors.tabs.odd.bg = nord['nord3']

## Foreground color of unselected odd tabs.
## Type: QtColor
c.colors.tabs.odd.fg = nord['nord5']

# ## Background color of selected even tabs.
# ## Type: QtColor
c.colors.tabs.selected.even.bg = nord['nord0']

# ## Foreground color of selected even tabs.
# ## Type: QtColor
c.colors.tabs.selected.even.fg = nord['nord5']

# ## Background color of selected odd tabs.
# ## Type: QtColor
c.colors.tabs.selected.odd.bg = nord['nord0']

# ## Foreground color of selected odd tabs.
# ## Type: QtColor
c.colors.tabs.selected.odd.fg = nord['nord5']

## Background color for webpages if unset (or empty to use the theme's
## color)
## Type: QtColor
# c.colors.webpage.bg = 'white'
## Font used in the completion categories.
## Type: Font
c.fonts.completion.category = 'bold default_size default_family'

## Font used in the completion widget.
## Type: Font
c.fonts.completion.entry = 'default_size default_family'

## Font used for the context menu. If set to null, the Qt default is
## used.
## Type: Font
c.fonts.contextmenu = None

## Font used for the debugging console.
## Type: Font
c.fonts.debug_console = 'default_size default_family'

## Default font families to use. Whenever "default_family" is used in a
## font setting, it's replaced with the fonts listed here. If set to an
## empty value, a system-specific monospace default is used.
## Type: List of Font, or Font
c.fonts.default_family = ['NovaMono']

## Default font size to use. Whenever "default_size" is used in a font
## setting, it's replaced with the size listed here. Valid values are
## either a float value with a "pt" suffix, or an integer value with a
## "px" suffix.
## Type: String
c.fonts.default_size = '10pt'

## Font used for the downloadbar.
## Type: Font
c.fonts.downloads = 'default_size default_family'

## Font used for the hints.
## Type: Font
c.fonts.hints = 'bold default_size default_family'

## Font used in the keyhint widget.
## Type: Font
c.fonts.keyhint = 'default_size default_family'

## Font used for error messages.
## Type: Font
c.fonts.messages.error = 'default_size default_family'

## Font used for info messages.
## Type: Font
c.fonts.messages.info = 'default_size default_family'

## Font used for warning messages.
## Type: Font
c.fonts.messages.warning = 'default_size default_family'

## Font used for prompts.
## Type: Font
c.fonts.prompts = 'default_size sans-serif'

## Font used in the statusbar.
## Type: Font
c.fonts.statusbar = 'default_size default_family'

## Font used for selected tabs.
## Type: Font
c.fonts.tabs.selected = 'default_size default_family'

## Font used for unselected tabs.
## Type: Font
c.fonts.tabs.unselected = 'default_size default_family'

## Font family for cursive fonts.
## Type: FontFamily
c.fonts.web.family.cursive = ''

## Font family for fantasy fonts.
## Type: FontFamily
c.fonts.web.family.fantasy = ''

## Font family for fixed fonts.
## Type: FontFamily
c.fonts.web.family.fixed = 'NovaMono'

## Font family for sans-serif fonts.
## Type: FontFamily
c.fonts.web.family.sans_serif = 'NovaMono'

## Font family for serif fonts.
## Type: FontFamily
c.fonts.web.family.serif = 'NovaMono'

## Font family for standard fonts.
## Type: FontFamily
c.fonts.web.family.standard = 'NovaMono'

## Default font size (in pixels) for regular text.
## Type: Int
c.fonts.web.size.default = 16

## Default font size (in pixels) for fixed-pitch text.
## Type: Int
c.fonts.web.size.default_fixed = 13

## Hard minimum font size (in pixels).
## Type: Int
c.fonts.web.size.minimum = 0

## Minimum logical font size (in pixels) that is applied when zooming
## out.
## Type: Int
c.fonts.web.size.minimum_logical = 6


