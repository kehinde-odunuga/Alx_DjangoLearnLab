from .models import UserProfile


def is_admin(user):
    if not user.is_authenticated:
        return False
    return UserProfile.objects.filter(user=user, role='Admin').exists()


def is_librarian(user):
    # Define your librarian check logic
    return user.groups.filter(name="Librarian").exists()


def is_member(user):
    # Define your member check logic
    return user.groups.filter(name="Member").exists()
