# test/test_errors.py
def test_not_found_route(client):
    response = client.get("/nonexistent")
    assert response.status_code == 404
    assert response.get_json()["error"] == "Not Found"


def test_internal_server_error(client, monkeypatch):
    from app.routes.artists import get_all_artists

    def boom(*args, **kwargs):
        raise Exception("Boom!")

    monkeypatch.setattr("app.routes.artists.get_all_artists", boom)

    response = client.get("/artists")
    assert response.status_code == 500
    assert response.get_json()["error"] == "Internal Server Error"
