def is_admin(user):
    # Return True if the user has admin privileges
    return user.is_staff  # or add custom logic here


def is_librarian(user):
    # Define your librarian check logic
    return user.groups.filter(name="Librarian").exists()


def is_member(user):
    # Define your member check logic
    return user.groups.filter(name="Member").exists()
