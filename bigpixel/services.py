from django.contrib.auth.models import User
from django.db import transaction, IntegrityError, DatabaseError

from bigpixel.models import PixelTrackingCode, PixelTrackingCodeSite
from helpers.generators import alphanumerical_generator


def create_user_pixel_tracking_code(*,
                                    user: User
                                    ):
    try:
        with transaction.atomic():
            return PixelTrackingCode.objects.create(
                user=user,
                tracking_code=alphanumerical_generator(16))
    except IntegrityError as e:
        return False
    except DatabaseError as e:
        return False


def validate_user_pixel_tracking_code(*,
                                      pixel_tracking_code: PixelTrackingCode,
                                      website: str,
                                      ping_result: str
                                      ):
    try:
        with transaction.atomic():
            # update main tracking code to ping_result status
            pixel_tracking_code.tracking_code_status = ping_result
            pixel_tracking_code.save()

            # update continuous website validation status
            return PixelTrackingCodeSite.objects.create(tracking_code=pixel_tracking_code,
                                                        website=website,
                                                        integration_status=ping_result)
    except IntegrityError as e:
        return False
    except DatabaseError as e:
        return False
