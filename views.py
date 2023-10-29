from flask.views import MethodView
from database import AdvertisementModel, Session
from flask import jsonify, request
from errors import ApiException
from validate import validate, CreateAdvertisementSchema
from sqlalchemy.exc import IntegrityError
from datetime import datetime


class AdvertisementView(MethodView):

    def get(self, adv_id: int):
        with Session() as session:
            advert = session.query(AdvertisementModel).get(adv_id)
            if advert is None:
                raise ApiException(404, 'advertisement not found')
            return jsonify({
                'id': advert.id,
                'title': advert.title,
                'description': advert.description,
                'owner': advert.owner,
                'created_at': advert.created_at
            }
            )

    def post(self):
        data = request.json
        data['created_at'] = datetime.now().strftime('%d/%m/%y %H:%M:%S')
        advert_data = validate(data, CreateAdvertisementSchema)
        with Session() as session:
            new_advert = AdvertisementModel(**advert_data)
            session.add(new_advert)
            try:
                session.commit()
            except IntegrityError:
                raise ApiException(400, 'title already exist')
            return jsonify({
                'id': new_advert.id,
                'title': new_advert.title,
                'description': new_advert.description,
                'owner': new_advert.owner,
                'created_at': new_advert.created_at
            })


    def delete(self, adv_id: int):
        with Session() as session:
            adver = session.query(AdvertisementModel).get(adv_id)
            session.delete(adver)
            session.commit()
            return jsonify({'status': 'deleted'})