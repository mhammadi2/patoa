from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from  .models import Patent

# @receiver(post_save,sender=User)    
# def build_profile(sender,instance,created, **kwargs):
#     if created:
#         Patent.objects.create(user_name=instance)
#         print('print patent profile created')


# @receiver(post_save,sender=User) 
# def update_profile(sender,instance,created, **kwargs):

#     if created == False:
#         instance.patent.save()
#         print('Patent updated')
    
