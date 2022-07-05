import sys
sys.path.append('footskate_reducer')
sys.path.append('footskate_reducer/ground_detector')
from footskate_reducer.ground_detector.op_filter_json_merge import main0
from demo_merge import main1
from demo_pare_result_merge import main2
import argparse
from merge_parser import parser_pare, parser_pare_result, parser_op_filter

if __name__ == "__main__":
    video_name='Color_flip'
    video_path='/root/code/mover/preprocess/input_data/Color_flip/Color_flip.mp4'
    openpose_dir='/root/code/mover/preprocess/input_data/Color_flip/openpose'
    image_dir='/root/code/mover/preprocess/input_data/Color_flip/imgs'
    out_dir='/root/code/mover/preprocess/out_data'


    # # step0: openpose filter
    # parser0 = parser_op_filter()
    # parser0.set_defaults(root=openpose_dir,
    #                     dump=f'{out_dir}/{video_name}/openpose_OneEurofilter',
    #                     img_dir=image_dir,
    #                     viz=True)
    # args0 = parser0.parse_args()
    # main0(args0)


    # step1: pare
    parser1 = parser_pare()
    pare_model = '../pare/hrnet_model'
    pare_model = '/root/code/mover/preprocess/pare/hrnet_model'
    parser1.set_defaults(cfg=f'{pare_model}/config.yaml', ckpt=f'{pare_model}/checkpoint.ckpt',
                         output_folder=f'{out_dir}', vid_file=f'{video_path}', draw_keypoints=True,
                         detector='maskrcnn')
    args1 = parser1.parse_args()
    main1(args1)


    # # step2: op2smplifyx_withPARE
    # parser2 = parser_pare_result()
    # OUTPUT_FOLDER = "/root/code/mover/preprocess/Color_flip_merge/OneEuro_filter_mv_smplifyx_input_withPARE"
    # JSON_FOLDER = "/root/code/mover/preprocess/Color_flip/Color_flip_openpose"
    # pare_result = '/root/code/mover/preprocess/Color_flip/pare_output.pkl'
    # cam_dir = '/root/code/mover/smplifyx_cam'
    # MODEL_FOLDER = '../pare/data/body_models'
    # VPOSER_FOLDER = '../../smplifyx-file/vposer_v1_0'
    # parser2.set_defaults(config='./cfg_files/fit_smpl.yaml', export_mesh=True, save_new_json=True,
    #                      json_folder=f'{JSON_FOLDER}', data_folder=f'{image_dir}', output_folder=f'{OUTPUT_FOLDER}',
    #                      pare_result=f'{pare_result}', cam_dir=f'{cam_dir}', visualize=False,
    #                      model_folder=f'{MODEL_FOLDER}', vposer_ckpt=f'{VPOSER_FOLDER}',
    #                      part_segm_fn='/root/code/mover/smplifyx-file/smplx_parts_segm.pkl', gender='male',
    #                      check_inverse_feet=False)
    # print('********************************************')
    # args2 = parser2.parse_args()
    # args_dict2 = vars(args2)
    # print(args_dict2)
    # main2(**args2)
    #
    # print(args1)
    # print('********************************************')
    #
    # args2 = parser2.parse_args()
    # args_dict2 = vars(args2)
    # print(args_dict2)