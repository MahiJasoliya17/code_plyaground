# from django import template
# from home.models import UserProfile
# register = template.Library()

# @register.filter
# def get_item(dictionary, key, user):
#     if dictionary is None:
#         return None
#     return dictionary.get(key)

# def get_profile_pic(user):
#     try:
#         return user.userprofile.profile_pic.url
#     except:
#         return '/media/profile_pics/default_user.png'  # fallback if none


from django import template
from home.models import UserProfile

register = template.Library()

@register.filter
def get_profile_pic(user):
    try:
        return user.profile.profile_pic.url
    except:
        return '/media/profile_pics/default_user.png'  # fallback

@register.filter
def get_item(dictionary, key):
    if dictionary is None:
        return None
    return dictionary.get(key)
