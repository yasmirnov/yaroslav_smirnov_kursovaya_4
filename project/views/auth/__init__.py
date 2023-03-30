from .auth import api as auth_ns
from project.views.auth.user import user_ns

__all__ = [
    'auth_ns',
    'user_ns',
]
