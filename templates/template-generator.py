from colormath.color_conversions import convert_color
from colormath.color_objects import LCHabColor,sRGBColor
import sys

if len(sys.argv) < 2:
  print 'specify theme name'
  sys.exit()
else:
  theme_name = sys.argv[1]

def tohex(l,c,h):
  rgb = convert_color(LCHabColor(l,c,h),sRGBColor)
  clamp = sRGBColor(rgb.clamped_rgb_r, rgb.clamped_rgb_g, rgb.clamped_rgb_b)
  return clamp.get_rgb_hex()

def print_airline(name,bg):
  print 'auxfile autoload/airline/themes/%s_%s.vim' % (name, bg)
  print 'let g:airline#themes#%s_%s#palette = {}' % (name, bg)
  print ''
  print 'let s:gry0 = [ "@guigry0", @termgry0 ]'
  print 'let s:gry1 = [ "@guigry1", @termgry1 ]'
  print 'let s:gry2 = [ "@guigry2", @termgry2 ]'
  print 'let s:gry3 = [ "@guigry3", @termgry3 ]'
  print 'let s:red_ = [ "@guired_", @termred_ ]'
  print 'let s:gren = [ "@guigren", @termgren ]'
  print 'let s:blue = [ "@guiblue", @termblue ]'
  print ''
  print 'let s:nrm1 = [ s:gry0[0] , s:gry2[0] , s:gry0[1] , s:gry2[1] ]'
  print 'let s:nrm2 = [ s:gry3[0] , s:gry1[0] , s:gry3[1] , s:gry1[1] ]'
  print 'let s:insr = [ s:gry0[0] , s:gren[0] , s:gry0[1] , s:gren[1] ]'
  print 'let s:visl = [ s:gry0[0] , s:blue[0] , s:gry0[1] , s:blue[1] ]'
  print 'let s:rplc = [ s:gry0[0] , s:red_[0] , s:gry0[1] , s:red_[1] ]'
  print 'let s:inac = [ s:gry2[0] , s:gry1[0] , s:gry2[1] , s:gry1[1] ]'
  print ''
  print 'let g:airline#themes#%s_%s#palette.normal =' % (name, bg)
  print '  \ airline#themes#generate_color_map( s:nrm1 , s:nrm2 , s:nrm2 )'
  print ''
  print 'let g:airline#themes#%s_%s#palette.insert =' % (name, bg)
  print '  \ airline#themes#generate_color_map( s:insr , s:nrm2 , s:nrm2 )'
  print ''
  print 'let g:airline#themes#%s_%s#palette.visual =' % (name, bg)
  print '  \ airline#themes#generate_color_map( s:visl , s:nrm2 , s:nrm2 )'
  print ''
  print 'let g:airline#themes#%s_%s#palette.replace =' % (name, bg)
  print '  \ airline#themes#generate_color_map( s:rplc , s:nrm2 , s:nrm2 )'
  print ''
  print 'let g:airline#themes#%s_%s#palette.inactive =' % (name, bg)
  print '  \ airline#themes#generate_color_map( s:inac , s:inac , s:inac )'
  print ''
  print 'let g:airline#themes#%s_%s#palette.ctrlp =' % (name, bg)
  print '  \ airline#extensions#ctrlp#generate_color_map( s:nrm2 , s:nrm1 , s:nrm2 )'
  print 'endauxfile'

def print_lightline(name,bg):
  print 'auxfile autoload/lightline/colorscheme/%s_%s.vim' % (name, bg)
  print 'let s:gry0 = "@guigry0"'
  print 'let s:gry1 = "@guigry1"'
  print 'let s:gry2 = "@guigry2"'
  print 'let s:gry3 = "@guigry3"'
  print 'let s:gry4 = "@guigry4"'
  print 'let s:red_ = "@guired_"'
  print 'let s:yllw = "@guiyllw"'
  print 'let s:gren = "@guigren"'
  print 'let s:blue = "@guiblue"'
  print ''
  print 'let s:p = { "normal" : {} , "inactive": {} , "insert"  : {} ,'
  print '          \ "replace": {} , "visual"  : {} , "tabline" : {} }'
  print ''
  print 'let s:p.normal.left     = [[ s:gry0, s:gry2 ], [ s:gry3, s:gry1 ]]'
  print 'let s:p.normal.middle   = [[ s:gry3, s:gry1 ]]'
  print 'let s:p.normal.right    = [[ s:gry0, s:gry2 ], [ s:gry0, s:gry2 ]]'
  print ''
  print 'let s:p.inactive.left   = copy(s:p.normal.middle)'
  print 'let s:p.inactive.middle = copy(s:p.normal.middle)'
  print 'let s:p.inactive.right  = copy(s:p.normal.middle)'
  print ''
  print 'let s:p.insert.left     = [[ s:gry0, s:gren ]]'
  print 'let s:p.insert.right    = [[ s:gry0, s:gren ], [ s:gry0, s:gren ]]'
  print ''
  print 'let s:p.visual.left     = [[ s:gry0, s:blue ]]'
  print 'let s:p.visual.right    = [[ s:gry0, s:blue ], [ s:gry0, s:blue ]]'
  print ''
  print 'let s:p.replace.left    = [[ s:gry0, s:red_ ]]'
  print 'let s:p.replace.right   = [[ s:gry0, s:red_ ], [ s:gry0, s:red_ ]]'
  print ''
  print 'let s:p.tabline.left    = [[ s:gry0, s:gry2 ]]'
  print 'let s:p.tabline.tabsel  = copy(s:p.normal.middle)'
  print 'let s:p.tabline.right   = [[ s:gry0, s:gry2 ]]'
  print ''
  print 'let s:p.normal.error    = [[ s:red_, s:gry0 ]]'
  print 'let s:p.normal.warning  = [[ s:yllw, s:gry4 ]]'
  print ''
  print 'let g:lightline#colorscheme#%s_%s#palette =' % (name, bg)
  print '  \ lightline#colorscheme#fill(s:p)'
  print 'endauxfile'

###

hue_bas0 = 075.0
hue_bas1 = 285.0
hue_yllw = 090.0

hexgry0_lt = tohex( 12.00/12.0*100.0 , 01.50/12.0*100.0 , hue_bas0 )
hexgry1_lt = tohex( 11.00/12.0*100.0 , 01.25/12.0*100.0 , hue_bas0 )
hexgry2_lt = tohex( 05.50/12.0*100.0 , 01.50/12.0*100.0 , hue_bas1 )
hexgry3_lt = tohex( 04.00/12.0*100.0 , 01.50/12.0*100.0 , hue_bas1 )
hexyllw_lt = tohex( 08.50/12.0*100.0 , 08.00/12.0*100.0 , hue_yllw )

hexgry0_dk = tohex( 02.00/12.0*100.0 , 01.00/12.0*100.0 , hue_bas1 )
hexgry1_dk = tohex( 02.75/12.0*100.0 , 01.25/12.0*100.0 , hue_bas1 )
hexgry2_dk = tohex( 07.11/12.0*100.0 , 01.50/12.0*100.0 , hue_bas0 )
hexgry3_dk = tohex( 08.76/12.0*100.0 , 01.50/12.0*100.0 , hue_bas0 )
hexyllw_dk = tohex( 08.50/12.0*100.0 , 06.00/12.0*100.0 , hue_yllw )

cro_lt = 61.803
cro_dk = 23.607

if theme_name == 'stellarized':
  hexred__lt = tohex( 05.00/12.0*100.0 , cro_lt , 040.0 )
  hexgren_lt = tohex( 05.00/12.0*100.0 , cro_lt , 135.0 )
  hexblue_lt = tohex( 04.75/12.0*100.0 , cro_lt , 255.0 )
  hexred__dk = tohex( 07.25/12.0*100.0 , cro_dk , 040.3 )
  hexgren_dk = tohex( 07.25/12.0*100.0 , cro_dk , 135.0 )
  hexblue_dk = tohex( 07.25/12.0*100.0 , cro_dk , 255.0 )
else:
  print 'invalid theme name'
  sys.exit()

###

print '# general'
print 'Author:          nightsense'
print 'Maintainer:      nightsense'
print 'License:         MIT'

print 'Full name:       %s' % theme_name
print 'Short name:      %s' % theme_name

print 'Terminal Colors: 256'
print ''
print '# light'
print 'Background: light'
print 'Color:      gry0 %s ~' % hexgry0_lt
print 'Color:      gry1 %s ~' % hexgry1_lt
print 'Color:      gry2 %s ~' % hexgry2_lt
print 'Color:      gry3 %s ~' % hexgry3_lt
print 'Color:      gry4 %s ~' % hexgry1_dk
print 'Color:      yllw %s ~' % hexyllw_lt
print 'Color:      red_ %s ~' % hexred__lt
print 'Color:      gren %s ~' % hexgren_lt
print 'Color:      blue %s ~' % hexblue_lt
print 'Include:    _common.colortemplate'
print 'DiffChanged yllw gry4 reverse'
print 'DiffText    yllw gry4 reverse'
print 'MatchParen  yllw gry4 reverse'
print 'Search      yllw gry4 reverse'
print ''
print_airline(theme_name,'light')
print_lightline(theme_name,'light')

###

print ''
print '# dark'
print 'Background: dark'
print 'Color:      gry0 %s ~' % hexgry0_dk
print 'Color:      gry1 %s ~' % hexgry1_dk
print 'Color:      gry2 %s ~' % hexgry2_dk
print 'Color:      gry3 %s ~' % hexgry3_dk
print 'Color:      gry4 %s ~' % hexgry1_lt
print 'Color:      yllw %s ~' % hexyllw_dk
print 'Color:      red_ %s ~' % hexred__dk
print 'Color:      gren %s ~' % hexgren_dk
print 'Color:      blue %s ~' % hexblue_dk
print 'Include:    _common.colortemplate'
print 'DiffChanged yllw gry0 reverse'
print 'DiffText    yllw gry0 reverse'
print 'MatchParen  yllw gry0 reverse'
print 'Search      yllw gry0 reverse'
print ''
print_airline(theme_name,'dark')
print_lightline(theme_name,'dark')
