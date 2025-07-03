from werkzeug.security import check_password_hash as checkph

from database.db import get_connection
from .entities.User import User, UserTutorConfirmation, UserType,GetUpdateUser, UserConfirmation,UserT
from .entities.Permission import PermissionList


class UserModel:
    @classmethod
    def get_users(self):
        try:
            connection = get_connection()

            users = []

            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT u.id, u.username, u.first_name, u.middle_name, u.last_name, r.role, u.token_fcw
                    FROM users u
                    INNER JOIN roles r ON r.id = u.role_id
                    WHERE u.active = true
                    ORDER BY username ASC"""
                )
                resultset = cursor.fetchall()

                for row in resultset:
                    user = UserT(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    users.append(user.to_JSON())

            connection.close()
            return users
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_user(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT u.id, u.username, u.first_name, u.middle_name, u.last_name, r.role, u.active
                    FROM users u
                    INNER JOIN roles r ON r.id = u.role_id
                    WHERE u.active = true
                    AND u.id = '{0}'
                    """.format(
                        id
                    )
                )
                row = cursor.fetchone()

                user = None
                if row != None:
                    user = User(row[0], row[1], row[2], row[3], row[4], row[5])
                    user = user.to_JSON()

            connection.close()
            return user
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_user_type(self, id):
        try:
            connection = get_connection()

            users = []

            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT u.id, CONCAT(u.first_name, ' ', u.middle_name, ' ', u.last_name) AS full_name, r.role, u.active
                    FROM users u
                    INNER JOIN roles r ON r.id = u.role_id
                    WHERE u.active = true
                    AND r.id = '{0}'
                    """.format(
                        id
                    )
                )
                resultset = cursor.fetchall()

            
                for row in resultset:
                    user = UserType(row[0], row[1], row[2], row[3])
                    users.append(user.to_JSON())

            connection.close()
            return users
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_user_update(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT u.id, u.username, u.first_name, u.middle_name, u.last_name, u.role_id, u.active
                    FROM users u
                    WHERE u.active = true
                    AND u.id = '{0}'
                    """.format(
                        id
                    )
                )
                row = cursor.fetchone()

                user = None
                if row != None:
                    user = GetUpdateUser(row[0], row[1], row[2], row[3], row[4], row[5])
                    user = user.to_JSON()

            connection.close()
            return user
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_user(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO users (id, role_id, username,first_name,middle_name,last_name,password, email,relationship_id,specialty) 
                                VALUES (%s, %s, %s,%s, %s, %s, %s,%s, %s,%s)""",
                    (
                        user.id,
                        user.role_id,
                        user.username,
                        user.first_name,
                        user.middle_name,
                        user.last_name,
                        user.password,
                        user.email,
                        user.relationship_id,
                        user.specialty
                    ),
                )
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_user(self, user):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    """UPDATE users SET 
                    role_id= %s, username= %s,first_name= %s,middle_name= %s,last_name= %s,password= %s
                                WHERE id = %s""",
                    (
                        user.role_id,
                        user.username,
                        user.first_name,
                        user.middle_name,
                        user.last_name,
                        user.password,
                        user.id,
                    ),
                )
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def update_user_token(self, token, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    """UPDATE users SET 
                    token_fcw= %s
                    WHERE id = %s""",
                    (token,id),
                )
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def delete_user(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE users SET active=false WHERE id = %s", (user.id,)
                )
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def login_user(cls, user):
        try:
            connection = get_connection()
            authenticated_user = None
            with connection.cursor() as cursor:
                cursor.execute(
                    """ SELECT u.id, u.username,u.first_name,u.middle_name,u.last_name,u.role_id,r.role,u.password
	                            FROM users u
                                INNER JOIN roles r ON r.id = u.role_id
                                WHERE 
                                u.username = '{0}'""".format(user.username)
                )
                row = cursor.fetchone()
                if row != None:
                    if(checkph(row[7],user.password) == True):
                        authenticated_user = UserConfirmation(
                            row[0], row[1], row[2], row[3], row[4], row[5], row[6]
                        )
                    else:
                        authenticated_user = None
            connection.close()
            return authenticated_user
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def login_tutor(cls, user):
        try:
            connection = get_connection()
            authenticated_user = None
            with connection.cursor() as cursor:
                cursor.execute(
                    """ SELECT 
                    u.id, 
                    u.username,
                    u.first_name,
                    u.middle_name,
                    u.last_name,
                    u.role_id,
                    r.role,
                    u.password,
                    p.id as patient_id,
                    CASE 
                        WHEN u.token_fcw  IS NULL THEN 'NO'
                        ELSE u.token_fcw
                    END AS token_fcw
                    FROM users u
                    INNER JOIN roles r ON r.id = u.role_id
                    INNER JOIN patients p ON p.tutor_id = u.id
                    WHERE
                        u.active AND
                        p.active AND
                        u.role_id = 'd88d9411-c944-463a-985c-8d938875d3e3' AND
                        u.username = '{0}'""".format(user.username)
                )
                row = cursor.fetchone()
                if row != None:
                    if(checkph(row[7],user.password) == True):
                        authenticated_user = UserTutorConfirmation(
                            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[8], row[9]
                        )
                    else:
                        authenticated_user = None
            connection.close()
            return authenticated_user
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_user_permissions(self, username):
        try:
            connection = get_connection()
            permissions = []

            with connection.cursor() as cursor:
                cursor.execute(
                  """SELECT p.permission
                        FROM users u
                        INNER JOIN role_has_permissions rp ON rp.role_id = u.role_id
                        INNER JOIN permissions p ON p.id = rp.permission_id
                        WHERE 
                        u.username = '{0}'""".format(username)
                )

                resultset = cursor.fetchall()

                for row in resultset:
                    user = PermissionList(row[0])
                    permissions.append(user.to_JSON())

            connection.close()
            return permissions
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_user_role(self, username):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                  """SELECT r.role
                        FROM users u
                        INNER JOIN roles r ON r.id = u.role_id
                        WHERE 
                        u.username = '{0}'""".format(username)
                )

                row = cursor.fetchone()

            connection.close()
            return row
        except Exception as ex:
            raise Exception(ex)