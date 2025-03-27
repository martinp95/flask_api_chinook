# app/schemas/albums_summary_schema.py
"""
Marshmallow schema for serializing album summary data,
including album title, artist name, and total track count.
"""

from app import ma


class AlbumSummarySchema(ma.Schema):
    """
    Schema for aggregated album summary data.

    Used to serialize query results that include:
    - Album ID
    - Album title
    - Artist name
    - Total number of tracks
    """

    AlbumId = ma.Integer(required=True, dump_only=True)
    AlbumTitle = ma.String(required=True)
    ArtistName = ma.String(required=True)
    TrackCount = ma.Integer(required=True)
