from odoo import models, fields, api


class Componentes(models.Model):
    _name = 'computerstore.componentes'
    cod = fields.Integer('Referencia', required=True)
    nombre = fields.Char('Nombre', required=True)
    descripcion = fields.Char('Descripción', required=True)
    proveedor = fields.Many2one('computerstore.proveedores', 'Proveedor')
    precio = fields.Float('Precio', required=True)
    cantidad = fields.Integer('Stock', required=True)

    def name_get(self):
        res = []
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res
