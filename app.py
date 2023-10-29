from flask import Flask, jsonify
from views import AdvertisementView
from errors import ApiException

appadv = Flask('appadv')


@appadv.errorhandler(ApiException)
def error_handler(error: ApiException):
    response = jsonify({
        'status': 'error',
        'message': error.message
    })
    response.status_code = error.status_code
    return response


appadv.add_url_rule('/advertisements/<int:adv_id>', view_func=AdvertisementView.as_view('users'), methods=['GET', 'PATCH', 'DELETE'])
appadv.add_url_rule('/advertisements/', view_func=AdvertisementView.as_view('users_create'), methods=['POST'])


appadv.run()