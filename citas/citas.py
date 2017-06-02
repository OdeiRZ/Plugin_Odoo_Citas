# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api, _

class citas_cita(models.Model):
	_name = 'citas.cita'
	
	autor = fields.Char(string='Autor', required=True, help='Inserta Autor de Cita')
	cita = fields.Text('Cita', required=True, help='Inserta Cita')
	fecha = fields.Date(string='Fecha de visualizacion', required=True, help='Selecciona Fecha de visualizacion')
	orden = fields.Integer(string='Orden de visualizacion', required=False, help='Inserta Orden de visualizacion')