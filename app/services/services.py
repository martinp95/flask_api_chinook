# app/services/services.py
"""
Service layer for business logic and database access related to Artists and Albums.
"""

from typing import List, Tuple
from flask import current_app
from sqlalchemy import func
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound

from app import db
from app.models.models import Artist, Album, Track


def get_all_artists(page: int, per_page: int) -> Tuple[List[Artist], int]:
    """
    Retrieve a paginated list of artists from the database.
    """
    current_app.logger.info(f"Fetching artists (page={page}, per_page={per_page})")

    query = (
        db.session.query(Artist)
        .order_by(Artist.ArtistId)
        .paginate(page=page, per_page=per_page, error_out=False)
    )

    return query.items, query.total


def get_all_albums_with_tracks(page: int, per_page: int) -> Tuple[List[Album], int]:
    """
    Retrieve a paginated list of albums with their associated tracks.
    """
    current_app.logger.info(
        f"Fetching albums with tracks (page={page}, per_page={per_page})"
    )

    query = (
        db.session.query(Album)
        .options(joinedload(Album.tracks))
        .order_by(Album.AlbumId)
        .paginate(page=page, per_page=per_page, error_out=False)
    )

    return query.items, query.total


def get_albums_by_artist(artist_id: int) -> List[Album]:
    """
    Retrieve all albums for a given artist.
    """
    current_app.logger.info(f"Fetching albums for artist {artist_id}")

    artist = db.session.get(Artist, artist_id)
    if not artist:
        raise NotFound(f"Artist with ID {artist_id} not found.")

    return artist.albums


def get_tracks_by_album(album_id: int) -> List[Track]:
    """
    Retrieve all tracks for a given album.
    """
    current_app.logger.info(f"Fetching tracks for album {album_id}")

    album = db.session.get(Album, album_id)
    if not album:
        raise NotFound(f"Album with ID {album_id} not found.")

    return album.tracks


def get_album_summaries() -> list:
    """
    Retrieve a list of albums with artist name and total number of tracks.
    """
    current_app.logger.info("Fetching album summaries with aggregated track count.")

    return (
        db.session.query(
            Album.AlbumId,
            Album.Title.label("AlbumTitle"),
            Artist.Name.label("ArtistName"),
            func.count(Track.TrackId).label("TrackCount"),
        )
        .join(Artist, Album.ArtistId == Artist.ArtistId)
        .join(Track, Track.AlbumId == Album.AlbumId)
        .group_by(Album.AlbumId, Album.Title, Artist.Name)
        .order_by(Album.AlbumId)
        .all()
    )
