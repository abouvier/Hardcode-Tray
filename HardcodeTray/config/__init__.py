"""
Fixes Hardcoded tray icons in Linux.

Author : Bilal Elmoussaoui (bil.elmoussaoui@gmail.com)
Contributors : Andreas Angerer, Joshua Fogg
Website : https://github.com/bil-elmoussaoui/Hardcode-Tray
Licence : The script is released under GPL, uses a modified script
     form Chromium project released under BSD license
This file is part of Hardcode-Tray.
Hardcode-Tray is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
Hardcode-Tray is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with Hardcode-Tray. If not, see <http://www.gnu.org/licenses/>.
"""
from .arguments import ArgumentsConfig
from .json import JSONConfig
from .system import SystemConfig


class Config:
    """Store the config from args, json file & system."""

    def __init__(self, args):
        self.data = {}
        self.sources = [
            ArgumentsConfig(args),
            JSONConfig(),
            SystemConfig()
        ]
        self.parse_data()

    def parse_data(self):
        """Parse the data from different sources."""
        for source in self.sources:
            for key, value in source.data.items():
                if value != None or not self.data.get(key):
                    self.data[key] = value

    def get(self, key):
        """Return the value of key."""
        return self.data.get(key)
