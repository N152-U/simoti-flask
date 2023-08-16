from database.db import get_connection
from .entities.Permission import Permission


class PermissionModel:
    @classmethod
    def get_permissions(self):
        try:
            connection = get_connection()
            print("connection", connection)
            permissions = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, permission, description,active FROM permissions ORDER BY permission ASC"
                )
                resultset = cursor.fetchall()

                for row in resultset:
                    movie = Permission(row[0], row[1], row[2])
                    permissions.append(movie.to_JSON())

            connection.close()
            return permissions
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_permission(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, permission, description, active FROM permissions WHERE id = %s",
                    (id,),
                )
                row = cursor.fetchone()

                permission = None
                if row != None:
                    permission = Permission(row[0], row[1], row[2], row[3])
                    permission = permission.to_JSON()

            connection.close()
            return permission
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_permission(self, permission):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO permissions (id, permission, description) 
                                VALUES (%s, %s, %s)""",
                    (permission.id, permission.permission, permission.description),
                )
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_permission(self, permission):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """UPDATE permissions SET title = %s, duration = %s, released = %s 
                                WHERE id = %s""",
                    (
                        permission.title,
                        permission.duration,
                        permission.released,
                        permission.id,
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
