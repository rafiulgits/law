from rest_framework.permissions import BasePermission

class IsStaffUser(BasePermission):
	"""
	Allow access only to `is_staff` users
	"""
	def has_permission(self, request, view):
		return request.user.is_staff



class IsStaffForManaging(BasePermission):
	"""
	Allow general user to access `GET` method
	Others methods could be accessed by `is_staff` user
	"""
	def has_permission(self, request, view):
		if request.method == 'GET':
			return True
		else:
			return request.user.is_staff