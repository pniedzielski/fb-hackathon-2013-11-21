# Learn Python -- level 7 logic
# Copyright (C) 2013 Cornell FB Hackathon Team.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

player1._position = [2, 2];
player2._position = [14, 6];

sign = Sign([3, 9], "The fearless, ambitious captain eavesdropped bravely on Olivia's kidnapper.")

def at_end():
    if (player1._messages.count("facebook") < 1 or
        player2._messages.count("facebook") < 1):
        raise Exception("Failure")
    
        
