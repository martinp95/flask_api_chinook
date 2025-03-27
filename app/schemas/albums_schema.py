# app/schemas/albums_schema.py
"""
Marshmallow schema for serializing and deserializing Album model data,
including its related tracks.
"""

from app import ma
from app.models.models import Album
from app.schemas.track_schema import TrackSchema


class AlbumSchema(ma.SQLAlchemyAutoSchema):
    """
    Schema for the Album model with optional nested tracks.
    """

    tracks = ma.Nested(TrackSchema, many=True)

    class Meta:
        model = Album
        load_instance = True  # Enables .load(...) → Album()
        include_fk = True  # Include foreign keys like ArtistId if needed
        # Explicitly define exposed fields
        fields = ("AlbumId", "Title", "tracks")

        def __init__(self, *args, only=None, **kwargs):
            """
            Allow passing 'only' to limit fields dynamically.
            """
            if only:
                kwargs["only"] = only
            super().__init__(*args, **kwargs)
