import math
from isaaclab.assets import RigidObjectCfg
from isaaclab.sensors import FrameTransformerCfg
from isaaclab.sensors.frame_transformer.frame_transformer_cfg import OffsetCfg
from isaaclab.sim.schemas.schemas_cfg import RigidBodyPropertiesCfg
from isaaclab.sim.spawners.from_files.from_files_cfg import UsdFileCfg
from isaaclab.utils import configclass
from isaaclab.utils.assets import ISAAC_NUCLEUS_DIR
from isaaclab.markers.config import FRAME_MARKER_CFG  # isort: skip

from . import mdp
from .lift_env_cfg import LiftEnvCfg
from .ur_gripper import UR10_ROBOTIQ_CFG  

from isaaclab.sensors import ContactSensorCfg

@configclass
class Liftur10eEnvCfg(LiftEnvCfg):
    def __post_init__(self):
        super().__post_init__()

        # Set UR10e as robot with correct prim path
        self.scene.robot = UR10_ROBOTIQ_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")

        # Set actions for UR10e
        self.actions.arm_action = mdp.JointPositionActionCfg(
            asset_name="robot",
            joint_names=[
                "shoulder_pan_joint",
                "shoulder_lift_joint",
                "elbow_joint",
                "wrist_1_joint",
                "wrist_2_joint",
                "wrist_3_joint"
            ],
            scale=1,
            use_default_offset=True
        )
        # region gripper_action
        # Gripper Not Working
        self.actions.gripper_action = mdp.BinaryJointPositionActionCfg(
            asset_name="robot",
            joint_names=[               
                "finger_joint",
            ],
            open_command_expr={ 
                "finger_joint": 0.0,                
            },
            # finger_joint to target position = 45 closes it -- math.pi/4
            close_command_expr={
                "finger_joint": 0.57,
            },            
        )

        # End effector body name
        self.commands.object_pose.body_name = "robotiq_base_link"

        # -----------------------------------------------------------------------------
        # -----------------------------------------------------------------------------
        # Example from the Franka --- Isaac-Lift-Cube-Franka-v0
        # -----------------------------------------------------------------------------
        # -----------------------------------------------------------------------------
        # Set actions for the specific robot type (franka)
        # self.actions.arm_action = mdp.JointPositionActionCfg(
        #     asset_name="robot", joint_names=["panda_joint.*"], scale=0.5, use_default_offset=True
        # )
        # self.actions.gripper_action = mdp.BinaryJointPositionActionCfg(
        #     asset_name="robot",
        #     joint_names=["panda_finger.*"],
        #     open_command_expr={"panda_finger_.*": 0.04},
        #     close_command_expr={"panda_finger_.*": 0.0},
        # )
        # # Set the body name for the end effector
        # self.commands.object_pose.body_name = "panda_hand"
        # -----------------------------------------------------------------------------
        # -----------------------------------------------------------------------------


        # Cube as object to lift
        #usd_path=f"{ISAAC_NUCLEUS_DIR}/Props/Flip_Stack/screw_99_physics.usd", 
        self.scene.object = RigidObjectCfg(
            prim_path="{ENV_REGEX_NS}/Object",
            init_state=RigidObjectCfg.InitialStateCfg(pos=[0.8, 0.0, 0.055], rot=[1.0, 0.0, 0.0, 0.0]),
            spawn=UsdFileCfg(
                usd_path=f"{ISAAC_NUCLEUS_DIR}/Props/Blocks/DexCube/dex_cube_instanceable.usd",               
                scale=(1.0,1.0,1.0),
                rigid_props=RigidBodyPropertiesCfg(
                    solver_position_iteration_count=16,
                    solver_velocity_iteration_count=1,
                    max_angular_velocity=1000.0,
                    max_linear_velocity=1000.0,
                    max_depenetration_velocity=5.0,
                    disable_gravity=False,
                ),
            ),
        )

        # Frame marker configuration per il cubo
        cube_marker_cfg = FRAME_MARKER_CFG.copy()
        cube_marker_cfg.markers["frame"].scale = (0.1, 0.1, 0.1)
        cube_marker_cfg.prim_path = "/Visuals/CubeFrame"

        self.scene.cube_frame = FrameTransformerCfg(
            prim_path="{ENV_REGEX_NS}/Object",  # path del cubo
            debug_vis=True,
            visualizer_cfg=cube_marker_cfg,
            target_frames=[
                FrameTransformerCfg.FrameCfg(
                    prim_path="{ENV_REGEX_NS}/Object",
                    name="cube_reference",
                    offset=OffsetCfg(
                        pos=[0.0, 0.0, 0.0],
                    ),
                )
            ],
        )
        

        # Frame marker configuration
        marker_cfg = FRAME_MARKER_CFG.copy()
        marker_cfg.markers["frame"].scale = (0.1, 0.1, 0.1)
        marker_cfg.prim_path = "/Visuals/FrameTransformer"

        self.scene.ee_frame = FrameTransformerCfg(
            prim_path="{ENV_REGEX_NS}/Robot/base_link",
            debug_vis=False,
            visualizer_cfg=marker_cfg,
            target_frames=[
                FrameTransformerCfg.FrameCfg(
                    prim_path="{ENV_REGEX_NS}/Robot/gripper/robotiq_base_link",
                    name="end_effector",
                    offset=OffsetCfg(
                        pos=[0.0, 0.0, 0.1034],
                    ),
                )
            ],
        )

        # ----------------------------------------------------------
        # region Contact Sensors
        # TODO: Reward shapping
        # Must add the contact sensors for the Grasping Learning Reward
        # add contact sensor to the gripper of the robot
        self.scene.contact_forces_LF = ContactSensorCfg(
            prim_path="{ENV_REGEX_NS}/Robot/<magical path>/left_inner_pad", #left_inner_pad
            update_period=0.0,
            history_length=6,
            debug_vis=False,
            filter_prim_paths_expr=["{ENV_REGEX_NS}/Object"],
        )

        self.scene.contact_forces_RF = ContactSensorCfg(
            prim_path="{ENV_REGEX_NS}/Robot/<magical path>/right_inner_pad", #right_inner_pad
            update_period=0.0,
            history_length=6,
            debug_vis=False,
            filter_prim_paths_expr=["{ENV_REGEX_NS}/Object"],
        )
        # ----------------------------------------------------------

@configclass
class Liftur10eEnvCfg_PLAY(Liftur10eEnvCfg):
    def __post_init__(self):
        super().__post_init__()
        self.scene.num_envs = 50
        self.scene.env_spacing = 4
        self.observations.policy.enable_corruption = False


        