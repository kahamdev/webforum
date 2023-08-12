from django.db import models
from django.contrib.auth.models import User


# javascript questions bundle list
class JavaScriptQuestion1(models.Model):
      qns=models.CharField(max_length=200)
      opt1=models.CharField(max_length=200)
      opt2=models.CharField(max_length=200)
      opt3=models.CharField(max_length=200)
      opt4=models.CharField(max_length=200)
      ans=models.CharField(max_length=200)

      def __str__(self):
          return self.qns

class JavaScriptQuestion2(models.Model):
      qns=models.CharField(max_length=200)
      opt1=models.CharField(max_length=200)
      opt2=models.CharField(max_length=200)
      opt3=models.CharField(max_length=200)
      opt4=models.CharField(max_length=200)
      ans=models.CharField(max_length=200)

      def __str__(self):
          return self.qns

class JavaScriptQuestion3(models.Model):
      qns=models.CharField(max_length=200)
      opt1=models.CharField(max_length=200)
      opt2=models.CharField(max_length=200)
      opt3=models.CharField(max_length=200)
      opt4=models.CharField(max_length=200)
      ans=models.CharField(max_length=200)

      def __str__(self):
          return self.qns

class JavaScriptQuestion4(models.Model):
      qns=models.CharField(max_length=200)
      opt1=models.CharField(max_length=200)
      opt2=models.CharField(max_length=200)
      opt3=models.CharField(max_length=200)
      opt4=models.CharField(max_length=200)
      ans=models.CharField(max_length=200)

      def __str__(self):
          return self.qns


# javascript createprofile model
class JavascriptCreateProfile(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=30)
	phone=models.IntegerField()
	title=models.CharField(max_length=100)
	description=models.TextField()
	image=models.ImageField(upload_to='JavascriptProfile Images/')
    

	class Meta:
		db_table='JavascriptCreateProfile'

	def __str__(self):
		return f'{self.name} Profile'

# javascript video post model
class JavascriptVideoPost(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    video=models.FileField(upload_to='javascriptVideo/')
    create_at=models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return f'{self.user.username} Posted'



# meet javascript expert model
class MeetJavascriptExpert(models.Model):
	name=models.CharField(max_length=100,null=True,blank=True)
	time=models.DateTimeField(auto_now_add=True,null=True,blank=True)
	screenshot=models.ImageField(upload_to='MeetJavascript Images/',null=True,blank=True)
	message=models.TextField(max_length=1000)

	class Meta:
		db_table='MeetJavascriptExpert'

	def __str__(self):
		return self.message



# php questions bundle list
class PhpQuestion1(models.Model):
      qns=models.CharField(max_length=200)
      opt1=models.CharField(max_length=200)
      opt2=models.CharField(max_length=200)
      opt3=models.CharField(max_length=200)
      opt4=models.CharField(max_length=200)
      ans=models.CharField(max_length=200)

      def __str__(self):
          return self.qns

class PhpQuestion2(models.Model):
      qns=models.CharField(max_length=200)
      opt1=models.CharField(max_length=200)
      opt2=models.CharField(max_length=200)
      opt3=models.CharField(max_length=200)
      opt4=models.CharField(max_length=200)
      ans=models.CharField(max_length=200)

      def __str__(self):
          return self.qns

class PhpQuestion3(models.Model):
      qns=models.CharField(max_length=200)
      opt1=models.CharField(max_length=200)
      opt2=models.CharField(max_length=200)
      opt3=models.CharField(max_length=200)
      opt4=models.CharField(max_length=200)
      ans=models.CharField(max_length=200)

      def __str__(self):
          return self.qns


class PhpQuestion4(models.Model):
      qns=models.CharField(max_length=200)
      opt1=models.CharField(max_length=200)
      opt2=models.CharField(max_length=200)
      opt3=models.CharField(max_length=200)
      opt4=models.CharField(max_length=200)
      ans=models.CharField(max_length=200)

      def __str__(self):
          return self.qns


# phpcreateprofile model
class PhpCreateProfile(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=30)
	phone=models.IntegerField()
	title=models.CharField(max_length=100)
	description=models.TextField()
	image=models.ImageField(upload_to='PhpProfile Images/')

	class Meta:
		db_table='PhpCreateProfile'

	def __str__(self):
		return f'{self.name} Profile'

# php video post model
class PhpVideoPost(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    video=models.FileField(upload_to='phpVideo/')
    create_at=models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return f'{self.user.username} Posted'



# meetphpexpert model
class MeetPhpExpert(models.Model):
	name=models.CharField(max_length=100,null=True,blank=True)
	time=models.DateTimeField(auto_now_add=True,null=True,blank=True)
	screenshot=models.ImageField(upload_to='MeetPhp Images/',null=True,blank=True)
	message=models.TextField(max_length=1000)

	class Meta:
		db_table='MeetPhpExpert'

	def __str__(self):
		return self.message


      
    