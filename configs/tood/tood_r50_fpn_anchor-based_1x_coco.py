_base_ = './tood_reg800_fpn_2x_cbam_visdrone.py'
model = dict(bbox_head=dict(anchor_type='anchor_based'))
