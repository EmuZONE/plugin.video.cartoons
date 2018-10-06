# -*- coding: utf-8 -*-
# Module: default
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

import sys
from urllib import urlencode
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

# Free sample videos are provided by www.vidsplay.com
# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.
VIDEOS = {'Bernhard & Bianca 1': [{'name': 'Die Mäusepolizei',
                       'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/cc001.jpg',
                       'video': 'https://archive.org/download/RobinHood1973/BernhardBianca-DieMusepolizei.mp4',
                       'genre': 'Cartoon'}
                       
                       ],
            'Bernhard & Bianca 2': [{'name': 'Im Kanguruhland',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/cc002.jpg',
                      'video': 'https://archive.org/download/RobinHood1973/BernhardBianca.Im.KanguruhLand.mp4',
                      'genre': 'Classic Cartoon'}
                      ],
            'Asterix erobert Rom': [{'name': 'Asterix erobert Rom',
                      'thumb': 'https://images-na.ssl-images-amazon.com/images/I/71tEWeR9RpL._SY445_.jpg',
                      'video': 'https://archive.org/download/RobinHood1973/BernhardBianca.Im.KanguruhLand.mp4',
                      'genre': 'Classic Cartoon'}
                      ],
            'Asterix der Gallier': [{'name': 'Asterix der Gallier',
                      'thumb': 'https://media1.jpc.de/image/w600/front/0/4006680072449.jpg',
                      'video': 'https://archive.org/download/AstrixEtLeCoupDuMenhir/Ast%C3%A9rix%20le%20Gaulois.mp4',
                      'genre': 'Classic Cartoon'}
                      ],
            'Asterix in Amerika': [{'name': 'Asterix in Amerika',
                      'thumb': 'https://is2-ssl.mzstatic.com/image/thumb/Video4/v4/1c/a6/7a/1ca67a82-48c8-806e-216c-f9b9ca2254eb/ticket.mnbhykqz.jpg/268x0w.jpg',
                      'video': 'https://archive.org/download/RobinHood1973/BernhardBianca.Im.KanguruhLand.mp4',
                      'genre': 'Classic Cartoon'}
                      ],
            'A Charly Brown Valentine': [{'name': 'A Charly Brown Valentine',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/GUEST_06b38d3f-091a-4e91-b9d9-bc5038d3c338.jpg',
                      'video': 'https://archive.org/download/RobinHood1973/BernhardBianca.Im.KanguruhLand.mp4',
                      'genre': 'Classic Cartoon'}
                      ],
            'Bambi': [{'name': 'Bambi',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/71C6kVIhCuL._SX425_.jpg',
                      'video': 'https://archive.org/download/RobinHood1973/BernhardBianca.Im.KanguruhLand.mp4',
                      'genre': 'Classic Cartoon'}
                      ],
            'Asterix Operation Hinkelstein': [{'name': 'Asterix Operation Hinkelstein',
                      'thumb': 'https://images-na.ssl-images-amazon.com/images/I/51ZNgX-htLL._SY445_.jpg',
                      'video': 'https://archive.org/download/AstrixEtLeCoupDuMenhir/Ast%C3%A9rix%20et%20le%20coup%20du%20menhir.mp4',
                      'genre': 'Classic Cartoon'}
                      ],
            'Bernhard & Bianca 2': [{'name': 'Im Kanguruhland',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/cc002.jpg',
                      'video': 'https://archive.org/download/RobinHood1973/BernhardBianca.Im.KanguruhLand.mp4',
                      'genre': 'Classic Cartoon'}
                       
                      ],
            'KÃ¶nig der LÃ¶wen': [{'name': 'KÃ¶nig der LÃ¶wen 1',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/cc003.jpg',
                      'video': 'https://archive.org/download/RobinHood1973/DerKnigDerLwen.mp4',
                      'genre': 'Cars'}
                      ],
                      'KÃ¶nig der LÃ¶wen 2': [{'name': 'KÃ¶nig der LÃ¶wen 2',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/cc004.jpg',
                      'video': 'https://archive.org/download/RobinHood1973/KnigDerLwen2-SimbasKnigreich.mp4',
                      'genre': 'Classic Cartoon'}
                      ],
                      'KÃ¶nig der LÃ¶wen 3': [{'name': 'KÃ¶nig der LÃ¶wen 2',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/cc005.jpg',
                      'video': 'https://archive.org/download/RobinHood1973/DerKnigDerLwen3HakunaMatata2004.mp4',
                      'genre': 'Classic Cartoon'}
                      
                      
                     ],
                     'Cap und Capper': [{'name': 'Cap und Capper 1',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/cc006.jpg',
                      'video': 'https://archive.org/download/RobinHood1973/CapCapper.mp4',
                      'genre': 'Classic Cartoon'}
                      
                      ],
                      
                     'Cap und Capper 2': [{'name': 'Cap und Capper 2',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/cc007.jpg',
                      'video': 'https://archive.org/download/RobinHood1973/Cap%20und%20Capper%202%20%282012%29.mp4',
                      'genre': 'Cars'}
                     ],
                     'Susi und Strolch': [{'name': 'Susi und Strolch',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/cc008.jpg',
                      'video': 'https://archive.org/download/RobinHood1973/SusiStrolch.mp4',
                      'genre': 'Classic Cartoon'}
                      ],
                     'Der Goofy Film': [{'name': 'Der Goofy Film',
                      'thumb': 'https://image.tmdb.org/t/p/w500/ftDAmjB7C8EUokGZPMeQ1sr6St4.jpg',
                      'video': 'https://archive.org/download/DerGoofyFilm/Der%20Goofy%20Film.mp4',
                      'genre': 'Classic Cartoon'}
                      ],
                      'Robin Hood': [{'name': 'Robin Hood (1973)',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/cc009.jpg',
                      'video': 'https://archive.org/download/RobinHood1973/Robin%20Hood%20%281973%29.mp4',
                      'genre': 'Cars'}
                      ],
                      'The AristoCats': [{'name': 'The AristoCats',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/cc010.jpg',
                      'video': 'https://archive.org/download/RobinHood1973/The.AristoCats.mp4',
                      'genre': 'Cars'}
                      ],
                      'Pocahontas': [{'name': 'Pocahontas',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/cc011.jpg',
                      'video': 'https://archive.org/download/RobinHood1973/Pocahontas.mp4',
                      'genre': 'Classic Cartoon'}
                      
                      ],
                      'Anastasia': [{'name': 'Anastasia',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/_anastasia.jpg',
                      'video': 'https://archive.org/download/RobinHood1973/Pocahontas.mp4',
                      'genre': 'Classic Cartoon'}
                      ],
                      'Heavy Metal FAKK2': [{'name': 'Heavy Metal FAKK2',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/_heavy.jpg',
                      'video': 'https://archive.org/download/RobinHood1973/Pocahontas.mp4',
                      'genre': 'Classic Cartoon'}
                      ],
                      'Aladdin': [{'name': 'Aladdin',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/_aladdin.jpg',
                      'video': 'https://archive.org/download/RobinHood1973/Pocahontas.mp4',
                      'genre': 'Classic Cartoon'}
                      ],
                      '101 Dalmatiner': [{'name': '101 Dalmatiner',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/_101.jpg',
                      'video': 'https://archive.org/download/RobinHood1973/Pocahontas.mp4',
                      'genre': 'Classic Cartoon'}
                      ],
                      'South Park - Der Film': [{'name': 'South Park - Der Film',
                      'thumb': 'https://images-na.ssl-images-amazon.com/images/I/51AB65SS8HL._SY445_.jpg',
                      'video': 'https://archive.org/download/RobinHood1973/Pocahontas.mp4',
                      'genre': 'Classic Cartoon'}
                      ],
                      'Asterix & Kleopatra': [{'name': 'Asterix & Kleopatra',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/asterix-und-kleopatra.jpg',
                      'video': 'https://archive.org/download/AstrixEtLeCoupDuMenhir/Ast%C3%A9rix%20et%20Cl%C3%A9op%C3%A2tre.mp4',
                      'genre': 'Classic Cartoon'}
                      ],
                      'Oliver & Company': [{'name': 'Oliver & Company',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/91iIlSEHRKL._SL1500_.jpg',
                      'video': 'https://archive.org/download/RobinHood1973/Pocahontas.mp4',
                      'genre': 'Classic Cartoon'}
                      ],
                      'Cinderella 2': [{'name': 'Cinderella 2',
                      'thumb': 'https://images-na.ssl-images-amazon.com/images/I/51GWG4HBSWL._SY445_.jpg',
                      'video': 'https://archive.org/download/RobinHood1973/Pocahontas.mp4',
                      'genre': 'Classic Cartoon'}
                      ],
                      'Der GlÃ¶ckner von Notre Dame': [{'name': 'Der GlÃ¶ckner von Notre Dame',
                      'thumb': 'https://media1.jpc.de/image/w600/front/0/4051238042351.jpg',
                      'video': 'https://archive.org/download/RobinHood1973/Pocahontas.mp4',
                      'genre': 'Classic Cartoon'}
                      ],
                      'Simpsons - Der Film': [{'name': 'Simpsons - Der Film',
                      'thumb': 'https://images-na.ssl-images-amazon.com/images/I/71SdNCz2WpL._SY445_.jpg',
                      'video': 'https://archive.org/download/RobinHood1973/Pocahontas.mp4',
                      'genre': 'Classic Cartoon'}
                      ],
                      'Arielle die Meerjungfrau': [{'name': 'Arielle die Meerjungfrau',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/cc012.jpg',
                      'video': 'https://archive.org/download/RobinHood1973/ArielleDieMeerjungfrau.mp4',
                      'genre': 'Classic Cartoon'}
                      ],
                      'Asterix bei den Briten': [{'name': 'Asterix bei den Briten',
                      'thumb': 'https://media1.jpc.de/image/w600/front/0/4006680072586.jpg',
                      'video': 'https://archive.org/download/AstrixChezLesBretons/Ast%C3%A9rix%20chez%20les%20Bretons.mp4',
                      'genre': 'Classic Cartoon'}
                      ],
                      'Asterix Sieg Ã¼ber CÃ¤sar': [{'name': 'Asterix Sieg Ã¼ber CÃ¤sar',
                      'thumb': 'https://media1.jpc.de/image/w600/front/0/4006680072579.jpg',
                      'video': 'https://archive.org/download/AstrixEtLaSurpriseDeCsar/Ast%C3%A9rix%20et%20la%20surprise%20de%20C%C3%A9sar.mp4',
                      'genre': 'Classic Cartoon'}
                      ],
            'Walhalla': [{'name': 'Walhalla der Film',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/cc013.jpg',
                      'video': 'https://ia601509.us.archive.org/8/items/Walhalla1986/Walhalla%20%281986%29.mp4',
                      'genre': 'Classic Cartoon'}
                     ]}


def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :type kwargs: dict
    :return: plugin call URL
    :rtype: str
    """
    return '{0}?{1}'.format(_url, urlencode(kwargs))


def get_categories():
    """
    Get the list of video categories.

    Here you can insert some parsing code that retrieves
    the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
    from some site or server.

    .. note:: Consider using `generator functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :return: The list of video categories
    :rtype: types.GeneratorType
    """
    return VIDEOS.iterkeys()


def get_videos(category):
    """
    Get the list of videofiles/streams.

    Here you can insert some parsing code that retrieves
    the list of video streams in the given category from some site or server.

    .. note:: Consider using `generators functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :param category: Category name
    :type category: str
    :return: the list of videos in the category
    :rtype: list
    """
    return VIDEOS[category]


def list_categories():
    """
    Create the list of video categories in the Kodi interface.
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, 'My Video Collection')
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, 'videos')
    # Get video categories
    categories = get_categories()
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category)
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': VIDEOS[category][0]['thumb'],
                          'icon': VIDEOS[category][0]['thumb'],
                          'fanart': VIDEOS[category][0]['thumb']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # https://codedocs.xyz/xbmc/xbmc/group__python__xbmcgui__listitem.html#ga0b71166869bda87ad744942888fb5f14
        # 'mediatype' is needed for a skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': category,
                                    'genre': category,
                                    'mediatype': 'video'})
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = get_url(action='listing', category=category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def list_videos(category):
    """
    Create the list of playable videos in the Kodi interface.

    :param category: Category name
    :type category: str
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, category)
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, 'videos')
    # Get the list of videos in the category.
    videos = get_videos(category)
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        # 'mediatype' is needed for skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': video['name'],
                                    'genre': video['genre'],
                                    'mediatype': 'video'})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/wp-content/uploads/2017/04/crab.mp4
        url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos(params['category'])
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_categories()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
