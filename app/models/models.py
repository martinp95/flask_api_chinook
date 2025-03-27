# app/models/models.py
"""
Database models for the Chinook API application.
"""

from app import db


class Artist(db.Model):
    """
    SQLAlchemy model representing an artist in the Chinook database.
    """

    __tablename__ = "artists"

    ArtistId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(120), nullable=False)

    # One-to-many: an artist can have multiple albums
    albums = db.relationship("Album", backref="artist", lazy=True)

    def __repr__(self) -> str:
        return f"<Artist {self.ArtistId}: {self.Name}>"

    def __str__(self) -> str:
        return self.Name


class Album(db.Model):
    """
    SQLAlchemy model representing an album in the Chinook database.
    """

    __tablename__ = "albums"

    AlbumId = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(160), nullable=False)

    # Many-to-one: each album belongs to a single artist
    ArtistId = db.Column(db.Integer, db.ForeignKey("artists.ArtistId"), nullable=False)

    # One-to-many: an album can have multiple tracks
    tracks = db.relationship("Track", backref="album", lazy=True)

    def __repr__(self) -> str:
        return f"<Album {self.AlbumId}: {self.Title}>"

    def __str__(self) -> str:
        return self.Title


class Track(db.Model):
    """
    SQLAlchemy model representing a track in the Chinook database.
    """

    __tablename__ = "tracks"

    TrackId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(200), nullable=False)
    MediaTypeId = db.Column(db.Integer, nullable=False)
    GenreId = db.Column(db.Integer)
    Composer = db.Column(db.String(220))
    Milliseconds = db.Column(db.Integer, nullable=False)
    Bytes = db.Column(db.Integer)
    UnitPrice = db.Column(db.Numeric(10, 2), nullable=False)

    # Many-to-one: each track belongs to a single album
    AlbumId = db.Column(db.Integer, db.ForeignKey("albums.AlbumId"), nullable=False)

    def __repr__(self) -> str:
        return f"<Track {self.TrackId}: {self.Name}>"

    def __str__(self) -> str:
        return self.Name
