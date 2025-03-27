# test/test_artists.py
def test_get_artists_returns_data(client, sample_data):
    response = client.get("/artists?page=1&per_page=5")
    data = response.get_json()

    assert response.status_code == 200
    assert data["total"] > 0
    assert any(a["Name"] == "Test Artist" for a in data["artists"])


def test_get_artist_albums_success(client, sample_data):
    artist_id = sample_data["artist_id"]
    response = client.get(f"/artists/{artist_id}/albums")
    assert response.status_code == 200
    albums = response.get_json()
    assert isinstance(albums, list)
    assert any(album["Title"] == "Test Album" for album in albums)


def test_get_artist_albums_not_found(client):
    response = client.get("/artists/99999/albums")
    assert response.status_code == 404
    assert "error" in response.get_json()
