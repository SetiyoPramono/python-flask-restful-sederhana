# import resource
from ast import parse
from asyncore import read
from flask import Flask, jsonify, request
import json
from flask_restful import Api, Resource, reqparse

# init app
app = Flask(__name__)
api = Api(app)


# # Using External Local Data
# with open("dreams.json") as f:
#     page1 = json.load(f)


# class All(Resource):
#     def get(self):
#         return jsonify({"page1": page1})


# with open("dreams1.json") as f:
#     page2 = json.load(f)


# class ops(Resource):
#     def get(self):
#         return jsonify({"page2": page2})
# Create Resource Class
class halaman(Resource):
    def get(self):
        return {

        }


class Page1(Resource):
    def get(self, element):
        parser = reqparse.RequestParser()
        parser.add_argument('jenisElement', choices=(
            'headers', 'body', 'footer'), help='jenis data tidak ditemukan: {error_msg}')
        parser.add_argument(
            'element', help='jenis data tidak ditemukan: {error_msg}')
        args = parser.parse_args()
        print(args)
        # validasi parameter
        if element == 'headers':
            # validasi argumen
            if (args.jenisElement != None and args.jenisElement == 'headers'):
                if (args.element != None and args.element == 'headerKiri'):
                    return {
                        "headerKiri": {
                            "teks": {
                                "teksIcon": "Pexman",
                                "teksSpan": "Agency",
                                "teksSpanSmall": "Creative"
                            },
                            "url": "https://preview.colorlib.com/theme/pexman/index.html"
                        }
                    }
                elif (args.element != None and args.element == 'headerKanan'):
                    return {
                        "headerKanan": [
                            {
                                "home": {
                                    "teks": "Home",
                                    "url": "https://preview.colorlib.com/theme/pexman/index.html"
                                }
                            },
                            {
                                "about": {
                                    "teks": "About",
                                    "url": "https://preview.colorlib.com/theme/pexman/about.html"
                                }
                            },
                            {
                                "work": {
                                    "teks": "Work",
                                    "url": "https://preview.colorlib.com/theme/pexman/work.html"
                                }
                            },
                            {
                                "blog": {
                                    "teks": "Blog",
                                    "url": "https://preview.colorlib.com/theme/pexman/blog.html"
                                }
                            },
                            {
                                "contact": {
                                    "teks": "Contact",
                                    "url": "https://preview.colorlib.com/theme/pexman/contact.html"
                                }
                            }
                        ]
                    }
                else:
                    return {
                        "headers": [
                            {
                                "headerKiri": {
                                    "teks": {
                                        "teksIcon": "Pexman",
                                        "teksSpan": "Agency",
                                        "teksSpanSmall": "Creative"
                                    },
                                    "url": "https://preview.colorlib.com/theme/pexman/index.html"
                                }
                            },
                            {
                                "headerKanan": [
                                    {
                                        "home": {
                                            "teks": "Home",
                                            "url": "https://preview.colorlib.com/theme/pexman/index.html"
                                        }
                                    },
                                    {
                                        "about": {
                                            "teks": "About",
                                            "url": "https://preview.colorlib.com/theme/pexman/about.html"
                                        }
                                    },
                                    {
                                        "work": {
                                            "teks": "Work",
                                            "url": "https://preview.colorlib.com/theme/pexman/work.html"
                                        }
                                    },
                                    {
                                        "blog": {
                                            "teks": "Blog",
                                            "url": "https://preview.colorlib.com/theme/pexman/blog.html"
                                        }
                                    },
                                    {
                                        "contact": {
                                            "teks": "Contact",
                                            "url": "https://preview.colorlib.com/theme/pexman/contact.html"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
        elif (element == 'body'):
            if (args.jenisElement != None and args.jenisElement == 'body'):
                if (args.element != None and args.element == 'banner'):
                    return {
                        "banner": [
                            {
                                "id": 1,
                                "img": "https://c4.wallpaperflare.com/wallpaper/39/346/426/digital-art-men-city-futuristic-night-hd-wallpaper-thumb.jpg",
                                "teks": {
                                    "teksid": "01",
                                    "teksJudul": "Make Creative Website",
                                    "teksParagraf": "A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth."
                                },
                                "button": {
                                    "teks": "View Portfolio",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                }
                            },
                            {
                                "id": 2,
                                "img": "https://c4.wallpaperflare.com/wallpaper/39/346/426/digital-art-men-city-futuristic-night-hd-wallpaper-thumb.jpg",
                                "teks": {
                                    "teksid": "02",
                                    "teksJudul": "Make Creative Website",
                                    "teksParagraf": "A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth."
                                },
                                "button": {
                                    "teks": "View Portfolio",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                }
                            },
                            {
                                "id": 3,
                                "img": "https://c4.wallpaperflare.com/wallpaper/39/346/426/digital-art-men-city-futuristic-night-hd-wallpaper-thumb.jpg",
                                "teks": {
                                    "teksid": "03",
                                    "teksJudul": "Make Creative Website",
                                    "teksParagraf": "A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth."
                                },
                                "button": {
                                    "teks": "View Portfolio",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                }
                            }
                        ]
                    }
                elif (args.element != None and args.element == 'welcomepexman'):
                    return {
                        "welcomepexman": {
                            "img": "https://c4.wallpaperflare.com/wallpaper/39/346/426/digital-art-men-city-futuristic-night-hd-wallpaper-thumb.jpg",
                            "teks": {
                                "teksJudul": "Welcome Pexman",
                                "teksJudul1": "We Are Creative Agency That Create Beautiful Website",
                                "teksParagraf": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.",
                                "button": {
                                    "teks": "Start A Project",
                                    "url": "https://preview.colorlib.com/theme/pexman/index.html#"
                                }
                            }
                        }
                    }
                else:
                    return {
                        "body": [
                            {
                                "banner": [
                                    {
                                        "id": 1,
                                        "img": "https://c4.wallpaperflare.com/wallpaper/39/346/426/digital-art-men-city-futuristic-night-hd-wallpaper-thumb.jpg",
                                        "teks": {
                                            "teksid": "01",
                                            "teksJudul": "Make Creative Website",
                                            "teksParagraf": "A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth."
                                        },
                                        "button": {
                                            "teks": "View Portfolio",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        }
                                    },
                                    {
                                        "id": 2,
                                        "img": "https://c4.wallpaperflare.com/wallpaper/39/346/426/digital-art-men-city-futuristic-night-hd-wallpaper-thumb.jpg",
                                        "teks": {
                                            "teksid": "02",
                                            "teksJudul": "Make Creative Website",
                                            "teksParagraf": "A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth."
                                        },
                                        "button": {
                                            "teks": "View Portfolio",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        }
                                    },
                                    {
                                        "id": 3,
                                        "img": "https://c4.wallpaperflare.com/wallpaper/39/346/426/digital-art-men-city-futuristic-night-hd-wallpaper-thumb.jpg",
                                        "teks": {
                                            "teksid": "03",
                                            "teksJudul": "Make Creative Website",
                                            "teksParagraf": "A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth."
                                        },
                                        "button": {
                                            "teks": "View Portfolio",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        }
                                    }
                                ]
                            },
                            {
                                "welcomepexman": {
                                    "img": "https://c4.wallpaperflare.com/wallpaper/39/346/426/digital-art-men-city-futuristic-night-hd-wallpaper-thumb.jpg",
                                    "teks": {
                                        "teksJudul": "Welcome Pexman",
                                        "teksJudul1": "We Are Creative Agency That Create Beautiful Website",
                                        "teksParagraf": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.",
                                        "button": {
                                            "teks": "Start A Project",
                                            "url": "https://preview.colorlib.com/theme/pexman/index.html#"
                                        }
                                    }
                                }
                            },
                            {
                                "keteranganProduct": [
                                    {
                                        "jumlah": 10,
                                        "teks": {
                                            "teksjumlah": "K+",
                                            "teksSpan": "Achievements"
                                        }
                                    },
                                    {
                                        "jumlah": 211,
                                        "teks": {
                                            "teksjumlah": "K+",
                                            "teksSpan": "Achievements"
                                        }
                                    },
                                    {
                                        "jumlah": 27,
                                        "teks": {
                                            "teksjumlah": "",
                                            "teksSpan": "Achievements"
                                        }
                                    },
                                    {
                                        "jumlah": 30,
                                        "teks": {
                                            "teksjumlah": "K+",
                                            "teksSpan": "Achievements"
                                        }
                                    }
                                ]
                            },
                            {
                                "whatWeOffer": {
                                    "img": "https://preview.colorlib.com/theme/pexman/index.html#",
                                    "teks": {
                                        "teksJudul": "What We Offer",
                                        "teksJudul1": "What We Offer",
                                        "teksParagraf": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.",
                                        "tekSpan": [
                                            {
                                                "research": {
                                                    "id": 1,
                                                    "teksJudul": "Resecearch",
                                                    "teksParagraf": "A small river named Duden flows by their place."
                                                }
                                            },
                                            {
                                                "Design": {
                                                    "id": 2,
                                                    "teksJudul": "Design",
                                                    "teksParagraf": "A small river named Duden flows by their place."
                                                }
                                            },
                                            {
                                                "Development": {
                                                    "id": 3,
                                                    "teksJudul": "Development",
                                                    "teksParagraf": "A small river named Duden flows by their place."
                                                }
                                            },
                                            {
                                                "Testing": {
                                                    "id": 4,
                                                    "teksJudul": "Testing",
                                                    "teksParagraf": "A small river named Duden flows by their place."
                                                }
                                            }
                                        ],
                                        "button": {
                                            "teks": "Start A Project",
                                            "url": "https://preview.colorlib.com/theme/pexman/index.html#"
                                        }
                                    }
                                }
                            },
                            {
                                "kontent": [
                                    {
                                        "webDesign": {
                                            "icon": "flaticon-computer",
                                            "teks": {
                                                "teksJudul": "Web Design",
                                                "teksParagraf": "A small river named Duden flows by their place and supplies it with the necessary regelialia."
                                            }
                                        }
                                    },
                                    {
                                        "Photography": {
                                            "icon": "flaticon-computer",
                                            "teks": {
                                                "teksJudul": "Web Design",
                                                "teksParagraf": "A small river named Duden flows by their place and supplies it with the necessary regelialia."
                                            }
                                        }
                                    },
                                    {
                                        "Marketing": {
                                            "icon": "flaticon-computer",
                                            "teks": {
                                                "teksJudul": "Web Design",
                                                "teksParagraf": "A small river named Duden flows by their place and supplies it with the necessary regelialia."
                                            }
                                        }
                                    },
                                    {
                                        "Grapic Degign": {
                                            "icon": "flaticon-computer",
                                            "teks": {
                                                "teksJudul": "Web Design",
                                                "teksParagraf": "A small river named Duden flows by their place and supplies it with the necessary regelialia."
                                            }
                                        }
                                    }
                                ]
                            },
                            {
                                "porfolio": {
                                    "teksJudul": "Our Porfolio",
                                    "teksJudul1": "Our Stunning Porfolio",
                                    "MenuPorfolio": [
                                        {
                                            "all": {
                                                "url": "https://preview.colorlib.com/theme/pexman/#",
                                                "teks": "All"
                                            }
                                        },
                                        {
                                            "branding": {
                                                "url": "https://preview.colorlib.com/theme/pexman/#",
                                                "teks": "Branding"
                                            }
                                        },
                                        {
                                            "webdesign": {
                                                "url": "https://preview.colorlib.com/theme/pexman/#",
                                                "teks": "Web Deign"
                                            }
                                        },
                                        {
                                            "ilustration": {
                                                "url": "https://preview.colorlib.com/theme/pexman/#",
                                                "teks": "Ilustration"
                                            }
                                        },
                                        {
                                            "Aplication": {
                                                "url": "https://preview.colorlib.com/theme/pexman/#",
                                                "teks": "Aplication"
                                            }
                                        }
                                    ],
                                    "fotoPorfolio": [
                                        {
                                            "img": "https://images.ctfassets.net/hrltx12pl8hq/7yQR5uJhwEkRfjwMFJ7bUK/dc52a0913e8ff8b5c276177890eb0129/offset_comp_772626-opt.jpg?fit=fill&w=800&h=300",
                                            "teks": {
                                                "teksJudul": "Hark Website",
                                                "teksJudul1": "Web Design,Branding"
                                            },
                                            "butoon": {
                                                "icon": "fa fa-search",
                                                "url": "https://preview.colorlib.com/theme/pexman/images/work-1.jpg"
                                            }
                                        },
                                        {
                                            "img": "https://images.ctfassets.net/hrltx12pl8hq/7yQR5uJhwEkRfjwMFJ7bUK/dc52a0913e8ff8b5c276177890eb0129/offset_comp_772626-opt.jpg?fit=fill&w=800&h=300",
                                            "teks": {
                                                "teksJudul": "Hark Website",
                                                "teksJudul1": "Web Design,Branding"
                                            },
                                            "butoon": {
                                                "icon": "fa fa-search",
                                                "url": "https://preview.colorlib.com/theme/pexman/images/work-1.jpg"
                                            }
                                        },
                                        {
                                            "img": "https://images.ctfassets.net/hrltx12pl8hq/7yQR5uJhwEkRfjwMFJ7bUK/dc52a0913e8ff8b5c276177890eb0129/offset_comp_772626-opt.jpg?fit=fill&w=800&h=300",
                                            "teks": {
                                                "teksJudul": "Hark Website",
                                                "teksJudul1": "Web Design,Branding"
                                            },
                                            "butoon": {
                                                "icon": "fa fa-search",
                                                "url": "https://preview.colorlib.com/theme/pexman/images/work-1.jpg"
                                            }
                                        },
                                        {
                                            "img": "https://images.ctfassets.net/hrltx12pl8hq/7yQR5uJhwEkRfjwMFJ7bUK/dc52a0913e8ff8b5c276177890eb0129/offset_comp_772626-opt.jpg?fit=fill&w=800&h=300",
                                            "teks": {
                                                "teksJudul": "Hark Website",
                                                "teksJudul1": "Web Design,Branding"
                                            },
                                            "butoon": {
                                                "icon": "fa fa-search",
                                                "url": "https://preview.colorlib.com/theme/pexman/images/work-1.jpg"
                                            }
                                        },
                                        {
                                            "img": "https://images.ctfassets.net/hrltx12pl8hq/7yQR5uJhwEkRfjwMFJ7bUK/dc52a0913e8ff8b5c276177890eb0129/offset_comp_772626-opt.jpg?fit=fill&w=800&h=300",
                                            "teks": {
                                                "teksJudul": "Hark Website",
                                                "teksJudul1": "Web Design,Branding"
                                            },
                                            "butoon": {
                                                "icon": "fa fa-search",
                                                "url": "https://preview.colorlib.com/theme/pexman/images/work-1.jpg"
                                            }
                                        },
                                        {
                                            "img": "https://images.ctfassets.net/hrltx12pl8hq/7yQR5uJhwEkRfjwMFJ7bUK/dc52a0913e8ff8b5c276177890eb0129/offset_comp_772626-opt.jpg?fit=fill&w=800&h=300",
                                            "teks": {
                                                "teksJudul": "Hark Website",
                                                "teksJudul1": "Web Design,Branding"
                                            },
                                            "butoon": {
                                                "icon": "fa fa-search",
                                                "url": "https://preview.colorlib.com/theme/pexman/images/work-1.jpg"
                                            }
                                        },
                                        {
                                            "img": "https://images.ctfassets.net/hrltx12pl8hq/7yQR5uJhwEkRfjwMFJ7bUK/dc52a0913e8ff8b5c276177890eb0129/offset_comp_772626-opt.jpg?fit=fill&w=800&h=300",
                                            "teks": {
                                                "teksJudul": "Hark Website",
                                                "teksJudul1": "Web Design,Branding"
                                            },
                                            "butoon": {
                                                "icon": "fa fa-search",
                                                "url": "https://preview.colorlib.com/theme/pexman/images/work-1.jpg"
                                            }
                                        },
                                        {
                                            "img": "https://images.ctfassets.net/hrltx12pl8hq/7yQR5uJhwEkRfjwMFJ7bUK/dc52a0913e8ff8b5c276177890eb0129/offset_comp_772626-opt.jpg?fit=fill&w=800&h=300",
                                            "teks": {
                                                "teksJudul": "Hark Website",
                                                "teksJudul1": "Web Design,Branding"
                                            },
                                            "butoon": {
                                                "icon": "fa fa-search",
                                                "url": "https://preview.colorlib.com/theme/pexman/images/work-1.jpg"
                                            }
                                        }
                                    ]
                                }
                            },
                            {
                                "testimoni": {
                                    "teks": {
                                        "teksJudul": "Testimoni",
                                        "teksJudul1": "What Are Clients Says",
                                        "teksParagraf": "Far far away, behind th word mountains, far from the countries Vokalia and Consonatia, there live blind texts",
                                        "tekSpanJudul": "Roger Scott",
                                        "tekSpan": "Cheif Executive Officer @pexman"
                                    },
                                    "img": "https://c4.wallpaperflare.com/wallpaper/39/346/426/digital-art-men-city-futuristic-night-hd-wallpaper-thumb.jpg",
                                    "icon": "fa fa-star"
                                }
                            },
                            {
                                "ourLatesBlog": {
                                    "teks": {
                                        "teksJudul": "Read Lates News",
                                        "teksJudul1": "Our Lates Blog"
                                    },
                                    "fotoOurLatesBlog": [
                                        {
                                            "img": "https://c4.wallpaperflare.com/wallpaper/39/346/426/digital-art-men-city-futuristic-night-hd-wallpaper-thumb.jpg",
                                            "url": "https://preview.colorlib.com/theme/pexman/blog-single.html",
                                            "teks": {
                                                "teksDate": {
                                                    "icon": "fa fa-calendar",
                                                    "teks": "OCT.27,2020"
                                                },
                                                "teksJudul": "Far far away, behind the word mountain",
                                                "teksParagraf": "Far far away, behind th word mountains, far from the countries"
                                            }
                                        },
                                        {
                                            "img": "https://c4.wallpaperflare.com/wallpaper/39/346/426/digital-art-men-city-futuristic-night-hd-wallpaper-thumb.jpg",
                                            "url": "https://preview.colorlib.com/theme/pexman/blog-single.html",
                                            "teks": {
                                                "teksDate": {
                                                    "icon": "fa fa-calendar",
                                                    "teks": "OCT.27,2020"
                                                },
                                                "teksJudul": "Far far away, behind the word mountain",
                                                "teksParagraf": "Far far away, behind th word mountains, far from the countries"
                                            }
                                        },
                                        {
                                            "img": "https://c4.wallpaperflare.com/wallpaper/39/346/426/digital-art-men-city-futuristic-night-hd-wallpaper-thumb.jpg",
                                            "url": "https://preview.colorlib.com/theme/pexman/blog-single.html",
                                            "teks": {
                                                "teksDate": {
                                                    "icon": "fa fa-calendar",
                                                    "teks": "OCT.27,2020"
                                                },
                                                "teksJudul": "Far far away, behind the word mountain",
                                                "teksParagraf": "Far far away, behind th word mountains, far from the countries"
                                            }
                                        },
                                        {
                                            "img": "https://c4.wallpaperflare.com/wallpaper/39/346/426/digital-art-men-city-futuristic-night-hd-wallpaper-thumb.jpg",
                                            "url": "https://preview.colorlib.com/theme/pexman/blog-single.html",
                                            "teks": {
                                                "teksDate": {
                                                    "icon": "fa fa-calendar",
                                                    "teks": "OCT.27,2020"
                                                },
                                                "teksJudul": "Far far away, behind the word mountain",
                                                "teksParagraf": "Far far away, behind th word mountains, far from the countries"
                                            }
                                        }
                                    ]
                                }
                            }
                        ]
                    }
        elif (element == 'footer'):
            if (args.jenisElement != None and args.jenisElement == 'footer'):
                if (args.element != None and args.element == 'footerleft'):
                    return {
                        "footerleft": {
                            "teks": {
                                "teksJudul": "Pexman",
                                "teksParagraf": "Far far away, behind th word mountains, far from the countries Vokalia and Consonatia, there live blind texts"
                            },
                            "connectWithUs": {
                                "teks": "Connect with us",
                                "sosialMedia": [
                                    {
                                        "icon": "fa fa-twitter",
                                        "url": "https://preview.colorlib.com/theme/pexman/#"
                                    },
                                    {
                                        "icon": "fa fa-facebook",
                                        "url": "https://preview.colorlib.com/theme/pexman/#"
                                    },
                                    {
                                        "icon": "fa fa-instagram",
                                        "url": "https://preview.colorlib.com/theme/pexman/#"
                                    }
                                ]
                            }
                        }
                    }
                elif (args.element != None and args.element == 'footercenter'):
                    return {
                        "footercenter": {
                            "teks": "Navigation",
                            "content": [
                                {
                                    "teks": "Home",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "teks": "Sevices",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "teks": "Work",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "teks": "About",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "teks": "Blog",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "teks": "Press",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "teks": "Blog",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "teks": "Contact",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "teks": "Support",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "teks": "Privacy",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                }
                            ]
                        }
                    }
                elif (args.element != None and args.element == 'footerright'):
                    return {
                        "footerright": {
                            "teks": "Have a Question?",
                            "contactsUs": [
                                {
                                    "icon": "icon fa fa-map marker",
                                    "teks": "203 Fake St. Mountain View, San Francisco, California, Usa"
                                },
                                {
                                    "icon": "icon fa fa-phone",
                                    "teks": "+2 392 3929 210"
                                },
                                {
                                    "icon": "icon fa fa-paper-plane",
                                    "teks": "info@yourdomain.com"
                                }
                            ]
                        }
                    }
                else:
                    return {
                        "footer": [
                            {
                                "footerleft": {
                                    "teks": {
                                        "teksJudul": "Pexman",
                                        "teksParagraf": "Far far away, behind th word mountains, far from the countries Vokalia and Consonatia, there live blind texts"
                                    },
                                    "connectWithUs": {
                                        "teks": "Connect with us",
                                        "sosialMedia": [
                                            {
                                                "icon": "fa fa-twitter",
                                                "url": "https://preview.colorlib.com/theme/pexman/#"
                                            },
                                            {
                                                "icon": "fa fa-facebook",
                                                "url": "https://preview.colorlib.com/theme/pexman/#"
                                            },
                                            {
                                                "icon": "fa fa-instagram",
                                                "url": "https://preview.colorlib.com/theme/pexman/#"
                                            }
                                        ]
                                    }
                                }
                            },
                            {
                                "footercenter": {
                                    "teks": "Navigation",
                                    "content": [
                                        {
                                            "teks": "Home",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "teks": "Sevices",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "teks": "Work",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "teks": "About",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "teks": "Blog",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "teks": "Press",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "teks": "Blog",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "teks": "Contact",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "teks": "Support",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "teks": "Privacy",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        }
                                    ]
                                }
                            },
                            {
                                "footerright": {
                                    "teks": "Have a Question?",
                                    "contactsUs": [
                                        {
                                            "icon": "icon fa fa-map marker",
                                            "teks": "203 Fake St. Mountain View, San Francisco, California, Usa"
                                        },
                                        {
                                            "icon": "icon fa fa-phone",
                                            "teks": "+2 392 3929 210"
                                        },
                                        {
                                            "icon": "icon fa fa-paper-plane",
                                            "teks": "info@yourdomain.com"
                                        }
                                    ]
                                }
                            },
                            {
                                "footerbottom": {
                                    "teks": "Copyright ©2022 All rights reserved | This template is made with  by",
                                    "icon": "fa fa-heart color-danger",
                                    "teksSpan": "Colorlib"
                                }
                            }
                        ]
                    }
        else:
            return "not found"


class Page2(Resource):
    def get(self, element):
        parser = reqparse.RequestParser()
        parser.add_argument('jenisElement', choices=(
            'headers', 'body', 'footer'), help='jenis data tidak ditemukan: {error_msg}')
        parser.add_argument(
            'element', help='jenis data tidak ditemukan: {error_msg}')
        args = parser.parse_args()
        print(args)
        # validasi parameter
        if element == 'headers':
            # validasi argumen
            if (args.jenisElement != None and args.jenisElement == 'headers'):
                if (args.element != None and args.element == 'headerKiri'):
                    return {
                        "headerKiri": {
                            "teks": {
                                "teksIcon": "Pexman",
                                "teksSpan": "Agency",
                                "teksSpanSmall": "Creative"
                            },
                            "url": "https://preview.colorlib.com/theme/pexman/index.html"
                        }
                    }
                elif (args.element != None and args.element == 'headerKanan'):
                    return {
                        "headerKanan": [
                            {
                                "home": {
                                    "teks": "Home",
                                    "url": "https://preview.colorlib.com/theme/pexman/index.html"
                                }
                            },
                            {
                                "about": {
                                    "teks": "About",
                                    "url": "https://preview.colorlib.com/theme/pexman/about.html"
                                }
                            },
                            {
                                "work": {
                                    "teks": "Work",
                                    "url": "https://preview.colorlib.com/theme/pexman/work.html"
                                }
                            },
                            {
                                "blog": {
                                    "teks": "Blog",
                                    "url": "https://preview.colorlib.com/theme/pexman/blog.html"
                                }
                            },
                            {
                                "contact": {
                                    "teks": "Contact",
                                    "url": "https://preview.colorlib.com/theme/pexman/contact.html"
                                }
                            }
                        ]
                    }
                else:
                    return {
                        "headers": [
                            {
                                "headerKiri": {
                                    "teks": {
                                        "teksIcon": "Pexman",
                                        "teksSpan": "Agency",
                                        "teksSpanSmall": "Creative"
                                    },
                                    "url": "https://preview.colorlib.com/theme/pexman/index.html"
                                }
                            },
                            {
                                "headerKanan": [
                                    {
                                        "home": {
                                            "teks": "Home",
                                            "url": "https://preview.colorlib.com/theme/pexman/index.html"
                                        }
                                    },
                                    {
                                        "about": {
                                            "teks": "About",
                                            "url": "https://preview.colorlib.com/theme/pexman/about.html"
                                        }
                                    },
                                    {
                                        "work": {
                                            "teks": "Work",
                                            "url": "https://preview.colorlib.com/theme/pexman/work.html"
                                        }
                                    },
                                    {
                                        "blog": {
                                            "teks": "Blog",
                                            "url": "https://preview.colorlib.com/theme/pexman/blog.html"
                                        }
                                    },
                                    {
                                        "contact": {
                                            "teks": "Contact",
                                            "url": "https://preview.colorlib.com/theme/pexman/contact.html"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
        elif (element == 'body'):
            if (args.jenisElement != None and args.jenisElement == 'body'):
                if (args.element != None and args.element == 'banner'):
                    return {
                        "banner": {
                            "img": "https://c4.wallpaperflare.com/wallpaper/39/346/426/digital-art-men-city-futuristic-night-hd-wallpaper-thumb.jpg",
                            "teks": {
                                "tekslink": {
                                    "url": "https://preview.colorlib.com/theme/pexman/index.html",
                                    "teks": "Home"
                                },
                                "teksSpan": "About Us",
                                "teksJudul": "About Us"
                            }
                        }
                    }
                elif (args.element != None and args.element == 'welcomepexman'):
                    return {
                        "welcomepexman": {
                            "img": "https://c4.wallpaperflare.com/wallpaper/39/346/426/digital-art-men-city-futuristic-night-hd-wallpaper-thumb.jpg",
                            "teks": {
                                "teksJudul": "Welcome Pexman",
                                "teksJudul1": "We Are Creative Agency That Create Beautiful Website",
                                "teksParagraf": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.",
                                "button": {
                                    "teks": "Start A Project",
                                    "url": "https://preview.colorlib.com/theme/pexman/index.html#"
                                }
                            }
                        }
                    }
                else:
                    return {
                        "body": [
                            {
                                "banner": {
                                    "img": "https://c4.wallpaperflare.com/wallpaper/39/346/426/digital-art-men-city-futuristic-night-hd-wallpaper-thumb.jpg",
                                    "teks": {
                                        "tekslink": {
                                            "url": "https://preview.colorlib.com/theme/pexman/index.html",
                                            "teks": "Home"
                                        },
                                        "teksSpan": "About Us",
                                        "teksJudul": "About Us"
                                    }
                                }
                            },
                            {
                                "welcomepexman": {
                                    "img": "https://c4.wallpaperflare.com/wallpaper/39/346/426/digital-art-men-city-futuristic-night-hd-wallpaper-thumb.jpg",
                                    "teks": {
                                        "teksJudul": "Welcome Pexman",
                                        "teksJudul1": "We Are Creative Agency That Create Beautiful Website",
                                        "teksParagraf": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.",
                                        "button": {
                                            "teks": "Start A Project",
                                            "url": "https://preview.colorlib.com/theme/pexman/index.html#"
                                        }
                                    }
                                }
                            },
                            {
                                "keteranganProduct": [
                                    {
                                        "jumlah": 10,
                                        "teks": {
                                            "teksjumlah": "K+",
                                            "teksSpan": "Achievements"
                                        }
                                    },
                                    {
                                        "jumlah": 211,
                                        "teks": {
                                            "teksjumlah": "K+",
                                            "teksSpan": "Achievements"
                                        }
                                    },
                                    {
                                        "jumlah": 27,
                                        "teks": {
                                            "teksjumlah": "",
                                            "teksSpan": "Achievements"
                                        }
                                    },
                                    {
                                        "jumlah": 30,
                                        "teks": {
                                            "teksjumlah": "K+",
                                            "teksSpan": "Achievements"
                                        }
                                    }
                                ]
                            },
                            {
                                "team": {
                                    "teks": {
                                        "teksJudul": "Team",
                                        "teksJudul1": "Expert Team"
                                    },
                                    "anggota": [
                                        {
                                            "img": "https://c4.wallpaperflare.com/wallpaper/39/346/426/digital-art-men-city-futuristic-night-hd-wallpaper-thumb.jpg",
                                            "teks": {
                                                "teksJudul": "Luis Wilson",
                                                "teksJudul1": "Web Designer"
                                            },
                                            "sosialMedia": [
                                                {
                                                    "icon": "fa fa-twitter",
                                                    "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                                },
                                                {
                                                    "icon": "fa fa-facebook",
                                                    "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                                },
                                                {
                                                    "icon": "fa fa-google",
                                                    "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                                },
                                                {
                                                    "icon": "fa fa-instagram",
                                                    "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                                }
                                            ]
                                        },
                                        {
                                            "img": "https://c4.wallpaperflare.com/wallpaper/39/346/426/digital-art-men-city-futuristic-night-hd-wallpaper-thumb.jpg",
                                            "teks": {
                                                "teksJudul": "Luis Wilson",
                                                "teksJudul1": "Web Designer"
                                            },
                                            "sosialMedia": [
                                                {
                                                    "icon": "fa fa-twitter",
                                                    "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                                },
                                                {
                                                    "icon": "fa fa-facebook",
                                                    "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                                },
                                                {
                                                    "icon": "fa fa-google",
                                                    "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                                },
                                                {
                                                    "icon": "fa fa-instagram",
                                                    "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                                }
                                            ]
                                        },
                                        {
                                            "img": "https://c4.wallpaperflare.com/wallpaper/39/346/426/digital-art-men-city-futuristic-night-hd-wallpaper-thumb.jpg",
                                            "teks": {
                                                "teksJudul": "Luis Wilson",
                                                "teksJudul1": "Web Designer"
                                            },
                                            "sosialMedia": [
                                                {
                                                    "icon": "fa fa-twitter",
                                                    "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                                },
                                                {
                                                    "icon": "fa fa-facebook",
                                                    "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                                },
                                                {
                                                    "icon": "fa fa-google",
                                                    "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                                },
                                                {
                                                    "icon": "fa fa-instagram",
                                                    "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                                }
                                            ]
                                        },
                                        {
                                            "img": "https://c4.wallpaperflare.com/wallpaper/39/346/426/digital-art-men-city-futuristic-night-hd-wallpaper-thumb.jpg",
                                            "teks": {
                                                "teksJudul": "Luis Wilson",
                                                "teksJudul1": "Web Designer"
                                            },
                                            "sosialMedia": [
                                                {
                                                    "icon": "fa fa-twitter",
                                                    "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                                },
                                                {
                                                    "icon": "fa fa-facebook",
                                                    "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                                },
                                                {
                                                    "icon": "fa fa-google",
                                                    "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                                },
                                                {
                                                    "icon": "fa fa-instagram",
                                                    "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            },
                            {
                                "testimoni": {
                                    "teks": {
                                        "teksJudul": "Testimoni",
                                        "teksJudul1": "What Are Clients Says",
                                        "teksParagraf": "Far far away, behind th word mountains, far from the countries Vokalia and Consonatia, there live blind texts",
                                        "tekSpanJudul": "Roger Scott",
                                        "tekSpan": "Cheif Executive Officer @pexman"
                                    },
                                    "img": "https://c4.wallpaperflare.com/wallpaper/39/346/426/digital-art-men-city-futuristic-night-hd-wallpaper-thumb.jpg",
                                    "icon": "fa fa-star"
                                }
                            }
                        ]
                    }
        elif (element == 'footer'):
            if (args.jenisElement != None and args.jenisElement == 'footer'):
                if (args.element != None and args.element == 'footerleft'):
                    return {
                        "footerleft": {
                            "teks": {
                                "teksJudul": "Pexman",
                                "teksParagraf": "Far far away, behind th word mountains, far from the countries Vokalia and Consonatia, there live blind texts"
                            },
                            "connectWithUs": {
                                "teks": "Connect with us",
                                "sosialMedia": [
                                    {
                                        "icon": "fa fa-twitter",
                                        "url": "https://preview.colorlib.com/theme/pexman/#"
                                    },
                                    {
                                        "icon": "fa fa-facebook",
                                        "url": "https://preview.colorlib.com/theme/pexman/#"
                                    },
                                    {
                                        "icon": "fa fa-instagram",
                                        "url": "https://preview.colorlib.com/theme/pexman/#"
                                    }
                                ]
                            }
                        }
                    }
                elif (args.element != None and args.element == 'footercenter'):
                    return {
                        "footercenter": {
                            "teks": "Navigation",
                            "content": [
                                {
                                    "teks": "Home",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "teks": "Sevices",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "teks": "Work",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "teks": "About",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "teks": "Blog",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "teks": "Press",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "teks": "Blog",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "teks": "Contact",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "teks": "Support",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "teks": "Privacy",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                }
                            ]
                        }
                    }
                elif (args.element != None and args.element == 'footerright'):
                    return {
                        "footerright": {
                            "teks": "Have a Question?",
                            "contactsUs": [
                                {
                                    "icon": "icon fa fa-map marker",
                                    "teks": "203 Fake St. Mountain View, San Francisco, California, Usa"
                                },
                                {
                                    "icon": "icon fa fa-phone",
                                    "teks": "+2 392 3929 210"
                                },
                                {
                                    "icon": "icon fa fa-paper-plane",
                                    "teks": "info@yourdomain.com"
                                }
                            ]
                        }
                    }
                else:
                    return {
                        "footer": [
                            {
                                "footerleft": {
                                    "teks": {
                                        "teksJudul": "Pexman",
                                        "teksParagraf": "Far far away, behind th word mountains, far from the countries Vokalia and Consonatia, there live blind texts"
                                    },
                                    "connectWithUs": {
                                        "teks": "Connect with us",
                                        "sosialMedia": [
                                            {
                                                "icon": "fa fa-twitter",
                                                "url": "https://preview.colorlib.com/theme/pexman/#"
                                            },
                                            {
                                                "icon": "fa fa-facebook",
                                                "url": "https://preview.colorlib.com/theme/pexman/#"
                                            },
                                            {
                                                "icon": "fa fa-instagram",
                                                "url": "https://preview.colorlib.com/theme/pexman/#"
                                            }
                                        ]
                                    }
                                }
                            },
                            {
                                "footercenter": {
                                    "teks": "Navigation",
                                    "content": [
                                        {
                                            "teks": "Home",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "teks": "Sevices",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "teks": "Work",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "teks": "About",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "teks": "Blog",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "teks": "Press",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "teks": "Blog",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "teks": "Contact",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "teks": "Support",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "teks": "Privacy",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        }
                                    ]
                                }
                            },
                            {
                                "footerright": {
                                    "teks": "Have a Question?",
                                    "contactsUs": [
                                        {
                                            "icon": "icon fa fa-map marker",
                                            "teks": "203 Fake St. Mountain View, San Francisco, California, Usa"
                                        },
                                        {
                                            "icon": "icon fa fa-phone",
                                            "teks": "+2 392 3929 210"
                                        },
                                        {
                                            "icon": "icon fa fa-paper-plane",
                                            "teks": "info@yourdomain.com"
                                        }
                                    ]
                                }
                            },
                            {
                                "footerbottom": {
                                    "teks": "Copyright ©2022 All rights reserved | This template is made with  by",
                                    "icon": "fa fa-heart color-danger",
                                    "teksSpan": "Colorlib"
                                }
                            }
                        ]
                    }
        else:
            return "not found"


#
# Get All Books
# api.add_resource(All, '/api/v1/page1')
# api.add_resource(ops, '/api/v1/page2')
api.add_resource(Page1, '/api/v1/home/<string:element>/')
api.add_resource(Page2, '/api/v1/about/<string:element>/')


@app.route('/')
def index():
    return 'API Tutorials with Flask.eg /api/v1/home'


# Using JSONIFY ERROR
@app.errorhandler(404)
def not_found(error):
    return (jsonify({'error': 'Not Found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
