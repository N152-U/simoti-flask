from database.db import get_connection
from .entities.User import User,UpdateUser


class UserModel:
    @classmethod
    def get_users(self):
        try:
            connection = get_connection()

            users = []

            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT u.id, u.username, u.first_name, u.middle_name, u.last_name, r.role, u.active
                    FROM users u
                    INNER JOIN roles r ON r.id = u.role_id
                    WHERE u.active = true
                    ORDER BY username ASC"""
                )
                resultset = cursor.fetchall()

                for row in resultset:
                    user = User(row[0], row[1], row[2], row[3], row[4], row[5])
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
                    user = UpdateUser(row[0], row[1], row[2], row[3], row[4], row[5])
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
                    """INSERT INTO users (id, role_id, username,first_name,middle_name,last_name,password) 
                                VALUES (%s, %s, %s,%s, %s, %s, %s)""",
                    (
                        user.id,
                        user.role_id,
                        user.username,
                        user.first_name,
                        user.middle_name,
                        user.last_name,
                        user.password,
                    ),
                )
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_permission(self, permissionData):
        try:
            connection = get_connection()
            print("entre permission")
            with connection.cursor() as cursor:
                cursor.execute(
                    """UPDATE permissions SET permission = %s, description = %s 
                                WHERE id = %s""",
                    (
                        permissionData.permission,
                        permissionData.description,
                        permissionData.id,
                    ),
                )
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_permission(self, permission):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM permissions WHERE id = %s", (permission.id,)
                )
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
