# app/schemas/track_schema.py
"""
Marshmallow schema for serializing and deserializing Track model data.
"""

from app import ma
from app.models.models import Track


class TrackSchema(ma.SQLAlchemyAutoSchema):
    """
    Schema for the Track model, used for both serialization (output)
    and deserialization (input) of track data.
    """

    class Meta:
        model = Track
        load_instance = True  # Enables .load(...) → Track()
        include_fk = True  # Include foreign key fields if needed
        fields = ("TrackId", "Name")  # Explicit field control
