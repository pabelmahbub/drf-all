from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)
    
    #It is used is ReviewDetail. Only admin can access PUT,DELETE api: others can read it:
    # class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [AdminOrReadOnly]
    
   
#permission to those who post to PUT,DELETE other will ReadOnly    
class IsReviewUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.review_user == request.user or request.user.is_staff