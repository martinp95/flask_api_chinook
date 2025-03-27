# tests/confest.py
import pytest
from app import create_app, db
from app.models.models import Artist, Album, Track


@pytest.fixture(scope="session")
def app():
    """
    Creates a Flask app instance for testing.
    """
    app = create_app()
    return app


@pytest.fixture
def client(app):
    """
    Creates a test client and ensures app context is active during test.
    """
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()  # Optional cleanup


@pytest.fixture
def sample_data(app):
    """
    Inserts sample data into the test database. Returns primitive values only.
    """
    with app.app_context():
        artist = Artist(Name="Test Artist")
        db.session.add(artist)
        db.session.commit()

        album = Album(Title="Test Album", ArtistId=artist.ArtistId)
        db.session.add(album)
        db.session.commit()

        tracks = [
            Track(
                Name="Track 1",
                AlbumId=album.AlbumId,
                MediaTypeId=1,
                Milliseconds=1000,
                UnitPrice=0.99,
            ),
            Track(
                Name="Track 2",
                AlbumId=album.AlbumId,
                MediaTypeId=1,
                Milliseconds=1000,
                UnitPrice=0.99,
            ),
        ]
        db.session.bulk_save_objects(tracks)
        db.session.commit()

        return {
            "artist_id": artist.ArtistId,
            "album_id": album.AlbumId,
            "track_ids": [track.TrackId for track in tracks],
        }
