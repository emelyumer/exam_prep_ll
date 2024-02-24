from exam_prep_ll.profiles.models import Profile


def get_profile():
    return Profile.objects.first()