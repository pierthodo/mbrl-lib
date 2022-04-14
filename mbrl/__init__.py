# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
__version__ = "0.2.0.dev4"
from gym.envs.registration import register

register(
    id='continuous_CartPole-v0',
    entry_point='mbrl.env:CartPoleEnv',
    max_episode_steps=200,
)

