import cv2 as cv
import matplotlib.pyplot as plt
import random
import numpy as np

COLOR_MAPS = [cv.COLORMAP_AUTUMN, cv.COLORMAP_BONE, cv.COLORMAP_JET,cv.COLORMAP_WINTER, cv.COLORMAP_RAINBOW,
cv.COLORMAP_OCEAN, cv.COLORMAP_SUMMER, cv.COLORMAP_SPRING, cv.COLORMAP_COOL, cv.COLORMAP_HSV, cv.COLORMAP_PINK,
cv.COLORMAP_HOT, cv.COLORMAP_PARULA, cv.COLORMAP_MAGMA, cv.COLORMAP_INFERNO, cv.COLORMAP_PLASMA,
cv.COLORMAP_VIRIDIS, cv.COLORMAP_CIVIDIS, cv.COLORMAP_TWILIGHT, cv.COLORMAP_TWILIGHT_SHIFTED,
cv.COLORMAP_TURBO, cv.COLORMAP_DEEPGREEN]

COLORS = [
('grey99',252,252,252),
('LemonChiffon',205,250,255),
('honeydew3',193,205,193),
('yellow4',0,139,139),
('sandy brown',96,164,244),
('aquamarine3',170,205,102),
('DarkBlue',139,0,0),
('grey76',194,194,194),
('light grey',211,211,211),
('DarkKhaki',107,183,189),
('gray91',232,232,232),
('old lace',230,245,253),
('orchid',214,112,218),
('grey25',64,64,64),
('firebrick',34,34,178),
('grey48',122,122,122),
('VioletRed3',120,50,205),
('SlateGray3',205,182,159),
('sky blue',235,206,135),
('gray19',48,48,48),
('gold1',0,215,255),
('gray43',110,110,110),
('grey61',156,156,156),
('SpringGreen',127,255,0),
('grey41',105,105,105),
('grey57',145,145,145),
('white',255,255,255),
('DarkOrange1',0,127,255),
('red3',0,0,205),
('grey72',184,184,184),
('dark salmon',122,150,233),
('gray83',212,212,212),
('LightBlue2',238,223,178),
('DodgerBlue3',205,116,24),
('dark orange',0,140,255),
('snow4',137,137,139),
('grey85',217,217,217),
('grey46',117,117,117),
('light blue',230,216,173),
('LightGoldenrodYellow',210,250,250),
('DeepPink4',80,10,139),
('dark grey',169,169,169),
('LightSkyBlue3',205,182,141),
('LightSkyBlue2',238,211,164),
('SpringGreen3',102,205,0),
('honeydew',240,255,240),
('lime green',50,205,50),
('CadetBlue2',238,229,142),
('SeaGreen',87,139,46),
('bisque4',107,125,139),
('grey22',56,56,56),
('burlywood4',85,115,139),
('orange red',0,69,255),
('PeachPuff',185,218,255),
('SlateGrey',144,128,112),
('FloralWhite',240,250,255),
('RosyBrown',143,143,188),
('gray8',20,20,20),
('LightSteelBlue1',255,225,202),
('sienna',45,82,160),
('salmon',114,128,250),
('medium orchid',211,85,186),
('grey56',143,143,143),
('hot pink',180,105,255),
('LightYellow4',122,139,139),
('light yellow',224,255,255),
('grey33',84,84,84),
('SlateGray2',238,211,185),
('navy blue',128,0,0),
('RoyalBlue',225,105,65),
('grey86',219,219,219),
('LawnGreen',0,252,124),
('LightCyan',255,255,224),
('brown4',35,35,139),
('DarkViolet',211,0,148),
('lavender',250,230,230),
('grey77',196,196,196),
('grey20',51,51,51),
('SteelBlue',180,130,70),
('seashell3',191,197,205),
('gray1',3,3,3),
('MediumPurple4',139,71,93),
('grey93',237,237,237),
('turquoise',208,224,64),
('LightPink2',173,162,238),
('IndianRed4',58,58,139),
('SaddleBrown',19,69,139),
('linen',230,240,250),
('rosy brown',143,143,188),
('red2',0,0,238),
('alice blue',255,248,240),
('gray45',115,115,115),
('goldenrod3',29,155,205),
('gray56',143,143,143),
('red',0,0,255),
('blue',255,0,0),
('red4',0,0,139),
('MediumOrchid3',205,82,180),
('LightSkyBlue4',139,123,96),
('grey87',222,222,222),
('gray15',38,38,38),
('DarkGoldenrod',11,134,184),
('LightSlateGrey',153,136,119),
('RosyBrown3',155,155,205),
('honeydew1',240,255,240),
('wheat4',102,126,139),
('plum2',238,174,238),
('blue4',139,0,0),
('PaleGreen1',154,255,154),
('grey37',94,94,94),
('DarkSlateGray1',255,255,151),
('gray65',166,166,166),
('LightSlateBlue',255,112,132),
('pink2',184,169,238),
('DarkGray',169,169,169),
('MediumSeaGreen',113,179,60),
('HotPink3',144,96,205),
('DarkSlateGray3',205,205,121),
('gray51',130,130,130),
('burlywood1',155,211,255),
('AntiqueWhite4',120,131,139),
('orchid1',250,131,255),
('grey4',10,10,10),
('OliveDrab2',58,238,179),
('DarkSeaGreen',143,188,143),
('light sky blue',250,206,135),
('honeydew2',224,238,224),
('chartreuse3',0,205,102),
('DarkSeaGreen4',105,139,105),
('pink',203,192,255),
('maroon1',179,52,255),
('DarkGreen',0,100,0),
('dark slate grey',79,79,47),
('ivory1',240,255,255),
('orange',0,165,255),
('salmon1',105,140,255),
('magenta3',205,0,205),
('sea green',87,139,46),
('tan1',79,165,255),
('light steel blue',222,196,176),
('orange2',0,154,238),
('grey40',102,102,102),
('grey52',133,133,133),
('gray9',23,23,23),
('gray24',61,61,61),
('LightPink3',149,140,205),
('firebrick4',26,26,139),
('deep sky blue',255,191,0),
('HotPink2',167,106,238),
('gray40',102,102,102),
('dim gray',105,105,105),
('light slate gray',153,136,119),
('DeepSkyBlue3',205,154,0),
('gray63',161,161,161),
('NavajoWhite3',139,179,205),
('LightSteelBlue2',238,210,188),
('gray66',168,168,168),
('tan2',73,154,238),
('PeachPuff3',149,175,205),
('LavenderBlush1',245,240,255),
('gray17',43,43,43),
('light green',144,238,144),
('magenta2',238,0,238),
('tan4',43,90,139),
('grey58',148,148,148),
('MediumOrchid',211,85,186),
('thistle3',205,181,205),
('gray10',26,26,26),
('LavenderBlush2',229,224,238),
('gray86',219,219,219),
('OliveDrab3',50,205,154),
('LightSalmon3',98,129,205),
('RoyalBlue1',255,118,72),
('light slate blue',255,112,132),
('aquamarine1',212,255,127),
('MediumSpringGreen',154,250,0),
('sienna2',66,121,238),
('light gray',211,211,211),
('blue2',238,0,0),
('thistle4',139,123,139),
('chocolate2',33,118,238),
('blue violet',226,43,138),
('MediumTurquoise',204,209,72),
('blanched almond',205,235,255),
('DarkOrchid',204,50,153),
('medium blue',205,0,0),
('MediumOrchid2',238,95,209),
('gray25',64,64,64),
('SlateBlue',205,90,106),
('coral',80,127,255),
('coral4',47,62,139),
('grey32',82,82,82),
('grey17',43,43,43),
('LightPink',193,182,255),
('purple4',139,26,85),
('OrangeRed',0,69,255),
('grey13',33,33,33),
('plum',221,160,221),
('SlateBlue4',139,60,71),
('plum4',139,102,139),
('gray95',242,242,242),
('pink4',108,99,139),
('purple3',205,38,125),
('grey50',127,127,127),
('PaleTurquoise4',139,139,102),
('PaleTurquoise',238,238,175),
('LightGoldenrod3',112,190,205),
('brown3',51,51,205),
('DarkOrange4',0,69,139),
('gray30',77,77,77),
('IndianRed1',106,106,255),
('dark sea green',143,188,143),
('DodgerBlue4',139,78,16),
('thistle',216,191,216),
('LightGoldenrod1',139,236,255),
('PaleTurquoise3',205,205,150),
('gray59',150,150,150),
('gray4',10,10,10),
('PeachPuff2',173,203,238),
('PaleGreen3',124,205,124),
('DarkSlateGray4',139,139,82),
('navy',128,0,0),
('cornsilk4',120,136,139),
('grey7',18,18,18),
('yellow1',0,255,255),
('gray29',74,74,74),
('cyan2',238,238,0),
('gray14',36,36,36),
('khaki1',143,246,255),
('silver',192,192,192),
('MediumSlateBlue',238,104,123),
('gray11',28,28,28),
('green3',0,205,0),
('DodgerBlue2',238,134,28),
('grey45',115,115,115),
('LemonChiffon1',205,250,255),
('DarkOrange',0,140,255),
('gray54',138,138,138),
('crymson',60,20,220),
('coral2',80,106,238),
('DarkOrchid4',139,34,104),
('forest green',34,139,34),
('yellow',0,255,255),
('SkyBlue4',139,112,74),
('purple2',238,44,145),
('PapayaWhip',213,239,255),
('LightCoral',128,128,240),
('gold4',0,117,139),
('snow',250,250,255),
('gray44',112,112,112),
('orchid4',137,71,139),
('gray78',199,199,199),
('firebrick1',48,48,255),
('DarkSeaGreen1',193,255,193),
('tan',140,180,210),
('cyan4',139,139,0),
('DarkGoldenrod2',14,173,238),
('chocolate',30,105,210),
('medium slate blue',238,104,123),
('green yellow',47,255,173),
('pale goldenrod',170,232,238),
('gray84',214,214,214),
('dark olive green',47,107,85),
('powder blue',230,224,176),
('tomato',71,99,255),
('violet red',144,32,208),
('gray42',107,107,107),
('OliveDrab1',62,255,192),
('grey94',240,240,240),
('slate grey',144,128,112),
('chartreuse1',0,255,127),
('cornsilk1',220,248,255),
('MediumBlue',205,0,0),
('sienna3',57,104,205),
('LavenderBlush3',197,193,205),
('light cyan',255,255,224),
('yellow3',0,205,205),
('maroon3',144,41,205),
('RosyBrown2',180,180,238),
('PaleTurquoise2',238,238,174),
('grey97',247,247,247),
('gray36',92,92,92),
('LightSalmon4',66,87,139),
('deep pink',147,20,255),
('cadet blue',160,158,95),
('DeepSkyBlue1',255,191,0),
('DimGrey',105,105,105),
('OldLace',230,245,253),
('gray18',46,46,46),
('maroon2',167,48,238),
('antique white',215,235,250),
('VioletRed1',150,62,255),
('grey0',0,0,0),
('grey16',41,41,41),
('LavenderBlush',245,240,255),
('gray68',173,173,173),
('grey43',110,110,110),
('PaleTurquoise1',255,255,187),
('grey1',3,3,3),
('gray64',163,163,163),
('tomato4',38,54,139),
('SlateBlue2',238,103,122),
('maroon',0,0,128),
('grey55',140,140,140),
('DarkOrange3',0,102,205),
('grey98',250,250,250),
('fuchsia',255,0,255),
('DarkOrange2',0,118,238),
('violet',238,130,238),
('DarkGoldenrod4',8,101,139),
('grey81',207,207,207),
('LightGreen',144,238,144),
('grey84',214,214,214),
('grey71',181,181,181),
('OliveDrab4',34,139,105),
('PaleVioletRed3',127,104,205),
('gray47',120,120,120),
('beige',220,245,245),
('MistyRose2',210,213,238),
('gray34',87,87,87),
('gray5',13,13,13),
('yellow2',0,238,238),
('HotPink1',180,110,255),
('chartreuse4',0,139,69),
('gray92',235,235,235),
('slate gray',144,128,112),
('grey19',48,48,48),
('RoyalBlue3',205,95,58),
('MistyRose3',181,183,205),
('grey3',8,8,8),
('cornflower blue',237,149,100),
('gray85',217,217,217),
('wheat2',174,216,238),
('gray49',125,125,125),
('wheat1',186,231,255),
('medium purple',219,112,147),
('red1',0,0,255),
('tan3',63,133,205),
('indian red',92,92,205),
('grey88',224,224,224),
('indigo',130,0,75),
('SeaGreen4',87,139,46),
('light sea green',170,178,32),
('grey78',199,199,199),
('thistle2',238,210,238),
('peach puff',185,218,255),
('plum3',205,150,205),
('goldenrod1',37,193,255),
('NavajoWhite',173,222,255),
('gray48',122,122,122),
('CadetBlue',160,158,95),
('gray33',84,84,84),
('gray75',191,191,191),
('gray90',229,229,229),
('gray77',196,196,196),
('DarkSlateGrey',79,79,47),
('DarkSlateGray',79,79,47),
('grey51',130,130,130),
('DarkOrchid1',255,62,191),
('BlanchedAlmond',205,235,255),
('grey47',120,120,120),
('olive',0,128,128),
('ivory4',131,139,139),
('chocolate1',36,127,255),
('DarkOliveGreen3',90,205,162),
('ForestGreen',34,139,34),
('NavyBlue',128,0,0),
('LightGoldenrod',130,221,238),
('dark magenta',139,0,139),
('grey34',87,87,87),
('pale turquoise',238,238,175),
('snow3',201,201,205),
('LightGoldenrod2',130,220,238),
('turquoise1',255,245,0),
('PeachPuff4',101,119,139),
('aquamarine2',198,238,118),
('DarkSeaGreen3',155,205,155),
('grey29',74,74,74),
('wheat3',150,186,205),
('dim grey',105,105,105),
('gray13',33,33,33),
('SlateBlue1',255,111,131),
('grey65',166,166,166),
('grey62',158,158,158),
('LightGrey',211,211,211),
('DarkOliveGreen2',104,238,188),
('DarkOliveGreen1',112,255,202),
('NavajoWhite1',173,222,255),
('dark khaki',107,183,189),
('grey96',245,245,245),
('SkyBlue',235,206,135),
('orange1',0,165,255),
('RoyalBlue4',139,64,39),
('gray87',222,222,222),
('CadetBlue4',139,134,83),
('grey63',161,161,161),
('PowderBlue',230,224,176),
('cornsilk3',177,200,205),
('goldenrod',32,165,218),
('SpringGreen4',69,139,0),
('gray81',207,207,207),
('grey100',255,255,255),
('honeydew4',131,139,131),
('salmon2',98,130,238),
('PaleVioletRed4',93,71,139),
('gray57',145,145,145),
('DarkGoldenrod3',12,149,205),
('SteelBlue2',238,172,92),
('coral3',69,91,205),
('MediumOrchid4',139,55,122),
('grey24',61,61,61),
('grey83',212,212,212),
('OrangeRed4',0,37,139),
('gray98',250,250,250),
('MintCream',250,255,245),
('NavajoWhite4',94,121,139),
('brown2',59,59,238),
('PeachPuff1',185,218,255),
('SeaGreen1',159,255,84),
('gray70',179,179,179),
('steel blue',180,130,70),
('grey69',176,176,176),
('gray23',59,59,59),
('aquamarine4',116,139,69),
('pale violet red',147,112,219),
('LightCyan3',205,205,180),
('DeepSkyBlue',255,191,0),
('grey23',59,59,59),
('SteelBlue4',139,100,54),
('LightSalmon',122,160,255),
('ivory',240,255,255),
('gray69',176,176,176),
('DodgerBlue',255,144,30),
('grey35',89,89,89),
('grey91',232,232,232),
('DimGray',105,105,105),
('grey74',189,189,189),
('khaki',140,230,240),
('magenta',255,0,255),
('burlywood',135,184,222),
('grey15',38,38,38),
('turquoise2',238,229,0),
('LightBlue4',139,131,104),
('DarkGrey',169,169,169),
('gray88',224,224,224),
('green1',0,255,0),
('papaya whip',213,239,255),
('gray93',237,237,237),
('LemonChiffon4',112,137,139),
('gray27',69,69,69),
('orange4',0,90,139),
('SlateGray4',139,123,108),
('OliveDrab',35,142,107),
('lavender blush',245,240,255),
('gray28',71,71,71),
('DarkSalmon',122,150,233),
('seashell',238,245,255),
('grey11',28,28,28),
('VioletRed4',82,34,139),
('gray74',189,189,189),
('WhiteSmoke',245,245,245),
('gray100',255,255,255),
('MediumPurple3',205,104,137),
('MistyRose',225,228,255),
('azure1',255,255,240),
('LightBlue',230,216,173),
('gray',128,128,128),
('LightCyan4',139,139,122),
('DarkOrchid2',238,58,178),
('lawn green',0,252,124),
('PaleVioletRed',147,112,219),
('purple1',255,48,155),
('GreenYellow',47,255,173),
('RoyalBlue2',238,110,67),
('VioletRed2',140,58,238),
('ivory2',224,238,238),
('gray72',184,184,184),
('grey60',153,153,153),
('DodgerBlue1',255,144,30),
('MistyRose1',225,228,255),
('LightCyan2',238,238,209),
('grey79',201,201,201),
('grey59',150,150,150),
('grey49',125,125,125),
('LightSteelBlue',222,196,176),
('DarkSlateBlue',139,61,72),
('purple',128,0,128),
('DeepSkyBlue2',238,178,0),
('gray55',140,140,140),
('IndianRed2',99,99,238),
('gray60',153,153,153),
('grey73',186,186,186),
('LightBlue3',205,192,154),
('gold',0,215,255),
('light salmon',122,160,255),
('gray73',186,186,186),
('white smoke',245,245,245),
('cyan',255,255,0),
('snow2',233,233,238),
('gray99',252,252,252),
('medium violet red',133,21,199),
('MidnightBlue',112,25,25),
('grey90',229,229,229),
('grey21',54,54,54),
('grey18',46,46,46),
('LightBlue1',255,239,191),
('medium sea green',113,179,60),
('moccasin',181,228,255),
('grey31',79,79,79),
('bisque1',196,228,255),
('AntiqueWhite2',204,223,238),
('dodger blue',255,144,30),
('grey12',31,31,31),
('LemonChiffon2',191,233,238),
('gray46',117,117,117),
('MediumAquamarine',170,205,102),
('CadetBlue1',255,245,152),
('grey89',227,227,227),
('blue1',255,0,0),
('firebrick2',44,44,238),
('gray61',156,156,156),
('lemon chiffon',205,250,255),
('grey95',242,242,242),
('seashell1',238,245,255),
('tomato3',57,79,205),
('plum1',255,187,255),
('azure3',205,205,193),
('ivory3',193,205,205),
('gray35',89,89,89),
('LightYellow2',209,238,238),
('gray50',127,127,127),
('gray22',56,56,56),
('magenta1',255,0,255),
('burlywood3',125,170,205),
('firebrick3',38,38,205),
('LightSteelBlue3',205,181,162),
('seashell4',130,134,139),
('CadetBlue3',205,197,122),
('orchid2',233,122,238),
('azure4',139,139,131),
('grey9',23,23,23),
('yellow green',50,205,154),
('chartreuse2',0,238,118),
('grey14',36,36,36),
('SlateGray1',255,226,198),
('medium spring green',154,250,0),
('MediumOrchid1',255,102,224),
('ghost white',255,248,248),
('dark cyan',139,139,0),
('gray38',97,97,97),
('MediumPurple1',255,130,171),
('spring green',127,255,0),
('salmon3',84,112,205),
('pink1',197,181,255),
('gray67',171,171,171),
('gray82',209,209,209),
('navajo white',173,222,255),
('tomato2',66,92,238),
('grey10',26,26,26),
('SkyBlue2',238,192,126),
('gray26',66,66,66),
('grey68',173,173,173),
('grey54',138,138,138),
('DeepPink1',147,20,255),
('light goldenrod yellow',210,250,250),
('gainsboro',220,220,220),
('SteelBlue3',205,148,79),
('olive drab',35,142,107),
('floral white',240,250,255),
('PaleGreen',152,251,152),
('bisque',196,228,255),
('LavenderBlush4',134,131,139),
('light slate grey',153,136,119),
('gray20',51,51,51),
('gray53',135,135,135),
('grey67',171,171,171),
('GhostWhite',255,248,248),
('LightSkyBlue',250,206,135),
('grey75',191,191,191),
('gray12',31,31,31),
('grey92',235,235,235),
('azure',255,255,240),
('AntiqueWhite',215,235,250),
('gray52',133,133,133),
('bisque3',158,183,205),
('OrangeRed3',0,55,205),
('gray3',8,8,8),
('SteelBlue1',255,184,99),
('gray96',245,245,245),
('sienna1',71,130,255),
('gray62',158,158,158),
('LightSeaGreen',170,178,32),
('LightPink1',185,174,255),
('turquoise3',205,197,0),
('grey66',168,168,168),
('OrangeRed2',0,64,238),
('gray94',240,240,240),
('light coral',128,128,240),
('cyan1',255,255,0),
('gray7',18,18,18),
('medium turquoise',204,209,72),
('IndianRed3',85,85,205),
('LightGoldenrod4',76,129,139),
('pale green',152,251,152),
('grey27',69,69,69),
('DeepPink2',137,18,238),
('MediumVioletRed',133,21,199),
('grey44',112,112,112),
('DarkSlateGray2',238,238,141),
('saddle brown',19,69,139),
('light pink',193,182,255),
('chocolate3',29,102,205),
('RosyBrown1',193,193,255),
('khaki3',115,198,205),
('gray58',148,148,148),
('PaleVioletRed2',159,121,238),
('gray21',54,54,54),
('PaleGreen4',84,139,84),
('chartreuse',0,255,127),
('DeepSkyBlue4',139,104,0),
('gray71',181,181,181),
('SeaGreen3',128,205,67),
('wheat',179,222,245),
('gray32',82,82,82),
('dark gray',169,169,169),
('green2',0,238,0),
('gold2',0,201,238),
('dark blue',139,0,0),
('grey39',99,99,99),
('LightSalmon2',114,149,238),
('grey42',107,107,107),
('thistle1',255,225,255),
('dark slate blue',139,61,72),
('SandyBrown',96,164,244),
('snow1',250,250,255),
('PaleVioletRed1',171,130,255),
('magenta4',139,0,139),
('MistyRose4',123,125,139),
('grey30',77,77,77),
('grey5',13,13,13),
('grey53',135,135,135),
('DeepPink3',118,16,205),
('LightSalmon1',122,160,255),
('DarkRed',0,0,139),
('cornsilk',220,248,255),
('grey28',71,71,71),
('NavajoWhite2',161,207,238),
('grey80',204,204,204),
('orange3',0,133,205),
('cornsilk2',205,232,238),
('burlywood2',145,197,238),
('coral1',86,114,255),
('gray39',99,99,99),
('orchid3',201,105,205),
('pink3',158,145,205),
('AntiqueWhite3',176,192,205),
('midnight blue',112,25,25),
('gray0',0,0,0),
('DarkMagenta',139,0,139),
('grey26',66,66,66),
('gray80',204,204,204),
('SpringGreen2',118,238,0),
('AntiqueWhite1',219,239,255),
('dark turquoise',209,206,0),
('khaki4',78,134,139),
('sienna4',38,71,139),
('HotPink4',98,58,139),
('agua',255,255,0),
('misty rose',225,228,255),
('DarkTurquoise',209,206,0),
('dark orchid',204,50,153),
('gold3',0,173,205),
('LightGray',211,211,211),
('LightSteelBlue4',139,123,110),
('MediumPurple2',238,121,159),
('salmon4',57,76,139),
('gray16',41,41,41),
('gray97',247,247,247),
('PaleGoldenrod',170,232,238),
('gray89',227,227,227),
('grey36',92,92,92),
('LightPink4',101,95,139),
('grey70',179,179,179),
('gray2',5,5,5),
('LightYellow3',180,205,205),
('turquoise4',139,134,0),
('green',0,128,0),
('IndianRed',92,92,205),
('SkyBlue3',205,166,108),
('MediumPurple',219,112,147),
('DeepPink',147,20,255),
('goldenrod4',20,105,139),
('SlateGray',144,128,112),
('LightSlateGray',153,136,119),
('SeaGreen2',148,238,78),
('brown',42,42,165),
('LightCyan1',255,255,224),
('OrangeRed1',0,69,255),
('LightYellow',224,255,255),
('blue3',205,0,0),
('grey8',20,20,20),
('SkyBlue1',255,206,135),
('khaki2',133,230,238),
('grey2',5,5,5),
('dark slate gray',79,79,47),
('peru',63,133,205),
('light goldenrod',130,221,238),
('DarkSeaGreen2',180,238,180),
('tomato1',71,99,255),
('dark violet',211,0,148),
('gray6',15,15,15),
('gray41',105,105,105),
('gray31',79,79,79),
('DarkOliveGreen4',61,139,110),
('seashell2',222,229,238),
('VioletRed',144,32,208),
('chocolate4',19,69,139),
('LightYellow1',224,255,255),
('teal',128,128,0),
('RosyBrown4',105,105,139),
('DarkOrchid3',205,50,154),
('AliceBlue',255,248,240),
('royal blue',225,105,65),
('DarkGoldenrod1',15,185,255),
('grey38',97,97,97),
('DarkOliveGreen',47,107,85),
('cyan3',205,205,0),
('dark green',0,100,0),
('mint cream',250,255,245),
('gray37',94,94,94),
('azure2',238,238,224),
('brown1',64,64,255),
('aquamarine',212,255,127),
('medium aquamarine',170,205,102),
('PaleGreen2',144,238,144),
('CornflowerBlue',237,149,100),
('grey82',209,209,209),
('grey6',15,15,15),
('gray79',201,201,201),
('slate blue',205,90,106),
('BlueViolet',226,43,138),
('LightSkyBlue1',255,226,176),
('grey',128,128,128),
('SpringGreen1',127,255,0),
('black',0,0,0),
('dark red',0,0,139),
('HotPink',180,105,255),
('gray76',194,194,194),
('bisque2',183,213,238),
('LemonChiffon3',165,201,205),
('dark goldenrod',11,134,184),
('maroon4',98,28,139),
('grey64',163,163,163),
('lime',0,255,0),
('green4',0,139,0),
('goldenrod2',34,180,238),
('SlateBlue3',205,89,105),
('LimeGreen',50,205,50),
('DarkCyan',139,139,0)]
#DEFORM -> COLOR -> BLUR -> SHADOW -> NOISE -> ROTATION
        #OUT_imgs []
        #for im in imgs
            #PROCESS
            #APPEND OUT_imgs
        #POP OUT_imgs into imgs
        #...
        #RETURN imgs
def GET_ALL(img, mask, solid_color = None, solid_color_random = False,
    color_dif_HSV = (0,0,0), color_dif_n_steps=0, blur = False, blur_random = False,
    color_mix = None, color_mix_random = False, color_mix_n_steps=0,
    shadow = False, shadow_random = False,
    noise = False, noise_random = False, reflection = False,
    rotate = 0, rotate_mirror = False, Flip_X = False, Flip_Y= False,
    deform_X = 0, deform_Y = 0, deform_chunks_X_min = 0, deform_chunks_Y_min = 0, deform_chunks_X_max = 0, deform_chunks_Y_max = 0):
    #TODO FILL :
    #COLOR_dif_hsv
    #COLOR MIX
    #NOISE_RANDOM
    #SHADOW_RANDOM
    IMGS = []
    IMGS.append(img)
    #DEFORMATION
    OUT_imgs = []
    if deform_X > 0:
        OUT_imgs.append(GET_deform(img,maxT=deform_X,chunks_min=deform_chunks_X_min,chunks_max=deform_chunks_X_max))
    if deform_Y > 0:
        OUT_imgs.append(GET_deform(img,maxT=deform_Y,axis=False,chunks_min=deform_chunks_Y_min,chunks_max=deform_chunks_Y_max))
    IMGS.extend(OUT_imgs)
    #COLOR SOLID
    OUT_imgs=[]
    if solid_color != None:
        for i in IMGS:
            OUT_imgs.extend(GET_change_color_solid(img,mask,solid_color))
    IMGS.extend(OUT_imgs)
    #COLOR SOLID RANDOM
    if solid_color_random:
        IMGS.append(GET_change_color_random(img,mask))
    
    #BLUR
    OUT_imgs=[]
    if blur:
        for i in IMGS:
            OUT_imgs.append(GET_blur(i, mask))
    #BLUR RANDOM
    if blur_random:
        for i in IMGS:
            OUT_imgs.append(GET_blur_random(i, mask))
    IMGS.extend(OUT_imgs)
    #REFLECTION
    OUT_imgs = []
    if reflection:
        for i in IMGS:
            OUT_imgs.append(GET_reflection(i,mask,90,10))
    IMGS.extend(OUT_imgs)
    #SHADOW
    OUT_imgs = []
    if shadow:
        for i in IMGS:
            OUT_imgs.append(GET_shadow(i,mask,90,10))
    IMGS.extend(OUT_imgs)
    #SHADOW RANDOM TODO
    #NOISE TODO: COLORED IMAGES SEEM TO GET NO NOISE 
    OUT_imgs = []
    if noise:
        for i in IMGS:
            OUT_imgs.append(GET_noise(i,mask,True))
            OUT_imgs.append(GET_noise(i,mask,False))
    IMGS.extend(OUT_imgs)
    #ROTATE
    OUT_imgs = []
    if rotate > 0:
        for i in IMGS:
            OUT_imgs.extend(GET_rotate(i, mask, rotate,rotate_mirror))
    IMGS.extend(OUT_imgs)
    #FLIP
    OUT_imgs = []
    if Flip_X:
        for i in IMGS:
            OUT_imgs.append(GET_flip_X(i,mask))
    if Flip_Y:
        for i in IMGS:
            OUT_imgs.append(GET_flip_Y(i,mask))
    if Flip_Y and Flip_X:
        for i in IMGS:
            OUT_imgs.append(GET_flip_Y(GET_flip_X(i,mask),mask))
    IMGS.extend(OUT_imgs)
    OUT_imgs=[]
    return IMGS
def GET_deform(img,minT=0, maxT=2,axis = True,chunks_min = 3,chunks_max = 7):
    h,w,_ = img.shape
    out = img.copy()
    img_chunks = []
    #getting CHUNKS
    cMax = 0
    if axis:
        cMax = h
    else: 
        cMax = w
    chunked = 0
    while chunked<cMax:
            c = random.randint(chunks_min,chunks_max)
            chunk = None
            #GETTING INDIVIDUAL CHUNK
            if axis:
                chunk = img[chunked:(chunked + c), :]

            else:
                chunk = img[:, chunked:(chunked + c)]
            img_chunks.append(chunk)
            chunked = chunked + c
    img_chunks.pop()
    #TRANSFORMING img by chunk
    used= 0
    for c in img_chunks:        
        #GETTING transition value
        plus_min = 1
        pmR = random.randint(0,1)
        if pmR == 1:
            plus_min = (-1)
        tv = plus_min * random.randint(minT,maxT)
        #GETTING transition matrix
        tx = 0
        ty = 0
        if axis:
            tx = tv
        else:
            ty = tv
        transitionM = np.array([
        [1, 0, tx], #positive RIGHT, negative LEFT
        [0, 1, ty] #positive DOWN, negative UP
        ], dtype='float32')
        #APPLYING transition to the chunk
        h_c, w_c, _ = c.shape
        t_chunk = cv.warpAffine(c,transitionM, (w_c, h_c))
        #STICHING CHUNK on to the output
        change = 0
        if axis:
            change = h_c
            out[used:(used + change), :] = t_chunk
        else:
            change = w_c
            out[:, used:(used + change)] = t_chunk
        used = used + change
    return  out
def GET_random_poly_pts(minX,maxX,minY,maxY):
    pts = []
    
    points = random.randint(3,9)
    for n in range(0, points):
        x = random.randint(minY,maxY)
        y = random.randint(minX,maxX)
        pts.append([x,y])
        
    pts = np.array(pts, dtype='uint8')
    return pts
def GET_random_mask(img, divisions, mask=''):
                                    #divisions is the number of divisions of the image
                                    #number of sections = 2^divisions
    out = np.zeros(img.shape, dtype='uint8')
    (h,w,_) = img.shape
    h1 = h
    w1 = w
    #SECTION SIZES
    for n in range(1,divisions):
        h1 = (h1/2)
        w1 = (w1/2)
    x = 0
    y = 0
    #GETING SHAPE TO EVERY SECTION
    while y != h:
        x = 0
        while x != w:
            points = GET_random_poly_pts(int(y), int(y+h1),int(x),int(x+w1))
            cv.fillPoly(out, pts=np.int32([points]), color = (255,255,255))
            x = x + w1
        y = y + h1
    if mask != '':
        #GETTING MASK BITWISE
        thresh = 254
        grey =cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
        (_, im_bw) = cv.threshold(grey, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
        im_bw_inv = cv.bitwise_not(im_bw)
        #GETTING BACKGROUND 
        bg = cv.bitwise_and(mask, mask, mask = im_bw_inv)
        fg = cv.bitwise_and(out, out, mask = im_bw)

        out = cv.add(bg,fg)
        return out
    else:
        return out
def GET_shadow(img, mask, opacity_top, opacity_bottom):
    (h,w,_) = img.shape
    out_img = cv.cvtColor(img, cv.COLOR_BGR2BGRA)
    #GET GRADIENT
    g_bot = (255*opacity_top)/100
    g_top = (255*opacity_bottom)/100
    g_y = np.linspace(g_bot,g_top,h,dtype='uint8')
    g_x = np.linspace(1,1,w,dtype='uint8')
    grad = np.outer(g_y,g_x)
    #ADD GRADIENT
    out_img[:,:,3] = grad
    #REDUCE BGRA to BGR
    out = np.zeros(img.shape, dtype='uint8')

    gray_grad = cv.cvtColor(grad,cv.COLOR_GRAY2BGR)
    for hh in range(0,h - 1):
        for ww in range(0, w-1):
            a = out_img[hh][ww][3]/255
            B = out_img[hh][ww][0]/255
            G = out_img[hh][ww][1]/255
            R = out_img[hh][ww][2]/255
            bgB = gray_grad[hh][ww][0]/255
            bgG = gray_grad[hh][ww][1]/255
            bgR = gray_grad[hh][ww][2]/255
            out[hh][ww][0] = (((1-a) * bgB) + (a*B)) * 255#B 
            out[hh][ww][1] = (((1-a) * bgG) + (a*G)) * 255 #G
            out[hh][ww][2] = (((1-a) * bgR) + (a*R)) * 255 #R
    #GETTING MASK BITWISE
    thresh = 254
    grey =cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    (_, im_bw) = cv.threshold(grey, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    im_bw_inv = cv.bitwise_not(im_bw)
    #GETTING BACKGROUND 
    bg = cv.bitwise_and(img, img, mask = im_bw_inv)
    #CREATING SOLID COLOR PICTURE
    #GETTING BACKGROUND
    fg = cv.bitwise_and(out, out, mask = im_bw)
    #BLENDING PICTURES
    out = cv.add(bg,fg)
    
    return out
def GET_reflection(img, mask, opacity_top, opacity_bottom):
    (h,w,_) = img.shape
    out_img = cv.cvtColor(img, cv.COLOR_BGR2BGRA)
    #GET GRADIENT
    g_bot = (255*opacity_top)/100
    g_top = (255*opacity_bottom)/100
    g_y = np.linspace(g_bot,g_top,h,dtype='uint8')
    g_x = np.linspace(1,1,w,dtype='uint8')
    grad = np.outer(g_y,g_x)
    #ADD GRADIENT
    out_img[:,:,3] = grad
    #REDUCE BGRA to BGR
    out = np.zeros(img.shape, dtype='uint8')

    gray_grad = cv.cvtColor(grad,cv.COLOR_GRAY2BGR)
    for hh in range(0,h - 1):
        for ww in range(0, w-1):
            a = out_img[hh][ww][3]/255
            B = out_img[hh][ww][0]/255
            G = out_img[hh][ww][1]/255
            R = out_img[hh][ww][2]/255
            bgB = gray_grad[hh][ww][0]/255
            bgG = gray_grad[hh][ww][1]/255
            bgR = gray_grad[hh][ww][2]/255
            out[hh][ww][0] = (((1-a) * B) + (a*bgB)) * 255#B 
            out[hh][ww][1] = (((1-a) * G) + (a*bgG)) * 255 #G
            out[hh][ww][2] = (((1-a) * R) + (a*bgR)) * 255 #R
    #GETTING MASK BITWISE
    thresh = 254
    grey =cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    (_, im_bw) = cv.threshold(grey, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    im_bw_inv = cv.bitwise_not(im_bw)
    #GETTING BACKGROUND 
    bg = cv.bitwise_and(img, img, mask = im_bw_inv)
    #CREATING SOLID COLOR PICTURE
    #GETTING BACKGROUND
    fg = cv.bitwise_and(out, out, mask = im_bw)
    #BLENDING PICTURES
    out = cv.add(bg,fg)
    
    return out
def GET_rotate(img, mask, angle, mirror):
    out = []
    (h, w, _ ) =img.shape
    #CENTER POINTS
    cX, cY = w/2, h/2
    if mirror == True:
        for a in range(360 - angle, 359):
            #ROTATION MATRIX
            rotationM = cv.getRotationMatrix2D((cX, cY), a, 1.0)
            #sin & cos ABSOLUTE VALUES
            cosRotationM = np.abs(rotationM[0][0])
            sinRotationM = np.abs(rotationM[0][1])
            #NEW DIMENSIONS
            nW = int((h*sinRotationM) + (w*cosRotationM))
            nH = int((h*cosRotationM) + (w*sinRotationM))
            #UPDATE ROTATION MATRIX
            rotationM[0][2] += (nW/2) - cX
            rotationM[1][2] += (nH/2) - cY
            #rotate image
            rot_img = cv.warpAffine(img, rotationM, (nW,nH))
            out.append(rot_img)
    for a in range(1, angle):
        #ROTATION MATRIX
        rotationM = cv.getRotationMatrix2D((cX, cY), a, 1.0)
        #sin & cos ABSOLUTE VALUES
        cosRotationM = np.abs(rotationM[0][0])
        sinRotationM = np.abs(rotationM[0][1])
        #NEW DIMENSIONS
        nW = int((h*sinRotationM) + (w*cosRotationM))
        nH = int((h*cosRotationM) + (w*sinRotationM))
        #UPDATE ROTATION MATRIX
        rotationM[0][2] += (nW/2) - cX
        rotationM[1][2] += (nH/2) - cY
        #rotate image
        rot_img = cv.warpAffine(img, rotationM, (nW,nH))
        out.append(rot_img)


    return out
def GET_flip_X(img, mask):
    return cv.flip(img,0)
def GET_flip_Y(img, mask):
    return cv.flip(img,1)
def GET_change_color_solid(img, mask, colors):#BGR
    out = []
    #GETTING MASK BITWISE
    thresh = 254
    grey =cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    (_, im_bw) = cv.threshold(grey, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    im_bw_inv = cv.bitwise_not(im_bw)
    #GETTING BACKGROUND 
    bg = cv.bitwise_and(img, img, mask = im_bw_inv)
    #CREATING SOLID COLOR PICTURE
    col_pic = np.zeros(mask.shape, dtype='uint8')
    for col in colors:
        (_, b,g,r) = col
        col_pic[:] = [b,g,r] 
        #GETTING BACKGROUND
        fg = cv.bitwise_and(col_pic, col_pic, mask = im_bw)
        #BLENDING PICTURES
        toSave = cv.add(bg,fg)
        out.append(toSave)
    return out
def GET_change_color_random(img, mask):
    out = img.copy()
    #GETTING MASK BITWISE
    thresh = 254
    grey =cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    (_, im_bw) = cv.threshold(grey, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    im_bw_inv = cv.bitwise_not(im_bw)
    #GETTING BACKGROUND 
    bg = cv.bitwise_and(out, out, mask = im_bw_inv)
    #CREATING COLOR PICTURE
    col_pic = np.zeros(mask.shape, dtype='uint8')
    (h,w,_) = out.shape
    used_h = 0
    while h>used_h:
        y = random.randint(1,h-used_h)
        used_w = 0
        while w>used_w:
            x = random.randint(1,w-used_w)
            #getting blur strength for the section
            color = random.randint(1,len(COLORS))
            #croping section
            paint_section = out[used_h:used_h+y, used_w:used_w+x]
            #coloring section
            (_, b,g,r) = COLORS[color]
            paint_section[:] = [b,g,r]
            #pasting section into image
            col_pic[used_h:used_h+y, used_w:used_w+x] = paint_section
            used_w = used_w + x
        used_h = used_h + y
    #GETTING BACKGROUND
    fg = cv.bitwise_and(col_pic, col_pic, mask = im_bw)
    #BLENDING PICTURES
    out = cv.add(bg,fg)
    return out
def GET_change_color_dif(img, mask, dif):#HSV VALUES
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hsv_img = hsv_img + dif
    #CREATING COLOR PICTURE
    col_img = cv.cvtColor(hsv_img.astype(np.uint8), cv.COLOR_HSV2BGR)
    #GETTING MASK BITWISE
    thresh = 254
    grey =cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    (_, im_bw) = cv.threshold(grey, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    im_bw_inv = cv.bitwise_not(im_bw)
    #GETTING BACKGROUND AND FOREGROUND
    bg = cv.bitwise_and(img, img, mask = im_bw_inv)
    fg = cv.bitwise_and(col_img, col_img, mask = im_bw)
    #BLENDING PICTURES
    out = cv.add(bg,fg)
    return out
def GET_blur(img, mask):
    out = img.copy()
    blur_img = cv.blur(out, (3,3))
    #GETTING MASK BITWISE
    thresh = 254
    grey =cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    (_, im_bw) = cv.threshold(grey, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    im_bw_inv = cv.bitwise_not(im_bw)
    #GETTING BACKGROUND AND FOREGROUND
    bg = cv.bitwise_and(out, out, mask = im_bw_inv)
    fg = cv.bitwise_and(blur_img, blur_img, mask = im_bw)
    #BLENDING PICTURES
    out = cv.add(bg,fg)
    return out
def GET_blur_random(img, mask):
    blur_img = img.copy()
    (h,w,_) = img.shape

    used_h = 0
    while h>used_h:
        y = random.randint(1,h-used_h)
        used_w = 0
        while w>used_w:
            x = random.randint(1,w-used_w)
            #getting blur strength for the section
            blur_strength = random.randint(1,5)
            #croping section
            blur_section = blur_img[used_h:used_h+y, used_w:used_w+x]
            #bluring
            blur_section = cv.blur(blur_section, (blur_strength,blur_strength))
            #pasting section into image
            blur_img[used_h:used_h+y, used_w:used_w+x] = blur_section
            used_w = used_w + x
        used_h = used_h + y
    #GETTING MASK BITWISE
    thresh = 254
    grey =cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    (_, im_bw) = cv.threshold(grey, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    im_bw_inv = cv.bitwise_not(im_bw)
    #GETTING BACKGROUND AND FOREGROUND
    bg = cv.bitwise_and(img, img, mask = im_bw_inv)
    fg = cv.bitwise_and(blur_img, blur_img, mask = im_bw)
    #BLENDING PICTURES
    out = cv.add(bg,fg)
    return out
def GET_color_mix(img, mask, colorMaps):
    out = []
    img_gray =cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #GETTING MASK BITWISE
    thresh = 254
    grey =cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    (_, im_bw) = cv.threshold(grey, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    im_bw_inv = cv.bitwise_not(im_bw)
    #GETTING BACKGROUND
    bg = cv.bitwise_and(img, img, mask = im_bw_inv)
    for col in colorMaps: 
        img_col = cv.applyColorMap(grey, col)
        #GETTING FOREGROUND
        fg = cv.bitwise_and(img_col, img_col, mask = im_bw)
        #BLENDING PICTURES
        toSave = cv.add(bg,fg)
        out.append(toSave)
   
    return out #list of images
def GET_color_mix_random(img, mask):
    img_gray =cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #GETTING MASK BITWISE
    thresh = 254
    grey =cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    (_, im_bw) = cv.threshold(grey, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    im_bw_inv = cv.bitwise_not(im_bw)
    #GETTING BACKGROUND 
    bg = cv.bitwise_and(img, img, mask = im_bw_inv)
    #CREATING COLOR PICTURE
    col_pic = np.zeros(mask.shape, dtype='uint8')
    (h,w,_) = img.shape
    used_h = 0
    while h>used_h:
        y = random.randint(1,h-used_h)
        used_w = 0
        while w>used_w:
            x = random.randint(1,w-used_w)
            #getting blur strength for the section
            color = random.randint(0,len(COLOR_MAPS)-1)
            #croping section
            paint_section = img_gray[used_h:used_h+y, used_w:used_w+x]
            #coloring section
            paint_section = cv.applyColorMap(paint_section, COLOR_MAPS[color])
            #pasting section into image
            col_pic[used_h:used_h+y, used_w:used_w+x] = paint_section
            used_w = used_w + x
        used_h = used_h + y
    #GETTING BACKGROUND
    fg = cv.bitwise_and(col_pic, col_pic, mask = im_bw)
    #BLENDING PICTURES
    out = cv.add(bg,fg)
    return out
def GET_noise(img, mask, whites = False):
    mean = 2
    var = 5
    sigma = var ** 0.5
    gaussian = np.random.normal(mean, sigma, (img.shape[0],img.shape[1])) 
    noise = np.zeros(img.shape, np.float32)
    if whites:
        noise[:, :, 0] = img[:, :, 0] + gaussian
        noise[:, :, 1] = img[:, :, 1] + gaussian
        noise[:, :, 2] = img[:, :, 2] + gaussian
    else:
        noise[:, :, 0] = img[:, :, 0] - gaussian
        noise[:, :, 1] = img[:, :, 1] - gaussian
        noise[:, :, 2] = img[:, :, 2] - gaussian
    noise = noise.astype(np.uint8)
    #GETTING MASK BITWISE
    thresh = 254
    grey =cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    (_, im_bw) = cv.threshold(grey, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    im_bw_inv = cv.bitwise_not(im_bw)
    #GETTING BACKGROUND 
    bg = cv.bitwise_and(img, img, mask = im_bw_inv)
    fg = cv.bitwise_and(noise, noise, mask = im_bw)

    out = cv.add(bg,fg.astype('uint8'))
    return out
#DEBUG

