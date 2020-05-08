def turnToMarker():
    #follow the gimbal aim
    robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
    vision_ctrl.detect_marker_and_aim(rm_define.marker_trans_red_heart)
    time.sleep(2)


def frontScan(target = None):
    if target == None:
        target = rm_define.cond_recognized_marker_trans_red_heart
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    gimbal_ctrl.set_rotate_speed(30)
    gimbal_ctrl.recenter()
    while not (vision_ctrl.check_condition(target)):
        gimbal_ctrl.rotate(rm_define.gimbal_right)
    media_ctrl.play_sound(rm_define.media_sound_recognize_success)
    gimbal_ctrl.stop()
    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 127 , 70, rm_define.effect_flash)
    time.sleep(2)
    return



def start():
    targetArray = [
                    rm_define.cond_recognized_marker_number_zero,
                    rm_define.cond_recognized_marker_number_one,
                    rm_define.cond_recognized_marker_number_two
                    ]
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_always_on)
    chassis_ctrl.enable_stick_overlay()
    index = 0
    while index < len(targetArray):
        detected = frontScan()
        if detected:
            turnToMarker()
            # chassis_ctrl.move_with_time(0, 1)
        index += 1


    return

