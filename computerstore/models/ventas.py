from odoo import models, fields, api


class Ventas(models.Model):
    _name = 'computerstore.ventas'
    cliente = fields.Many2one('computerstore.clientes', 'Cliente')
    fecha_actual = fields.Date(string='Fecha actual', default=lambda s: fields.Date.context_today(s))
    articulo = fields.Many2one('computerstore.componentes', 'Componente')
    cantidad = fields.Integer('Cantidad', required=True)
    precio = fields.Float('PVP')
    total = fields.Float(string='Precio total', compute='_total')

    @api.one
    @api.depends('precio', 'cantidad')
    def _total(self):
        cursor = self.env.cr
        cursor.execute('select precio from computerstore_componentes where cod=%s', (self.articulo.cod,))
        for x in cursor.fetchall():
            self.precio = x[0]
            self.total = self.total + (self.precio * self.cantidad)
