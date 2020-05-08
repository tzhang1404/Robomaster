def turnToMarker(target = rm_define.marker_trans_red_heart):
    #follow the gimbal aim
    robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
    vision_ctrl.detect_marker_and_aim(target)
    time.sleep(2)

def turnCamera(direction):
    found = True
    while not (vision_ctrl.check_condition(target)):
        print("right")
        if gimbal_ctrl.get_axis_angle(rm_define.gimbal_axis_yaw) > 100 or gimbal_ctrl.get_axis_angle(rm_define.gimbal_axis_yaw) < -100:
            found = False
            break;
        gimbal_ctrl.rotate(direction)
    return found


def frontScan(target = rm_define.cond_recognized_marker_trans_red_heart):
    found = True
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    gimbal_ctrl.set_rotate_speed(60)
    gimbal_ctrl.recenter()
    while not (vision_ctrl.check_condition(target)):
        print("right")
        if gimbal_ctrl.get_axis_angle(rm_define.gimbal_axis_yaw) > 100:
            found = False
            break;
        gimbal_ctrl.rotate(rm_define.gimbal_right)
    if not found:
        while not (vision_ctrl.check_condition(target)):
            print("left")
            if gimbal_ctrl.get_axis_angle(rm_define.gimbal_axis_yaw) < -100:
                print("left not found")
                found = False
                break;
            gimbal_ctrl.rotate(rm_define.gimbal_left)

    if found:
        media_ctrl.play_sound(rm_define.media_sound_recognize_success)
        led_ctrl.set_top_led(rm_define.armor_top_all, 0, 127 , 70, rm_define.effect_flash)
    gimbal_ctrl.stop()
    time.sleep(1)
    return found



def start():
    scanArray = [
                    rm_define.cond_recognized_marker_number_one,
                    rm_define.cond_recognized_marker_number_two,
                    rm_define.cond_recognized_marker_number_three
                    ]
    aimArray = [
                    rm_define.marker_number_one,
                    rm_define.marker_number_two,
                    rm_define.marker_number_three
                    ]
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_always_on)
    chassis_ctrl.enable_stick_overlay()
    chassis_ctrl.set_rotate_speed(60)
    index = 0
    while index < len(scanArray):
        scanTarget = scanArray[index]
        aimTarget = aimArray[index]
        detected = frontScan(scanTarget)
        if detected:
            turnToMarker(aimTarget)
            chassis_ctrl.move_with_time(0, 0.5)
        index += 1


    return

