# -*- coding: utf-8 -*-


# OpenFisca -- A versatile microsimulation software
# By: OpenFisca Team <contact@openfisca.fr>
#
# Copyright (C) 2011, 2012, 2013, 2014, 2015 OpenFisca Team
# https://github.com/openfisca
#
# This file is part of OpenFisca.
#
# OpenFisca is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# OpenFisca is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from openfisca_france_data.input_data_builders.fake_openfisca_data_builder import get_fake_input_data_frame
from openfisca_france_data.surveys import SurveyScenario


def check_run(simulation, year):
    assert simulation.calculate('revdisp') is not None, "Cannot compute revdisp in {}".format(year)
    assert simulation.calculate('salsuperbrut') is not None, "Cannot compute salsuperbrut in {}".format(year)


def test_fake_survey_simulation():
    for year in range(2015, 2002, -1):
        input_data_frame = get_fake_input_data_frame()
        survey_scenario = SurveyScenario().init_from_data_frame(
            input_data_frame = input_data_frame,
            year = year,
            )
        simulation = survey_scenario.new_simulation()
        yield check_run, simulation, year


if __name__ == '__main__':
    import logging
    log = logging.getLogger(__name__)
    import sys
    logging.basicConfig(level = logging.INFO, stream = sys.stdout)
    test_fake_survey_simulation()
