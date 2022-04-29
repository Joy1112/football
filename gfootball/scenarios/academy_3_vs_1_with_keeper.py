# coding=utf-8
# Copyright 2019 Google LLC
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.






from . import *
from numpy import random as rnd


def build_scenario(builder):
  cfg = builder._config['scenario_cfg']
  if cfg is None:
    cfg = {}
  builder.config().game_duration = 400
  builder.config().deterministic = False
  builder.config().offsides = False
  builder.config().end_episode_on_score = True
  builder.config().end_episode_on_out_of_play = True
  if cfg.get('pc_ok', False):
    builder.config().end_episode_on_possession_change = False
  else:
    builder.config().end_episode_on_possession_change = True
  builder.SetBallPosition(0.62, 0.0)
  builder.SetTeam(Team.e_Left)
  builder.AddPlayer(-1.0, 0.0, e_PlayerRole_GK)
  if cfg.get('full_court', False):
    ori_pos = [[0.2,0.0],[-0.5,0.2],[-0.5,-0.2]]
  else:
    ori_pos = [[0.6,0.0],[0.7,0.2],[0.7,-0.2]]
  if cfg.get('random_init', False):
    rnd_range = cfg.get('random_scale')
    ori_pos = [[0.6,0.0],[0.7,0.2],[0.7,-0.2]]
    for i in range(3):
      epsilon0 = rnd.uniform(-rnd_range, rnd_range)
      epsilon1 = rnd.uniform(-rnd_range*0.42, rnd_range*0.42)
      pos = [ori_pos[i][0] + epsilon0, ori_pos[i][1]+epsilon1]
      builder.AddPlayer(pos[0],pos[1],e_PlayerRole_CM)
    # for _ in range(3):
    #   builder.AddPlayer(rnd.uniform(0.4,0.9), rnd.uniform(-0.3,0.3), e_PlayerRole_CM)
  else:
    for pos in ori_pos:
      builder.AddPlayer(pos[0], pos[1], e_PlayerRole_CM)
  builder.SetTeam(Team.e_Right)
  builder.AddPlayer(-1.0, 0.0, e_PlayerRole_GK)
  builder.AddPlayer(-0.75, 0.0, e_PlayerRole_CB)
