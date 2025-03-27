# app/schemas/artist_schema.py
"""
Marshmallow schema for serializing and deserializing Artist model data.
"""

from app import ma
from app.models.models import Artist


class ArtistSchema(ma.SQLAlchemyAutoSchema):
    """
    Schema for the Artist model, used for both serialization and deserialization
    of artist data via Marshmallow.
    """

    class Meta:
        model = Artist
        load_instance = True  # Enables .load(...) → Artist()
        # Enables foreign key fields (if present)
        include_fk = True
        # Limits the serialized/deserialized fields
        fields = ("ArtistId", "Name")
