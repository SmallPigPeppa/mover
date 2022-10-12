USE_PROX_VPOSER = False

## dataset for VirtualHome
# OLD_SKELETON_IDX = [2, 1, 5, 4, 8, 7, #65, 62,
#     12, # 3, 6
#     17, 16, 19, 18, 21,
#     20, 63, 60, 24, 23]

# this mapping is opposite from SMPL-X.


IDX_MAPPING = [
    # body joints
    -1, 2, 1, 5, 4, 8,
    7, -1, -1, 12, -1, -1, -1,  # 0, 3 | 3, 6 | 'Neck': 12, | feet: 11, 12; angle: 7, 8
    17, 16, 19, 18, 21,
    20, 63, 60, 24, 23,
    # 22, in_valid.
    # left hand joints
    # TODO: check the hand idx.
    52, 53, 54,
    40, 41, 42,
    43, 44, 45,
    49, 50, 51,
    46, 47, 48,
    # right hand joints
    37, 38, 39,
    25, 26, 27,
    28, 29, 30,
    34, 35, 36,
    31, 32, 33,
    #
    # 9, -1, in_valid
]
# IDX_MAPPING_GTA = [
#     # body joints
#     15, 12, -1, 17, 19, 21, -1,
#     16, 18, 20, 3, 6, 9, -1, -1, # 0, 3 | 3, 6 | 'Neck': 12, | feet: 11, 12; angle: 7, 8
#     2, 5, 8, 1, 4,
#     7]
# best
# IDX_MAPPING_GTA = [
#     # body joints
#     15, 12, -1, 17, 19, 21, -1,
#     16, 18, 20, -1, -1, -1, -1, -1, # 0, 3 | 3, 6 | 'Neck': 12, | feet: 11, 12; angle: 7, 8
#     2, 5, 8, 1, 4,
#     7]
# IDX_MAPPING_GTA = [
#     # body joints
#     15, 12, -1, 16, 18, 20, -1,
#     17, 19, 21, -1, -1, -1, -1, -1, # 0, 3 | 3, 6 | 'Neck': 12, | feet: 11, 12; angle: 7, 8
#     1, 4, 7, 2, 5,
#     8]
IDX_MAPPING_GTA = [0, 1, 2, 3, 4, 5, 6, 7, 8, -1, 10, 11, 12, -1, -1, 15, 16, 17, 18, 19, 20, 21, -1, -1, -1, 25, 26,
                   27, 28, 29, 30, 31, 32, 33, 34, 35, 36, -1, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
                   -1, 53, 54, 55, 56, 57, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

# SKELETON_IDX = [IDX_MAPPING[i] for i in range(23) if IDX_MAPPING[i] != -1]
# SKELETON_IDX = [IDX_MAPPING_GTA[i] for i in range(21) if IDX_MAPPING_GTA[i] != -1]
SKELETON_IDX = [IDX_MAPPING_GTA[i] for i in
                [0, 1, 2, 16, 17, 3, 6, 9, 12, 15, 7, 4, 8, 5, 11, 10, 13, 14, 18, 19, 20, 21, 60, 61, 62, 63, 64, 65,
                 59, 58, 56, 55, 57, 22] if IDX_MAPPING_GTA[i] != -1]
# RIGHT_HAND_IDX = []
# LEFT_HAND_IDX = []
RIGHT_HAND_IDX = [IDX_MAPPING_GTA[i] for i in
                  [21, 52, 53, 54, 71, 40, 41, 42, 72, 43, 44, 45, 73, 49, 50, 51, 74, 46, 47, 48, 75] if
                  IDX_MAPPING_GTA[i] != -1]
LEFT_HAND_IDX = [IDX_MAPPING_GTA[i] for i in
                  [20, 37, 38, 39, 66, 25, 26, 27, 67, 28, 29, 30, 68, 34, 35, 36, 69, 31, 32, 33, 70] if
                  IDX_MAPPING_GTA[i] != -1]
# print(OLD_SKELETON_IDX == SKELETON_IDX)
# SKELETON_IDX = [IDX_MAPPING[i] for i in range(23) if IDX_MAPPING[i] != -1]
# RIGHT_HAND_IDX = [37, 38, 39,
#             25, 26, 27,
#             28, 29, 30,
#             34, 35, 36,
#             31, 32, 33]
# LEFT_HAND_IDX = [52, 53, 54,
#             40, 41, 42,
#             43, 44, 45,
#             49, 50, 51,
#             46, 47, 48]

HAND_IDX = RIGHT_HAND_IDX + LEFT_HAND_IDX
# SKELETON_IDX = [2, 1, 5, 4, 65, 
#                 62, 0, 3, 12, 15,
#                 17, 16, 19, 18, 21,
#                 20, 63, 60, 24, 23]
# HAND_IDX = [37, 38, 39,
#             25, 26, 27,
#             28, 29, 30,
#             34, 35, 36,
#             31, 32, 33,
#             52, 53, 54,
#             40, 41, 42,
#             43, 44, 45,
#             49, 50, 51,
#             46, 47, 48]


# IDX_MAPPING = [
#     # body joints
#     -1, 1, 2, 4, 5, 62, 
#     65, 0, 3, 12, 15, -1, -1,
#     16, 17, 18, 19, 20,
#     21, 60, 63, 23, 24, 
#     # 22, in_valid.
#     # left hand joints
#     # TODO: check the hand idx.
#     37, 38, 39,
#     25, 26, 27,
#     28, 29, 30,
#     34, 35, 36,
#     31, 32, 33,
#     # right hand joints
#     52, 53, 54,
#     40, 41, 42,
#     43, 44, 45,
#     49, 50, 51,
#     46, 47, 48,
#     #  
#     # 9, -1, in_valid
# ]


VH_joint_names = ['Hips', 'LeftUpperLeg', 'RightUpperLeg', 'LeftLowerLeg', 'RightLowerLeg', 'LeftFoot',
                  'RightFoot', 'Spine', 'Chest', 'Neck', 'Head', 'LeftShoulder', 'RightShoulder',
                  'LeftUpperArm', 'RightUpperArm', 'LeftLowerArm', 'RightLowerArm', 'LeftHand',
                  'RightHand', 'LeftToes', 'RightToes', 'LeftEye', 'RightEye',
                  'Jaw',
                  'LeftThumbProximal',
                  'LeftThumbIntermediate', 'LeftThumbDistal', 'LeftIndexProximal',
                  'LeftIndexIntermediate', 'LeftIndexDistal', 'LeftMiddleProximal',
                  'LeftMiddleIntermediate', 'LeftMiddleDistal', 'LeftRingProximal',
                  'LeftRingIntermediate', 'LeftRingDistal', 'LeftLittleProximal',
                  'LeftLittleIntermediate', 'LeftLittleDistal',
                  'RightThumbProximal',
                  'RightThumbIntermediate', 'RightThumbDistal', 'RightIndexProximal',
                  'RightIndexIntermediate', 'RightIndexDistal', 'RightMiddleProximal',
                  'RightMiddleIntermediate', 'RightMiddleDistal', 'RightRingProximal',
                  'RightRingIntermediate', 'RightRingDistal', 'RightLittleProximal',
                  'RightLittleIntermediate', 'RightLittleDistal',
                  'UpperChest', 'LastBone']

JOINT_NAMES = [
    'pelvis',
    'left_hip',
    'right_hip',
    'spine1',
    'left_knee',
    'right_knee',
    'spine2',
    'left_ankle',
    'right_ankle',
    'spine3',
    'left_foot',
    'right_foot',
    'neck',
    'left_collar',
    'right_collar',
    'head',
    'left_shoulder',
    'right_shoulder',
    'left_elbow',
    'right_elbow',
    'left_wrist',
    'right_wrist',
    'jaw',
    'left_eye_smplhf',
    'right_eye_smplhf',
    'left_index1',
    'left_index2',
    'left_index3',
    'left_middle1',
    'left_middle2',
    'left_middle3',
    'left_pinky1',
    'left_pinky2',
    'left_pinky3',
    'left_ring1',
    'left_ring2',
    'left_ring3',
    'left_thumb1',
    'left_thumb2',
    'left_thumb3',
    'right_index1',
    'right_index2',
    'right_index3',
    'right_middle1',
    'right_middle2',
    'right_middle3',
    'right_pinky1',
    'right_pinky2',
    'right_pinky3',
    'right_ring1',
    'right_ring2',
    'right_ring3',
    'right_thumb1',
    'right_thumb2',
    'right_thumb3',
    'nose',
    'right_eye',
    'left_eye',
    'right_ear',
    'left_ear',
    'left_big_toe',
    'left_small_toe',
    'left_heel',
    'right_big_toe',
    'right_small_toe',
    'right_heel',
    'left_thumb',
    'left_index',
    'left_middle',
    'left_ring',
    'left_pinky',
    'right_thumb',
    'right_index',
    'right_middle',
    'right_ring',
    'right_pinky',
    'right_eye_brow1',
    'right_eye_brow2',
    'right_eye_brow3',
    'right_eye_brow4',
    'right_eye_brow5',
    'left_eye_brow5',
    'left_eye_brow4',
    'left_eye_brow3',
    'left_eye_brow2',
    'left_eye_brow1',
    'nose1',
    'nose2',
    'nose3',
    'nose4',
    'right_nose_2',
    'right_nose_1',
    'nose_middle',
    'left_nose_1',
    'left_nose_2',
    'right_eye1',
    'right_eye2',
    'right_eye3',
    'right_eye4',
    'right_eye5',
    'right_eye6',
    'left_eye4',
    'left_eye3',
    'left_eye2',
    'left_eye1',
    'left_eye6',
    'left_eye5',
    'right_mouth_1',
    'right_mouth_2',
    'right_mouth_3',
    'mouth_top',
    'left_mouth_3',
    'left_mouth_2',
    'left_mouth_1',
    'left_mouth_5',  # 59 in OpenPose output
    'left_mouth_4',  # 58 in OpenPose output
    'mouth_bottom',
    'right_mouth_4',
    'right_mouth_5',
    'right_lip_1',
    'right_lip_2',
    'lip_top',
    'left_lip_2',
    'left_lip_1',
    'left_lip_3',
    'lip_bottom',
    'right_lip_3',
    # Face contour
    'right_contour_1',
    'right_contour_2',
    'right_contour_3',
    'right_contour_4',
    'right_contour_5',
    'right_contour_6',
    'right_contour_7',
    'right_contour_8',
    'contour_middle',
    'left_contour_8',
    'left_contour_7',
    'left_contour_6',
    'left_contour_5',
    'left_contour_4',
    'left_contour_3',
    'left_contour_2',
    'left_contour_1',
]

SMPLH_JOINT_NAMES = [
    'pelvis',
    'left_hip',
    'right_hip',
    'spine1',
    'left_knee',
    'right_knee',
    'spine2',
    'left_ankle',
    'right_ankle',
    'spine3',
    'left_foot',
    'right_foot',
    'neck',
    'left_collar',
    'right_collar',
    'head',
    'left_shoulder',
    'right_shoulder',
    'left_elbow',
    'right_elbow',
    'left_wrist',
    'right_wrist',
    'left_index1',
    'left_index2',
    'left_index3',
    'left_middle1',
    'left_middle2',
    'left_middle3',
    'left_pinky1',
    'left_pinky2',
    'left_pinky3',
    'left_ring1',
    'left_ring2',
    'left_ring3',
    'left_thumb1',
    'left_thumb2',
    'left_thumb3',
    'right_index1',
    'right_index2',
    'right_index3',
    'right_middle1',
    'right_middle2',
    'right_middle3',
    'right_pinky1',
    'right_pinky2',
    'right_pinky3',
    'right_ring1',
    'right_ring2',
    'right_ring3',
    'right_thumb1',
    'right_thumb2',
    'right_thumb3',
    'nose',
    'right_eye',
    'left_eye',
    'right_ear',
    'left_ear',
    'left_big_toe',
    'left_small_toe',
    'left_heel',
    'right_big_toe',
    'right_small_toe',
    'right_heel',
    'left_thumb',
    'left_index',
    'left_middle',
    'left_ring',
    'left_pinky',
    'right_thumb',
    'right_index',
    'right_middle',
    'right_ring',
    'right_pinky',
]

valid_joint_ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28,
                   29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]

if __name__ == '__main__':
    for i, n in enumerate(VH_joint_names):
        print(f'{i}: {n}')
