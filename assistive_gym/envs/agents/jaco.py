import os
import numpy as np
import pybullet as p
from .robot import Robot

class Jaco(Robot):
    def __init__(self, arm='right'):
        self.torso = 0
        right_arm_joint_indices = [1, 2, 3, 4, 5, 6, 7] # Controllable arm joints
        left_arm_joint_indices = right_arm_joint_indices # Controllable arm joints
        right_end_effector = 8 # Used to get the pose of the end effector
        left_end_effector = right_end_effector # Used to get the pose of the end effector
        right_gripper_indices = [9, 11, 13] # Gripper actuated joints
        left_gripper_indices = right_gripper_indices # Gripper actuated joints
        gripper_pos = {'scratch_itch': [1]*3, '': 0} # Gripper open position for holding tools
        right_tool_joint = 8 # Joint that tools are attached to
        left_tool_joint = right_tool_joint # Joint that tools are attached to
        tool_pos_offset = {'scratch_itch': [0, 0, 0.02], '': 0} # Position offset between tool and robot tool joint
        tool_orient_offset = {'scratch_itch': [0, -np.pi/2.0, 0], '': 0} # RPY orientation offset between tool and robot tool joint
        right_gripper_collision_indices = list(range(7, 15)) # Used to disable collision between gripper and tools
        left_gripper_collision_indices = right_gripper_collision_indices # Used to disable collision between gripper and tools
        toc_base_pos_offset = {'scratch_itch': [-0.35, -0.3, 0.3], '': 0} # Robot base offset before TOC base pose optimization
        toc_ee_orient_rpy = {'scratch_itch': [0, np.pi/2.0, 0], '': 0} # Initial end effector orientation
        wheelchair_mounted = True

        super(Jaco, self).__init__(arm, right_arm_joint_indices, left_arm_joint_indices, right_end_effector, left_end_effector, right_gripper_indices, left_gripper_indices, gripper_pos, right_tool_joint, left_tool_joint, tool_pos_offset, tool_orient_offset, right_gripper_collision_indices, left_gripper_collision_indices, toc_base_pos_offset, toc_ee_orient_rpy, wheelchair_mounted, half_range=False)

    def init(self, directory, id, np_random):
        self.body = p.loadURDF(os.path.join(directory, 'jaco', 'j2s7s300_gym.urdf'), useFixedBase=True, basePosition=[-2, -2, 0.975], flags=p.URDF_USE_SELF_COLLISION, physicsClientId=id)
        super(Jaco, self).init(self.body, id, np_random)
