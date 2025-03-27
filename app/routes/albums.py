# app/routes/albums.py
"""
Albums API routes for listing albums and their associated tracks or summary data.
"""

from flask import Blueprint, jsonify, request
from werkzeug.exceptions import NotFound

from app.services.services import (
    get_all_albums_with_tracks,
    get_tracks_by_album,
    get_album_summaries,
)
from app.schemas.albums_schema import AlbumSchema
from app.schemas.track_schema import TrackSchema
from app.schemas.albums_summary_schema import AlbumSummarySchema

albums_bp = Blueprint("albums", __name__)
album_schema = AlbumSchema(many=True)
track_schema = TrackSchema(many=True)
album_summary_schema = AlbumSummarySchema(many=True)


@albums_bp.route("", methods=["GET"])
def get_albums() -> tuple:
    """
    Retrieve a paginated list of albums with their associated tracks.

    ---
    tags:
      - Albums
    parameters:
      - name: page
        in: query
        type: integer
        required: false
        default: 1
        description: Page number (1-indexed)
      - name: per_page
        in: query
        type: integer
        required: false
        default: 20
        description: Number of results per page
    responses:
      200:
        description: Paginated list of albums with their tracks
        schema:
          type: object
          properties:
            total:
              type: integer
            page:
              type: integer
            per_page:
              type: integer
            albums:
              type: array
              items:
                $ref: '#/definitions/Album'
    definitions:
      Album:
        type: object
        properties:
          AlbumId:
            type: integer
          Title:
            type: string
          tracks:
            type: array
            items:
              $ref: '#/definitions/Track'
      Track:
        type: object
        properties:
          TrackId:
            type: integer
          Name:
            type: string
    """
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=20, type=int)

    albums, total = get_all_albums_with_tracks(page, per_page)

    return (
        jsonify(
            {
                "total": total,
                "page": page,
                "per_page": per_page,
                "albums": album_schema.dump(albums),
            }
        ),
        200,
    )


@albums_bp.route("/<int:album_id>/tracks", methods=["GET"])
def get_album_tracks(album_id: int) -> tuple:
    """
    Retrieve a list of tracks for a given album.

    ---
    tags:
      - Albums
    parameters:
      - name: album_id
        in: path
        type: integer
        required: true
        description: Album ID
    responses:
      200:
        description: Tracks for the specified album
        schema:
          type: object
          properties:
            album_id:
              type: integer
            tracks:
              type: array
              items:
                $ref: '#/definitions/Track'
      404:
        description: Album not found
    """
    tracks = get_tracks_by_album(album_id)
    return jsonify({"album_id": album_id, "tracks": track_schema.dump(tracks)}), 200


@albums_bp.route("/summary", methods=["GET"])
def get_album_summary() -> tuple:
    """
    Retrieve a summary of all albums with artist name and track count.

    ---
    tags:
      - Albums
    responses:
      200:
        description: List of album summaries
        schema:
          type: array
          items:
            $ref: '#/definitions/AlbumSummary'
    definitions:
      AlbumSummary:
        type: object
        properties:
          AlbumId:
            type: integer
          AlbumTitle:
            type: string
          ArtistName:
            type: string
          TrackCount:
            type: integer
    """
    summaries = get_album_summaries()
    return jsonify(album_summary_schema.dump(summaries)), 200
