# app/routes/artists.py
"""
Artists API routes for listing and managing artist resources.
"""

from flask import Blueprint, jsonify, request

from app.services.services import get_all_artists, get_albums_by_artist
from app.schemas.artists_schema import ArtistSchema
from app.schemas.albums_schema import AlbumSchema

artists_bp = Blueprint("artists", __name__)
artist_schema = ArtistSchema(many=True)
album_schema = AlbumSchema(many=True, only=("AlbumId", "Title"))


@artists_bp.route("", methods=["GET"])
def get_artists() -> tuple:
    """
    Retrieve and return a paginated list of all artists.

    ---
    tags:
      - Artists
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
        description: Number of items per page
    responses:
      200:
        description: Paginated list of artists.
        schema:
          type: object
          properties:
            total:
              type: integer
              description: Total number of artists.
            page:
              type: integer
              description: Current page number.
            per_page:
              type: integer
              description: Number of items per page.
            artists:
              type: array
              items:
                $ref: '#/definitions/Artist'
    definitions:
      Artist:
        type: object
        properties:
          ArtistId:
            type: integer
          Name:
            type: string
    """
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=20, type=int)

    artists, total = get_all_artists(page, per_page)

    return (
        jsonify(
            {
                "total": total,
                "page": page,
                "per_page": per_page,
                "artists": artist_schema.dump(artists),
            }
        ),
        200,
    )


@artists_bp.route("/<int:artist_id>/albums", methods=["GET"])
def get_artist_albums(artist_id: int) -> tuple:
    """
    Retrieve all albums for a specific artist.

    ---
    tags:
      - Artists
    parameters:
      - name: artist_id
        in: path
        required: true
        type: integer
        description: The ID of the artist
    responses:
      200:
        description: List of albums for the artist
        schema:
          type: array
          items:
            $ref: '#/definitions/Album'
      404:
        description: Artist not found
    definitions:
      Album:
        type: object
        properties:
          AlbumId:
            type: integer
          Title:
            type: string
    """
    albums = get_albums_by_artist(artist_id)
    return jsonify(album_schema.dump(albums)), 200
