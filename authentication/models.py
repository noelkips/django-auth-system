from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager

class UserAccountManager(BaseUserManager):
	def _create_user(self, email, password, first_name, last_name,mobile, **extra_fields):
		if not email:
			raise ValueError("Email must be provided")
		if not password:
			raise ValueError("Password must be provided")
		user = self.model(
        	email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
	    	mobile = mobile,
            **extra_fields
        )
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self , email, password, first_name, last_name, mobile,  **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_active', True)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, first_name, last_name, mobile, **extra_fields)

	
	def create_superuser(self , email, password, first_name, last_name, mobile,  **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_active', True)
		extra_fields.setdefault('is_superuser', True)
		return self._create_user(email, password, first_name, last_name, mobile, **extra_fields)
	
class UserAccount(AbstractBaseUser):
	class Types(models.TextChoices):
		USER = "USER" , "user"
		STAFF = "STAFF" , "staff"
		ADMIN = "ADMIN" , "admin"
		
	type = models.CharField(max_length = 20, choices = Types.choices ,
							# Default is user is officer
							default = Types.ADMIN)
	email = models.EmailField(max_length = 200 , unique = True)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	is_active = models.BooleanField(default = True)
	is_staff = models.BooleanField(default = False)
	is_superuser = models.BooleanField(default = False)
	mobile = models.CharField(max_length=13, unique=True, verbose_name='Phone Number')
	
	#custom 
    
	user = models.BooleanField(default = False)
	staff = models.BooleanField(default = False)
	
	
	USERNAME_FIELD = "mobile"

	REQUIRED_FIELDS = ['first_name', 'last_name', 'email']
	
	# defining the manager for the UserAccount model
	objects = UserAccountManager()
	
	def __str__(self):
		return str(self.first_name)
	
	def has_perm(self , perm, obj = None):
		return self.is_superuser
	
	def has_module_perms(self , app_label):
		return True
	
	def save(self , *args , **kwargs):
		if not self.type or self.type == None :
			self.type = UserAccount.Types.ADMIN
		return super().save(*args , **kwargs)


#CUSTOM normal user MODELS
class UserManager(models.Manager):
	def create_user(self , email , first_name, last_name, mobile,  password = None):
		if not email or len(email) <= 0 :
			raise ValueError("Email field is required !")
		if not password :
			raise ValueError("Password is must !")
		email = email.lower()
		user = self.model(
			email = email,
			first_name = first_name,
			last_name = last_name,
			mobile = mobile,
		)
		
		user.set_password(password)
		user.save(using = self._db)
		return user
	
	def get_queryset(self , *args, **kwargs):
		queryset = super().get_queryset(*args , **kwargs)
		queryset = queryset.filter(type = UserAccount.Types.ADMIN)
		return queryset	
		
class User(UserAccount):
	class Meta :
		proxy = True
	objects = UserManager()
	
	def save(self , *args , **kwargs):
		self.type = UserAccount.Types.USER
		self.user = True
		return super().save(*args , **kwargs)
	
class StaffManager(models.Manager):
	def create_user(self , email , first_name, last_name, mobile,  password = None):
		if not email or len(email) <= 0 :
			raise ValueError("Email field is required !")
		if not password :
			raise ValueError("Password is must !")
		email = email.lower()
		user = self.model(
			email = email,
			first_name = first_name,
			last_name = last_name,
			mobile = mobile,
		)
		user.staff = True
		user.set_password(password)
		user.save(using = self._db)
		return user
		
	def get_queryset(self , *args , **kwargs):
		queryset = super().get_queryset(*args , **kwargs)
		queryset = queryset.filter(type = UserAccount.Types.STAFF)
		return queryset
	
class Staff(UserAccount):
	class Meta :
		proxy = True
	objects = StaffManager()
	
	def save(self , *args , **kwargs):
		self.type = UserAccount.Types.STAFF
		self.staff = True
		return super().save(*args , **kwargs)
