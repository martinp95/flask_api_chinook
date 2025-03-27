# test/test_albums.py
def test_get_albums_with_tracks(client, sample_data):
    response = client.get("/albums?page=1&per_page=5")
    data = response.get_json()

    assert response.status_code == 200
    assert data["total"] > 0
    assert any("tracks" in album for album in data["albums"])


def test_get_album_tracks_success(client, sample_data):
    album_id = sample_data["album_id"]
    response = client.get(f"/albums/{album_id}/tracks")
    data = response.get_json()

    assert response.status_code == 200
    assert "tracks" in data
    assert len(data["tracks"]) == 2


def test_get_album_tracks_not_found(client):
    response = client.get("/albums/99999/tracks")
    assert response.status_code == 404
    assert "error" in response.get_json()


def test_get_album_summary(client, sample_data):
    response = client.get("/albums/summary")
    data = response.get_json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert any(summary["ArtistName"] == "Test Artist" for summary in data)
