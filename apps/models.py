# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.policy import default
from apps import db
from sqlalchemy.exc import SQLAlchemyError
from apps.exceptions.exception import InvalidUsage
import datetime as dt
from sqlalchemy.orm import relationship
from enum import Enum

class CURRENCY_TYPE(Enum):
    usd = 'usd'
    eur = 'eur'

class Product(db.Model):

    __tablename__ = 'products'

    id            = db.Column(db.Integer,      primary_key=True)
    name          = db.Column(db.String(128),  nullable=False)
    info          = db.Column(db.Text,         nullable=True)
    price         = db.Column(db.Integer,      nullable=False)
    currency      = db.Column(db.Enum(CURRENCY_TYPE), default=CURRENCY_TYPE.usd, nullable=False)

    date_created  = db.Column(db.DateTime,     default=dt.datetime.utcnow())
    date_modified = db.Column(db.DateTime,     default=db.func.current_timestamp(),
                                               onupdate=db.func.current_timestamp())
    
    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.name} / ${self.price}"

    @classmethod
    def find_by_id(cls, _id: int) -> "Product":
        return cls.query.filter_by(id=_id).first() 

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)

    def delete(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)
        return


#__MODELS__
class User_Roles(db.Model):

    __tablename__ = 'User_Roles'

    id = db.Column(db.Integer, primary_key=True)

    #__User_Roles_FIELDS__
    id = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String(255),  nullable=True)
    persmissions = db.Column(db.String(255),  nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__User_Roles_FIELDS__END

    def __init__(self, **kwargs):
        super(User_Roles, self).__init__(**kwargs)


class Users(db.Model):

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)

    #__Users_FIELDS__
    id_users = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String(255),  nullable=True)
    email = db.Column(db.String(255),  nullable=True)
    password = db.Column(db.String(255),  nullable=True)
    avatar = db.Column(db.String(255),  nullable=True)
    last_login = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.Boolean, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Users_FIELDS__END

    def __init__(self, **kwargs):
        super(Users, self).__init__(**kwargs)


class Suppliers(db.Model):

    __tablename__ = 'Suppliers'

    id = db.Column(db.Integer, primary_key=True)

    #__Suppliers_FIELDS__
    id_suppliers = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String(255),  nullable=True)
    contact = db.Column(db.String(255),  nullable=True)
    email = db.Column(db.String(255),  nullable=True)
    phone = db.Column(db.String(255),  nullable=True)
    address = db.Column(db.Text, nullable=True)
    status = db.Column(db.Boolean, nullable=True)
    bank_name = db.Column(db.String(255),  nullable=True)
    bank_account = db.Column(db.String(255),  nullable=True)
    npwp = db.Column(db.String(255),  nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Suppliers_FIELDS__END

    def __init__(self, **kwargs):
        super(Suppliers, self).__init__(**kwargs)


class Purchase_Orders(db.Model):

    __tablename__ = 'Purchase_Orders'

    id = db.Column(db.Integer, primary_key=True)

    #__Purchase_Orders_FIELDS__
    date = db.Column(db.DateTime, default=db.func.current_timestamp())
    due_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    name = db.Column(db.String(255),  nullable=True)
    quantity = db.Column(db.Integer, nullable=True)
    unit = db.Column(db.String(255),  nullable=True)
    price = db.Column(db.Integer, nullable=True)
    total = db.Column(db.Integer, nullable=True)
    status = db.Column(db.Boolean, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Purchase_Orders_FIELDS__END

    def __init__(self, **kwargs):
        super(Purchase_Orders, self).__init__(**kwargs)


class Customers(db.Model):

    __tablename__ = 'Customers'

    id = db.Column(db.Integer, primary_key=True)

    #__Customers_FIELDS__
    name = db.Column(db.String(255),  nullable=True)
    type = db.Column(db.String(255),  nullable=True)
    contact = db.Column(db.String(255),  nullable=True)
    email = db.Column(db.String(255),  nullable=True)
    phone = db.Column(db.String(255),  nullable=True)
    address = db.Column(db.Text, nullable=True)
    status = db.Column(db.Boolean, nullable=True)
    bank_name = db.Column(db.String(255),  nullable=True)
    bank_account = db.Column(db.String(255),  nullable=True)
    npwp = db.Column(db.String(255),  nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Customers_FIELDS__END

    def __init__(self, **kwargs):
        super(Customers, self).__init__(**kwargs)


class Penjualan(db.Model):

    __tablename__ = 'Penjualan'

    id = db.Column(db.Integer, primary_key=True)

    #__Penjualan_FIELDS__
    id_penjualan = db.Column(db.Integer, nullable=True)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())
    due_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.Boolean, nullable=True)
    total = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Penjualan_FIELDS__END

    def __init__(self, **kwargs):
        super(Penjualan, self).__init__(**kwargs)


class Penjualan_Items(db.Model):

    __tablename__ = 'Penjualan_Items'

    id = db.Column(db.Integer, primary_key=True)

    #__Penjualan_Items_FIELDS__
    name = db.Column(db.String(255),  nullable=True)
    quantity = db.Column(db.Integer, nullable=True)
    unit = db.Column(db.String(255),  nullable=True)
    price = db.Column(db.Integer, nullable=True)
    total = db.Column(db.Integer, nullable=True)

    #__Penjualan_Items_FIELDS__END

    def __init__(self, **kwargs):
        super(Penjualan_Items, self).__init__(**kwargs)



#__MODELS__END
