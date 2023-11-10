from decouple import config
import datetime
import jwt
import pytz


class Security:
    secret = config("JWT_KEY")
    tz = pytz.timezone("America/Mexico_City")

    @classmethod
    def generate_token(cls, authenticated_user):
        payload = {
            "iat": datetime.datetime.now(tz=cls.tz),
            "exp": datetime.datetime.now(tz=cls.tz) + datetime.timedelta(minutes=30),
            "username": authenticated_user.username,
            "firstName": authenticated_user.first_name,
            "middleName": authenticated_user.middle_name,
            "lastName": authenticated_user.last_name,
            "roleId": authenticated_user.role_id,
            "role": authenticated_user.role,
        }
        return jwt.encode(payload, cls.secret, algorithm="HS256")

    @classmethod
    def verify_token(cls, headers):
        if "Authorization" in headers.keys():
            authorization = headers["Authorization"]
            encoded_token = authorization.split(" ")[1]

            if len(encoded_token) > 0:
                try:
                    payload = jwt.decode(
                        encoded_token, cls.secret, algorithms=["HS256"]
                    )

                    return True
                except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
                    return False

        return False
