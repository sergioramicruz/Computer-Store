from odoo import models, fields, api


class Proveedores(models.Model):
    _name = 'computerstore.proveedores'
    cif = fields.Char('Codigo', required=True)
    nombre = fields.Char('Nombre', required=True)
    direccion = fields.Char('Dirección', required=False)
    poblacion = fields.Char('Población', required=False)
    provincia = fields.Char('Provincia', required=False)
    codPostal = fields.Integer('Cod Postal', required=False)
    telefono = fields.Integer('Telefono', required=True)
    email = fields.Char('Email', required=True)

    def name_get(self):
        res = []
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res
