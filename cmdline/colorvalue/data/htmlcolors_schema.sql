CREATE TABLE IF NOT EXISTS colorgroups(
    groupname TEXT NOT NULL UNIQUE ON CONFLICT IGNORE
);

CREATE TABLE IF NOT EXISTS htmlcolors(
    group_id INTEGER NOT NULL,
    colorname TEXT NOT NULL UNIQUE ON CONFLICT IGNORE,
    rgb [TUPLE] TEXT NOT NULL,
    hex [HEXCOLOR] TEXT NOT NULL,
    FOREIGN KEY (group_id) REFERENCES colorgroups(rowid)
);

INSERT INTO colorgroups (groupname) VALUES ("Pinks");
INSERT INTO colorgroups (groupname) VALUES ("Reds");
INSERT INTO colorgroups (groupname) VALUES ("Oranges");
INSERT INTO colorgroups (groupname) VALUES ("Yellows");
INSERT INTO colorgroups (groupname) VALUES ("Browns");
INSERT INTO colorgroups (groupname) VALUES ("Greens");
INSERT INTO colorgroups (groupname) VALUES ("Cyans");
INSERT INTO colorgroups (groupname) VALUES ("Blues");
INSERT INTO colorgroups (groupname) VALUES ("Purples");
INSERT INTO colorgroups (groupname) VALUES ("Whites");
INSERT INTO colorgroups (groupname) VALUES ("Blacks");

INSERT INTO htmlcolors VALUES (1,"MediumVioletRed","(199, 21, 133)","#C71585");
INSERT INTO htmlcolors VALUES (1,"DeepPink","(255, 20, 147)","#FF1493");
INSERT INTO htmlcolors VALUES (1,"PaleVioletRed","(219, 112, 147)","#DB7093");
INSERT INTO htmlcolors VALUES (1,"HotPink","(255, 105, 180)","#FF69B4");
INSERT INTO htmlcolors VALUES (1,"LightPink","(255, 182, 193)","#FFB6C1");
INSERT INTO htmlcolors VALUES (1,"Pink","(255, 192, 203)","#FFC0CB");
INSERT INTO htmlcolors VALUES (2,"DarkRed","(139, 0, 0)","#8B0000");
INSERT INTO htmlcolors VALUES (2,"Red","(255, 0, 0)","#FF0000");
INSERT INTO htmlcolors VALUES (2,"Firebrick","(178, 34, 34)","#B22222");
INSERT INTO htmlcolors VALUES (2,"Crimson","(220, 20, 60)","#DC143C");
INSERT INTO htmlcolors VALUES (2,"IndianRed","(205, 92, 92)","#CD5C5C");
INSERT INTO htmlcolors VALUES (2,"LightCoral","(240, 128, 128)","#F08080");
INSERT INTO htmlcolors VALUES (2,"Salmon","(250, 128, 114)","#FA8072");
INSERT INTO htmlcolors VALUES (2,"DarkSalmon","(233, 150, 122)","#E9967A");
INSERT INTO htmlcolors VALUES (2,"LightSalmon","(255, 160, 122)","#FFA07A");
INSERT INTO htmlcolors VALUES (3,"OrangeRed","(255, 69, 0)","#FF4500");
INSERT INTO htmlcolors VALUES (3,"Tomato","(255, 99, 71)","#FF6347");
INSERT INTO htmlcolors VALUES (3,"DarkOrange","(255, 140, 0)","#FF8C00");
INSERT INTO htmlcolors VALUES (3,"Coral","(255, 127, 80)","#FF7F50");
INSERT INTO htmlcolors VALUES (3,"Orange","(255, 165, 0)","#FFA500");
INSERT INTO htmlcolors VALUES (4,"DarkKhaki","(189, 183, 107)","#BDB76B");
INSERT INTO htmlcolors VALUES (4,"Gold","(255, 215, 0)","#FFD700");
INSERT INTO htmlcolors VALUES (4,"Khaki","(240, 230, 140)","#F0E68C");
INSERT INTO htmlcolors VALUES (4,"PeachPuff","(255, 218, 185)","#FFDAB9");
INSERT INTO htmlcolors VALUES (4,"Yellow","(255, 255, 0)","#FFFF00");
INSERT INTO htmlcolors VALUES (4,"PaleGoldenrod","(238, 232, 170)","#EEE8AA");
INSERT INTO htmlcolors VALUES (4,"Moccasin","(255, 228, 181)","#FFE4B5");
INSERT INTO htmlcolors VALUES (4,"PapayaWhip","(255, 239, 213)","#FFEFD5");
INSERT INTO htmlcolors VALUES (4,"LightGoldenrodYellow","(250, 250, 210)","#FAFAD2");
INSERT INTO htmlcolors VALUES (4,"LemonChiffon","(255, 250, 205)","#FFFACD");
INSERT INTO htmlcolors VALUES (4,"LightYellow","(255, 255, 224)","#FFFFE0");
INSERT INTO htmlcolors VALUES (5,"Maroon","(128, 0, 0)","#800000");
INSERT INTO htmlcolors VALUES (5,"Brown","(165, 42, 42)","#A52A2A");
INSERT INTO htmlcolors VALUES (5,"SaddleBrown","(139, 69, 19)","#8B4513");
INSERT INTO htmlcolors VALUES (5,"Sienna","(160, 82, 45)","#A0522D");
INSERT INTO htmlcolors VALUES (5,"Chocolate","(210, 105, 30)","#D2691E");
INSERT INTO htmlcolors VALUES (5,"DarkGoldenrod","(184, 134, 11)","#B8860B");
INSERT INTO htmlcolors VALUES (5,"Peru","(205, 133, 63)","#CD853F");
INSERT INTO htmlcolors VALUES (5,"RosyBrown","(188, 143, 143)","#BC8F8F");
INSERT INTO htmlcolors VALUES (5,"Goldenrod","(218, 165, 32)","#DAA520");
INSERT INTO htmlcolors VALUES (5,"SandyBrown","(244, 164, 96)","#F4A460");
INSERT INTO htmlcolors VALUES (5,"Tan","(210, 180, 140)","#D2B48C");
INSERT INTO htmlcolors VALUES (5,"Burlywood","(222, 184, 135)","#DEB887");
INSERT INTO htmlcolors VALUES (5,"Wheat","(245, 222, 179)","#F5DEB3");
INSERT INTO htmlcolors VALUES (5,"NavajoWhite","(255, 222, 173)","#FFDEAD");
INSERT INTO htmlcolors VALUES (5,"Bisque","(255, 228, 196)","#FFE4C4");
INSERT INTO htmlcolors VALUES (5,"BlanchedAlmond","(255, 235, 205)","#FFEBCD");
INSERT INTO htmlcolors VALUES (5,"Cornsilk","(255, 248, 220)","#FFF8DC");
INSERT INTO htmlcolors VALUES (6,"DarkGreen","(0, 100, 0)","#006400");
INSERT INTO htmlcolors VALUES (6,"Green","(0, 128, 0)","#008000");
INSERT INTO htmlcolors VALUES (6,"DarkOliveGreen","(85, 107, 47)","#556B2F");
INSERT INTO htmlcolors VALUES (6,"ForestGreen","(34, 139, 34)","#228B22");
INSERT INTO htmlcolors VALUES (6,"SeaGreen","(46, 139, 87)","#2E8B57");
INSERT INTO htmlcolors VALUES (6,"Olive","(128, 128, 0)","#808000");
INSERT INTO htmlcolors VALUES (6,"OliveDrab","(107, 142, 35)","#6B8E23");
INSERT INTO htmlcolors VALUES (6,"MediumSeaGreen","(60, 179, 113)","#3CB371");
INSERT INTO htmlcolors VALUES (6,"LimeGreen","(50, 205, 50)","#32CD32");
INSERT INTO htmlcolors VALUES (6,"Lime","(0, 255, 0)","#00FF00");
INSERT INTO htmlcolors VALUES (6,"SpringGreen","(0, 255, 127)","#00FF7F");
INSERT INTO htmlcolors VALUES (6,"MediumSpringGreen","(0, 250, 154)","#00FA9A");
INSERT INTO htmlcolors VALUES (6,"DarkSeaGreen","(143, 188, 143)","#8FBC8F");
INSERT INTO htmlcolors VALUES (6,"MediumAquamarine","(102, 205, 170)","#66CDAA");
INSERT INTO htmlcolors VALUES (6,"YellowGreen","(154, 205, 50)","#9ACD32");
INSERT INTO htmlcolors VALUES (6,"LawnGreen","(124, 252, 0)","#7CFC00");
INSERT INTO htmlcolors VALUES (6,"Chartreuse","(127, 255, 0)","#7FFF00");
INSERT INTO htmlcolors VALUES (6,"LightGreen","(144, 238, 144)","#90EE90");
INSERT INTO htmlcolors VALUES (6,"GreenYellow","(173, 255, 47)","#ADFF2F");
INSERT INTO htmlcolors VALUES (6,"PaleGreen","(152, 251, 152)","#98FB98");
INSERT INTO htmlcolors VALUES (7,"Teal","(0, 128, 128)","#008080");
INSERT INTO htmlcolors VALUES (7,"DarkCyan","(0, 139, 139)","#008B8B");
INSERT INTO htmlcolors VALUES (7,"LightSeaGreen","(32, 178, 170)","#20B2AA");
INSERT INTO htmlcolors VALUES (7,"CadetBlue","(95, 158, 160)","#5F9EA0");
INSERT INTO htmlcolors VALUES (7,"DarkTurquoise","(0, 206, 209)","#00CED1");
INSERT INTO htmlcolors VALUES (7,"MediumTurquoise","(72, 209, 204)","#48D1CC");
INSERT INTO htmlcolors VALUES (7,"Turquoise","(64, 224, 208)","#40E0D0");
INSERT INTO htmlcolors VALUES (7,"Aqua","(0, 255, 255)","#00FFFF");
INSERT INTO htmlcolors VALUES (7,"Cyan","(0, 255, 255)","#00FFFF");
INSERT INTO htmlcolors VALUES (7,"Aquamarine","(127, 255, 212)","#7FFFD4");
INSERT INTO htmlcolors VALUES (7,"PaleTurquoise","(175, 238, 238)","#AFEEEE");
INSERT INTO htmlcolors VALUES (7,"LightCyan","(224, 255, 255)","#E0FFFF");
INSERT INTO htmlcolors VALUES (8,"Navy","(0, 0, 128)","#000080");
INSERT INTO htmlcolors VALUES (8,"DarkBlue","(0, 0, 139)","#00008B");
INSERT INTO htmlcolors VALUES (8,"MediumBlue","(0, 0, 205)","#0000CD");
INSERT INTO htmlcolors VALUES (8,"Blue","(0, 0, 255)","#0000FF");
INSERT INTO htmlcolors VALUES (8,"MidnightBlue","(25, 25, 112)","#191970");
INSERT INTO htmlcolors VALUES (8,"RoyalBlue","(65, 105, 225)","#4169E1");
INSERT INTO htmlcolors VALUES (8,"SteelBlue","(70, 130, 180)","#4682B4");
INSERT INTO htmlcolors VALUES (8,"DodgerBlue","(30, 144, 255)","#1E90FF");
INSERT INTO htmlcolors VALUES (8,"DeepSkyBlue","(0, 191, 255)","#00BFFF");
INSERT INTO htmlcolors VALUES (8,"CornflowerBlue","(100, 149, 237)","#6495ED");
INSERT INTO htmlcolors VALUES (8,"SkyBlue","(135, 206, 235)","#87CEEB");
INSERT INTO htmlcolors VALUES (8,"LightSkyBlue","(135, 206, 250)","#87CEFA");
INSERT INTO htmlcolors VALUES (8,"LightSteelBlue","(176, 196, 222)","#B0C4DE");
INSERT INTO htmlcolors VALUES (8,"LightBlue","(173, 216, 230)","#ADD8E6");
INSERT INTO htmlcolors VALUES (8,"PowderBlue","(176, 224, 230)","#B0E0E6");
INSERT INTO htmlcolors VALUES (9,"Indigo","(75, 0, 130)","#4B0082");
INSERT INTO htmlcolors VALUES (9,"Purple","(128, 0, 128)","#800080");
INSERT INTO htmlcolors VALUES (9,"DarkMagenta","(139, 0, 139)","#8B008B");
INSERT INTO htmlcolors VALUES (9,"DarkViolet","(148, 0, 211)","#9400D3");
INSERT INTO htmlcolors VALUES (9,"DarkSlateBlue","(72, 61, 139)","#483D8B");
INSERT INTO htmlcolors VALUES (9,"BlueViolet","(138, 43, 226)","#8A2BE2");
INSERT INTO htmlcolors VALUES (9,"DarkOrchid","(153, 50, 204)","#9932CC");
INSERT INTO htmlcolors VALUES (9,"Fuchsia","(255, 0, 255)","#FF00FF");
INSERT INTO htmlcolors VALUES (9,"Magenta","(255, 0, 255)","#FF00FF");
INSERT INTO htmlcolors VALUES (9,"SlateBlue","(106, 90, 205)","#6A5ACD");
INSERT INTO htmlcolors VALUES (9,"MediumSlateBlue","(123, 104, 238)","#7B68EE");
INSERT INTO htmlcolors VALUES (9,"MediumOrchid","(186, 85, 211)","#BA55D3");
INSERT INTO htmlcolors VALUES (9,"MediumPurple","(147, 112, 219)","#9370DB");
INSERT INTO htmlcolors VALUES (9,"Orchid","(218, 112, 214)","#DA70D6");
INSERT INTO htmlcolors VALUES (9,"Violet","(238, 130, 238)","#EE82EE");
INSERT INTO htmlcolors VALUES (9,"Plum","(221, 160, 221)","#DDA0DD");
INSERT INTO htmlcolors VALUES (9,"Thistle","(216, 191, 216)","#D8BFD8");
INSERT INTO htmlcolors VALUES (9,"Lavender","(230, 230, 250)","#E6E6FA");
INSERT INTO htmlcolors VALUES (10,"MistyRose","(255, 228, 225)","#FFE4E1");
INSERT INTO htmlcolors VALUES (10,"AntiqueWhite","(250, 235, 215)","#FAEBD7");
INSERT INTO htmlcolors VALUES (10,"Linen","(250, 240, 230)","#FAF0E6");
INSERT INTO htmlcolors VALUES (10,"Beige","(245, 245, 220)","#F5F5DC");
INSERT INTO htmlcolors VALUES (10,"WhiteSmoke","(245, 245, 245)","#F5F5F5");
INSERT INTO htmlcolors VALUES (10,"LavenderBlush","(255, 240, 245)","#FFF0F5");
INSERT INTO htmlcolors VALUES (10,"OldLace","(253, 245, 230)","#FDF5E6");
INSERT INTO htmlcolors VALUES (10,"AliceBlue","(240, 248, 255)","#F0F8FF");
INSERT INTO htmlcolors VALUES (10,"Seashell","(255, 245, 238)","#FFF5EE");
INSERT INTO htmlcolors VALUES (10,"GhostWhite","(248, 248, 255)","#F8F8FF");
INSERT INTO htmlcolors VALUES (10,"Honeydew","(240, 255, 240)","#F0FFF0");
INSERT INTO htmlcolors VALUES (10,"FloralWhite","(255, 250, 240)","#FFFAF0");
INSERT INTO htmlcolors VALUES (10,"Azure","(240, 255, 255)","#F0FFFF");
INSERT INTO htmlcolors VALUES (10,"MintCream","(245, 255, 250)","#F5FFFA");
INSERT INTO htmlcolors VALUES (10,"Snow","(255, 250, 250)","#FFFAFA");
INSERT INTO htmlcolors VALUES (10,"Ivory","(255, 255, 240)","#FFFFF0");
INSERT INTO htmlcolors VALUES (10,"White","(255, 255, 255)","#FFFFFF");
INSERT INTO htmlcolors VALUES (11,"Black","(0, 0, 0)","#000000");
INSERT INTO htmlcolors VALUES (11,"DarkSlateGray","(47, 79, 79)","#2F4F4F");
INSERT INTO htmlcolors VALUES (11,"DimGray","(105, 105, 105)","#696969");
INSERT INTO htmlcolors VALUES (11,"SlateGray","(112, 128, 144)","#708090");
INSERT INTO htmlcolors VALUES (11,"Gray","(128, 128, 128)","#808080");
INSERT INTO htmlcolors VALUES (11,"LightSlateGray","(119, 136, 153)","#778899");
INSERT INTO htmlcolors VALUES (11,"DarkGray","(169, 169, 169)","#A9A9A9");
INSERT INTO htmlcolors VALUES (11,"Silver","(192, 192, 192)","#C0C0C0");
INSERT INTO htmlcolors VALUES (11,"LightGray","(211, 211, 211)","#D3D3D3");
INSERT INTO htmlcolors VALUES (11,"Gainsboro","(220, 220, 220)","#DCDCDC");
