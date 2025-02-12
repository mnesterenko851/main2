from functools import wraps

def require_user_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if not hasattr(user, "role") or user.role != role:
                raise PermissionError(f"Access denied: required role '{role}'")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

@require_user_role("admin")
def admin_panel(user):
    return f"Welcome to the admin panel, {user.name}!"

admin = User("Alice", "admin")
guest = User("Bob", "guest")

print(admin_panel(admin))  

try:
    print(admin_panel(guest))  
except PermissionError as e:
    print(e)
