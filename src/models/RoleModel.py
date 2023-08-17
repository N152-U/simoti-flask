from database.db import get_connection
from .entities.Role import Role
from datetime import datetime


class RoleModel:
    @classmethod
    def get_roles(self):
        try:
            connection = get_connection()
            print("connection", connection)
            permissions = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, role,active FROM roles ORDER BY role ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    movie = Role(row[0], row[1], row[2])
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
                    permission = Role(row[0], row[1], row[2], row[3])
                    permission = permission.to_JSON()

            connection.close()
            return permission
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_role(self, roleData):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                name = "ADMIN"
                now = datetime.now()
                now = now.strftime("%G-%m-%d %X")
                cursor.execute(
                    """ INSERT INTO roles (id, role,created_at,created_by,updated_at,updated_by)
                                VALUES (%s, %s,%s,%s,%s,%s) """,
                    (roleData.id, roleData.role, now, name, now, name),
                )
                for permission in roleData.permissions:
                    cursor.execute(
                        """ INSERT INTO role_has_permissions (role_id, permission_id) 
                                    VALUES (%s, %s) """,
                        (roleData.id, permission),
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
