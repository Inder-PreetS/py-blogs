import requests
from geopy.geocoders import Nominatim
import geocoder
from blogapp.models import Blog

# calling the Nominatim tool
def get_ip():
    loc = Nominatim(user_agent="GetLoc")
    ip = requests.get('http://ipinfo.io/json').json()['ip']

    g = geocoder.ipinfo(ip) 
    return g[0].state

def likeByUser(request):
    if request.method == 'POST':
        blog_id = request.POST.get('blog_id')
        blog_obj = Blog.objects.filter(id=blog_id)
        blog_obj.update(like=blog_obj.values()[0]['like']+1) 
        return blog_obj

