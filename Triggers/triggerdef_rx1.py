from __future__ import print_function, division

'''
Trigger definition class

'by_key' and 'values' member variables are automatically created when instantiated.

Usage: See the sample code


Kyuhwa Lee, 2014
Swiss Federal Institute of Technology Lausanne (EPFL)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''

from triggerdef_template import TriggerDefTemplate

# Trigger values up to 15
class TriggerDef(TriggerDefTemplate):
	"""
	Trigger definition class

	'by_key' and 'values' member variables are automatically created when instantiated.

	Usage: See the sample code
	"""
	PL= 100
	LL= 101
	PR= 102
	RR= 103