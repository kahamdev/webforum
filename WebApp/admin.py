from django.contrib import admin

# we import our models here.
from .models import PhpCreateProfile,MeetPhpExpert,JavascriptCreateProfile,MeetJavascriptExpert
from .models import JavaScriptQuestion1,JavaScriptQuestion2,JavaScriptQuestion3,JavaScriptQuestion4
from .models import PhpVideoPost,JavascriptVideoPost
from .models import PhpQuestion1,PhpQuestion2,PhpQuestion3,PhpQuestion4

# php model here.
admin.site.register(PhpCreateProfile)
admin.site.register(MeetPhpExpert)

# javascript model here.
admin.site.register(JavascriptCreateProfile)
admin.site.register(MeetJavascriptExpert)



# Javascript questions models
admin.site.register(JavaScriptQuestion1)
admin.site.register(JavaScriptQuestion2)
admin.site.register(JavaScriptQuestion3)
admin.site.register(JavaScriptQuestion4)


# Php questions models
admin.site.register(PhpQuestion1)
admin.site.register(PhpQuestion2)
admin.site.register(PhpQuestion3)
admin.site.register(PhpQuestion4)


#register php video post
admin.site.register(PhpVideoPost)


#register javascript video post
admin.site.register(JavascriptVideoPost)











