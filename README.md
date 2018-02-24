# Auto Wallpaper

These python files download and set wallpaper(only on windows)
1. Downloading links for bing daily wallpaper images and images from pinterest boards
	-> This is done using 'imageLinks.pyw' 
	-> Functions under imageLinks.pyw:
		pinterest()
		bing()
	Function description:
	bing()		
		###############################################################################################
		# bing                                                                                        #
		# Uses bing api to get the bing daily wallpapers from the bing.com                            #
		# http://www.bing.com/HPImageArchive.aspx?format=js&n=10&mkt=en-US                            #
		# 'format' defines request type (js = json , xml = XML , rss = RSS)                           #
		# 'n' defines number of images to be returned(but only returns 8)                             #
		# 'mkt' defines the location( It can be ommited too)                                          #
		# Here the api returns a json array                                                           #
		# From which only the image url is picked up                                                  #
		###############################################################################################
		
	Things needed to be changed to run properly:
		Only change the drive letter in the open commands
		For example:
		Change : "E:\\Wallpaper\\Links.txt" To : "<Drive_letter>:\\Wallpaper\\Links.txt" -> "G:\\Wallpaper\\Links.txt"
		
	pinterest()
		###############################################################################################
		# pinterest                                                                                   #
		# Uses pinterest api to get the pinned images from the users board                            #
		# https://api.pinterest.com/v3/pidgets/boards/<username>/<board>/pins/                        #
		# The api returns a json array                                                                #
		# From which only the image url is picked up                                                  #
		# The image url is of a small image of something size '273x'                                  #
		# By replacing the text '273x' with 'originals' gives the image links of the larger image     #
		###############################################################################################

	Things needed to be changed to run properly:
		Change the drive letter in the 'open' commands
		For example:
		Change : "E:\\Wallpaper\\Links.txt" To : "<Drive_letter>:\\Wallpaper\\Links.txt" -> "G:\\Wallpaper\\Links.txt"
		&
		Change the request url as follows:
		https://api.pinterest.com/v3/pidgets/boards/<username>/<board>/pins/ 
		Eg: 
		change: "https://api.pinterest.com/v3/pidgets/boards/sayokdeymajumder1998/wallpapers/pins/" ->
				"https://api.pinterest.com/v3/pidgets/boards/kjonson199958/dogpics/pins/"