from .models import PropertyImage, Property


def save_photos(property: Property, photos: list) -> None:
    # Set the first photos as the primary photo that will be shown on the list page
    for i, photo in enumerate(photos):
        if i == 0:
            is_primary = True
        else:
            is_primary = False
        PropertyImage.objects.create(property=property, images=photo, is_primary=is_primary)
