from database.db import get_connection
from .entities.Role import Role
from .entities.RoleAll import RoleAll
from datetime import datetime


class RoleModel:
    @classmethod
    def get_roles(self):
        try:
            connection = get_connection()
            roles = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, role,active FROM roles ORDER BY role ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    role = RoleAll(row[0], row[1], row[2])
                    roles.append(role.to_JSON())

            connection.close()
            return roles
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_role(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT r.id,r.role, 
                        json_agg(json_build_object(
                        	'description',p.description:: varchar(255)
                        )) permissions
                        FROM roles r
                        INNER JOIN role_has_permissions rhp ON rhp.role_id = r.id 
                        INNER JOIN permissions p ON p.id = rhp.permission_id
                        WHERE r.id = %s
                        GROUP BY r.id,r.role """,
                    (id,),
                )
                row = cursor.fetchone()

                role = None
                if row != None:
                    role = Role(row[0], row[1], row[2])
                    role = role.to_JSON()

            connection.close()
            return role
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_update_role(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT r.id,r.role, 
                        json_agg(json_build_object(
                        	'id',p.id:: varchar(255)
                        )) permissions
                        FROM roles r
                        INNER JOIN role_has_permissions rhp ON rhp.role_id = r.id 
                        INNER JOIN permissions p ON p.id = rhp.permission_id
                        WHERE r.id = %s
                        GROUP BY r.id,r.role """,
                    (id,),
                )
                row = cursor.fetchone()

                role = None
                if row != None:
                    role = Role(row[0], row[1], row[2])
                    role = role.to_JSON()

            connection.close()
            return role
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
    def update_role(self, roleData):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                name = "ADMIN"
                now = datetime.now()
                now = now.strftime("%G-%m-%d %X")
                print("DELETE FROM role_has_permissions WHERE role_id = '{0}'",
                    (roleData.id))
                cursor.execute(
                    "DELETE FROM role_has_permissions WHERE role_id = '{0}'",
                    (roleData.id),
                )
                affected_rows = cursor.rowcount
                connection.commit()

                cursor.execute(
                    """ UPDATE roles 
                        SET role = %s,updated_at = %s,updated_by = %s WHERE id = %s""",
                    (roleData.role, now, name, roleData.id),
                )
                affected_rows = cursor.rowcount
                connection.commit()
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
    def delete_role(self, role):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM role_has_permissions WHERE role_id = '{0}'", (role.id)
                )
                affected_rows = cursor.rowcount
                connection.commit()
                cursor.execute("DELETE FROM roles WHERE id = '{0}'".format(role.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
