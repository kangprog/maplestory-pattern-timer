#
# create by kangprog
#
import time

from consts.const import *
from utils.thread import THREADING_WITH_TRACE


boom_pattern = None
left_stone_pattern = None
brase_30_pattern = None
brase_45_pattern = None
brase_60_pattern = None
out_timer_pattern = None


def on_reset(root, stringvar, sec, entry):
    try:
        temp = sec
    except:
        print("[Error] Please input the right value")

    while temp >-1:  
        try:
            if temp < 10:
                stringvar.set("{0:2d}".format(temp))
                entry.configure(fg=WARRNING_COLOR)
            else:
                stringvar.set("{0:2d}".format(temp))
                entry.configure(fg=COMMON_COLOR)
        except Exception as ex:
            print(f"[Error] Set Time Label Error: {ex}")
            break

        root.update()
        time.sleep(1)

        if (temp == 0):
            temp = sec
            
        temp -= 1


def on_click(
        root,
        boom_stringvar = None, boom_sec = 0, boom_second_entry = None,
        left_stone_stringvar = None, left_stone_sec = 0, left_stone_second_entry = None,
        brase_30_stringvar = None, brase_30_sec = 0, brase_30_second_entry = None,
        brase_45_stringvar = None, brase_45_sec = 0, brase_45_second_entry = None,
        brase_60_stringvar = None, brase_60_sec = 0, brase_60_second_entry = None,
        out_timer_stringvar = None, out_timer_sec = 0, out_timer_second_entry = None,
        check = False,
    ):

    global boom_pattern, left_stone_pattern, brase_30_pattern, brase_45_pattern, brase_60_pattern, out_timer_pattern

    if check:
        try:
            boom_pattern.kill()
        except:
            pass
        try:
            left_stone_pattern.kill()
        except:
            pass
        try:
            brase_30_pattern.kill()
        except:
            pass
        try:
            brase_45_pattern.kill()
        except:
            pass
        try:
            brase_60_pattern.kill()
        except:
            pass
        try:
            out_timer_pattern.kill()
        except:
            pass

    else:
        if boom_sec == BOOM_SECOND:
            if boom_pattern:
                boom_pattern.kill()
            boom_pattern = THREADING_WITH_TRACE(
                target=on_reset,
                args=(root, boom_stringvar, boom_sec, boom_second_entry),
            )
            boom_pattern.start()

        if left_stone_sec == LEFT_STONE_SECOND:
            if left_stone_pattern:
                left_stone_pattern.kill()
            left_stone_pattern = THREADING_WITH_TRACE(
                target=on_reset,
                args=(root, left_stone_stringvar, left_stone_sec, left_stone_second_entry),
            )
            left_stone_pattern.start()

        if brase_30_sec == BRASE_30_SECOND:
            if brase_30_pattern:
                brase_30_pattern.kill()
            brase_30_pattern = THREADING_WITH_TRACE(
                target=on_reset,
                args=(root, brase_30_stringvar, brase_30_sec, brase_30_second_entry),
            )
            brase_30_pattern.start()

        if brase_45_sec == BRASE_45_SECOND:
            if brase_45_pattern:
                brase_45_pattern.kill()
            brase_45_pattern = THREADING_WITH_TRACE(
                target=on_reset,
                args=(root, brase_45_stringvar, brase_45_sec, brase_45_second_entry),
            )
            brase_45_pattern.start()

        if brase_60_sec == BRASE_60_SECOND:
            if brase_60_pattern:
                brase_60_pattern.kill()
            brase_60_pattern = THREADING_WITH_TRACE(
                target=on_reset,
                args=(root, brase_60_stringvar, brase_60_sec, brase_60_second_entry),
            )
            brase_60_pattern.start()

        if out_timer_sec == OUT_TIMER_SECOND:
            if out_timer_pattern:
                out_timer_pattern.kill()
            out_timer_pattern = THREADING_WITH_TRACE(
                target=on_reset,
                args=(root, out_timer_stringvar, out_timer_sec, out_timer_second_entry),
            )
            out_timer_pattern.start()
