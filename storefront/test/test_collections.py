from rest_framework import status
import pytest

@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/', collection)
    return do_create_collection



@pytest.mark.django_db
class TestCreateCollection:
    # @pytest.mark.skip


    def test_if_user_is_annonymous_return_404(self, create_collection):
        #AAA
        respons = create_collection({'title': 'a'})
        # assert
        assert respons.status_code == status.HTTP_401_UNAUTHORIZED


    def test_if_user_is_not_admin_return_403(self, api_client, create_collection):
        api_client.force_authenticate(user={})

        respons = create_collection({'title': 'a'})
    
        assert respons.status_code == status.HTTP_403_FORBIDDEN



    def test_if_data_is_invalid_return_400(self, create_collection, user_authenticate):
        user_authenticate(is_staff= True)

        respons = create_collection( {'title': ''})

        assert respons.status_code == status.HTTP_400_BAD_REQUEST
        assert respons.data['title'] is not None



    def test_if_data_is_valid_return_201(self, user_authenticate, create_collection):
        user_authenticate(is_staff= True)

        respons = create_collection({'title': 'a'})
    
        assert respons.status_code == status.HTTP_201_CREATED
        assert respons.data['id'] > 0