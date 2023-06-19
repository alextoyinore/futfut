from django.contrib.auth.models import UserManager

class FutUserManager(UserManager):
    use_in_migrations = True

    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('Username is required')
        extra_fields.setdefault('age', 0)
        return create_user(username, email, password, **extra_fields)

    def create_super_user(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must set is_staff to true')
        
        return self.create_user(username, email, password, **extra_fields)

