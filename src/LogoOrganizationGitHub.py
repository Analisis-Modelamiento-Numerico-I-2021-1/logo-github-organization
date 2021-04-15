# Copyright (C) 2021 Analisis-Modelamiento-Numerico-I-2021-1
#
# This file is part of logo-github-organization.
#
# logo-github-organization is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# logo-github-organization is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with logo-github-organization.  If not, see <http://www.gnu.org/licenses/>.

from manim import Scene, Tex, LEFT, RIGHT, DOWN, BLUE, GREEN


class LogoOrganizationGitHub(Scene):
    def construct(self):
        analysis = Tex(
            r"Análisis y Modelamiento", color=BLUE).scale(1.4)
        numeric = Tex(
            r"Numérico I", color=BLUE).scale(1.4).shift(DOWN + LEFT)
        year_name = Tex(
            "2020-1", color=GREEN).scale(1.4).next_to(numeric, RIGHT)
        self.add(analysis, numeric, year_name)
        self.wait(1)
