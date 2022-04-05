from bson import ObjectId, json_util
from tweeter import mongo


def test_profile(client, headers):
    user_id = headers.get('user_id')
    url = f'/{user_id}/profile'
    response = client.get(url, headers=headers)
    data = json_util.loads(response.data)
    assert response.status_code == 200
    assert data.get('self') is True
    assert data.get('follows_you') is False