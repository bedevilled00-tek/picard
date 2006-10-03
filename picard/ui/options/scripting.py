# -*- coding: utf-8 -*-
#
# Picard, the next-generation MusicBrainz tagger
# Copyright (C) 2006 Lukáš Lalinský
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

from PyQt4 import QtGui
from picard.api import IOptionsPage
from picard.component import Component, implements
from picard.config import BoolOption, TextOption

class ScriptingOptionsPage(Component):

    implements(IOptionsPage)

    options = [
        BoolOption("setting", "enable_tagger_script", False),
        TextOption("setting", "tagger_script", ""),
    ]

    def get_page_info(self):
        return _("Scripting"), "scripting", "advanced", 30

    def get_page_widget(self, parent=None):
        from picard.ui.ui_options_script import Ui_Form
        self.page = QtGui.QWidget(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self.page)
        self.ui.enable_tagger_script.setChecked(
            self.config.setting["enable_tagger_script"])
        self.ui.tagger_script.document().setPlainText(
            self.config.setting["tagger_script"])
        return self.page

    def save_options(self):
        self.config.setting["enable_tagger_script"] = \
            self.ui.enable_tagger_script.isChecked()
        self.config.setting["tagger_script"] = self.ui.tagger_script.toPlainText()

