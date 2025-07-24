# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Configuration for the Universal Robots UR10e with Robotiq 2F-140 gripper.

The following configuration parameters are available:

* :obj:`UR10_ROBOTIQ_CFG`: The UR10e arm equipped with a Robotiq 2F-140 gripper.

Reference: https://github.com/ros-industrial/universal_robot
"""
import math
import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg
import os
##
# Configuration
##

_THIS_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROBOT_PATH = os.path.join(_THIS_SCRIPT_DIR, "assets", "ur10e.usd")

UR10_ROBOTIQ_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=ROBOT_PATH,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            max_depenetration_velocity=5.0,
        ),
        activate_contact_sensors=True,
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True, solver_position_iteration_count=8, solver_velocity_iteration_count=0
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        joint_pos={
            # Arm joints
            "shoulder_pan_joint": 0.0,
            "shoulder_lift_joint": -1.712,
            "elbow_joint": 1.712,
            "wrist_1_joint": 0.0,#math.pi/2,
            "wrist_2_joint": math.pi/2, #math.pi/2,
            "wrist_3_joint": 0.0,
            # Gripper joints (optional initial positions) 0.04 'finger_joint': 45.000 not in [0.000, 0.785]
            "finger_joint": 0.785,            
        },
    ),
    actuators={
        "arm": ImplicitActuatorCfg(
            joint_names_expr=[
                "shoulder_pan_joint",
                "shoulder_lift_joint",
                "elbow_joint",
                "wrist_1_joint",
                "wrist_2_joint",
                "wrist_3_joint",
            ],
            velocity_limit_sim=0.5,
            effort_limit_sim=87.0,
            stiffness=300.0,
            damping=20.0,
        ),
        "gripper": ImplicitActuatorCfg(
            joint_names_expr=[
                "finger_joint",                
            ],
            velocity_limit_sim=10.0,
            effort_limit_sim=200.0,
            stiffness=300.0,
            damping=10.0,
        ),
    },
)
"""Configuration of UR10e arm with Robotiq 2F-140 gripper using implicit actuator models."""
