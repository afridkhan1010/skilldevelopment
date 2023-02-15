import string
import random
from django.http import HttpResponse

def randomString(stringLength=20):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
print(randomString())
name='linkgenaration'

def generate_link(req):
    the_string = randomString(stringLength=20)
    # OneTimeLinkModel.objects.create(one_time_code=the_string)
    one_time_code=the_string
    return HttpResponse('<a href="/polls/one_time_link/{}">{}{}</a>'.format(the_string, req.build_absolute_uri(), the_string))
print(generate_link(name))
