from ekyc.viewsets import StudentViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('viewstudent',StudentViewset)
